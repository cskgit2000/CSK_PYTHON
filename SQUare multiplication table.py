for row in range(1,12):
    for column in range (1,12):
        product=row*column
        if product<10:
            print('',product,'',end='')

        else:
            print(product,'',end='')
    print()