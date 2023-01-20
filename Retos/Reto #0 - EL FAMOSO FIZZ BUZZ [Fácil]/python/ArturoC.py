for n in range(1,101):
    if n%3==0 and n%5==0:
        print('{} --> fizzbuzz'.format(n))
    elif n%3==0:
        print('{} --> fizz'.format(n))
    elif n%5==0:
        print('{} --> buzz'.format(n))
    else:
        print('{} --> {}'.format(n,n))

        