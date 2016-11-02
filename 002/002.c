#include <stdio.h>

int total = 0;
int a = 1;
int b = 2;
int c;

int main(){
  while (b<4000000) {
    if (b%2==0) {
      total += b;
    }
    c = b;
    b = a + b;
    a = c;
  }
  printf("%i\n", total);
  return 0;
}


// total = 0
// a = 1
// b = 2
//
// while b < 4000000:
//     if b % 2 == 0:
//         total += b
//     [a, b] = [b, a+b]
// print(total)
