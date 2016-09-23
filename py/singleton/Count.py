import sys

class Count(object):
    def __init__(self):
        print "init count"
        self.a = 0
    def up(self):
        print "+1"
        self.a = self.a + 1
    def down(self):
        print "-1"
        self.a = self.a - 1

sys.modules[__name__] = Count()


''' python使用模块实现单例模式 '''

# 使用方法如下:

# [GCC 6.1.1 20160621 (Red Hat 6.1.1-3)] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import Count
# init count
# >>> Count.up()
# +1
# >>> Count.a
# 1
# >>> Count.up()
# +1
# >>> Count.a
# 2
# >>>
