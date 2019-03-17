def myazdir(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print("[ ",m[i][j]," ]", end=" ")
        print()

def gauss_jordan(m):
    for i in range(len(m)):
        for j in range(len(m)-1, i, -1):
            kat = m[j][i] / m[i][i]
            for k in range(len(m[0])):
                m[j][k] -= kat*m[i][k]


    for i in range(len(m)-1, 0, -1):
        for j in range(i-1, -1, -1):
            kat = m[j][i] / m[i][i]
            for k in range(len(m[0])):
                m[j][k] -= kat * m[i][k]

    for i in range(len(m)):
        m[i][-1] = m[i][-1] / m[i][i]
        m[i][i] = m[i][i] / m[i][i]
    myazdir(m)
    return m


A = [[1, 2, 1, 5], [2, 5, 3, 14], [-1, -3, 1, -6]]

# x + 2y + z =5
# 2x + 5y + 3z =14
# -x -3y +z = -6

B = [[1, 2, 4], [3, 4, 9]]

# x + 2y =4
# 3 + 4y = 9

C = [[1, 2, 4, 4, 42],
     [2, 3, 5, 5, 79],
     [3, 2, 5, 8, 67],
     [9, 5, 9, 7, 99]]#4x4



D = [[1,-2,1,1],
    [2,-5,3,4],
    [2,-3,1,0]] # sonsuz cozume sahip

gauss_jordan(C)
# 0'a bolme hatasi alan matrisler icin hata kontrol eklenecek...