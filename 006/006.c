#include <stdio.h>

long total=0;
long summation=0;
int limit=100;

int main(){
  for (size_t i = 1; i <= limit; i++) {
    total -= i*i;
    summation += i;
  }

  total += summation * summation;

  printf("%li\n", total);
  return 0;
}
