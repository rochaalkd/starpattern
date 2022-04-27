n=int(input('Enter no.of rows:'))
i=0
while i<=n:
    j=0
    while j<=n-i:
        print('*',end=' ')
        j+=1

    print()
    i+=1