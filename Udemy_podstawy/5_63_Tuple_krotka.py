if __name__ == '__main__':
    Tax = (4,7,8,23,8)
    print(Tax)

    print(Tax[1])
    print(Tax[-1])

    print(Tax.index(7))
    print(Tax.count(8))
    print(max(Tax))
   # print(Tax.revert()) blad

    TaxList = list(Tax)
    TaxList.append(30)
    NewTax = tuple(TaxList)
    print(Tax)
    print(TaxList)
    print(NewTax)

    print('-----------------------------------')
    #print(Tax)
    (tax1,tax2,tax3,tax4,tax5) = Tax
    print(tax1,tax2,tax3,tax4,tax5)

    a=1
    b=10
    print("a=",a,"\tb =",b)

    (a,b) = (b,a)
    print("a=", a, "\tb =", b)