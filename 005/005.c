#include <stdio.h>

int product;

int factor(int product) {
  int factors[product];
  factors[0] = 0;
  factors[1] = 0;
  int remaining = product;
  for (int n = 2; n < product; n++) {
    factors[n] = 0;
    while (remaining % n == 0){
      factors[n]++;
      remaining /= n;
    }
  }
  for (int i = 0; i < product; i++) {
    if (factors[i]){
      printf("%i^%i\n", i, factors[i]);
    }

  }
  return factors[2];
}

int main(){
  factor(222222);
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
