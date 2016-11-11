#include "prime.h"
#include <stdio.h>
#include <math.h>

int prime(value){
  if (value<2) {
    return 0;
  }
  if (value==2 | value==3){
    return 1;
  }
  if (value%2==0 | value%3==0){
    return 0;
  }

  int max_divisor = sqrt((float) value);
  int divisor = 5;

  while (divisor <= max_divisor) {
    if (value%divisor == 0 | value%(divisor+2)==0) {
      return 0;
    }
    divisor += 6;
  }
  return 1;
}
