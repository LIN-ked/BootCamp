#1
def count_vowels(word):
	vowels=["A","a","E","e","I","i","O","o","U","u"]
	count=0
	for i in word:
		if i in vowels:
			count+=1
	return count
#4
def sum_of_integers(a,b):
	return a+b
#2
animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for i in animals:
	print(i.upper())
#3
for i in range(1,21):
	print(i,end="")
	if i%2==0:
		print("even")
	else:
		print("odd")