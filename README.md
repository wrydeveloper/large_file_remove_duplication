python大文件去重

亲测百万条数据只需一秒不到即可完成去重



使用方法：

从git上拉取下来后，导入文件

```
from package.deal_file import LargeFileRemoveDuplication

# 指定要去重的文件
oldfile = '/home/wry/workspace/large_file_remove/files/article_link.txt'
# 指定要生成的文件
newfile = '/home/wry/workspace/large_file_remove/files/test_space.txt'
# 运行
LargeFileRemoveDuplication(oldfile, newfile)
```



效果：

源文件：
![](/home/wry/下载/1807569089.jpg)

去重结果：

![](/home/wry/图片/2018-11-21 01-33-41屏幕截图.png)

打印用时：

![](/home/wry/图片/2018-11-21 01-35-52屏幕截图.png)