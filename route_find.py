# coding = utf-8
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

# def get_page_content(requests_url):
#     headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 YaBrowser/19.7.0.1635 Yowser/2.5 Safari/537.36'}
#     html = requests.get(requests_url,headers=headers)
#     html.encoding = 'gzip'
#     soup = BeautifulSoup(html.text,'html.parser',from_encoding='utf-8')
#     return soup
#
# url = 'https://ditie.mapbar.com/hongkong_line/'
# soup = get_page_content(url)
# df = pd.DataFrame(columns=['name','site'])
# subways = soup.find_all(class_='station')
# for subway in subways:
#     route_name = subway.find('strong',class_='bolder').text
#     routes = subway.find('ul')
#     routes = routes.find_all('a')
#     for route in routes:
#         temp = {'name':route.text,'site':route_name}
#         df = df.append(temp,ignore_index=True)
# df['city'] = '香港'
# # print(df)
# df.to_csv('subway.csv',index=False)
def get_location(keyword,city):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 YaBrowser/19.7.0.1635 Yowser/2.5 Safari/537.36'}
    requests_url = 'http://restapi.amap.com/v3/place/text?key=acfd653458326536bfc719fcf2fa83cf&keywords='+keyword+'&types=&city='+city+'&children=1&offset=1&page=1&extensions=all'
    data = requests.get(requests_url,headers=headers)
    # print(requests_url)
    data = data.text
    pattern = 'location":"(.*?),(.*?)"'
    result = re.findall(pattern,data)
    try:
        return result[0][0],result[0][1]
    except:
        return get_location(keyword.replace('站',''),city)
#
# df['longitude'],df['latitude'] = None,None
# for index,row in df.iterrows():
#     longitude,latitude = get_location(row['name'],row['city'])
#     print(row['name'],longitude,latitude)
#     df.iloc[index]['longitude'] = float(longitude)
#     df.iloc[index]['latitude'] = float(latitude)
# df.to_csv('subway.csv',index=False)
