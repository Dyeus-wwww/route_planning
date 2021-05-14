# coding = utf-8
import route_api
import route_find
import pandas as pd

def get_nearest_subway(data,location1):
    distance = float('inf')
    nearest = None
    for i in range(data.shape[0]):
        site1 = data.iloc[i]['name']
        longitude = float(data.iloc[i]['longitude'])
        latitude = float(data.iloc[i]['latitude'])
        temp = (float(location1[0])-longitude)**2+(float(location1[1])-latitude)**2
        if temp < distance:
            distance = temp
            nearest = site1
    return nearest

def compute(site1,site2):
    location1 = route_find.get_location(site1, city)
    location2 = route_find.get_location(site2, city)
    # print(site1+'的坐标是:',location1)
    # print(site2+'的坐标是:',location2)
    data = pd.read_csv('subway.csv')
    start = get_nearest_subway(data=data,location1=location1)
    end = get_nearest_subway(data=data,location1=location2)
    print('離出發點{}最近的地鐵站為{}，離終點{}最近的地鐵站為{}'.format(site1,start,site2,end))
    shortest_path = route_api.compute(start, end)
    if site1 != start:
        shortest_path.insert(0,site1)
    if site1 != end:
        shortest_path.append(site2)
    print('從{}=>{}的最短路徑為{}'.format(site1,site2,shortest_path))
city = '香港'
if __name__ == '__main__':
    place_start = input('請輸入出發點(注意要用簡體中文):')
    place_end = input('請輸入終點(注意要用簡體中文):')
    compute(place_start,place_end)
