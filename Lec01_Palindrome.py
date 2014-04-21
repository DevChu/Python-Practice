x = input("請輸入一段文字:")
y = x + x[::-1][1:]
#Another Ans: 
#x + x[:-1][::-1] 
print("結果為:"+y)
input();