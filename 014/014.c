#include <stdio.h>

long  MAXSIZE = 9223372036854775807;
long collatz (long n);

long collatz_ref[1000000];

int main(){
    int longest = 0;
    int best_result = 0; 
    int result = 0;

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

    while (n>1) {
        // printf("loop %li\n", n);
        if (n < 100000){
            if (collatz_ref[n]!=0){
                // printf("lookup %li\n", n);
                collatz_ref[n_orig] = collatz_ref[n] + i;
                break;
            }
        }
        
        i += 1;
        if (n%2==0){
            // printf("dividing %li\n", n);
            n=n/2;
        } else {
            // printf("multiplying %li\n", n);
            n = n*3+1;
            if (n>MAXSIZE){
                return -1;
            }
        }
    collatz_ref[n_orig] = i;
    }


    return collatz_ref[n_orig];

}