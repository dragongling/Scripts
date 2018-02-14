#Достаём словарь из файла
def get_dict(f):
	result = [] #Список с результатом
	i=0 #Мтератор
	buf = str() #Объявляем буффер для символов
	spec_sym = '-','\n' #Спецсимволы
	while(f): #Пока в файле что-то есть
		result.append([]) #Добавляем к концу массива список
		for x in range(2):
			result[i].append('') #К нему пустую строку
			while True:
				buf=f.read(1) #Читаем символ в buf
				if(buf!=spec_sym[x]): #Проверяем на спецсимвол
					result[i][x] += buf #Если не он, то строим слово
				else:
					break
		++i
	return result

#Пишем слово и запрашиваем перевод
def transl(s):
	r = random.randomint(0,1)
	ask = ''
	print(s[r],'-',end=' ')
	input(ask)
	if (ask==s[1-r]):
		print('Правильно')
	else:
		print('Неправильно')


import random
try:
	f = open(r'dictionary.txt')
	dictionary = get_dict(f)
	f.close()
	#if len(dictionary)==0:
	#	raise EmptyDict
	welcome = 'Программа для запоминания английских слов v 0.1.1\n\
				Чтобы выйти, введите в поле ответа exit'
	print(welcome)
	while len(dictionary):
		r = random.randomint(0,len(dictionary)-1)
		transl(dictionary[r])
		del dictionary[r]
	print()	
except IOError:
	print('Runtime error: file "dictionary.txt" not found')
	input()
#except EmptyDict:
#	print('Runtime error: dictionary is empty')
#	input()