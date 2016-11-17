#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "factor.h"

long *factor(long product) {

  // upper bound on number of factors is log 2
  int bound = log((float) product) / log(2.0);

  long *result = calloc(bound, sizeof(long));

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

int main(int argc, char * argv[]) {
  char *ptr;
  long n = strtol(argv[1], &ptr, 10);
  long *p = factor(n);
  for (size_t i = 0; p[i]!=-1; i++) {
    printf("%li\n", p[i]);
  }

  free(p);

  return 0;
}
