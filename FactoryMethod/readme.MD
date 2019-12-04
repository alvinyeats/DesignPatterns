# 工厂模式

将实例的生成交给子类
在Template Method模式中，我们在父类中规定处理的流程，在子类中实现具体的处理。
如果我们将该模式用于生成实例，它就演变为本章中我们所要学习的Factory Method模式。

## 任务

制作身份证

## 源码结构

Product类和Factory类属于framework包。这两个类组成了生成实例的框架。
IDCard类和IDCardFactory类负责实际的加工处理，它们属于idcard包

main.py，测试文件，测试我们的工厂模式