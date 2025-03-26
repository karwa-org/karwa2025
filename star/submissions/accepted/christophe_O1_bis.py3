from decimal import Decimal, getcontext
getcontext().prec = 50
print(int((Decimal(2*Decimal(int(input()))-1).sqrt()+1)//2)-1)