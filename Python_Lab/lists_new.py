import copy 
li1 = [1, 2, [3,5], 4]  
li2 = copy.deepcopy(li1) 	# using deepcopy to deep copy 
li3 = copy.copy(li1)	# using copy to shallow copy
print (li1) 			#ANS: 1 2 [3, 5] 4
li2[2][0] = 7
print (li2) 			#ANS: 1 2 [7, 5] 4 
# Change is NOT reflected in original list
print (li1) 			#ANS: 1 2 [3, 5] 4 

li3[2][0] = 7
# Change is Reflected in original list
print (li1) 			#ANS: 1 2 [7, 5] 4 
