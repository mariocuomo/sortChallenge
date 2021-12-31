#CHALLENGE
#This script takes in input a sequence of int number a_1 a_2 ... a_n and a target int number K.
#It returns a list of integer a_1 a_2 ... a_n that has this property: |a_1 - K| <= |a_2 - K| <= ... <= |a_n - K|

#EXAMPLE
#input  [3,6,7,1,5,10,0,15] K=4
#output [3,5,6,1,7,0,10,15]


input_list = [3,6,7,1,5,10,0,15]
target = 4

print("INPUT LIST")
print(input_list)
print("TARGET: "+str(target))

support_list = []
number_of_element = len(input_list)

i=0
while i<number_of_element:
	support_list.append([abs(input_list[i]-target), input_list[i]])
	i=i+1

print("\nLIST OF DISTANCE\t[distance, original number]")
for x in support_list:
	print(x)

i=0
j=0
while i<number_of_element:
	j=i+1
	min=support_list[i][0]
	while j<number_of_element:
		if(support_list[j][0]<min):
			tmp = support_list[i].copy()
			support_list[i]=support_list[j].copy()
			support_list[j]=tmp.copy()
		j=j+1
	i=i+1


print("\nORDERED LIST OF DISTANCE")
for x in support_list:
	print(x)

ordered_distace_list=[]

for x in support_list:
	ordered_distace_list.append(x[1])


print("\nOUTPUT LIST")
print(ordered_distace_list)