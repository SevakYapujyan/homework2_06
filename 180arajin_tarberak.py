ls = [
[1,2,3,4],
[5,6,7,8,],
[9,10,11,12],
[13,14,15,16]
]
ls_new = []
ls1 = ls[0]
ls2 = ls[1]
ls3 = ls[2]
ls4 = ls[3]

ls1 = ls1[::-1]
ls2 = ls2[::-1]
ls3 = ls3[::-1]
ls4 = ls4[::-1]

ls_new.append(ls4)
ls_new.append(ls3)
ls_new.append(ls2)
ls_new.append(ls1)
print(ls_new)
