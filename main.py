'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
    n = int(input("Number: "))
    if n< 2:
        return False
    if n == 2 :
        return True

    for i in range(2,n):
        if n%i == 0 :
            return False

    return True

  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
    produs = 1
    for i in lst :
        produs = produs * i

    return produs




    '''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.

    '''

def get_cmmdc_v1(x, y):
    while x != y:
        if x > y :
            x = x- y
        else :
            y = y -x

    return x

  
  
    '''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
    '''
def get_cmmdc_v2(x, y):
    while  y :
        r = x % y
        x = y
        y = r

    return  x

  
  
def main():
    print(get_product([3,4,5]))
    print(get_cmmdc_v1(12,36))
    print(get_cmmdc_v2(12,36))
if __name__ == '__main__':
  main()
