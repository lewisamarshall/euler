examples=[]

def canceling_test(numerator, denominator, digit):
  if not numerator/denominator<1:
    return False
  if str(digit) not in str(numerator) or str(digit) not in str(denominator):
    return False
  new_num=("".join([i for i in str(numerator) if not i==str(digit)]))
  new_den=("".join([i for i in str(denominator) if not i==str(digit)]))
  if not new_num or not new_den:
    return False
  elif not int(new_num) or not int(new_den):
    return False
  elif float(new_num)/float(new_den)==float(numerator)/float(denominator):
    return True
  else:
    return False

print canceling_test(49, 98, 9)


for numerator in range(11,100):
  for denomimator in range(11,100):
    for digit in range(1,10):
      if canceling_test(numerator, denomimator, digit):
        print numerator, denomimator, digit
        examples.append(float(numerator)/float(denominator)
