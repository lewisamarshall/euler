def palindrome_test(i):
  for idx, char in enumerate(str(i)):
    if not char==str(i)[-(idx+1)]:
      return False
  return True
