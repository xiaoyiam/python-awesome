##  问题集锦  

1、SyntaxError: Non-ASCII character '\xe8' in file ex6.py on line 2, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details  

![](http://oqym24k6p.bkt.clouddn.com/xiaoyi/2018-07-19-Snip20180719_15.png)  

解决方法：在文件顶端添加一行    
<code>
 # -*- coding: utf-8 -*-    
</code>
