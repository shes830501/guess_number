#產生一個隨機整數1~100(不要印出來)
#讓使用者重複數入數字去猜
#猜對的話 印出"終於猜對了!"
#猜錯的話 要告知 比答案大/小

import random

r = random.randint(1, 100)
while True:
	num = int(input('請猜數字: '))
	if num == r:
		print('你猜對中了!')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')



