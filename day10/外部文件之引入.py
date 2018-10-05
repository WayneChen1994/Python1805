from test.hello import sayHello
'''
可引入的文件：当前项目下的所有文件都可以引入，
以及安装的第三方模块，另外还有内置模块，这几种都可以引入，
但是其他项目中的文件不能直接引入。
'''

'''
引入外部文件的语法：
from 包名.模块名 import *
import 包名.模块名 as 别名
'''


sayHello()
