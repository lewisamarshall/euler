#include "../lib/prime.h"
#include <stdio.h>

int n = 1;
int count = 0;

int main(){
  while (count<=10000){
    n++;
    if (prime(n)){
      count++;
    }
  }
  printf("%i\n", n);
  return 0;
}
