#! /usr/bin/env python2.7
# encoding=utf-8

""" 快速排序的练习程序
"""

import sys
import getopt

class QuickSort(object):
    """ 快速排序类
    """

    def __init__(self, data = []):
        self.data = list(data)

    def sort(self, data = []):
        """ 实际排序
            Args:
                data: 调用者可以给出需要排序的数列，如果为空则默认在对象实例初始化
                    之时已经给出了输入数列；数据格式为 tuple

            Returns:
                返回排好序的结果，list 数据格式

            Raises:
                IOError: 如果没有给出输入数列，直接报错
        """

        if data:
            self.data = None    # 置空之前的数列
            self.data = list(data)

        self._sort(0, len(self.data)-1)
        
        return self.data

    def _sort(self, b, e):
        """ 对 self.data 数列的 range 进行排序 [b, e]
            Args: 
                b: Range 的起始位置 begin
                e: Range 的终止位置 end
            
            Returns:
                Nothing
        """ 


        if e <= b: return

        m = self._select_m(b, e) # 选择一个轴
        
        self._dprint("before range:   list=", self.data[b:e+1], ", b=%d, e=%d, m=%d" % (b, e, m))

        m = self._sort_range(b, e, m)

        # print "after range:   list=", self.data[b:e+1], ", b=%d, e=%d, m=%d" % (b, e, m)

        self._sort(b, m-1)
        self._sort(m+1, e)
 
    def _sort_range(self, b, e, m):

        assert b <= m <= e

        n = self.data[m]

        while b < e:
            # e 从右向左找到第一个比 m 小的值
            while m < e and self.data[m] <= self.data[e]: e -= 1

            if m < e:
                self._swap(e, m)
                m = e

            # b 从左向右找到第一个比 m 大的值
            while b < m and self.data[b] <= self.data[m]: b += 1

            if b < m:
                self._swap(b, m)
                m = b

        return m

    def _swap(self, i, j):
        tmp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = tmp

    def _select_m(self, b, e):
        # TODO: 暂时选择中间位置，之后可以试探性选择，性能优化

        assert b <= e

        return b+(e-b)/2  # 之所以不使用 (e+b)/2 为了防止加法溢出

    def _dprint(self, *p):
        global _DEBUG

        try:
            type(_DEBUG)
        except:
            _DEBUG = False

        if _DEBUG: print p


if __name__ == "__main__":

    # 参数初始化
    global _DEBUG
    _DEBUG = False

    data = list()

    # 读入命令行参数
    opts, args = getopt.getopt(sys.argv[1:], "di:")
    for op, value in opts:
        if op == "-d": _DEBUG = True
        if op == "-i": data = [int(i) for i in value.split()]

    print QuickSort(data).sort()
