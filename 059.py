import csv
import string

datafile = open('cipher1.txt')
reader = csv.reader(datafile)
for row in reader:
  cipher=(map(int, row))

print len(cipher)

def xor_decipher(cipher, key):
  msg=''
  for idx, letter in enumerate(cipher):
    keyletter=ord(key[idx%len(key)])
    # letter=ord(letter)
    newletter=chr((letter)^(keyletter))
    msg+=newletter
  return msg



# for letter1 in string.lowercase:
#  for letter2 in string.lowercase:
#    for letter3 in string.lowercase:
#      key=letter1+letter2+letter3
#      msg=xor_decipher(cipher, key)
#      if 'Gospel' in msg:
#        print key
#        print msg

msg=xor_decipher(cipher, 'god')
print sum(map(ord, msg))
