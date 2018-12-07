## 介绍


对于一些小型项目不必要使用 `ci` 的自动化处理, 但直接手动操作也很繁琐。

此时, 可以使用 [fabric](http://www.fabfile.org/) 进行部署流程的简单优化。


## demo 使用

1. 定义需要执行的服务器的配置。
2. 执行命令

``` bash
# 拉取代码部署。 env: 对应的部署环境  branch: 代码分支
fab deploy --env=dev --branch=dev

fab stop 

fab start

fab restart
```
