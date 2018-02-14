ls = [1,2,3]

def func(ls):
	ls[0] = ls[1]+ls[2]
	ls[1] = ls[0]+ls[2]
	ls[2] = ls[1]+ls[0]

for i in range(20):
	print(ls)
	func(ls)

input()