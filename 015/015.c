#include <stdio.h>

unsigned long paths( int n);

int main(){
    printf("%lu\n", paths(20));
    // printf("%ld", factorial(20));
    return 0;


// print math.factorial(40)/math.factorial(20)**2
}

unsigned long paths( int n){

    unsigned long result = 1;
    for(int i=1; i<=n; i++){
        printf("i = %d\n", i);
        printf("m+i = %d\n", i+n);
        result = result * (i+n)/(i);
        printf("result = %lu\n", result);
    }
    return result;
}



// unsigned long long factorial (int i, int j){
    // if kk
    // unsigned long long temp = i;
    // if(i==j){
        // return j;
    // }else{
        // return factorial(i-1, j)*i;
    // }
// }