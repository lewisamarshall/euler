#include <stdlib.h>
#include <stdio.h>

int *factor(int product) {

  int *result = calloc(product/2, sizeof(int));

  int remaining = product;

  for (int n = 2; n <= remaining ; n++) {
    while (remaining % n == 0){
      result[n]++;
      remaining /= n;
    }
  }
  return result;
}

int main(){
  int value = 12214;
  int *result = factor(value);
  // print results
  for (int i = 0; i < value/2; i++) {
    if (result[i]){
      printf("%i^%i\n", i, result[i]);
    }
  }
  return 0;
}




// pfactors = [2, 3, 5, 7, 11, 13, 17, 19]
// factor_number = [0]*8
// for n in range(1, 20):
//     for idx, val in enumerate(pfactors):
//         j = 0
//         m = n
//         while m % val == 0:
//             j += 1
//             m = m/val
//         if j > factor_number[idx]:
//             factor_number[idx] = j
//
// product = 1
// for idx, val in enumerate(pfactors):
//     product = product*val**factor_number[idx]
// print product
