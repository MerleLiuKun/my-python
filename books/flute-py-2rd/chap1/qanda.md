### Q&A

<details>
    <summary>What is the difference between __str__ and __repr__?</summary>


`__repr__` 方法返回的字符串应当没有歧义，如果可能，最好与源码保持一致，方便重新创建所表示的对象, 可以用 `eval` 反向转化为对象

`__str__` 方法由内置函数`str()`调用，在背后供`print`函数使用，返回对终端用户友好的字符串。


如果没有定义 `__str__` 最终对象将会调用到 `__repr__` 方法

Refer: 
- [What is the difference between __str__ and __repr__?](https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr)
</details>
