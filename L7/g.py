from decimal import Decimal,ROUND_HALF_UP
print(Decimal('0.1')+Decimal('0.2'))
print(Decimal('0.1').log10())
n=Decimal('4.65')
n_rounded=n.quantize(Decimal('0.0'),rounding=ROUND_HALF_UP)
print(n_rounded)
