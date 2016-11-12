#include "../lib/prime.h"
#include <stdio.h>

long total=0;

int main(){
  for (long i = 2; i < 2000000; i++) {
    if (prime(i)) {
      total+=i;
    }
  }
  printf("%li\n", total);
}
