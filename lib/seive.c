#include "seive.h"
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

long *seive(long limit) {
  long max_divisor = sqrt((float) limit);
  long *result = calloc(limit, sizeof(long));

  for (long i = 0; i < limit; i++) {
    result[i] = i;
  }

  result[1] = 0;

  for (long i = 2; i < max_divisor; i++) {
    if (result[i]==i){
      for (long j = i; j*i < limit; j++) {
        result[j*i] = 0;
      }
    }
  }
  return result;
}


int main(int argc, char * argv[]) {
  char *ptr;
  long n = strtol(argv[1], &ptr, 10);
  long *p = seive(n);
  for (size_t i = 0; i < n; i++) {
    if (p[i]){
      printf("%li\n", p[i]);
    }
  }
  free(p);

  return 0;
}
