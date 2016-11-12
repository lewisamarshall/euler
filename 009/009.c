#include <stdio.h>
#include <math.h>

const int count=1000;
long a, b, c;

int main(){
  for (a = 1; a < count; a++) {
    for (b = 1; b < a; b++) {
      if (((a*a + b*b)) == ((1000-a-b)*(1000-a-b))){
        c = (long) sqrt(a*a + b*b);
        printf("%li, %li, %li\n", a, b, c);
        printf("%li\n", a*b*c);
        return 0;
      }
    }
  }
}
