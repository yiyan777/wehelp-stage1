consultants=[
    {"name":"John", "rate":4.5, "price":1000},
    {"name":"Bob", "rate":3, "price":1200},
    {"name":"Jenny", "rate":3.8, "price":800}
]    
schedule_time = {consultant["name"]: [] for consultant in consultants}
# 已經被預約走的時間 # ex: schedule_time = {"John": [(8, 2)]}

def book(consultants, hour, duration, criteria):
    if criteria == "rate":   
        highest_rate = sorted(consultants, key=lambda x: x["rate"], reverse=True)
        for consultant in highest_rate:
            if schedule_time[consultant["name"]] == []:  # 如果顧問有空，就預約
                print(consultant["name"])
                schedule_time[consultant["name"]] += [(hour, duration)]
                # print(schedule_time[consultant["name"]])
                return
            schedule_time_expand = [start + i for start, duration in schedule_time[consultant["name"]] for i in range(duration)] 
            if len(set(schedule_time_expand) & set(list(range(hour, hour+duration)))) == 0:
                print(consultant["name"])
                schedule_time[consultant["name"]] += [(hour, duration)]
                return
            else:  #如果交集的長度不是0，就是有交集，表示跟別人重複，不能預約
                continue
        print("no service") 
    elif criteria == "price":   
        lowest_price = sorted(consultants, key=lambda x: x["price"])
        for consultant in lowest_price:
            if schedule_time[consultant["name"]] == []:  # 如果顧問有空，就預約
                print(consultant["name"])
                schedule_time[consultant["name"]] += [(hour, duration)]
                # print(schedule_time[consultant["name"]])
                return
            schedule_time_expand = [start + i for start, duration in schedule_time[consultant["name"]] for i in range(duration)] 
            if len(set(schedule_time_expand) & set(list(range(hour, hour+duration)))) == 0:
                print(consultant["name"])
                schedule_time[consultant["name"]] += [(hour, duration)]
                return
            else:  #如果交集的長度不是0，就是有交集，表示跟別人重複，不能預約，跑下一個迴圈的顧問
                continue
        print("no service")
                       
book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John