"""

lst = [1,2,3]

for i in lst:

    if lst.count(i)>1:

        print("true")
        break

else: print("false")

"""

lst = [1,2,3,1]

print(len(lst)!=len(set(lst)))