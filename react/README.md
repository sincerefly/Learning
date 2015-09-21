###目录简介

- react-0.13.3 官方网站下载的react包，包含一些例子和react库
- react-tutorial 来自[reactjs.cn](http://reactjs.cn/react/docs/tutorial.html)的评论框例子
- react-trader 一个使用Node.js+Socket.io+React.js的股市数据模拟展示例子来自[coenraets](http://coenraets.org/blog/2015/03/real-time-trader-desktop-with-react-node-js-and-socket-io/)

其余的一些小文件为学习中测试的例子

###运行方法及演示

####react-tutorial

`说明`
目录中包含多个简单的“服务器”, 使用随便选择一个你使用过的后端即可。服务器中已经内置好了一些操作，所以不需要懂得后端，或者不必分散精力去编写后端代码，在评论区编写的内容会被提交到`comment.json`文件中，同样，`comment.json`中的内容发生变化，也会及时的反馈到界面


```python
python server.py
```

访问[http://127.0.0.1/](http://127.0.0.1/)


![http://ishell-imgs.b0.upaiyun.com/github/react-commend-1.gif](http://ishell-imgs.b0.upaiyun.com/github/react-commend-1.gif)


####react-trader

`说明`
这是一个运用`Node.js`, `Socket.io`, `React.js`的综合例子，一个模拟股票参数的网页应用

```
npm install
node server.js
```

访问[http://127.0.0.1/](http://127.0.0.1/)

![http://ishell-imgs.b0.upaiyun.com/github/react-trader.gif](http://ishell-imgs.b0.upaiyun.com/github/react-trader.gif)

