#####################--Импорт--######################

import time

#####################--Функции--#####################

#Тест на простое числo:
#	если простое - возвращает 0
#	иначе возвращает наименьший делитель
def prime(n):
	for x in range(2,n):
		if n%x==0:
			return x
	else:
		return 0

#Печатает список простых делителей у числа
def primeText(n):
	s,d = 0,1
	print(n,'-',end=' ')
	if(prime(n)):
		while(prime(n)):
			print(prime(n),'*',end=' ')
			n=n//prime(n)
		print(n)
	else:
		print('простое число')

#Сравнивает числа, в резльтате:
#	a - меньшее
#	b - большее
def compare(a,b):
	ret = a,b
	if(a>b):
		ret = b,a
	return ret

#Наибольший общий делитель
def greatestCommonDivisor(a,b):
	a,b = compare(a,b)
	while (a%b!=0):
		a,b = b,a%b
	return b

#Наименьшее общее кратное
def leastCommonMultiple(a,b):
	return a*b/greatestCommonDivisor(a,b)

#Печатает список чисел и их простых делителей
def primeList(low=2,high=100):
	if((low<2)|(high<2)):
		low = high = 2
	low,high = compare(low,high)
	for n in range(low,high+1):
		primeText(n)	

#Ряд Финабоччи
def fib(n=60):
	a,b = 0,1
	result = []
	while (b<n):
		result.append(b)
		a, b = b, a+b
	return result

#Запрос да/нет
def ask_ok(question='Do you really want to quit?'):
	raise NotImplementedError

########################--Код--########################

s = int(input())
print(primeList(high=s))
time.sleep(2)