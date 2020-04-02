def asterisk_test(a, *args):
    print(a, args)
    print(type(args))

asterisk_test(1,2,3,4,5,6)



u = [2,2]
v = [2,3]
z = [3,5]

result = [sum(t) for t in zip(u,v,z)]
print(result)


matrix_a = [[1,1,2],[2,1,1]]
matrix_b = [[1,1],[2,1],[1,3]]
result = [[sum(a*b for a, b in zip(row_a, column_b))
            for column_b in zip(*matrix_b)] for row_a in matrix_a]
print(result)
