#include <stdlib.h>
#include <stdio.h>
#include "../lib/factor.h"

// Limit of loop
int max = 20;
// Record of total factors.
int factors [20] = {0};
// Temporary factor list for filtering.
int temp [20] = {0};

int main(){
  // Make a list of all the factors.
  int *result;
  for (int i = 1; i<=max; i++) {
    result = factor(i);
    for (int a = 0; result[a]>0; a++) {
      temp[result[a]]++;
    }
    free(result);
    for (int j = 0; j < max; j++) {
      if (temp[j] > factors[j]){
        factors[j] = temp[j];
      }
      temp[j]=0;
    }
  }


  // Product of all factors.
  long product = 1;
  for (int j = 0; j < max; j++) {
    for (int k = 0; k < factors[j]; k++) {
      product *= j;
    }
  }
  //print result
  printf("%li\n", product);
  return 0;
}
