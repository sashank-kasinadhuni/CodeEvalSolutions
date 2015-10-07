def Mult_table():
    for i in range(1,13):
        for j in range(1,13):
            print('{0:{width}}'.format(i*j,width = 4) if j!=1 else i*j,end = '')
        print()

Mult_table()
