##  问题集锦  

1、SyntaxError: Non-ASCII character '\xe8' in file ex6.py on line 2, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details  

![](http://oqym24k6p.bkt.clouddn.com/xiaoyi/2018-07-19-Snip20180719_15.png)  

解决方法：在文件顶端添加一行    
<code>
 # -*- coding: utf-8 -*-    
</code>


2、print  end1+end2+end3+end4+end5+end6,
   print  end7+end8+end9+end10+end11+end12  

   上面的逗号（，）如果去掉的话，那么在第一行之后将有一个回车，两行不能并作一行来进行处理。存在逗号，并不会显示出逗号，但是两行能够并作一行显示了
