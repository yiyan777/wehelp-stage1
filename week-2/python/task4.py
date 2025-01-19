def find_a_ans(an): #求an的值
    a1 = 4
    d = 7
    an = int(an)
    ans = a1+ (an-1)*7
    return ans

def find_b_ans(bn): #求bn的值
    b1 = 8
    d = 7
    bn = int(bn)
    ans = b1+ (bn-1)*7
    return ans

def find_c_ans(cn): #求cn的值
    c1 = 7
    d = 7
    cn = int(cn)
    ans = c1+ (cn-1)*7
    return ans

def get_number(index):
    index = int(index)
    q = index // 3   # 將index對3求商數
    r = index % 3    # 將index對3求餘數
    if r == 1:   # 餘數為1的狀況
        q += 1
        s = find_a_ans(q)
        print(f"您查找的index為{index}, 答案是{s}")
    elif r == 2:  # 餘數為2的狀況
        q += 1
        s = find_b_ans(q)
        print(f"您查找的index為{index}, 答案是{s}")
    else:         # 餘數為其他(0)的狀況
        s = find_c_ans(q)
        print(f"您查找的index為{index}, 答案是{s}")

get_number(1)
get_number(5)
get_number(10)
get_number(30)