#include <stdio.h>

long  MAXSIZE = 100 000 000 000;
long collatz (long n);

long collatz_ref[100 000 000 000];

int main(){
    int longest = 0;
    int best_result = 0; 
    int result = 0;
    collatz_ref[1] = 1;

    for (int i =1; i<=1000000; i++){
        result = collatz(i);
        if (result>longest){
            longest=result;
            best_result=i;
        } else if (result == -1){
            printf("Input %d exceeds allocated memory.", i);
            return -1;
        }

    }
    printf("Result: %i\n", longest);
    printf("Best_Input: %i\n", best_result);

    printf("Correct: %li\n", collatz(837799));
    return 0;
}




long collatz(long n){
    long i = 0;
    long n_orig = n; 

    while(!collatz_ref[n]){
        // printf("%li\n", n);
        i += 1;
        if (n%2==0){
            n=n/2;
        } else {
            n = n*3+1;
            if (n>MAXSIZE){

                return -1;
            }
        }
    }

    collatz_ref[n_orig] = collatz_ref[n] + i;


    return collatz_ref[n_orig]-1;

}