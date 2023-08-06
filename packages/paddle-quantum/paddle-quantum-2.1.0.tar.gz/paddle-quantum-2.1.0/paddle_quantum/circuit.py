﻿# Copyright (c) 2021 Institute for Quantum Computing, Baidu Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warnings
import numpy as np
import math
from functools import reduce
from collections import defaultdict
import matplotlib.pyplot as plt
from paddle_quantum.simulator import transfer_state, init_state_gen, measure_state
import paddle
from paddle import matmul, trace, real, imag, reshape
from paddle_quantum.utils import dagger, pauli_str_to_matrix
from paddle_quantum.intrinsic import *
from paddle_quantum.state import density_op

__all__ = [
    "UAnsatz",
    "H_prob"
]


class UAnsatz:
    r"""基于 PaddlePaddle 的动态图机制实现量子电路的 ``class`` 。

    用户可以通过实例化该 ``class`` 来搭建自己的量子电路。

    Attributes:
        n (int): 该电路的量子比特数
    """

    def __init__(self, n):
        r"""UAnsatz 的构造函数，用于实例化一个 UAnsatz 对象

        Args:
            n (int): 该电路的量子比特数

        """
        self.n = n
        self.__has_channel = False
        self.__state = None
        self.__run_state = ''
        # Record history of adding gates to the circuit
        self.__history = []
        
    def _count_history(self):
        r"""calculate how many blocks needed for printing

        Note:
        这是内部函数，你并不需要直接调用到该函数。
        """
        # Record length of each section
        length = [5]
        n = self.n
        # Record current section number for every qubit
        qubit = [0] * n
        # Number of sections
        qubit_max = max(qubit)
        # Record section number for each gate
        gate = []
        history = self.__history
        
        for current_gate in history:
            # Single-qubit gates with no params to print
            if current_gate[0] in {'h', 's', 't', 'x', 'y', 'z', 'u'}:
                curr_qubit = current_gate[1][0]
                gate.append(qubit[curr_qubit])
                qubit[curr_qubit] = qubit[curr_qubit] + 1
                # A new section is added
                if qubit[curr_qubit] > qubit_max:
                    length.append(5)
                    qubit_max = qubit[curr_qubit]
            # Gates with params to print
            elif current_gate[0] in {'rx', 'ry', 'rz'}:
                curr_qubit = current_gate[1][0]
                gate.append(qubit[curr_qubit])
                if length[qubit[curr_qubit]] == 5:
                    length[qubit[curr_qubit]] = 13
                qubit[curr_qubit] = qubit[curr_qubit] + 1
                if qubit[curr_qubit] > qubit_max:
                    length.append(5)
                    qubit_max = qubit[curr_qubit]
            # Two-qubit gates
            elif current_gate[0] in {'CNOT', 'SWAP', 'RXX_gate', 'RYY_gate', 'RZZ_gate', 'MS_gate'}:
                p = current_gate[1][0]
                q = current_gate[1][1]
                a = max(p, q)
                b = min(p, q)
                ind = max(qubit[b: a + 1])
                gate.append(ind)
                if length[ind] < 13 and current_gate[0] in {'RXX_gate', 'RYY_gate', 'RZZ_gate'}:
                    length[ind] = 13
                for j in range(b, a + 1):
                    qubit[j] = ind + 1
                if ind + 1 > qubit_max:
                    length.append(5)
                    qubit_max = ind + 1
    
        return length, gate
    
    def __str__(self):
        r"""实现画电路的功能
        
        Returns:
            string: 用来print的字符串
        
        代码示例:

        .. code-block:: python

            import paddle
            from paddle_quantum.circuit import UAnsatz
            import numpy as np
            
            cir = UAnsatz(5)
            cir.superposition_layer()
            rotations = paddle.to_tensor(np.random.uniform(-2, 2, size=(3, 5, 1)))
            cir.real_entangled_layer(rotations, 3)
            
            print(cir)
        ::
            
            The printed circuit is:
            
            --H----Ry(-0.14)----*-------------------X----Ry(-0.77)----*-------------------X--
                                |                   |                 |                   |  
            --H----Ry(-1.00)----X----*--------------|----Ry(-0.83)----X----*--------------|--
                                     |              |                      |              |  
            --H----Ry(-1.88)---------X----*---------|----Ry(-0.98)---------X----*---------|--
                                          |         |                           |         |  
            --H----Ry(1.024)--------------X----*----|----Ry(-0.37)--------------X----*----|--
                                               |    |                                |    |  
            --H----Ry(1.905)-------------------X----*----Ry(-1.82)-------------------X----*--
                                                                                             
        """
        length, gate = self._count_history()
        history = self.__history
        n = self.n
        # Ignore the unused section 
        total_length = sum(length) - 5
    
        print_list = [['-' if i % 2 == 0 else ' '] * total_length for i in range(n * 2)]

        for i, current_gate in enumerate(history):
            if current_gate[0] in {'h', 's', 't', 'x', 'y', 'z', 'u'}:
                # Calculate starting position ind of current gate
                sec = gate[i]
                ind = sum(length[:sec])
                print_list[current_gate[1][0] * 2][ind + length[sec] // 2] = current_gate[0].upper()
            elif current_gate[0] in {'rx', 'ry', 'rz'}:
                sec = gate[i]
                ind = sum(length[:sec])
                line = current_gate[1][0] * 2
                param = current_gate[2][2 if current_gate[0] == 'rz' else 0]
                print_list[line][ind + 2] = 'R'
                print_list[line][ind + 3] = current_gate[0][1]
                print_list[line][ind + 4] = '('
                print_list[line][ind + 5: ind + 10] = format(float(param.numpy()), '.3f')[:5]
                print_list[line][ind + 10] = ')'
            elif current_gate[0] in {'CNOT', 'SWAP', 'RXX_gate', 'RYY_gate', 'RZZ_gate', 'MS_gate'}:
                sec = gate[i]
                ind = sum(length[:sec])
                cqubit = current_gate[1][0]
                tqubit = current_gate[1][1]
                if current_gate[0] in {'CNOT', 'SWAP'}:
                    print_list[cqubit * 2][ind + length[sec] // 2] = '*'
                    print_list[tqubit * 2][ind + length[sec] // 2] = 'X' if current_gate[0] == 'CNOT' else '*'
                elif current_gate[0] == 'MS_gate':
                    for qubit in {cqubit, tqubit}:
                        print_list[qubit * 2][ind + length[sec] // 2 - 1] = 'M'
                        print_list[qubit * 2][ind + length[sec] // 2] = '_'
                        print_list[qubit * 2][ind + length[sec] // 2 + 1] = 'S'
                elif current_gate[0] in {'RXX_gate', 'RYY_gate', 'RZZ_gate'}:
                    param = current_gate[2]
                    for line in {cqubit * 2, tqubit * 2}:
                        print_list[line][ind + 2] = 'R'
                        print_list[line][ind + 3: ind + 5] = current_gate[0][1:3].lower()
                        print_list[line][ind + 5] = '('
                        print_list[line][ind + 6: ind + 10] = format(float(param.numpy()), '.2f')[:4]
                        print_list[line][ind + 10] = ')'
                start_line = min(cqubit, tqubit)
                end_line = max(cqubit, tqubit)
                for k in range(start_line * 2 + 1, end_line * 2):
                    print_list[k][ind + length[sec] // 2] = '|'

        print_list = list(map(''.join, print_list))
        return_str = '\n'.join(print_list)

        return return_str
        
    def run_state_vector(self, input_state=None, store_state=True):
        r"""运行当前的量子电路，输入输出的形式为态矢量。

        Warning:
            该方法只能运行无噪声的电路。
        
        Args:
            input_state (Tensor, optional): 输入的态矢量，默认为 :math:`|00...0\rangle`
            store_state (Bool, optional): 是否存储输出的态矢量，默认为 ``True`` ，即存储
        
        Returns:
            Tensor: 量子电路输出的态矢量
        
        代码示例:

        .. code-block:: python

            import numpy as np
            import paddle
            from paddle_quantum.circuit import UAnsatz
            from paddle_quantum.state import vec
            n = 2
            theta = np.ones(3)

            input_state = paddle.to_tensor(vec(n))
            theta = paddle.to_tensor(theta)
            cir = UAnsatz(n)
            cir.h(0)
            cir.ry(theta[0], 1)
            cir.rz(theta[1], 1)
            output_state = cir.run_state_vector(input_state).numpy()
            print(f"The output state vector is {output_state}")

        ::

            The output state vector is [[0.62054458+0.j 0.18316521+0.28526291j 0.62054458+0.j 0.18316521+0.28526291j]]
        """
        # Throw a warning when cir has channel
        if self.__has_channel:
            warnings.warn('The noiseless circuit will be run.', RuntimeWarning)
        state = init_state_gen(self.n, 0) if input_state is None else input_state
        old_shape = state.shape
        assert reduce(lambda x, y: x * y, old_shape) == 2 ** self.n, 'The length of the input vector is not right'
        state = reshape(state, (2 ** self.n,))

        state_conj = paddle.conj(state)
        assert paddle.abs(real(paddle.sum(paddle.multiply(state_conj, state))) - 1) < 1e-8, \
            'Input state is not a normalized vector'

        state = transfer_by_history(state, self.__history)

        if store_state:
            self.__state = state
            # Add info about which function user called
            self.__run_state = 'state_vector'

        return reshape(state, old_shape)

    def run_density_matrix(self, input_state=None, store_state=True):
        r"""运行当前的量子电路，输入输出的形式为密度矩阵。
        
        Args:
            input_state (Tensor, optional): 输入的密度矩阵，默认为 :math:`|00...0\rangle \langle00...0|`
            store_state (bool, optional): 是否存储输出的密度矩阵，默认为 ``True`` ，即存储
        
        Returns:
            Tensor: 量子电路输出的密度矩阵

        代码示例:

        .. code-block:: python

            import numpy as np
            import paddle
            from paddle_quantum.circuit import UAnsatz
            from paddle_quantum.state import density_op
            n = 1
            theta = np.ones(3)

            input_state = paddle.to_tensor(density_op(n))
            theta = paddle.to_tensor(theta)
            cir = UAnsatz(n)
            cir.rx(theta[0], 0)
            cir.ry(theta[1], 0)
            cir.rz(theta[2], 0)
            density_matrix = cir.run_density_matrix(input_state).numpy()
            print(f"The output density matrix is\n{density_matrix}")

        ::

            The output density matrix is
            [[0.64596329+0.j         0.47686058+0.03603751j]
            [0.47686058-0.03603751j 0.35403671+0.j        ]]
        """
        state = paddle.to_tensor(density_op(self.n)) if input_state is None else input_state
        assert state.shape == [2 ** self.n, 2 ** self.n], "The dimension is not right"

        if not self.__has_channel:
            state = matmul(self.U, matmul(state, dagger(self.U)))
        else:
            dim = 2 ** self.n
            shape = (dim, dim)
            num_ele = dim ** 2
            identity = paddle.eye(dim, dtype='float64')
            identity = paddle.cast(identity, 'complex128')
            identity = reshape(identity, [num_ele])

            u_start = 0
            for i, history_ele in enumerate(self.__history):
                if history_ele[0] == 'channel':
                    # Combine preceding unitary operations
                    unitary = transfer_by_history(identity, self.__history[u_start:i])
                    sub_state = paddle.zeros(shape, dtype='complex128')
                    # Sum all the terms corresponding to different Kraus operators
                    for op in history_ele[1]:
                        pseudo_u = reshape(transfer_state(unitary, op, history_ele[2]), shape)
                        sub_state += pseudo_u @ state @ dagger(pseudo_u)
                    state = sub_state
                    u_start = i + 1
            # Apply unitary operations left
            unitary = reshape(transfer_by_history(identity, self.__history[u_start:(i + 1)]), shape)
            state = matmul(unitary, matmul(state, dagger(unitary)))

        if store_state:
            self.__state = state
            # Add info about which function user called
            self.__run_state = 'density_matrix'

        return state

    @property
    def U(self):
        r"""量子电路的酉矩阵形式。

        Warning:
            该属性只限于无噪声的电路。
        
        Returns:
            Tensor: 当前电路的酉矩阵表示

        代码示例:

        .. code-block:: python

            import paddle
            from paddle_quantum.circuit import UAnsatz
            n = 2
            cir = UAnsatz(2)
            cir.h(0)
            cir.cnot([0, 1])
            unitary_matrix = cir.U
            print("The unitary matrix of the circuit for Bell state preparation is\n", unitary_matrix.numpy())

        ::

            The unitary matrix of the circuit for Bell state preparation is
            [[ 0.70710678+0.j  0.        +0.j  0.70710678+0.j  0.        +0.j]
            [ 0.        +0.j  0.70710678+0.j  0.        +0.j  0.70710678+0.j]
            [ 0.        +0.j  0.70710678+0.j  0.        +0.j -0.70710678+0.j]
            [ 0.70710678+0.j  0.        +0.j -0.70710678+0.j  0.        +0.j]]
        """
        # Throw a warning when cir has channel
        if self.__has_channel:
            warnings.warn('The unitary matrix of the noiseless circuit will be given.', RuntimeWarning)
        dim = 2 ** self.n
        shape = (dim, dim)
        num_ele = dim ** 2
        state = paddle.eye(dim, dtype='float64')
        state = paddle.cast(state, 'complex128')
        state = reshape(state, [num_ele])
        state = transfer_by_history(state, self.__history)

        return reshape(state, shape)

    def basis_encoding(self, x, invert=False):
        r"""将输入的经典数据使用基态编码的方式编码成量子态。

        在 basis encoding 中，输入的经典数据只能包括 0 或 1。如输入数据为 1101，则编码后的量子态为 :math:`|1101\rangle` 。
        这里假设量子态在编码前为全 0 的态，即 :math:`|00\ldots 0\rangle` 。

        Args:
            x (Tensor): 待编码的向量
            invert (bool): 添加的是否为编码电路的逆电路，默认为 ``False`` ，即添加正常的编码电路
        """
        x = paddle.flatten(x)
        x = paddle.cast(x, dtype="int32")
        assert x.size == self.n, "the number of classical data should be equal to the number of qubits"
        for idx, element in enumerate(x):
            if element:
                self.x(idx)

    def amplitude_encoding(self, x, mode):
        r"""将输入的经典数据使用振幅编码的方式编码成量子态。

        Args:
            x (Tensor): 待编码的向量
            mode (str): 生成的量子态的表示方式，``"state_vector"`` 代表态矢量表示， ``"density_matrix"`` 代表密度矩阵表示

        Returns:
            Tensor: 一个形状为 ``(2 ** n, )`` 或 ``(2 ** n, 2 ** n)`` 的张量，表示编码之后的量子态。

        """
        assert x.size <= 2 ** self.n, "the number of classical data should be equal to the number of qubits"
        x = paddle.flatten(x)
        pad_num = 2 ** self.n - x.size
        if pad_num > 0:
            zero_tensor = paddle.zeros((pad_num,), x.dtype)
            x = paddle.concat([x, zero_tensor])
        length = paddle.norm(x, p=2)
        x = paddle.divide(x, length)
        if mode == "state_vector":
            x = paddle.cast(x, dtype="complex128")
        elif mode == "density_matrix":
            x = paddle.reshape(x, (2**self.n, 1))
            x = matmul(x, dagger(x))
        else:
            raise ValueError("the mode should be state_vector or density_matrix")
        return x

    def angle_encoding(self, x, encoding_gate, invert=False):
        r"""将输入的经典数据使用角度编码的方式进行编码。

        Args:
            x (Tensor): 待编码的向量
            encoding_gate (str): 编码要用的量子门，可以是 ``"rx"`` 、 ``"ry"`` 和 ``"rz"``
            invert (bool): 添加的是否为编码电路的逆电路，默认为 ``False`` ，即添加正常的编码电路
        """
        assert x.size <= self.n, "the number of classical data should be equal to the number of qubits"
        x = paddle.flatten(x)
        if invert:
            x = -x

        def add_encoding_gate(theta, idx, gate):
            if gate == "rx":
                self.rx(theta, idx)
            elif gate == "ry":
                self.ry(theta, idx)
            elif gate == "rz":
                self.rz(theta, idx)
            else:
                raise ValueError("the encoding_gate should be rx, ry, or rz")

        for idx, element in enumerate(x):
            add_encoding_gate(element[0], idx, encoding_gate)

    def iqp_encoding(self, x, num_repeats=1, pattern=None, invert=False):
        r"""将输入的经典数据使用 IQP 编码的方式进行编码。

        Args:
            x (Tensor): 待编码的向量
            num_repeats (int): 编码层的层数
            pattern (list): 量子比特的纠缠方式
            invert (bool): 添加的是否为编码电路的逆电路，默认为 ``False`` ，即添加正常的编码电路
        """
        assert x.size <= self.n, "the number of classical data should be equal to the number of qubits"
        num_x = x.size
        x = paddle.flatten(x)
        if pattern is None:
            pattern = list()
            for idx0 in range(0, self.n):
                for idx1 in range(idx0 + 1, self.n):
                    pattern.append((idx0, idx1))

        while num_repeats > 0:
            num_repeats -= 1
            if invert:
                for item in pattern:
                    self.cnot(list(item))
                    self.rz(-x[item[0]]*x[item[1]], item[1])
                    self.cnot(list(item))
                for idx in range(0, num_x):
                    self.rz(-x[idx], idx)
                for idx in range(0, num_x):
                    self.h(idx)
            else:
                for idx in range(0, num_x):
                    self.h(idx)
                for idx in range(0, num_x):
                    self.rz(x[idx], idx)
                for item in pattern:
                    self.cnot(list(item))
                    self.rz(x[item[0]]*x[item[1]], item[1])
                    self.cnot(list(item))

    """
    Common Gates
    """

    def rx(self, theta, which_qubit):
        r"""添加关于 x 轴的单量子比特旋转门。

        其矩阵形式为：
        
        .. math::
        
            \begin{bmatrix} \cos\frac{\theta}{2} & -i\sin\frac{\theta}{2} \\ -i\sin\frac{\theta}{2} & \cos\frac{\theta}{2} \end{bmatrix}

        Args:
            theta (Tensor): 旋转角度
            which_qubit (int): 作用在的 qubit 的编号，其值应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数

        ..  code-block:: python

            import numpy as np
            import paddle
            from paddle_quantum.circuit import UAnsatz
            theta = np.array([np.pi], np.float64)
            theta = paddle.to_tensor(theta)
            num_qubits = 1
            cir = UAnsatz(num_qubits)
            which_qubit = 0
            cir.rx(theta[0], which_qubit)

        """
        assert 0 <= which_qubit < self.n, "the qubit should >= 0 and < n (the number of qubit)"
        self.__history.append(['rx', [which_qubit], [theta,
                                                     paddle.to_tensor(np.array([-math.pi / 2])),
                                                     paddle.to_tensor(np.array([math.pi / 2]))]])

    def ry(self, theta, which_qubit):
        r"""添加关于 y 轴的单量子比特旋转门。

        其矩阵形式为：
        
        .. math::
        
            \begin{bmatrix} \cos\frac{\theta}{2} & -\sin\frac{\theta}{2} \\ \sin\frac{\theta}{2} & \cos\frac{\theta}{2} \end{bmatrix}

        Args:
            theta (Tensor): 旋转角度
            which_qubit (int): 作用在的 qubit 的编号，其值应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数

        ..  code-block:: python
        
            import numpy as np
            import paddle
            from paddle_quantum.circuit import UAnsatz
            theta = np.array([np.pi], np.float64)
            theta = paddle.to_tensor(theta)
            num_qubits = 1
            cir = UAnsatz(num_qubits)
            which_qubit = 0
            cir.ry(theta[0], which_qubit)
        """
        assert 0 <= which_qubit < self.n, "the qubit should >= 0 and < n (the number of qubit)"
        self.__history.append(['ry', [which_qubit], [theta,
                                                     paddle.to_tensor(np.array([0.0])),
                                                     paddle.to_tensor(np.array([0.0]))]])

    def rz(self, theta, which_qubit):
        r"""添加关于 z 轴的单量子比特旋转门。

        其矩阵形式为：
        
        .. math::

            \begin{bmatrix} 1 & 0 \\ 0 & e^{i\theta} \end{bmatrix}

        Args:
            theta (Tensor): 旋转角度
            which_qubit (int): 作用在的 qubit 的编号，其值应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数

        ..  code-block:: python
        
            import numpy as np
            import paddle
            from paddle_quantum.circuit import UAnsatz
            theta = np.array([np.pi], np.float64)
            theta = paddle.to_tensor(theta)
            num_qubits = 1
            cir = UAnsatz(num_qubits)
            which_qubit = 0
            cir.rz(theta[0], which_qubit)
        """
        assert 0 <= which_qubit < self.n, "the qubit should >= 0 and < n (the number of qubit)"
        self.__history.append(['rz', [which_qubit], [paddle.to_tensor(np.array([0.0])),
                                                     paddle.to_tensor(np.array([0.0])),
                                                     theta]])

    def cnot(self, control):
        r"""添加一个 CNOT 门。

        对于 2 量子比特的量子电路，当 ``control`` 为 ``[0, 1]`` 时，其矩阵形式为：

        .. math::
        
            \begin{align}
            CNOT &=|0\rangle \langle 0|\otimes I + |1 \rangle \langle 1|\otimes X\\
            &=\begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{bmatrix}
            \end{align}

        Args:
            control (list): 作用在的 qubit 的编号，``control[0]`` 为控制位，``control[1]`` 为目标位，其值都应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数

        ..  code-block:: python
        
            import numpy as np
            import paddle
            from paddle_quantum.circuit import UAnsatz
            num_qubits = 2
            cir = UAnsatz(num_qubits)
            cir.cnot([0, 1])
        """
        assert 0 <= control[0] < self.n and 0 <= control[1] < self.n,\
            "the qubit should >= 0 and < n (the number of qubit)"
        assert control[0] != control[1], "the control qubit is the same as the target qubit"
        self.__history.append(['CNOT', control, None])

    def swap(self, control):
        r"""添加一个 SWAP 门。

        其矩阵形式为：

        .. math::

            \begin{align}
            SWAP = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}
            \end{align}

        Args:
            control (list): 作用在的 qubit 的编号，``control[0]`` 和 ``control[1]`` 是想要交换的位，其值都应该在 :math:`[0, n)`范围内， :math:`n` 为该量子电路的量子比特数

        ..  code-block:: python

            import numpy as np
            import paddle 
            from paddle_quantum.circuit import UAnsatz
            num_qubits = 2
            cir = UAnsatz(num_qubits)
            cir.swap([0, 1])
        """
        assert 0 <= control[0] < self.n and 0 <= control[1] < self.n,\
            "the qubit should >= 0 and < n (the number of qubit)"
        assert control[0] != control[1], "the indices needed to be swapped should not be the same"
        self.__history.append(['SWAP', control, None])

    def x(self, which_qubit):
        r"""添加单量子比特 X 门。

        其矩阵形式为：
        
        .. math::
        
            \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}

        Args:
            which_qubit (int): 作用在的qubit的编号，其值应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数

        .. code-block:: python
            
            import paddle
            from paddle_quantum.circuit import UAnsatz
            num_qubits = 1
            cir = UAnsatz(num_qubits)
            which_qubit = 0
            cir.x(which_qubit)
            cir.run_state_vector()
            print(cir.measure(shots = 0))

        ::

            {'0': 0.0, '1': 1.0}
        """
        assert 0 <= which_qubit < self.n, "the qubit should >= 0 and < n (the number of qubit)"
        self.__history.append(['x', [which_qubit], None])

    def y(self, which_qubit):
        r"""添加单量子比特 Y 门。

        其矩阵形式为：
        
        .. math::
        
            \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}

        Args:
            which_qubit (int): 作用在的 qubit 的编号，其值应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数

        .. code-block:: python
            
            import paddle
            from paddle_quantum.circuit import UAnsatz
            num_qubits = 1
            cir = UAnsatz(num_qubits)
            which_qubit = 0
            cir.y(which_qubit)
            cir.run_state_vector()
            print(cir.measure(shots = 0))

        ::

            {'0': 0.0, '1': 1.0}
        """
        assert 0 <= which_qubit < self.n, "the qubit should >= 0 and < n (the number of qubit)"
        self.__history.append(['y', [which_qubit], None])

    def z(self, which_qubit):
        r"""添加单量子比特 Z 门。

        其矩阵形式为：
        
        .. math::
        
            \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}

        Args:
            which_qubit (int): 作用在的qubit的编号，其值应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数

        .. code-block:: python
        
            import paddle
            from paddle_quantum.circuit import UAnsatz
            num_qubits = 1
            cir = UAnsatz(num_qubits)
            which_qubit = 0
            cir.z(which_qubit)
            cir.run_state_vector()
            print(cir.measure(shots = 0))

        ::

            {'0': 1.0, '1': 0.0}
        """
        assert 0 <= which_qubit < self.n, "the qubit should >= 0 and < n (the number of qubit)"
        self.__history.append(['z', [which_qubit], None])

    def h(self, which_qubit):
        r"""添加一个单量子比特的 Hadamard 门。

        其矩阵形式为：

        .. math::
        
            H = \frac{1}{\sqrt{2}}\begin{bmatrix} 1&1\\1&-1 \end{bmatrix}

        Args:
            which_qubit (int): 作用在的 qubit 的编号，其值应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数
        """
        assert 0 <= which_qubit < self.n, "the qubit should >= 0 and < n (the number of qubit)"
        self.__history.append(['h', [which_qubit], None])

    def s(self, which_qubit):
        r"""添加一个单量子比特的 S 门。

        其矩阵形式为：

        .. math::
        
            S = \begin{bmatrix} 1&0\\0&i \end{bmatrix}

        Args:
            which_qubit (int): 作用在的 qubit 的编号，其值应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数
        """
        assert 0 <= which_qubit < self.n, "the qubit should >= 0 and < n (the number of qubit)"
        self.__history.append(['s', [which_qubit], [paddle.to_tensor(np.array([0.0])),
                                                    paddle.to_tensor(np.array([0.0])),
                                                    paddle.to_tensor(np.array([math.pi / 2]))]])

    def t(self, which_qubit):
        r"""添加一个单量子比特的 T 门。

        其矩阵形式为：

        .. math::

            T = \begin{bmatrix} 1&0\\0&e^\frac{i\pi}{4} \end{bmatrix}

        Args:
            which_qubit (int): 作用在的 qubit 的编号，其值应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数
        """
        assert 0 <= which_qubit < self.n, "the qubit should >= 0 and < n (the number of qubit)"
        self.__history.append(['t', [which_qubit], [paddle.to_tensor(np.array([0.0])),
                                                    paddle.to_tensor(np.array([0.0])),
                                                    paddle.to_tensor(np.array([math.pi / 4]))]])

    def u3(self, theta, phi, lam, which_qubit):
        r"""添加一个单量子比特的旋转门。

        其矩阵形式为：

        .. math::
        
            \begin{align}
            U3(\theta, \phi, \lambda) =
            \begin{bmatrix}
                \cos\frac\theta2&-e^{i\lambda}\sin\frac\theta2\\
                e^{i\phi}\sin\frac\theta2&e^{i(\phi+\lambda)}\cos\frac\theta2
            \end{bmatrix}
            \end{align}

        Args:
              theta (Tensor): 旋转角度 :math:`\theta` 。
              phi (Tensor): 旋转角度 :math:`\phi` 。
              lam (Tensor): 旋转角度 :math:`\lambda` 。
              which_qubit (int): 作用在的 qubit 的编号，其值应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数
        """
        assert 0 <= which_qubit < self.n, "the qubit should >= 0 and < n (the number of qubit)"
        self.__history.append(['u', [which_qubit], [theta, phi, lam]])

    def rxx(self, theta, which_qubits):
        r"""添加一个 RXX 门。

        其矩阵形式为：

        .. math::

            \begin{align}
            RXX(\theta) =
            \begin{bmatrix} 
                \cos\frac{\theta}{2} & 0 & 0 & -i\sin\frac{\theta}{2} \\ 
                0 & \cos\frac{\theta}{2} & -i\sin\frac{\theta}{2} & 0 \\ 
                0 & -i\sin\frac{\theta}{2} & \cos\frac{\theta}{2} & 0 \\ 
                -i\sin\frac{\theta}{2} & 0 & 0 & \cos\frac{\theta}{2}
            \end{bmatrix}
            \end{align}

        Args:
            theta (Tensor): 旋转角度
            which_qubits (list): 作用在的两个量子比特的编号，其值都应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数

        ..  code-block:: python

            import numpy as np
            import paddle
            from paddle_quantum.circuit import UAnsatz
            num_qubits = 2
            cir = UAnsatz(num_qubits)
            cir.rxx(paddle.to_tensor(np.array([np.pi/2])), [0, 1])
        """
        assert 0 <= which_qubits[0] < self.n and 0 <= which_qubits[1] < self.n, \
            "the qubit should >= 0 and < n (the number of qubit)"
        assert which_qubits[0] != which_qubits[1], "the indices of two qubits should be different"
        self.__history.append(['RXX_gate', which_qubits, theta])

    def ryy(self, theta, which_qubits):
        r"""添加一个 RYY 门。

        其矩阵形式为：

        .. math::

            \begin{align}
            RYY(\theta) =
            \begin{bmatrix} 
                \cos\frac{\theta}{2} & 0 & 0 & i\sin\frac{\theta}{2} \\ 
                0 & \cos\frac{\theta}{2} & -i\sin\frac{\theta}{2} & 0 \\ 
                0 & -i\sin\frac{\theta}{2} & \cos\frac{\theta}{2} & 0 \\ 
                i\sin\frac{\theta}{2} & 0 & 0 & cos\frac{\theta}{2}
            \end{bmatrix}
            \end{align}

        Args:
            theta (Tensor): 旋转角度
            which_qubits (list): 作用在的两个量子比特的编号，其值都应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数

        ..  code-block:: python

            import numpy as np
            import paddle
            from paddle_quantum.circuit import UAnsatz
            num_qubits = 2
            cir = UAnsatz(num_qubits)
            cir.ryy(paddle.to_tensor(np.array([np.pi/2])), [0, 1])
        """
        assert 0 <= which_qubits[0] < self.n and 0 <= which_qubits[1] < self.n, \
            "the qubit should >= 0 and < n (the number of qubit)"
        assert which_qubits[0] != which_qubits[1], "the indices of two qubits should be different"
        self.__history.append(['RYY_gate', which_qubits, theta])

    def rzz(self, theta, which_qubits):
        r"""添加一个 RZZ 门。

        其矩阵形式为：

        .. math::

            \begin{align}
            RZZ(\theta) =
            \begin{bmatrix} 
                e^{-i\frac{\theta}{2}} & 0 & 0 & 0 \\ 
                0 & e^{i\frac{\theta}{2}} & 0 & 0 \\ 
                0 & 0 & e^{i\frac{\theta}{2}} & 0 \\ 
                0 & 0 & 0 & e^{-i\frac{\theta}{2}}
            \end{bmatrix}
            \end{align}

        Args:
            theta (Tensor): 旋转角度
            which_qubits (list): 作用在的两个量子比特的编号，其值都应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数

        ..  code-block:: python

            import numpy as np
            import paddle
            from paddle_quantum.circuit import UAnsatz
            num_qubits = 2
            cir = UAnsatz(num_qubits)
            cir.rzz(paddle.to_tensor(np.array([np.pi/2])), [0, 1])
        """
        assert 0 <= which_qubits[0] < self.n and 0 <= which_qubits[1] < self.n, \
            "the qubit should >= 0 and < n (the number of qubit)"
        assert which_qubits[0] != which_qubits[1], "the indices of two qubits should be different"
        self.__history.append(['RZZ_gate', which_qubits, theta])

    def ms(self, which_qubits):
        r"""添加一个 Mølmer-Sørensen (MS) 门，用于离子阱设备。

        其矩阵形式为：

        .. math::

            \begin{align}
            MS = RXX(-\frac{\pi}{2}) = \frac{1}{\sqrt{2}}
            \begin{bmatrix}
                1 & 0 & 0 & i \\ 
                0 & 1 & i & 0 \\ 
                0 & i & 1 & 0 \\ 
                i & 0 & 0 & 1 
            \end{bmatrix}
            \end{align}

        Args:
            which_qubits (list): 作用在的两个量子比特的编号，其值都应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数

        Note:
            参考文献 https://arxiv.org/abs/quant-ph/9810040

        ..  code-block:: python

            import numpy as np
            import paddle
            from paddle_quantum.circuit import UAnsatz
            num_qubits = 2
            cir = UAnsatz(num_qubits)
            cir.ms([0, 1])
        """
        assert 0 <= which_qubits[0] < self.n and 0 <= which_qubits[1] < self.n, \
            "the qubit should >= 0 and < n(the number of qubit)"
        assert which_qubits[0] != which_qubits[1], "the indices of two qubits should be different"
        self.__history.append(['MS_gate', which_qubits, paddle.to_tensor(-np.array([np.pi / 2]))])

    def universal_2_qubit_gate(self, theta, which_qubits):
        r"""添加 2-qubit 通用门，这个通用门需要 15 个参数。

        Args:
            theta (Tensor): 2-qubit 通用门的参数，其维度为 ``(15, )``
            which_qubits(list): 作用的量子比特编号

        代码示例:

        .. code-block:: python

            import numpy as np
            import paddle
            from paddle_quantum.circuit import UAnsatz
            n = 2
            theta = paddle.to_tensor(np.ones(15))
            cir = UAnsatz(n)
            cir.universal_2_qubit_gate(theta, [0, 1])
            cir.run_state_vector()
            print(cir.measure(shots = 0))

        ::

            {'00': 0.4306256106527819, '01': 0.07994547866706268, '10': 0.07994547866706264, '11': 0.40948343201309334}
        """
 
        assert len(theta.shape) == 1, 'The shape of theta is not right'
        assert len(theta) == 15, 'This Ansatz accepts 15 parameters'
        assert len(which_qubits) == 2, "You should add this gate on two qubits"

        a, b = which_qubits
    
        self.u3(theta[0], theta[1], theta[2], a)
        self.u3(theta[3], theta[4], theta[5], b)
        self.cnot([b, a])
        self.rz(theta[6], a)
        self.ry(theta[7], b)
        self.cnot([a, b])
        self.ry(theta[8], b)
        self.cnot([b, a])
        self.u3(theta[9], theta[10], theta[11], a)
        self.u3(theta[12], theta[13], theta[14], b)

    def __u3qg_U(self, theta, which_qubits):
        r"""
        用于构建 universal_3_qubit_gate
        """
        self.cnot(which_qubits[1:])
        self.ry(theta[0], which_qubits[1])
        self.cnot(which_qubits[:2])
        self.ry(theta[1], which_qubits[1])
        self.cnot(which_qubits[:2])
        self.cnot(which_qubits[1:])
        self.h(which_qubits[2])
        self.cnot([which_qubits[1], which_qubits[0]])
        self.cnot([which_qubits[0], which_qubits[2]])
        self.cnot(which_qubits[1:])
        self.rz(theta[2], which_qubits[2])
        self.cnot(which_qubits[1:])
        self.cnot([which_qubits[0], which_qubits[2]])

    def __u3qg_V(self, theta, which_qubits):
        r"""
        用于构建 universal_3_qubit_gate
        """
        self.cnot([which_qubits[2], which_qubits[0]])
        self.cnot(which_qubits[:2])
        self.cnot([which_qubits[2], which_qubits[1]])
        self.ry(theta[0], which_qubits[2])
        self.cnot(which_qubits[1:])
        self.ry(theta[1], which_qubits[2])
        self.cnot(which_qubits[1:])
        self.s(which_qubits[2])
        self.cnot([which_qubits[2], which_qubits[0]])
        self.cnot(which_qubits[:2])
        self.cnot([which_qubits[1], which_qubits[0]])
        self.h(which_qubits[2])
        self.cnot([which_qubits[0], which_qubits[2]])
        self.rz(theta[2], which_qubits[2])
        self.cnot([which_qubits[0], which_qubits[2]])

    def universal_3_qubit_gate(self, theta, which_qubits):
        r"""添加 3-qubit 通用门，这个通用门需要 81 个参数。

        Note:
            参考: https://cds.cern.ch/record/708846/files/0401178.pdf

        Args:
            theta (Tensor): 3-qubit 通用门的参数，其维度为 ``(81, )``
            which_qubits(list): 作用的量子比特编号

        代码示例:

        .. code-block:: python

            import numpy as np
            import paddle
            from paddle_quantum.circuit import UAnsatz
            n = 3
            theta = paddle.to_tensor(np.ones(81))
            cir = UAnsatz(n)
            cir.universal_3_qubit_gate(theta, [0, 1, 2])
            cir.run_state_vector()
            print(cir.measure(shots = 0))

        ::

            {'000': 0.06697926831547105, '001': 0.13206788591381013, '010': 0.2806525391078656, '011': 0.13821526515701105, '100': 0.1390530116439897, '101': 0.004381404333075108, '110': 0.18403296778911565, '111': 0.05461765773966483}
        """
        assert len(which_qubits) == 3, "You should add this gate on three qubits"
        assert len(theta) == 81, "The length of theta is supposed to be 81"

        psi = reshape(x=theta[: 60], shape=[4, 15])
        phi = reshape(x=theta[60:], shape=[7, 3])
        self.universal_2_qubit_gate(psi[0], which_qubits[:2])
        self.u3(phi[0][0], phi[0][1], phi[0][2], which_qubits[2])

        self.__u3qg_U(phi[1], which_qubits)

        self.universal_2_qubit_gate(psi[1], which_qubits[:2])
        self.u3(phi[2][0], phi[2][1], phi[2][2], which_qubits[2])

        self.__u3qg_V(phi[3], which_qubits)

        self.universal_2_qubit_gate(psi[2], which_qubits[:2])
        self.u3(phi[4][0], phi[4][1], phi[4][2], which_qubits[2])

        self.__u3qg_U(phi[5], which_qubits)

        self.universal_2_qubit_gate(psi[3], which_qubits[:2])
        self.u3(phi[6][0], phi[6][1], phi[6][2], which_qubits[2])

    """
    Measurements
    """

    def __process_string(self, s, which_qubits):
        r"""
        This functions return part of string s baesd on which_qubits
        If s = 'abcdefg', which_qubits = [0,2,5], then it returns 'acf'

        Note:
            这是内部函数，你并不需要直接调用到该函数。
        """
        new_s = ''.join(s[j] for j in which_qubits)
        return new_s

    def __process_similiar(self, result):
        r"""
        This functions merges values based on identical keys.
        If result = [('00', 10), ('01', 20), ('11', 30), ('11', 40), ('11', 50), ('00', 60)], then it returns {'00': 70, '01': 20, '11': 120}

        Note:
            这是内部函数，你并不需要直接调用到该函数。
        """
        data = defaultdict(int)
        for idx, val in result:
            data[idx] += val

        return dict(data)

    def __measure_hist(self, result, which_qubits, shots):
        r"""将测量的结果以柱状图的形式呈现。

        Note:
            这是内部函数，你并不需要直接调用到该函数。

        Args:
              result (dictionary): 测量结果
              which_qubits (list): 测量的量子比特，如测量所有则是 ``None``
              shots(int): 测量次数

        Returns
            dict: 测量结果

        """
        n = self.n if which_qubits is None else len(which_qubits)
        assert n < 6, "Too many qubits to plot"

        ylabel = "Measured Probabilities"
        if shots == 0:
            shots = 1
            ylabel = "Probabilities"

        state_list = [np.binary_repr(index, width=n) for index in range(0, 2 ** n)]
        freq = []
        for state in state_list:
            freq.append(result.get(state, 0.0) / shots)

        plt.bar(range(2 ** n), freq, tick_label=state_list)
        plt.xticks(rotation=90)
        plt.xlabel("Qubit State")
        plt.ylabel(ylabel)
        plt.show()

        return result

    # Which_qubits is list-like
    def measure(self, which_qubits=None, shots=2 ** 10, plot=False):
        r"""对量子电路输出的量子态进行测量。

        Warning:
            当 ``plot`` 为 ``True`` 时，当前量子电路的量子比特数需要小于 6 ，否则无法绘制图片，会抛出异常。

        Args:
            which_qubits (list, optional): 要测量的qubit的编号，默认全都测量
            shots (int, optional): 该量子电路输出的量子态的测量次数，默认为 1024 次；若为 0，则返回测量结果的精确概率分布
            plot (bool, optional): 是否绘制测量结果图，默认为 ``False`` ，即不绘制
        
        Returns:
            dict: 测量的结果

        代码示例:

        .. code-block:: python
        
            import paddle
            from paddle_quantum.circuit import UAnsatz
            cir = UAnsatz(2)
            cir.h(0)
            cir.cnot([0,1])
            cir.run_state_vector()
            result = cir.measure(shots = 2048, which_qubits = [1])
            print(f"The results of measuring qubit 1 2048 times are {result}")

        ::

            The results of measuring qubit 1 2048 times are {'0': 964, '1': 1084}

        .. code-block:: python

            import paddle
            from paddle_quantum.circuit import UAnsatz
            cir = UAnsatz(2)
            cir.h(0)
            cir.cnot([0,1])
            cir.run_state_vector()
            result = cir.measure(shots = 0, which_qubits = [1])
            print(f"The probability distribution of measurement results on qubit 1 is {result}")

        ::

            The probability distribution of measurement results on qubit 1 is {'0': 0.4999999999999999, '1': 0.4999999999999999}
        """
        if self.__run_state == 'state_vector':
            state = self.__state
        elif self.__run_state == 'density_matrix':
            # Take the diagonal of the density matrix as a probability distribution
            diag = np.diag(self.__state.numpy())
            state = paddle.to_tensor(np.sqrt(diag))
        else:
            # Raise error
            raise ValueError("no state for measurement; please run the circuit first")

        if shots == 0:  # Returns probability distribution over all measurement results
            dic2to10, dic10to2 = dic_between2and10(self.n)
            result = {}
            for i in range(2 ** self.n):
                result[dic10to2[i]] = (real(state)[i] ** 2 + imag(state)[i] ** 2).numpy()[0]

            if which_qubits is not None:
                new_result = [(self.__process_string(key, which_qubits), value) for key, value in result.items()]
                result = self.__process_similiar(new_result)
        else:
            if which_qubits is None:  # Return all the qubits
                result = measure_state(state, shots)
            else:
                assert all([e < self.n for e in which_qubits]), 'Qubit index out of range'
                which_qubits.sort()  # Sort in ascending order

                collapse_all = measure_state(state, shots)
                new_collapse_all = [(self.__process_string(key, which_qubits), value) for key, value in
                                    collapse_all.items()]
                result = self.__process_similiar(new_collapse_all)

        return result if not plot else self.__measure_hist(result, which_qubits, shots)

    def expecval(self, H):
        r"""量子电路输出的量子态关于可观测量 H 的期望值。

        Hint:
            如果想输入的可观测量的矩阵为 :math:`0.7Z\otimes X\otimes I+0.2I\otimes Z\otimes I` 。则 ``H`` 应为 ``[[0.7, 'z0,x1'], [0.2, 'z1']]`` 。
        Args:
            H (list): 可观测量的相关信息
        Returns:
            Tensor: 量子电路输出的量子态关于 H 的期望值

        代码示例:
        
        .. code-block:: python
            
            import paddle
            from paddle_quantum.circuit import UAnsatz
            n = 5
            H_info = [[0.1, 'x1'], [0.2, 'y0,z4']]
            theta = paddle.ones([3], dtype='float64')
            cir = UAnsatz(n)
            cir.rx(theta[0], 0)
            cir.rz(theta[1], 1)
            cir.rx(theta[2], 2)
            cir.run_state_vector()
            expect_value = cir.expecval(H_info).numpy()
            print(f'Calculated expectation value of {H_info} is {expect_value}')

        ::

            Calculated expectation value of [[0.1, 'x1'], [0.2, 'y0,z4']] is [-0.1682942]

        """
        if self.__run_state == 'state_vector':
            return real(vec_expecval(H, self.__state))
        elif self.__run_state == 'density_matrix':
            state = self.__state
            H_mat = paddle.to_tensor(pauli_str_to_matrix(H, self.n))
            return real(trace(matmul(state, H_mat)))
        else:
            # Raise error
            raise ValueError("no state for measurement; please run the circuit first")

    """
    Circuit Templates
    """

    def superposition_layer(self):
        r"""添加一层 Hadamard 门。

        代码示例:

        .. code-block:: python
        
            import paddle
            from paddle_quantum.circuit import UAnsatz
            cir = UAnsatz(2)
            cir.superposition_layer()
            cir.run_state_vector()
            result = cir.measure(shots = 0)
            print(f"The probability distribution of measurement results on both qubits is {result}")

        ::

            The probability distribution of measurement results on both qubits is {'00': 0.2499999999999999, '01': 0.2499999999999999, '10': 0.2499999999999999, '11': 0.2499999999999999}
        """
        for i in range(self.n):
            self.h(i)

    def weak_superposition_layer(self):
        r"""添加一层旋转角度为 :math:`\pi/4` 的 Ry 门。

        代码示例:

        .. code-block:: python
        
            import paddle
            from paddle_quantum.circuit import UAnsatz
            cir = UAnsatz(2)
            cir.weak_superposition_layer()
            cir.run_state_vector()
            result = cir.measure(shots = 0)
            print(f"The probability distribution of measurement results on both qubits is {result}")

        ::

            The probability distribution of measurement results on both qubits is {'00': 0.7285533905932737, '01': 0.12500000000000003, '10': 0.12500000000000003, '11': 0.021446609406726238}
        """
        _theta = paddle.to_tensor(np.array([np.pi / 4]))  # Used in fixed Ry gate
        for i in range(self.n):
            self.ry(_theta, i)

    def linear_entangled_layer(self, theta, depth, which_qubits=None):
        r"""添加 ``depth`` 层包含 Ry 门，Rz 门和 CNOT 门的线性纠缠层。

        Attention:
            ``theta`` 的维度为 ``(depth, n, 2)`` ，最低维内容为对应的 ``ry`` 和 ``rz`` 的参数。

        Args:
            theta (Tensor): Ry 门和 Rz 门的旋转角度
            depth (int): 纠缠层的深度
            which_qubits(list): 作用的量子比特编号

        代码示例:

        .. code-block:: python

            import paddle
            from paddle_quantum.circuit import UAnsatz
            n = 2
            DEPTH = 3
            theta = paddle.ones([DEPTH, n, 2], dtype='float64')
            cir = UAnsatz(n)
            cir.linear_entangled_layer(theta, DEPTH, [0, 1])
            cir.run_state_vector()
            print(cir.measure(shots = 0))

        ::

            {'00': 0.646611169077063, '01': 0.06790630495474384, '10': 0.19073671025717626, '11': 0.09474581571101756}
        """
        assert self.n > 1, 'you need at least 2 qubits'
        assert len(theta.shape) == 3, 'the shape of theta is not right'
        assert theta.shape[2] == 2, 'the shape of theta is not right'
        # assert theta.shape[1] == self.n, 'the shape of theta is not right'
        assert theta.shape[0] == depth, 'the depth of theta has a mismatch'

        if which_qubits is None:
            which_qubits = np.arange(self.n)

        for repeat in range(depth):
            for i, q in enumerate(which_qubits):
                self.ry(theta[repeat][i][0], q)
            for i in range(len(which_qubits) - 1):
                self.cnot([which_qubits[i], which_qubits[i + 1]])
            for i, q in enumerate(which_qubits):
                self.rz(theta[repeat][i][1], q)
            for i in range(len(which_qubits) - 1):
                self.cnot([which_qubits[i + 1], which_qubits[i]])

    def real_entangled_layer(self, theta, depth, which_qubits=None):
        r"""添加 ``depth`` 层包含 Ry 门和 CNOT 门的强纠缠层。

        Note:
            这一层量子门的数学表示形式为实数酉矩阵。

        Attention:
            ``theta`` 的维度为 ``(depth, n, 1)`` 。

        Args:
            theta (Tensor): Ry 门的旋转角度
            depth (int): 纠缠层的深度
            which_qubits(list): 作用的量子比特编号

        代码示例:

        .. code-block:: python

            import paddle
            from paddle_quantum.circuit import UAnsatz
            n = 2
            DEPTH = 3
            theta = paddle.ones([DEPTH, n, 1], dtype='float64')
            cir = UAnsatz(n)
            cir.real_entangled_layer(paddle.to_tensor(theta), DEPTH, [0, 1])
            cir.run_state_vector()
            print(cir.measure(shots = 0))
        
        ::

            {'00': 2.52129874867343e-05, '01': 0.295456784923382, '10': 0.7045028818254718, '11': 1.5120263659845063e-05}
        """
        assert self.n > 1, 'you need at least 2 qubits'
        assert len(theta.shape) == 3, 'the shape of theta is not right'
        assert theta.shape[2] == 1, 'the shape of theta is not right'
        # assert theta.shape[1] == self.n, 'the shape of theta is not right'
        assert theta.shape[0] == depth, 'the depth of theta has a mismatch'

        if which_qubits is None:
            which_qubits = np.arange(self.n)

        for repeat in range(depth):
            for i, q in enumerate(which_qubits):
                self.ry(theta[repeat][i][0], q)
            for i in range(len(which_qubits) - 1):
                self.cnot([which_qubits[i], which_qubits[i + 1]])
            self.cnot([which_qubits[-1], which_qubits[0]])

    def complex_entangled_layer(self, theta, depth, which_qubits=None):
        r"""添加 ``depth`` 层包含 U3 门和 CNOT 门的强纠缠层。

        Note:
            这一层量子门的数学表示形式为复数酉矩阵。
        
        Attention:
            ``theta`` 的维度为 ``(depth, n, 3)`` ，最低维内容为对应的 ``u3`` 的参数 ``(theta, phi, lam)`` 。
        
        Args:
            theta (Tensor): U3 门的旋转角度
            depth (int): 纠缠层的深度
            which_qubits(list): 作用的量子比特编号

        代码示例:

        .. code-block:: python
        
            import paddle
            from paddle_quantum.circuit import UAnsatz
            n = 2
            DEPTH = 3
            theta = paddle.ones([DEPTH, n, 3], dtype='float64')
            cir = UAnsatz(n)
            cir.complex_entangled_layer(paddle.to_tensor(theta), DEPTH, [0, 1])
            cir.run_state_vector()
            print(cir.measure(shots = 0))
        
        ::

            {'00': 0.15032627279218896, '01': 0.564191201239618, '10': 0.03285998070292556, '11': 0.25262254526526823}
        """
        assert self.n > 1, 'you need at least 2 qubits'
        assert len(theta.shape) == 3, 'the shape of theta is not right'
        assert theta.shape[2] == 3, 'the shape of theta is not right'
        # assert theta.shape[1] == self.n, 'the shape of theta is not right'
        assert theta.shape[0] == depth, 'the depth of theta has a mismatch'

        if which_qubits is None:
            which_qubits = np.arange(self.n)

        for repeat in range(depth):
            for i, q in enumerate(which_qubits):
                self.u3(theta[repeat][i][0], theta[repeat][i][1], theta[repeat][i][2], q)
            for i in range(len(which_qubits) - 1):
                self.cnot([which_qubits[i], which_qubits[i + 1]])
            self.cnot([which_qubits[-1], which_qubits[0]])

    def __add_real_block(self, theta, position):
        r"""
        Add a real block to the circuit in (position). theta is a one dimensional tensor

        Note:
            这是内部函数，你并不需要直接调用到该函数。
        """
        assert len(theta) == 4, 'the length of theta is not right'
        assert 0 <= position[0] < self.n and 0 <= position[1] < self.n, 'position is out of range'
        self.ry(theta[0], position[0])
        self.ry(theta[1], position[1])

        self.cnot([position[0], position[1]])

        self.ry(theta[2], position[0])
        self.ry(theta[3], position[1])

    def __add_complex_block(self, theta, position):
        r"""
        Add a complex block to the circuit in (position). theta is a one dimensional tensor

        Note:
            这是内部函数，你并不需要直接调用到该函数。
        """
        assert len(theta) == 12, 'the length of theta is not right'
        assert 0 <= position[0] < self.n and 0 <= position[1] < self.n, 'position is out of range'
        self.u3(theta[0], theta[1], theta[2], position[0])
        self.u3(theta[3], theta[4], theta[5], position[1])

        self.cnot([position[0], position[1]])

        self.u3(theta[6], theta[7], theta[8], position[0])
        self.u3(theta[9], theta[10], theta[11], position[1])

    def __add_real_layer(self, theta, position):
        r"""
        Add a real layer on the circuit. theta is a two dimensional tensor. position is the qubit range the layer needs to cover

        Note:
            这是内部函数，你并不需要直接调用到该函数。
        """
        assert theta.shape[1] == 4 and theta.shape[0] == (position[1] - position[0] + 1) / 2,\
            'the shape of theta is not right'
        for i in range(position[0], position[1], 2):
            self.__add_real_block(theta[int((i - position[0]) / 2)], [i, i + 1])

    def __add_complex_layer(self, theta, position):
        r"""
        Add a complex layer on the circuit. theta is a two dimensional tensor. position is the qubit range the layer needs to cover

        Note:
            这是内部函数，你并不需要直接调用到该函数。
        """
        assert theta.shape[1] == 12 and theta.shape[0] == (position[1] - position[0] + 1) / 2,\
            'the shape of theta is not right'
        for i in range(position[0], position[1], 2):
            self.__add_complex_block(theta[int((i - position[0]) / 2)], [i, i + 1])

    def real_block_layer(self, theta, depth):
        r"""添加 ``depth`` 层包含 Ry 门和 CNOT 门的弱纠缠层。

        Note:
            这一层量子门的数学表示形式为实数酉矩阵。
        
        Attention:
            ``theta`` 的维度为 ``(depth, n-1, 4)`` 。
        
        Args:
            theta(Tensor): Ry 门的旋转角度
            depth(int): 纠缠层的深度

        代码示例:

        .. code-block:: python
        
            import paddle
            from paddle_quantum.circuit import UAnsatz
            n = 4
            DEPTH = 3
            theta = paddle.ones([DEPTH, n - 1, 4], dtype='float64')
            cir = UAnsatz(n)
            cir.real_block_layer(paddle.to_tensor(theta), DEPTH)
            cir.run_density_matrix()
            print(cir.measure(shots = 0, which_qubits = [0]))
        
        ::

            {'0': 0.9646724056906162, '1': 0.035327594309385896}
        """
        assert self.n > 1, 'you need at least 2 qubits'
        assert len(theta.shape) == 3, 'The dimension of theta is not right'
        _depth, m, block = theta.shape
        assert depth > 0, 'depth must be greater than zero'
        assert _depth == depth, 'the depth of parameters has a mismatch'
        assert m == self.n - 1 and block == 4, 'The shape of theta is not right'

        if self.n % 2 == 0:
            for i in range(depth):
                self.__add_real_layer(theta[i][:int(self.n / 2)], [0, self.n - 1])
                self.__add_real_layer(theta[i][int(self.n / 2):], [1, self.n - 2]) if self.n > 2 else None
        else:
            for i in range(depth):
                self.__add_real_layer(theta[i][:int((self.n - 1) / 2)], [0, self.n - 2])
                self.__add_real_layer(theta[i][int((self.n - 1) / 2):], [1, self.n - 1])

    def complex_block_layer(self, theta, depth):
        r"""添加 ``depth`` 层包含 U3 门和 CNOT 门的弱纠缠层。

        Note:
            这一层量子门的数学表示形式为复数酉矩阵。

        Attention:
            ``theta`` 的维度为 ``(depth, n-1, 12)`` 。

        Args:
            theta (Tensor): U3 门的角度信息
            depth (int): 纠缠层的深度

        代码示例:

        .. code-block:: python
        
            import paddle
            from paddle_quantum.circuit import UAnsatz
            n = 4
            DEPTH = 3
            theta = paddle.ones([DEPTH, n - 1, 12], dtype='float64')
            cir = UAnsatz(n)
            cir.complex_block_layer(paddle.to_tensor(theta), DEPTH)
            cir.run_density_matrix()
            print(cir.measure(shots = 0, which_qubits = [0]))
        
        ::

            {'0': 0.5271554811768046, '1': 0.4728445188231988}
        """
        assert self.n > 1, 'you need at least 2 qubits'
        assert len(theta.shape) == 3, 'The dimension of theta is not right'
        assert depth > 0, 'depth must be greater than zero'
        _depth, m, block = theta.shape
        assert _depth == depth, 'the depth of parameters has a mismatch'
        assert m == self.n - 1 and block == 12, 'The shape of theta is not right'

        if self.n % 2 == 0:
            for i in range(depth):
                self.__add_complex_layer(theta[i][:int(self.n / 2)], [0, self.n - 1])
                self.__add_complex_layer(theta[i][int(self.n / 2):], [1, self.n - 2]) if self.n > 2 else None
        else:
            for i in range(depth):
                self.__add_complex_layer(theta[i][:int((self.n - 1) / 2)], [0, self.n - 2])
                self.__add_complex_layer(theta[i][int((self.n - 1) / 2):], [1, self.n - 1])

    """
    Channels
    """

    @apply_channel
    def amplitude_damping(self, gamma, which_qubit):
        r"""添加振幅阻尼信道。

        其 Kraus 算符为：
        
        .. math::

            E_0 = \begin{bmatrix} 1 & 0 \\ 0 & \sqrt{1-\gamma} \end{bmatrix},
            E_1 = \begin{bmatrix} 0 & \sqrt{\gamma} \\ 0 & 0 \end{bmatrix}.

        Args:
            gamma (float): 减振概率，其值应该在 :math:`[0, 1]` 区间内
            which_qubit (int): 该信道作用在的 qubit 的编号，其值应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数

        代码示例:

        .. code-block:: python

            from paddle_quantum.circuit import UAnsatz
            N = 2
            gamma = 0.1
            cir = UAnsatz(N)
            cir.h(0)
            cir.cnot([0, 1])
            cir.amplitude_damping(gamma, 0)
            final_state = cir.run_density_matrix()
            print(final_state.numpy())

        ::

            [[0.5       +0.j 0.        +0.j 0.        +0.j 0.47434165+0.j]
             [0.        +0.j 0.05      +0.j 0.        +0.j 0.        +0.j]
             [0.        +0.j 0.        +0.j 0.        +0.j 0.        +0.j]
             [0.47434165+0.j 0.        +0.j 0.        +0.j 0.45      +0.j]]
        """
        assert 0 <= gamma <= 1, 'the parameter gamma should be in range [0, 1]'

        e0 = paddle.to_tensor([[1, 0], [0, np.sqrt(1 - gamma)]], dtype='complex128')
        e1 = paddle.to_tensor([[0, np.sqrt(gamma)], [0, 0]], dtype='complex128')

        return [e0, e1]

    @apply_channel
    def generalized_amplitude_damping(self, gamma, p, which_qubit):
        r"""添加广义振幅阻尼信道。

        其 Kraus 算符为：

        .. math::

            E_0 = \sqrt{p} \begin{bmatrix} 1 & 0 \\ 0 & \sqrt{1-\gamma} \end{bmatrix},
            E_1 = \sqrt{p} \begin{bmatrix} 0 & \sqrt{\gamma} \\ 0 & 0 \end{bmatrix},\\
            E_2 = \sqrt{1-p} \begin{bmatrix} \sqrt{1-\gamma} & 0 \\ 0 & 1 \end{bmatrix},
            E_3 = \sqrt{1-p} \begin{bmatrix} 0 & 0 \\ \sqrt{\gamma} & 0 \end{bmatrix}.

        Args:
            gamma (float): 减振概率，其值应该在 :math:`[0, 1]` 区间内
            p (float): 激发概率，其值应该在 :math:`[0, 1]` 区间内
            which_qubit (int): 该信道作用在的 qubit 的编号，其值应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数

        代码示例:

        .. code-block:: python

            from paddle_quantum.circuit import UAnsatz
            N = 2
            gamma = 0.1
            p = 0.2
            cir = UAnsatz(N)
            cir.h(0)
            cir.cnot([0, 1])
            cir.generalized_amplitude_damping(gamma, p, 0)
            final_state = cir.run_density_matrix()
            print(final_state.numpy())

        ::

            [[0.46      +0.j 0.        +0.j 0.        +0.j 0.47434165+0.j]
             [0.        +0.j 0.01      +0.j 0.        +0.j 0.        +0.j]
             [0.        +0.j 0.        +0.j 0.04      +0.j 0.        +0.j]
             [0.47434165+0.j 0.        +0.j 0.        +0.j 0.49      +0.j]]
        """
        assert 0 <= gamma <= 1, 'the parameter gamma should be in range [0, 1]'
        assert 0 <= p <= 1, 'The parameter p should be in range [0, 1]'

        e0 = paddle.to_tensor(np.sqrt(p) * np.array([[1, 0], [0, np.sqrt(1 - gamma)]], dtype='complex128'))
        e1 = paddle.to_tensor(np.sqrt(p) * np.array([[0, np.sqrt(gamma)], [0, 0]]), dtype='complex128')
        e2 = paddle.to_tensor(np.sqrt(1 - p) * np.array([[np.sqrt(1 - gamma), 0], [0, 1]], dtype='complex128'))
        e3 = paddle.to_tensor(np.sqrt(1 - p) * np.array([[0, 0], [np.sqrt(gamma), 0]]), dtype='complex128')

        return [e0, e1, e2, e3]

    @apply_channel
    def phase_damping(self, gamma, which_qubit):
        r"""添加相位阻尼信道。

        其 Kraus 算符为：

        .. math::

            E_0 = \begin{bmatrix} 1 & 0 \\ 0 & \sqrt{1-\gamma} \end{bmatrix},
            E_1 = \begin{bmatrix} 0 & 0 \\ 0 & \sqrt{\gamma} \end{bmatrix}.

        Args:
            gamma (float): phase damping 信道的参数，其值应该在 :math:`[0, 1]` 区间内
            which_qubit (int): 该信道作用在的 qubit 的编号，其值应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数

        代码示例:

        .. code-block:: python

            from paddle_quantum.circuit import UAnsatz
            N = 2
            p = 0.1
            cir = UAnsatz(N)
            cir.h(0)
            cir.cnot([0, 1])
            cir.phase_damping(p, 0)
            final_state = cir.run_density_matrix()
            print(final_state.numpy())

        ::

            [[0.5       +0.j 0.        +0.j 0.        +0.j 0.47434165+0.j]
             [0.        +0.j 0.        +0.j 0.        +0.j 0.        +0.j]
             [0.        +0.j 0.        +0.j 0.        +0.j 0.        +0.j]
             [0.47434165+0.j 0.        +0.j 0.        +0.j 0.5       +0.j]]
        """
        assert 0 <= gamma <= 1, 'the parameter gamma should be in range [0, 1]'

        e0 = paddle.to_tensor([[1, 0], [0, np.sqrt(1 - gamma)]], dtype='complex128')
        e1 = paddle.to_tensor([[0, 0], [0, np.sqrt(gamma)]], dtype='complex128')

        return [e0, e1]

    @apply_channel
    def bit_flip(self, p, which_qubit):
        r"""添加比特反转信道。

        其 Kraus 算符为：

        .. math::

            E_0 = \sqrt{1-p} I,
            E_1 = \sqrt{p} X.

        Args:
            p (float): 发生 bit flip 的概率，其值应该在 :math:`[0, 1]` 区间内
            which_qubit (int): 该信道作用在的 qubit 的编号，其值应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数

        代码示例:

        .. code-block:: python

            from paddle_quantum.circuit import UAnsatz
            N = 2
            p = 0.1
            cir = UAnsatz(N)
            cir.h(0)
            cir.cnot([0, 1])
            cir.bit_flip(p, 0)
            final_state = cir.run_density_matrix()
            print(final_state.numpy())

        ::

            [[0.45+0.j 0.  +0.j 0.  +0.j 0.45+0.j]
             [0.  +0.j 0.05+0.j 0.05+0.j 0.  +0.j]
             [0.  +0.j 0.05+0.j 0.05+0.j 0.  +0.j]
             [0.45+0.j 0.  +0.j 0.  +0.j 0.45+0.j]]
        """
        assert 0 <= p <= 1, 'the probability p of a bit flip should be in range [0, 1]'

        e0 = paddle.to_tensor([[np.sqrt(1-p), 0], [0, np.sqrt(1-p)]], dtype='complex128')
        e1 = paddle.to_tensor([[0, np.sqrt(p)], [np.sqrt(p), 0]], dtype='complex128')

        return [e0, e1]

    @apply_channel
    def phase_flip(self, p, which_qubit):
        r"""添加相位反转信道。

        其 Kraus 算符为：

        .. math::

            E_0 = \sqrt{1 - p} I,
            E_1 = \sqrt{p} Z.

        Args:
            p (float): 发生 phase flip 的概率，其值应该在 :math:`[0, 1]` 区间内
            which_qubit (int): 该信道作用在的 qubit 的编号，其值应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数

        代码示例:

        .. code-block:: python

            from paddle_quantum.circuit import UAnsatz
            N = 2
            p = 0.1
            cir = UAnsatz(N)
            cir.h(0)
            cir.cnot([0, 1])
            cir.phase_flip(p, 0)
            final_state = cir.run_density_matrix()
            print(final_state.numpy())

        ::

            [[0.5+0.j 0. +0.j 0. +0.j 0.4+0.j]
             [0. +0.j 0. +0.j 0. +0.j 0. +0.j]
             [0. +0.j 0. +0.j 0. +0.j 0. +0.j]
             [0.4+0.j 0. +0.j 0. +0.j 0.5+0.j]]
        """
        assert 0 <= p <= 1, 'the probability p of a phase flip should be in range [0, 1]'

        e0 = paddle.to_tensor([[np.sqrt(1-p), 0], [0, np.sqrt(1-p)]], dtype='complex128')
        e1 = paddle.to_tensor([[np.sqrt(p), 0], [0, -np.sqrt(p)]], dtype='complex128')

        return [e0, e1]

    @apply_channel
    def bit_phase_flip(self, p, which_qubit):
        r"""添加比特相位反转信道。

        其 Kraus 算符为：

        .. math::

            E_0 = \sqrt{1 - p} I,
            E_1 = \sqrt{p} Y.

        Args:
            p (float): 发生 bit phase flip 的概率，其值应该在 :math:`[0, 1]` 区间内
            which_qubit (int): 该信道作用在的 qubit 的编号，其值应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数

        代码示例:

        .. code-block:: python

            from paddle_quantum.circuit import UAnsatz
            N = 2
            p = 0.1
            cir = UAnsatz(N)
            cir.h(0)
            cir.cnot([0, 1])
            cir.bit_phase_flip(p, 0)
            final_state = cir.run_density_matrix()
            print(final_state.numpy())

        ::

            [[ 0.45+0.j  0.  +0.j  0.  +0.j  0.45+0.j]
             [ 0.  +0.j  0.05+0.j -0.05+0.j  0.  +0.j]
             [ 0.  +0.j -0.05+0.j  0.05+0.j  0.  +0.j]
             [ 0.45+0.j  0.  +0.j  0.  +0.j  0.45+0.j]]
        """
        assert 0 <= p <= 1, 'the probability p of a bit phase flip should be in range [0, 1]'

        e0 = paddle.to_tensor([[np.sqrt(1-p), 0], [0, np.sqrt(1-p)]], dtype='complex128')
        e1 = paddle.to_tensor([[0, -1j * np.sqrt(p)], [1j * np.sqrt(p), 0]], dtype='complex128')

        return [e0, e1]

    @apply_channel
    def depolarizing(self, p, which_qubit):
        r"""添加去极化信道。

        其 Kraus 算符为：

        .. math::

            E_0 = \sqrt{1-p} I,
            E_1 = \sqrt{p/3} X,
            E_2 = \sqrt{p/3} Y,
            E_3 = \sqrt{p/3} Z.

        Args:
            p (float): depolarizing 信道的参数，其值应该在 :math:`[0, 1]` 区间内
            which_qubit (int): 该信道作用在的 qubit 的编号，其值应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数

        代码示例:

        .. code-block:: python

            from paddle_quantum.circuit import UAnsatz
            N = 2
            p = 0.1
            cir = UAnsatz(N)
            cir.h(0)
            cir.cnot([0, 1])
            cir.depolarizing(p, 0)
            final_state = cir.run_density_matrix()
            print(final_state.numpy())

        ::

            [[0.46666667+0.j 0.        +0.j 0.        +0.j 0.43333333+0.j]
             [0.        +0.j 0.03333333+0.j 0.        +0.j 0.        +0.j]
             [0.        +0.j 0.        +0.j 0.03333333+0.j 0.        +0.j]
             [0.43333333+0.j 0.        +0.j 0.        +0.j 0.46666667+0.j]]
        """
        assert 0 <= p <= 1, 'the parameter p should be in range [0, 1]'

        e0 = paddle.to_tensor([[np.sqrt(1-p), 0], [0, np.sqrt(1-p)]], dtype='complex128')
        e1 = paddle.to_tensor([[0, np.sqrt(p/3)], [np.sqrt(p/3), 0]], dtype='complex128')
        e2 = paddle.to_tensor([[0, -1j * np.sqrt(p/3)], [1j * np.sqrt(p/3), 0]], dtype='complex128')
        e3 = paddle.to_tensor([[np.sqrt(p/3), 0], [0, -np.sqrt(p/3)]], dtype='complex128')

        return [e0, e1, e2, e3]

    @apply_channel
    def pauli_channel(self, p_x, p_y, p_z, which_qubit):
        r"""添加泡利信道。

        Args:
            p_x (float): 泡利矩阵 X 的对应概率，其值应该在 :math:`[0, 1]` 区间内
            p_y (float): 泡利矩阵 Y 的对应概率，其值应该在 :math:`[0, 1]` 区间内
            p_z (float): 泡利矩阵 Z 的对应概率，其值应该在 :math:`[0, 1]` 区间内
            which_qubit (int): 该信道作用在的 qubit 的编号，其值应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数

        Note:
            三个输入的概率加起来需要小于等于 1。

        代码示例:

        .. code-block:: python

            from paddle_quantum.circuit import UAnsatz
            N = 2
            p_x = 0.1
            p_y = 0.2
            p_z = 0.3
            cir = UAnsatz(N)
            cir.h(0)
            cir.cnot([0, 1])
            cir.pauli_channel(p_x, p_y, p_z, 0)
            final_state = cir.run_density_matrix()
            print(final_state.numpy())

        ::

            [[ 0.35+0.j  0.  +0.j  0.  +0.j  0.05+0.j]
             [ 0.  +0.j  0.15+0.j -0.05+0.j  0.  +0.j]
             [ 0.  +0.j -0.05+0.j  0.15+0.j  0.  +0.j]
             [ 0.05+0.j  0.  +0.j  0.  +0.j  0.35+0.j]]
        """
        prob_list = [p_x, p_y, p_z]
        assert sum(prob_list) <= 1, 'the sum of probabilities should be smaller than or equal to 1 '
        X = np.array([[0, 1], [1, 0]], dtype='complex128')
        Y = np.array([[0, -1j], [1j, 0]], dtype='complex128')
        Z = np.array([[1, 0], [0, -1]], dtype='complex128')
        I = np.array([[1, 0], [0, 1]], dtype='complex128')

        op_list = [X, Y, Z]
        for i, prob in enumerate(prob_list):
            assert 0 <= prob <= 1, 'the parameter p' + str(i + 1) + ' should be in range [0, 1]'
            op_list[i] = paddle.to_tensor(np.sqrt(prob_list[i]) * op_list[i])
        op_list.append(paddle.to_tensor(np.sqrt(1 - sum(prob_list)) * I))

        return op_list

    @apply_channel
    def reset(self, p, q, which_qubit):
        r"""添加重置信道。有 p 的概率将量子态重置为 :math:`|0\rangle` 并有 q 的概率重置为 :math:`|1\rangle`。
        
        其 Kraus 算符为：
        
        .. math::
        
            E_0 = \begin{bmatrix} \sqrt{p} & 0 \\ 0 & 0 \end{bmatrix},
            E_1 = \begin{bmatrix} 0 & \sqrt{p} \\ 0 & 0 \end{bmatrix},\\
            E_2 = \begin{bmatrix} 0 & 0 \\ \sqrt{q} & 0 \end{bmatrix},
            E_3 = \begin{bmatrix} 0 & 0 \\ 0 & \sqrt{q} \end{bmatrix},\\
            E_4 = \sqrt{1-p-q} I.
            
        Args:
            p (float): 重置为 :math:`|0\rangle`的概率，其值应该在 :math:`[0, 1]` 区间内
            q (float): 重置为 :math:`|1\rangle`的概率，其值应该在 :math:`[0, 1]` 区间内
            which_qubit (int): 该信道作用在的 qubit 的编号，其值应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数
        
        Note:
            两个输入的概率加起来需要小于等于 1。
        
        代码示例:
        
        .. code-block:: python
        
            from paddle_quantum.circuit import UAnsatz
            N = 2
            p = 1
            q = 0
            cir = UAnsatz(N)
            cir.h(0)
            cir.cnot([0, 1])
            cir.reset(p, q, 0)
            final_state = cir.run_density_matrix()
            print(final_state.numpy())
            
        ::
        
            [[0.5+0.j 0. +0.j 0. +0.j 0. +0.j]
             [0. +0.j 0.5+0.j 0. +0.j 0. +0.j]
             [0. +0.j 0. +0.j 0. +0.j 0. +0.j]
             [0. +0.j 0. +0.j 0. +0.j 0. +0.j]]
        """
        assert p + q <= 1, 'the sum of probabilities should be smaller than or equal to 1 '
        
        e0 = paddle.to_tensor([[np.sqrt(p), 0], [0, 0]], dtype='complex128')
        e1 = paddle.to_tensor([[0, np.sqrt(p)], [0, 0]], dtype='complex128')
        e2 = paddle.to_tensor([[0, 0], [np.sqrt(q), 0]], dtype='complex128')
        e3 = paddle.to_tensor([[0, 0], [0, np.sqrt(q)]], dtype='complex128')
        e4 = paddle.to_tensor([[np.sqrt(1 - (p + q)), 0], [0, np.sqrt(1 - (p + q))]], dtype='complex128')
        
        return [e0, e1, e2, e3, e4]
        
    @apply_channel
    def thermal_relaxation(self, t1, t2, time, which_qubit):
        r"""添加热弛豫信道，模拟超导硬件上的 T1 和 T2 混合过程。

        Args:
            t1 (float): :math:`T_1` 过程的弛豫时间常数，单位是微秒
            t2 (float): :math:`T_2` 过程的弛豫时间常数，单位是微秒
            time (float): 弛豫过程中量子门的执行时间，单位是纳秒
            which_qubit (int): 该信道作用在的 qubit 的编号，其值应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数

        Note:
            时间常数必须满足 :math:`T_2 \le T_1`，参考文献 https://arxiv.org/abs/2101.02109

        代码示例:

        .. code-block:: python

            from paddle_quantum.circuit import UAnsatz
            N = 2
            t1 = 30
            t2 = 20
            tg = 200
            cir = UAnsatz(N)
            cir.h(0)
            cir.cnot([0, 1])
            cir.thermal_relaxation(t1, t2, tg, 0)
            cir.thermal_relaxation(t1, t2, tg, 1)
            final_state = cir.run_density_matrix()
            print(final_state.numpy())

        ::

            [[0.5   +0.j 0.    +0.j 0.    +0.j 0.4901+0.j]
             [0.    +0.j 0.0033+0.j 0.    +0.j 0.    +0.j]
             [0.    +0.j 0.    +0.j 0.0033+0.j 0.    +0.j]
             [0.4901+0.j 0.    +0.j 0.    +0.j 0.4934+0.j]]

        """
        assert 0 <= t2 <= t1, 'Relaxation time constants are not valid as 0 <= T2 <= T1!'
        assert 0 <= time, 'Invalid gate time!'
        
        # Change time scale
        time = time / 1000
        # Probability of resetting the state to |0>
        p_reset = 1 - np.exp(-time / t1)          
        # Probability of phase flip
        p_z = (1 - p_reset) * (1 - np.exp(-time / t2) * np.exp(time / t1)) / 2 
        # Probability of identity
        p_i = 1- p_reset - p_z
        
        e0 = paddle.to_tensor([[np.sqrt(p_i), 0], [0, np.sqrt(p_i)]], dtype='complex128')
        e1 = paddle.to_tensor([[np.sqrt(p_z), 0], [0, -np.sqrt(p_z)]], dtype='complex128')
        e2 = paddle.to_tensor([[np.sqrt(p_reset), 0], [0, 0]], dtype='complex128')
        e3 = paddle.to_tensor([[0, np.sqrt(p_reset)], [0, 0]], dtype='complex128')
        
        return [e0, e1, e2, e3]
        
    @apply_channel
    def customized_channel(self, ops, which_qubit):
        r"""添加自定义的量子信道。

        Args:
            ops (list): 表示信道的 Kraus 算符的列表
            which_qubit (int): 该信道作用在的 qubit 的编号，其值应该在 :math:`[0, n)` 范围内， :math:`n` 为该量子电路的量子比特数

        代码示例:

        .. code-block:: python

            import paddle
            from paddle_quantum.circuit import UAnsatz
            N = 2
            k1 = paddle.to_tensor([[1, 0], [0, 0]], dtype='complex128')
            k2 = paddle.to_tensor([[0, 0], [0, 1]], dtype='complex128')
            cir = UAnsatz(N)
            cir.h(0)
            cir.cnot([0, 1])
            cir.customized_channel([k1, k2], 0)
            final_state = cir.run_density_matrix()
            print(final_state.numpy())

        ::

            [[0.5+0.j 0. +0.j 0. +0.j 0. +0.j]
             [0. +0.j 0. +0.j 0. +0.j 0. +0.j]
             [0. +0.j 0. +0.j 0. +0.j 0. +0.j]
             [0. +0.j 0. +0.j 0. +0.j 0.5+0.j]]
        """
        completeness = paddle.to_tensor([[0, 0], [0, 0]], dtype='complex128')
        for op in ops:
            assert isinstance(op, paddle.Tensor), 'The input operators should be Tensors.'
            assert op.shape == [2, 2], 'The shape of each operator should be [2, 2].'
            assert op.dtype.name == 'COMPLEX128', 'The dtype of each operator should be COMPLEX128.'
            completeness += matmul(dagger(op), op)
        assert np.allclose(completeness.numpy(), np.eye(2, dtype='complex128')), 'Kraus operators should satisfy completeness.'

        return ops


def _local_H_prob(cir, hamiltonian, shots=1024):
    r"""
    构造出 Pauli 测量电路并测量 ancilla，处理实验结果来得到 ``H`` (只有一项)期望值的实验测量值。

    Note:
        这是内部函数，你并不需要直接调用到该函数。
    """
    # Add one ancilla, which we later measure and process the result
    new_cir = UAnsatz(cir.n + 1)
    input_state = paddle.kron(cir.run_state_vector(store_state=False), init_state_gen(1))
    # Used in fixed Rz gate
    _theta = paddle.to_tensor(np.array([-np.pi / 2]))

    op_list = hamiltonian.split(',')
    # Set up pauli measurement circuit
    for op in op_list:
        element = op[0]
        index = int(op[1:])
        if element == 'x':
            new_cir.h(index)
            new_cir.cnot([index, cir.n])
        elif element == 'z':
            new_cir.cnot([index, cir.n])
        elif element == 'y':
            new_cir.rz(_theta, index)
            new_cir.h(index)
            new_cir.cnot([index, cir.n])

    new_cir.run_state_vector(input_state)
    prob_result = new_cir.measure(shots=shots, which_qubits=[cir.n])
    if shots > 0:
        if len(prob_result) == 1:
            if '0' in prob_result:
                result = (prob_result['0']) / shots
            else:
                result = (prob_result['1']) / shots
        else:
            result = (prob_result['0'] - prob_result['1']) / shots
    else:
        result = (prob_result['0'] - prob_result['1'])

    return result


def H_prob(cir, H, shots=1024):
    r"""构造 Pauli 测量电路并测量关于 H 的期望值。

    Args:
        cir (UAnsatz): UAnsatz 的一个实例化对象
        H (list): 记录哈密顿量信息的列表
        shots (int, optional): 默认为 1024，表示测量次数；若为 0，则表示返回测量期望值的精确值，即测量无穷次后的期望值

    Returns:
        float: 测量得到的H的期望值
    
    代码示例:

    .. code-block:: python
        
        import numpy as np
        import paddle
        from paddle_quantum.circuit import UAnsatz, H_prob
        n = 4
        experiment_shots = 2**10
        H_info = [[0.1, 'x2'], [0.3, 'y1,z3']]

        theta = paddle.to_tensor(np.ones(3))
        cir = UAnsatz(n)
        cir.rx(theta[0], 0)
        cir.ry(theta[1], 1)
        cir.rz(theta[2], 1)
        result_1 = H_prob(cir, H_info, shots = experiment_shots)
        result_2 = H_prob(cir, H_info, shots = 0)
        print(f'The expectation value obtained by {experiment_shots} measurements is {result_1}')
        print(f'The accurate expectation value of H is {result_2}')

    ::

        The expectation value obtained by 1024 measurements is 0.2177734375
        The accurate expectation value of H is 0.21242202548207134
    """
    expval = 0
    for term in H:
        expval += term[0] * _local_H_prob(cir, term[1], shots=shots)
    return expval
