for i in range(1,10,2):
    print ("i=",i)

************************************************************

N =4
for i in range(1,N+1,1):
    for j in range(1,N+1,1)
        print (i,"*",j,"=",i*j)

***********************************************************

N =10
SS=0
for i in range(1,N,2):
    i = int(input("please input a int :"))
    SS += i
    print ("i=",i)
print("sum =",SS)
print("ave =",SS/(N-1))

*********************************************************

print("列映出 0 到 4 :")
for i in range(1,5,1):
    print (i)
print("\n列映出 1 到 10 :")
for i in range(1,11):
    print (i, end="")
print("\n\n列映出 2 到 20 :")
for i in range(2,21,2):
    print (i, end="")

************************************************************************

count = 1
while count <= 5:
    print(f"數字:{count}")
    count += 1  # 重要:更新計數器
    
print("迴圈結束")

**************************************************************************

correct_password = "python123"
attempts = 3

while attempts > 0:
    password = input(f"enter the password({attempts} chances left) :")
    if password == correct_password:
        print("right password")   
        break # 跳出迴圈
    else:
        attempts -= 1
        if attempts > 0:
            print("wrong password, try it one more time")
        else:
            print("account locked")
    
*************************************************************************

# 計算1到100的總和
total = 0
number = 1
    
while number <= 100:
    total += number
    number += 1
    
print(f"1到100的總和:到100的總和:{total}")   

**********************************************************************

while True:
    print("\n=== 簡單計算機 ===")
    print("1. 加法")
    print("2. 減法")
    print("3. 退出")
    
    choice = input("請選擇功能（1-3）：")
    
    if choice == "3":
        print("謝謝使用，再見！")
        break
    elif choice == "1":
        a = float(input("請輸入第一個數字："))
        b = float(input("請輸入第二個數字："))
        print(f"結果：{a} + {b} = {a + b}")
    elif choice == "2":
        a = float(input("請輸入第一個數字："))
        b = float(input("請輸入第二個數字："))
        print(f"結果：{a} - {b} = {a - b}")
    else:
        print("無效的選擇，請重新選擇。")

********************************************************************************************************


def get_day_message(day):
    match day:
        case "星期一":
            return "新的一週開始！加油！"
        case "星期二":
            return "繼續努力，還有四天！"
        case "星期三":
            return "週中了，堅持下去！"
        case "星期四":
            return "快到週末了！"
        case "星期五":
            return "TGIF！明天就是週末！"
        case "星期六" | "星期日":  # 多個值
            return "享受週末時光！"
        case _:
            return "請輸入有效的星期"

# 測試
days = ["星期一", "星期五", "星期日", "無效日期"]
for day in days:
    print(f"{day}: {get_day_message(day)}")

******************************************************************************************************

# 根據分數給予評語
def get_grade_comment(score):
    match score:
        case n if 90 <= n <= 100:
            return "優秀！"
        case n if 80 <= n < 90:
            return "良好！"
        case n if 70 <= n < 80:
            return "普通"
        case n if 60 <= n < 70:
            return "需要加油"
        case n if 0 <= n < 60:
            return "不及格，需要重修"
        case _:
            return "無效分數"

# 測試
scores = [95, 83, 75, 65, 45, 105]
for score in scores:
    print(f"分數 {score}: {get_grade_comment(score)}")






    




