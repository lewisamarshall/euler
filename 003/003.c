#include <stdio.h>

long n = 600851475143;
int i = 2;

int main(){
    while (i*i < n){
        while (n % i == 0){
            n /= i;
        }
        i++;
    }
    printf("%ld\n", n);
}
