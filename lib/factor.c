#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "factor.h"

int *factor(int product) {

  // upper bound on number of factors is log 2
  int bound = log((float) product) / log(2.0);

  int *result = calloc(bound, sizeof(int));

  int loc = 0;
  for (int n = 2; n <= product; n++) {
    while (product % n == 0){
      if (loc>bound){
        result[0] = -1;
      }
      result[loc] = n;
      loc++;
      product /= n;
    }
  }
  result[loc] = -1;
  return result;
}
