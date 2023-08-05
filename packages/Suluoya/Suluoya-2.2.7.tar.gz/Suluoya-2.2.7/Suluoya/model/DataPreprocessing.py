import pandas as pd
import numpy as np
import math

class DataPreprocessing(object):

    def __init__(self, series=np.random.normal(0, 1, 100)):
        self.series = pd.Series(series)

    def cat_missing(self):
        na_count = len(self.series)-self.series.count()  # 缺失值个数
        var_count = self.series.value_counts()
        if int(na_count) > math.ceil(0.05*var_count.min()):
            print('缺失值过多，用“None”填充并自动重新编码')
            return self.series.fillna('None')
        elif int(na_count) == 0:
            print('无缺失值')
            return self.series
        else:
            print('缺失值用众数填充')
            print(str(self.series.mode()[0]))
            return self.series.fillna(str(self.series.mode()[0]))

    def con_missing(self):
        self.series = self.series.astype('float')
        if self.series.count()<=0.95*len(self.series):
            print('该连续变量缺失值个数超过5%,但仍然填充平均值')
        return self.series.fillna(self.series.mean())

    def con(self):
        '''连续变量
        '''
        series = self.con_missing()
        from scipy.stats import kstest
        # 正态分布数据
        if kstest(series.dropna(), 'norm')[1] > 0.05:
            print('正态分布数值变量')
            mean = series.mean()
            std = series.std()
            max = mean+3*std
            min = mean-3*std
        # 非正态分布数据
        else:
            print('非正态分布数值变量')
            Q1 = series.quantile(q=0.25)
            Q3 = series.quantile(q=0.75)
            max = Q1 + 1.5 * (Q3 - Q1)
            min = Q1 - 1.5 * (Q3 - Q1)
        s = series[series.map(lambda x:min <= x <= max)]
        max=s.max()
        min=s.min()
        return series.map(lambda x: x if min <= x <= max else max if x>max else min)

    def cat(self, order=[]):
        '''分类变量
        '''
        series = self.cat_missing()
        if not order:
            print('无序二/多分类')
            series = series.astype('category').cat.codes
        else:
            index_dict = {}
            if len(order) > 2:
                print('有序多分类')
                j = 1
            else:
                print('有序二分类（是/否）')
                j = 0
            for i in order:
                index_dict[i] = j
                j += 1
            series = series.map(lambda x: index_dict[x])
        return series
    
if __name__ == '__main__':
    dp = DataPreprocessing([ None,2, 3, 4, 5, 6, 7, 8, 9, 10, 2, -3000,  None])
    print(dp.con())