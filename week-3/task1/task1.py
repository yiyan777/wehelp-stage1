import re
import urllib.request as request
import json
src1="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
with request.urlopen(src1) as response: 
    data1 = json.load(response)
data1_spot_list = data1["data"]["results"]

src2="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"
with request.urlopen(src2) as response: 
    data2 = json.load(response)
data2_list = data2["data"]
data2_list_dict = {item["SERIAL_NO"]: item["address"][5:8] for item in data2_list}
# print(data2_list_dict)

for spot in data1_spot_list:
    if spot["SERIAL_NO"] in data2_list_dict:
        spot["address"] = data2_list_dict[spot["SERIAL_NO"]]

    jpgs = spot["filelist"]  #字串型態 一堆.jpg
    match = re.search(r"https://.*?\.(jpg|JPG)", jpgs)
    first_img = match.group() # 取第一筆
    spot["filelist"] = first_img

with open("spot.csv", "w", encoding="utf-8") as file:
    for spot in data1_spot_list:
        ans1 = f"{spot["stitle"]},{spot["address"]},{spot["longitude"]},{spot["latitude"]},{spot["filelist"]}"+"\n"
        file.write(ans1)

for spot in data1_spot_list:
    for k in data2_list:
        if spot["SERIAL_NO"] == k["SERIAL_NO"]:
            spot["MRT"] = k["MRT"]+"站"

# print(data1_spot_list)  # 將各景點的MRT新增進來

keys_to_keep = ["MRT", "stitle"]

simple_list = []
for spot in data1_spot_list:
    simple_list.append({k: spot[k] for k in keys_to_keep})
# print(simple_list)

mrt_to_sttitle = {}
for item in simple_list:
    mrt = item['MRT']
    stitle = item['stitle']
    if mrt not in mrt_to_sttitle:
        mrt_to_sttitle[mrt] = []
    mrt_to_sttitle[mrt].append(stitle)
# print(mrt_to_sttitle)

with open("mrt.csv", "w", encoding="utf-8") as file:
    for k,v in mrt_to_sttitle.items():
        v = ",".join(v)
        ans2 = f"{k},{v}"+"\n"
        file.write(ans2)