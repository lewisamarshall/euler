#include <stdlib.h>
#include <stdio.h>
#include <math.h>

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

int main(){
  int value = 12214;
  int *result = factor(value);
  // print results
  for (int i = 0; result[i]!=-1; i++) {
    printf("%i\n", result[i]);
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
