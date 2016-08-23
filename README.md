# GraspABook
This python script is designed for grasp text from specific website. 
>Let me know if you got any question.如有问题请联系邮箱: wjunshuo@qq.com

## 如何运行
**注意: 需要修改全局变量 `fileDirPath` 规定的路径才可以运行**  
运行这个Python3 的脚本
###Mac OS
打开 terminal 然后使用命令 <br> `python3 (拖拽文件到窗口 然后回车键)`<br>
根据提示输入需要的信息

###示例
比如这本书 从第一章节抓取这部小说 `http://www.biquge.la/book/401/302287.html`
请输入书序号: 401
请输入需要抓取书的起始章节: 1
需要重命名新书吗?(n/y)y
请输入书名: frxxz

## 原理简述

调用`userInteraction()` 部分获取输入的内容

文件会在`saveBrief(self,content,name)`规定的`filePath`地址存储抓取到的目录信息<br>
并在`getFetchedContent(self)`规定的`filePath`地址读取抓取到的目录信息<br>
然后进行目录中的章节地址提取<br>
地址标题提取<br>
存入文件<br>
在每一章节的开头加入了`###`来占位 配合一些软件 比如 calibre 可以制作带目录的mobi等<br>
