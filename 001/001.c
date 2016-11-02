#include <stdio.h>

int main() {
  int i;
  int total = 0;

  for (i=1; i<1000; i++) {
    if (i % 3 ==0){
      total += i;
    } else if (i % 5==0){
      total += i;
    }
  };
   /* my first program in C */
   printf("%i\n", total);

   return 0;
}
