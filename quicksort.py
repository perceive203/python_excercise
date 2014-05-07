#! /usr/bin/env python2.7
# encoding=utf-8

""" 快速排序的练习程序
"""

import sys
import getopt

class QuickSort(object):
    """ 快速排序类
    """

    def __init__(self, idata = None):
        if idata is not None:
            self.data = list(idata)

    def sort(self, idata = None):
        """ 实际排序
            Args:
                data: 调用者可以给出需要排序的数列，如果为空则默认在对象实例初始化
                    之时已经给出了输入数列；数据格式为 tuple

            Returns:
                返回排好序的结果，list 数据格式

            Raises:
                IOError: 如果没有给出输入数列，直接报错
        """

        if idata is not None:
            self.data = None    # 置空之前的数列
            self.data = list(idata)

        self._sort(0, len(self.data)-1)
        
        return self.data

    def _sort(self, begin, end):
        """ 对 self.data 数列的 range 进行排序 [b, end]
            Args: 
                begin: Range 的起始位置 begin
                end: Range 的终止位置 end
            
            Returns:
                Nothing
        """ 


        if end <= begin:
            return

        axle = self._select_axle(begin, end) # 选择一个轴
        
        self._dprint("before range:   list=", self.data[begin:end+1],
            ", b=%d, e=%d, m=%d" % (begin, end, axle))

        axle = self._sort_range(begin, end, axle)

        self._dprint("after range:   list=", self.data[begin:end+1], 
            ", b=%d, e=%d, m=%d" % (begin, end, axle))

        self._sort(begin, axle-1)
        self._sort(axle+1, end)
 
    def _sort_range(self, begin, end, axle):
        """ 对 self.data[begin, end] 的范围进行快排
        """
        assert begin <= axle <= end

        while begin < end:
            # e 从右向左找到第一个比 m 小的值
            while axle < end and self.data[axle] <= self.data[end]:
                end -= 1

            if axle < end:
                self._swap(end, axle)
                axle = end

            # b 从左向右找到第一个比 m 大的值
            while begin < axle and self.data[begin] <= self.data[axle]:
                begin += 1

            if begin < axle:
                self._swap(begin, axle)
                axle = begin

        return axle

    def _swap(self, src, dst):
        """ 交换 self.data[src] 与 self.data[dst] 的值
        """
        tmp = self.data[src]
        self.data[src] = self.data[dst]
        self.data[dst] = tmp

    @staticmethod
    def _select_axle(begin, end):
        """ 选择一个轴
            Todo: 暂时选择中间位置，之后可以试探性选择，性能优化
        """

        assert begin <= end

        return begin+(end-begin)/2  # 之所以不使用 (e+b)/2 为了防止加法溢出

    @staticmethod
    def _dprint(*message):
        """ 输出调试信息
        """
        global _DEBUG

        try:
            type(_DEBUG)
        except Exception:
            _DEBUG = False

        if _DEBUG:
            print message


if __name__ == "__main__":

    # 参数初始化
    global _DEBUG
    _DEBUG = False

    DATA = list()

    # 读入命令行参数
    OPTS, ARGS = getopt.getopt(sys.argv[1:], "di:")

    for op, value in OPTS:
        if op == "-d":
            _DEBUG = True

        if op == "-i":
            DATA = [int(i) for i in value.split()]

    print QuickSort(DATA).sort()
