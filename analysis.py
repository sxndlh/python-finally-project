import pandas as pd
from collections import Counter
from pyecharts import Map, Geo, Bar, Pie

import jieba
import jieba.analyse
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import numpy as np


# 读取csv文件数据
def read_csv(filename, titles):
    comments = pd.read_csv(filename, names=titles)
    return comments


# 观众地域图
def draw_map(comments):
    try:
        attr = comments['cityName'].fillna("zero_token")
        data = Counter(attr).most_common(300)
        data.remove(data[data.index([(i, x) for i, x in (data) if i == 'zero_token'][0])])
        #print(data)
        geo = Geo("《Avengers:Endgame》全国观众地域分布", "数据来源：猫眼电影",
                  title_color="#fff", title_pos="center", width=1450,
                  height=725, background_color='#404a59')
        attr, value = geo.cast(data)
        geo.add("", attr, value, visual_range=[0, 1000], maptype='china', visual_text_color="#fff", symbol_size=10,
                is_visualmap=True)
        geo.render("./全国观众地域分布地理坐标图.html")
        print("全国观众地域分布已完成")
    except Exception as e:
        print(e)


def draw_bar(comments):
    data_top20 = Counter(comments['cityName']).most_common(20)
    bar = Bar('《Avengers:Endgame》观众地域排行榜单', '数据来源：猫眼电影', title_pos='center', width=1450, height=725)
    attr, value = bar.cast(data_top20)
    bar.add('', attr, value, is_visualmap=True, visual_range=[0, 4500], visual_text_color='#fff', is_more_utils=True,
            is_label_show=True)
    bar.render('./观众地域排行榜单.html')
    print("观众地域排行榜单已完成")


def draw_cloud(comments):
    data = comments['content']

    comment_data = []
    print("由于数据量比较大，分词这里稍微有点慢，请耐心等候")
    for item in data:
        if pd.isnull(item) == False:
            comment_data.append(item)

    comment_after_split = jieba.cut(str(comment_data), cut_all=False)
    words = ' '.join(comment_after_split)

    # 自定义停用词
    stopwords = STOPWORDS.copy()
    stopwords.add('复仇者联盟')
    stopwords.add('复联')
    stopwords.add('联盟')
    stopwords.add('复仇')
    stopwords.add('电影')
    stopwords.add('一部')
    stopwords.add('一个')
    stopwords.add('没有')
    stopwords.add('什么')
    stopwords.add('有点')
    stopwords.add('感觉')
    stopwords.add('就是')
    stopwords.add('觉得')
    stopwords.add('但是')
    stopwords.add('自己')
    stopwords.add('我们')
    stopwords.add('真的')
    stopwords.add('可以')
    stopwords.add('非常')
    stopwords.add('还是')
    stopwords.add('还有')
    stopwords.add('这部')

    # 这里的字体路径请根据自己电脑的实际情况设置'simfang.ttf'
    fortpath = './SourceHanSansCN-Normal-2.otf'
    wc = WordCloud(width=1000, height=700, background_color='#000000', font_path=fortpath, scale=5,
                   stopwords=stopwords, max_font_size=200)
    wc.generate_from_text(words)

    plt.figure(figsize=(10, 8))
    plt.imshow(wc)
    plt.axis('off')
    plt.savefig('./WordCloud.png')
    plt.show()


def draw_DateBar(comments):
    time = comments['startTime']
    timeData = []
    for t in time:
        if pd.isnull(t) == False:
            date = t.split(' ')[0]
            timeData.append(date)

    data = Counter(timeData).most_common()
    data = sorted(data, key=lambda data: data[0])

    bar = Bar('《Avengers:Endgame》观众评论数量与日期的关系', '数据来源：猫眼电影',
              title_pos='center', width=1450, height=725)
    attr, value = bar.cast(data)
    bar.add('', attr, value, is_visualmap=True, visual_range=[0, 5000], visual_text_color='#fff', is_more_utils=True,
            is_label_show=True)
    bar.render('./观众评论数量与日期的关系.html')
    print("观众评论数量与日期的关系已完成")


def draw_TimeBar(comments):
    time = comments['startTime']
    timedata = []
    for t in time:
        if pd.isnull(t) == False:
            time = t.split(' ')[1]
            hour = time.split(':')[0]
            timedata.append(int(hour))

    data = Counter(timedata).most_common()
    print(data)
    print(type(data))
    data = sorted(data, key=lambda data: data[0])

    bar = Bar('《Avengers:Endgame》观众评论数量与时间的关系', '数据来源：猫眼电影',
              title_pos='center', width=1450, height=725)
    attr, value = bar.cast(data)
    bar.add('', attr, value, is_visualmap=True, visual_range=[0, 5000], visual_text_color='#fff', is_more_utils=True,
            is_label_show=True)
    bar.render('./观众评论数量与时间的关系.html')
    print("观众评论数量与时间的关系已完成")


if __name__ == "__main__":
    filename = "./data.csv"
    titles = ['nickName', 'cityName', 'content', 'score', 'startTime']
    comments = read_csv(filename, titles)
    draw_map(comments)
    draw_bar(comments)
    draw_DateBar(comments)
    draw_TimeBar(comments)
    draw_cloud(comments)
    print("全部完成")