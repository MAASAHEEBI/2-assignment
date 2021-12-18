
#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

L = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
length = len(L)

for count in range(length):
    for count2 in range(length - 1):
        sec_val = L[count2][1] 
        sec_val_next = L[count2 + 1][1] 
        if sec_val > sec_val_next:
            
            L[count2],L[count2 + 1]= L[count2 + 1],L[count2]
print(L)

