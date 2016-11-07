#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "../lib/factor.h"

int main(){
  int value = 12214;
  int *result = factor(value);
  // print results
  for (int i = 0; result[i]!=-1; i++) {
    printf("%i\n", result[i]);
  }
  return 0;
}
