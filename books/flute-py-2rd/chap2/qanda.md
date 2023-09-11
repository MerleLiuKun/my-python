### Q&A

<details> 
<summary>类型划分</summary>

按承载内容划分

- 容器序列
  - 可存放不同类型的项，其中包括嵌套容器
  - list、tuple 和 collections.deque。
  - 存放的是所包含对象的引用，对象可以是任何类型

- 扁平序列
  - 只可以存储一种简单类型的项
  - 如 str、bytes 和 array.array。
  - 在自己的内存空间中存储所含内容的值，而不是各自不同的 Python 对象

按可变性划分

- 可变序列
  - list、bytearray、array.array 和 collections.deque

- 不可变序列
  - tuple、str 和 bytes。

</details>