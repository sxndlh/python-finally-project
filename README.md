# 猫眼复联四影评爬虫及分析

## 设计思路

利用爬虫对猫眼电影上的电影《Avengers:Endgame》（复仇者联盟4：终局之战）的影评进行抓取，然后利用echarts对数据进行可视化分析。

##### 爬取数据阶段

利用requests请求评论API接口然后解析接口并返回数据，返回的数据格式为json,然后利用pandas将json数据转换为csv文件并保存。

##### 分析数据阶段

利用pyecharts可视化分析观众的地域分布，观众评论数量与电影上映时长的关系，利用jieba中文分词生成词云。

## 使用说明

1. 运行 spider.py 文件产生爬虫数据 data.csv 文件。

2. 运行 analysis.py 文件对爬取的数据进行分析。

## 注意事项

1. python使用3.x版本

2. pyecharts安装版本：`pip install pyecharts==0.5.11`

3. 如果报错pyecharts_snapshot，需要网上(https://pypi.org/project/pyecharts-snapshot/#files)下载并安装，比如： 

   ![](C:\Users\acer\AppData\Roaming\Typora\typora-user-images\image-20200223225012139.png)

   `	pip install pyecharts_snapshot-0.2.0-py2.py3-none-any.whl` 

    4.需要下载地图库

   `pip install echarts-countries-pypkg`

   `pip install echarts-china-provinces-pypkg`

   `pip install echarts-china-cities-pypkg`

   `pip install echarts-china-counties-pypkg`

   `pip install echarts-china-misc-pypkg`

   `pip install echarts-united-kingdom-pypkg`

