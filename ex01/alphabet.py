import time
import random

tmji = 10
challenge = 2

def shutudai(ans_li):
    quiz = ""
    quiz_li = []
    for _ in range(tmji):
        ans_random = random.choice(ans_li)
        quiz += ans_random + " "
        quiz_li.append(ans_random)
        ans_li.remove(ans_random)
    print("対象文字：", quiz)
    

    keson = random.randint(1,tmji/2)
    ke = ""
    ke_li = []
    for _ in range(keson):
        ke_random = random.choice(quiz_li)
        ke += ke_random+" "
        ke_li.append(ke_random)
        quiz_li.remove(ke_random)
    #print("欠損文字：", ke)

    quiz1 = ""
    quiz1_li = []
    for _ in range(len(quiz_li)):
        ans_random = random.choice(quiz_li)
        quiz1 += ans_random + " "
        quiz1_li.append(ans_random)
        quiz_li.remove(ans_random)
    print("表示文字：", quiz1)
    print()
    return ke_li
    
def kaito(ans):
    num = int(input("欠損文字はいくつあるでしょうか？："))
    if num != len(ans):
        print("不正解です。")
    else:
        print("正解です。では、具体的な欠損文字を1文字ずつ入力してください。")
        for i in range(num):
            c = input(f"{i+1}文字目を入力してください。")
            if c not in ans:
                print("不正解です。またチャレンジしてください。")
                return False
            else:
                ans.remove(c)
        else:
            print("欠損文字も含めて完全正解です!!!")
            return True
    return False

if __name__ == "__main__":
    st = time.time()
    li = ["A", "B", "C", "D", "E", "F", "G", "H",
    "I", "J", "K", "L", "M", "N", "O", "P", "Q",
    "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]
    for _ in range(challenge):
        ans_li = shutudai(li)
        ans = kaito(ans_li)
        if ans:
            break
        else:
            print("-"*20)
    ed = time.time()
    print(f"所要時間：{(ed-st):.2f}")