car = input('請問你有沒有開過車?')
age = input('請輸入你的年齡:')
age = int(age)
if age < 18 and car == '有':
	print('你才', age, '怎麼會開過車???')
elif age >= 18 and car == '沒有':
	print('可以去考駕照喔')
else:
	print('很好，沒有問題')
