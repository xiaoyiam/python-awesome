# -*- coding: utf-8 -*-
# 输出一行格式化字符
x="There are %d types of people." % 10
# 定义变量binary
binary="binary"
# 定义变量do_not
do_not="don't"
# 输出两个格式化字符，有一个百分号 %把两部分隔开，然后多个变量要放到一个括号里面，并且用逗号隔开
y="Those who know %s and those who %s." %(binary,do_not)

# 输出x和y两行字符
print x
print y

# 输出格式化字符,有一个问题 16行中如果不是 %r，而是%s。那么如果想要x这句话跟y这句话一样有单引号，就需要手动加单引号
print "I said : %r." %x
print "I also said : ‘%s’." %y

hilarious1=False
hilarious2=True

# 这里和#24一起完成一个格式化字符串输出，这里先定义出格式化字符串，后面再输出

joke_evaluation="Isn't that joke so funny?! %r"

print joke_evaluation % hilarious1

w="This is the left side of...  "
e="a string with a right side "
# 将两行字符串连接到一起，并且输出
print w+e
