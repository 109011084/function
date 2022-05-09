def is_leap_year(year):  #def+變數名稱():
	if (year % 400 == 0) or (year % 100 != 0 and year % 4 ==0):
		return True #代表是閏年
	else:
		return False #代表不是閏年
a = int (input('請輸入年:'))
print(is_leap_year(a))