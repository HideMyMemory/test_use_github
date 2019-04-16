# !/usr/bin/env python 
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)


# 显示x对应的y值
def show_y_value(price_trends):
	for one_price in price_trends:
		height = one_price.get_height()

		# 显示值对应的x,y坐标的值
		x_position = one_price.get_x() + one_price.get_width() / 2. - 0.35
		y_position = 1.002 * height

		# 显示的值
		show_value = '%s' % float(height)
		plt.text(x_position, y_position, s=show_value)


names = ['UU898', '5173', '7881', 'DD373', '3YX', 'vv881', '51niu']
all_info_list = [0.0263, 0.0272, 0.0264, 0.0274, 0.0268, 0.0256, 0.0267]
# 设置显示区间
plt.ylim(0.025, 0.030)
# 设置显示间隔
show_tick = np.arange(0.025, 0.030, 0.001)
plt.yticks(show_tick)

price_trend = plt.bar(names, all_info_list, width=0.5, color="#87CEFA")
print("type(price_trend) %s" % type(price_trend))
show_y_value(price_trend)
plt.xlabel(u'web/网站', fontproperties=font)
plt.ylabel(u'price/价格', fontproperties=font)
plt.title(u'trend chart/各网站价格高低图', fontproperties=font)
plt.show()
