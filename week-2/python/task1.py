from collections import deque
station_map={
    "Songshan":["Nanjing Sanmin"],
    "Nanjing Sanmin":["Songshan", "Taipei Arena"],
    "Taipei Arena":["Nanjing Sanmin", "Nanjing Fuxing"],
    "Nanjing Fuxing":["Taipei Arena", "Songjiang Nanjing"],
    "Songjiang Nanjing":["Nanjing Fuxing", "Zhongshan"],
    "Zhongshan":["Songjiang Nanjing", "Beimen"],
    "Beimen":["Zhongshan", "Ximen"],
    "Ximen":["Beimen", "Xiaonanmen"],
    "Xiaonanmen":["Ximen", "Chiang Kai-Shek Memorial Hall"],
    "Chiang Kai-Shek Memorial Hall":["Xiaonanmen", "Guting"],
    "Guting":["Chiang Kai-Shek Memorial Hall", "Taipower Building"],
    "Taipower Building":["Guting", "Gongguan"],
    "Gongguan":["Taipower Building", "Wanlong"],
    "Wanlong":["Gongguan", "Jingmei"],
    "Jingmei":["Wanlong", "Dapinglin"],
    "Dapinglin":["Jingmei", "Qizhang"],
    "Qizhang":["Xiaobitan", "Xindian City Hall"],
    "Xiaobitan":["Qizhang"],
    "Xindian City Hall":["Qizhang", "Xindian"],
    "Xindian":["Xindian City Hall"]
}
messages={
    "Leslie":"I'm at home near Xiaobitan station.",     # Xiaobitan    小碧潭
    "Bob":"I'm at Ximen MRT station.",                  # Ximen        西門
    "Mary":"I have a drink near Jingmei MRT station.",  # Jingmei      景美
    "Copper":"I just saw a concert at Taipei Arena.",   # Taipei Arena 台北小巨蛋
    "Vivian":"I'm at Xindian station waiting for you."  # Xindian      新店
}

for name, info in messages.items():   # name對應朋友名字, info對應朋友資訊 (name, info)
    for station in station_map:  # 在station_map地圖裡尋找每一個station_map的鍵(站名)
        if station in info:  # 如果站名出現在朋友資訊裡
            messages[name] = station  # 就將該朋友資訊替換為捷運站名稱
            break  # 找到就停止內部迴圈
# 將原本messages的值裡的其餘資訊踢除，只保留"站名"在值裡面

def bfs(graph, start):
        visited = set()  # 紀錄已訪問的站點
        queue = deque([(start, 0)])  # 存放 (站點, 距離)
        distances = {}
        while queue:   # 若不為空就執行
            current, distance = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            distances[current] = distance  # 紀錄到當前站點的距離
            for neighbor in graph[current]: # 對於每一個子節點(鄰站)
                if neighbor not in visited: # 如果還沒造訪
                    queue.append((neighbor, distance + 1)) #就將該鄰站加入對列queue
        return distances  #回傳字典，記錄著自己與其他所有站的距離

def find_and_print(messages, current_station):
     dis = bfs(station_map, current_station) # 字典，記載從我的位置到所有站點的站名和距離
     nearest_friend = None   # 最近的朋友，初始為None
     shortest_distance = float('inf') # 最短距離，初始為無限大
     for friend, spot in messages.items():
          if spot in dis and dis[spot] < shortest_distance:
               nearest_friend = friend
               shortest_distance = dis[spot]
     print(nearest_friend)

find_and_print(messages, "Wanlong")
find_and_print(messages, "Songshan")
find_and_print(messages, "Qizhang")
find_and_print(messages, "Ximen")
find_and_print(messages, "Xindian City Hall")