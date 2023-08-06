# -*- coding:utf-8 -*-

# __author:ly_peppa
# date:2020/12/10

# 导入必要的几个包
import requests
from bs4 import BeautifulSoup
import pandas as pd



# 定义映射表
key_map=dict(zip(['全站','番剧','国产动画','国创相关','纪录片','动画','音乐','舞蹈','游戏','知识','数码','生活','美食','鬼畜','时尚','娱乐','影视','电影','电视剧','原创','新人'],
                 ['all','bangumi','guochan','guochuang','documentary','douga','music','dance','game','technology','digital','life','food','kichiku','fashion','ent','cinephile','movie','tv','origin','rookie']))

xhr_map=dict(zip(['全站','番剧','国产动画','国创相关','纪录片','动画','音乐','舞蹈','游戏','知识','数码','生活','美食','鬼畜','时尚','娱乐','影视','电影','电视剧','原创','新人'],
                 [('v2',0,'all'),('list',3,1),('list',3,4),('v2',168,'all'),('list',3,3),('v2',1,'all'),('v2',3,'all'),('v2',129,'all'),('v2',4,'all'),('v2',36,'all'),('v2',188,'all'),('v2',160,'all'),('v2',211,'all'),('v2',119,'all'),('v2',155,'all'),('v2',5,'all'),('v2',181,'all'),('list',3,2),('list',3,5),('v2',0,'origin'),('v2',0,'rookie')]))

xhrHeader = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "max-age=0",
    "cookie": "_uuid=DA8BA553-CBEB-DBFB-E743-B17941FC9A2775415infoc; buvid3=C0F0AFE6-7E40-465C-9612-34B8CC084DFB143080infoc; sid=bd6u8j4p; CURRENT_FNVAL=80; blackside_state=1; bsource=search_baidu; fingerprint=61e7471323bb39d03e9632ff89ded5d3; buvid_fp=C0F0AFE6-7E40-465C-9612-34B8CC084DFB143080infoc; buvid_fp_plain=24D8CCA7-358A-49B6-85C0-D4C0A5969D53185001infoc; PVID=2; bfe_id=6f285c892d9d3c1f8f020adad8bed553",
    "origin": "https://www.bilibili.com",
    "referer": "https://www.bilibili.com/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua": '''" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"''',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62"
}

htmlHeader = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "max-age=0",
    "cookie": "finger=158939783; _uuid=DA8BA553-CBEB-DBFB-E743-B17941FC9A2775415infoc; buvid3=C0F0AFE6-7E40-465C-9612-34B8CC084DFB143080infoc; sid=bd6u8j4p; CURRENT_FNVAL=80; blackside_state=1; bsource=search_baidu; fingerprint=61e7471323bb39d03e9632ff89ded5d3; buvid_fp=C0F0AFE6-7E40-465C-9612-34B8CC084DFB143080infoc; buvid_fp_plain=24D8CCA7-358A-49B6-85C0-D4C0A5969D53185001infoc; PVID=2",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua": '''" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"''',
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62"
}


def PopularTop100(keyword='全站'):
    '''
    下载bilibili排行榜数据，
    :return:
    返回pandas格式的数据
    '''
    df_rank = pd.DataFrame(columns=['排名', '标题', '网址', '播放量', '弹幕量', 'UP主/收藏量', '综合得分'])     # 指定列名构造pandas表格
    response=requests.get('https://www.bilibili.com/v/popular/rank/{:s}'.format(key_map[keyword]), headers=htmlHeader)        # requests向url网址发送get请求获返回网页数据
    response.encoding='utf-8'                                       # 设置字符集
    soup = BeautifulSoup(response.text, "html.parser")              # 使用BeautifulSoup解析web网页
    rank_list = soup.find('ul', attrs={'class': 'rank-list'}).find_all('li', attrs={'class': 'rank-item'})  # find()找到指定的节点
    for item in rank_list:                      # 遍历该节点，解析每一行数据
        num=item.div.text.strip()               # 解析出排名
        info=item.find('div', class_='info')
        title=info.a.text.strip()               # 解析出标题
        link='https:'+info.a['href']            # 解析出链接
        detail=item.find('div', class_='detail').find_all('span')
        play = detail[0].text.strip()           # 解析出播放量
        view = detail[1].text.strip()           # 解析出弹幕量
        name = detail[2].text.strip()           # 解析出UP主名字
        pts=item.find('div', class_='pts')
        score=pts.div.text.strip()              # 解析出综合得分

        row = [num, title, link, play, view, name, score]
        # print(row)
        df_rank.loc[len(df_rank)]=row           # 解析出来的数据按行追加到DataFrame表中
    df_rank.set_index('排名',drop=True,append=False,inplace=True,verify_integrity=False)  # 设置索引
    return df_rank

def PopularHot(pn=None):
    '''
    下载bilibili综合热门数据，
    :return:
    返回pandas格式的数据
    '''
    hot_list = None
    pn_count=0
    while True if pn is None else (pn_count<pn):
        pn_count+=1
        url='https://api.bilibili.com/x/web-interface/popular?ps=20&pn={:d}'.format(pn_count)
        response=requests.get(url, headers=xhrHeader)        # requests向url网址发送get请求获返回网页数据
        response.encoding='utf-8'                                       # 设置字符集
        data_json=response.json()['data']
        if data_json['no_more']:
            break
        if hot_list is None:
            hot_list=data_json['list']
        else:
            hot_list.extend(data_json['list'])
    df=pd.DataFrame(data=hot_list)
    return df

def PopularHistory():
    '''
    下载bilibili入站必刷数据，
    :return:
    返回pandas格式的数据
    '''
    url='https://api.bilibili.com/x/web-interface/popular/precious?page_size=100&page=1'
    response = requests.get(url, headers=xhrHeader)  # requests向url网址发送get请求获返回网页数据
    response.encoding = 'utf-8'  # 设置字符集
    hot_list = response.json()['data']['list']
    df=pd.DataFrame(data=hot_list)
    return df

def PopularWeekly(number=-1):
    '''
    下载bilibili每周必看数据，
    :return:
    返回pandas格式的数据
    '''
    if number>0:
        url='https://api.bilibili.com/x/web-interface/popular/series/one?number={:d}'.format(number)
        response = requests.get(url, headers=xhrHeader)  # requests向url网址发送get请求获返回网页数据
        response.encoding = 'utf-8'  # 设置字符集
        hot_list = response.json()['data']['list']
    else:
        # 往期列表
        url='https://api.bilibili.com/x/web-interface/popular/series/list'
        response = requests.get(url, headers=xhrHeader)  # requests向url网址发送get请求获返回网页数据
        response.encoding = 'utf-8'  # 设置字符集
        hot_list = response.json()['data']['list']
        # -1表示最近一期
        if number<0:
            number=len(hot_list)+number+1
            url='https://api.bilibili.com/x/web-interface/popular/series/one?number={:d}'.format(number)
            response = requests.get(url, headers=xhrHeader)  # requests向url网址发送get请求获返回网页数据
            response.encoding = 'utf-8'  # 设置字符集
            hot_list = response.json()['data']['list']

    df=pd.DataFrame(data=hot_list)
    return df

def PopularRank(keyword='全站'):
    '''
    下载bilibili排行榜数据，
    :return:
    返回pandas格式的数据
    '''
    value=xhr_map[keyword]
    if value[0]=='v2':
        url='https://api.bilibili.com/x/web-interface/ranking/v2?rid={:d}&type={:s}'.format(value[1],value[2])
    elif value[0]=='list':
        url = 'https://api.bilibili.com/pgc/season/rank/web/list?day={:d}&season_type={:d}'.format(value[1], value[2])
    response = requests.get(url, headers=xhrHeader)  # requests向url网址发送get请求获返回网页数据
    response.encoding = 'utf-8'  # 设置字符集
    hot_list = response.json()['data']['list']
    df=pd.DataFrame(data=hot_list)
    return df


if __name__ == '__main__':

    df=PopularTop100('全站')
    print(df)
    df.to_csv('bilibili_top100.csv',encoding="utf-8-sig")         # pandas直接保存到csv

    # df = PopularHot()
    # print(df)
    # df.to_excel('bilibili_hot.xlsx')
    #
    # df = PopularHistory()
    # print(df)
    # df.to_excel('bilibili_history.xlsx')
    #
    # df = PopularWeekly(-1)
    # print(df)
    # df.to_excel('bilibili_weekly.xlsx')
    #
    # df = PopularRank('番剧')
    # print(df)
    # df.to_excel('bilibili_rank.xlsx')


