import decimal
import string
decimal.getcontext().prec = 110

# a = str(decimal.Decimal(2).sqrt())
# print a
total = 0
for i in range(1,101):
    s = (decimal.Decimal(i).sqrt())
    if not s == int(s):
        digs = [n for n in str(s) if n.isdigit()]
        for n in digs[:100]:
            total += int(n)
print total
