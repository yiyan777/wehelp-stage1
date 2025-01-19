def func(*data):
    storage = []
    for i in data:
        if len(i)==1 or len(i) > 5:
            print("請正確輸入2至5位數的中文名字")
            return
    for i in data:
        if len(i) == 2:
            storage = storage + [(i,i[-1])]
        elif len(i) == 3:
            storage = storage + [(i,i[-2])]
        elif len(i) == 4:
            storage = storage + [(i,i[-2])]
        elif len(i) == 5:
            storage = storage + [(i,i[-3])]
    # print(storage)
    tem = []
    result = []
    for name, key_word in storage:   #(name, key_word)
        tem = tem + [key_word]
    # print(tem)
    for name, key_word in storage:
        if tem.count(key_word) == 1:
            result = result + [name]
    # print(result)
    if len(result) == 0:
        print("沒有")
    elif len(result) >= 1:
        for i in result:
            print(i)
    

func("彭大牆", "陳王明雅", "吳明")  # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安