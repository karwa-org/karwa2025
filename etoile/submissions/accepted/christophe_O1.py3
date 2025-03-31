from decimal import Decimal, getcontext
getcontext().prec = 50 # f(x)=2x^2+2x+1; so x = (sqrt(2f(x)-1)-1)/2
print(int((Decimal(2*Decimal(int(input()))-1).sqrt()-1)//2))