# coding = utf-8
import re
import requests
import pandas as pd
from collections import defaultdict

costs = {}
parents = {}
processed = []
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        if node not in processed:
            if costs[node] < lowest_cost:
                lowest_cost = costs[node]
                lowest_cost_node = node
    return lowest_cost_node
def find_shortest_path():
    node = end
    shortest_path = [end]
    while parents[node] != start:
        shortest_path.append(parents[node])
        node = parents[node]
    shortest_path.append(start)

    return shortest_path
def dijkstra():
    node = find_lowest_cost_node(costs)
    # print('當前cost最小節點:',node)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for neighbor in neighbors.keys():
            new_cost = cost + float(neighbors[neighbor])
            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
        # print('當前cost最小節點:', node)
    shortest_path = find_shortest_path()
    shortest_path.reverse()
    # print('從{}到{}的最短路徑是:{}'.format(start,end,shortest_path))
    return shortest_path
def compute_distance(longitude1,latitude1,longitude2,latitude2):
    requests_url = 'http://restapi.amap.com/v3/distance?key=acfd653458326536bfc719fcf2fa83cf&origins='+str(longitude1)+','+str(latitude1)+'&destination='+str(longitude2)+','+str(latitude2)+'&type=1'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 YaBrowser/19.7.0.1635 Yowser/2.5 Safari/537.36'}
    data = requests.get(requests_url,headers=headers)
    data.encoding = 'utf-8'
    data = data.text
    pattern = 'distance":"(.*?)","duration":"(.*?)"'
    result = re.findall(pattern,data)
    return result[0][0]
# print(compute_distance(longitude1=114.005051,latitude1=22.466389,longitude2=114.231268,latitude2=22.30943))
data = pd.read_csv('subway.csv')
# print(data)

graph = defaultdict(dict)
for i in range(data.shape[0]-1):
    site1 = data.iloc[i]['site']
    site2 = data.iloc[i+1]['site']
    if site1 == site2:
        longitude1,latitude1 = data.iloc[i]['longitude'],data.iloc[i]['latitude']
        longitude2,latitude2 = data.iloc[i+1]['longitude'], data.iloc[i+1]['latitude']
        name1,name2 = data.iloc[i]['name'],data.iloc[i+1]['name']
        distance = compute_distance(longitude1,latitude1,longitude2,latitude2)
        graph[name1][name2] = distance
        graph[name2][name1] = distance
        # print(name1,name2,distance)

def compute(site1,site2):
    global start,end,parents,costs,processed
    start  = site1
    end = site2
    parents[end] = None
    for node in graph[start].keys():
        costs[node] = float(graph[start][node])
        parents[node] = start
    costs[end] = float('inf')
    shortest_path = dijkstra()
    return shortest_path

if __name__ == '__main__':
    site1 = '观塘站'
    site2 = '元朗站'
    shortest_path = compute(site1,site2)
    print(shortest_path)

