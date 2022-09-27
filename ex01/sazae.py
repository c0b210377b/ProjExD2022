import random

def shutudai(li):
    ans = random.choice(li)
    print("問題：" + ans["q"])
    return ans["a"]

def kaito(ans_list):
    ans = input("答えなさい:")
    if ans in ans_list:
        print("正解ｯｯ!!!")
    else:
        print("違ェよ、ボケｯ!!")

if __name__ == "__main__":
    li = [
        {"q":"サザエの旦那は？", "a":["マスオ", "ますお"]},
        {"q":"カツオの妹は？", "a":["ワカメ", "わかめ"]},
        {"q":"タラオはカツオから見てどんな関係？", "a":["甥", "甥っ子", "おい", "おいっこ"]}]

    ans_list = shutudai(li)
    ans = kaito(ans_list)
