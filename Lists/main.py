lst = [0, "hello", None, True, 1+2]
print(lst)

lst = lst * 3
print(lst)

lst2 = [4,3,6,5]
print(lst + lst2)

lst3 = [1,2, lst2]
print(lst3)

lst3.append(7)
print(lst3)

lst3 = [1,2,7]
lst3.extend(lst2)
print(lst3)

lst3.sort()
print(lst3)