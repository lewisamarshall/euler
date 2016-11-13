#include "../lib/factor.h"
#include <stdio.h>

long triangle=0;
long i = 1;
long j = 1;


int main(){
  long *factors;
  while (i<80000000){
    // Create the next triangle number
    triangle += i;
    printf("%li\n", triangle);

    // Find the factors.
    factors = factor(triangle);

    // Find the number of divisors
    // TODO: Make this work properly.
    j=0;
    while (factors[j]!=-1){
      j++;
    }
    if (j>=15){
      break;
    }
    i++;
  }
  printf("%li\n", triangle);
  return 0;
}
