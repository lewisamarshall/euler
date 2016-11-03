#include <stdio.h>

int total = 0;

int main() {

  for (int i=1; i<1000; i++) {
    if ( !(i%3) || !(i%5) ){
      total += i;
    }
  }
   printf("%i\n", total);
   return 0;
}
