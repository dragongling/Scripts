#####################--������--######################

import time
import math

#####################--�������--#####################

#���� �� ������� ����o:
#	���� ������� - ���������� 0
#	����� ���������� ���������� ��������
def prime(n):
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return i # �� �������
	else:
		return 0 # �������

#�������� ������ ������� ��������� � �����
def primeText(n):
	s, d = 0, 51
	print(n,'-',end=' ')
	if(prime(n)):
		while(prime(n)):
			print(prime(n),'*',end=' ')
			n=n//prime(n)
		print(n)
	else:
		print('prime number')

#���������� �����, � ���������:
#	a - �������
#	b - �������
def compare(a,b):
	ret = a,b
	if(a>b):
		ret = b,a
	return ret

#���������� ����� ��������
def greatestCommonDivisor(a,b):
	a,b = compare(a,b)
	while (a%b!=0):
		a,b = b,a%b
	return b

#���������� ����� �������
def leastCommonMultiple(a,b):
	return a*b/greatestCommonDivisor(a,b)

#�������� ������ ����� � �� ������� ���������
def primeList(low=2,high=100):
	if((low<2)|(high<2)):
		low = high = 2
	low,high = compare(low,high)
	for n in range(low,high+1):
		primeText(n)	

#��� ���������
def fib(n=60):
	a,b = 0,1
	result = []
	while (b<n):
		result.append(b)
		a, b = b, a+b
	return result

#������ ��/���
def ask_ok(question='Do you really want to quit?'):
	raise NotImplementedError

def getPrimes(lst):
    primes = list()
    for number in lst:
        if(prime(number) == 0):
            primes.append(number)
    return primes

def substractList(source, sub):
    l = len(source)
    for i in range(0, l):
        if(source[i] in sub):
            del(source[i])
            l -= 1


array = list(int(s) for s in input().split())
c = 0
for i in range(0, len(array)):
    if(prime(array[i]) == 0):
        array[i], array[c] = array[c], array[i]
        c += 1

for i in range(c + 1, len(array)):
    if(array[i] % 2 == 0):
        array[i], array[c] = array[c], array[i]
        c += 1

print(array)
########################--���--########################

#s = int(input())
#print(primeList(high=s))
#time.sleep(2)
