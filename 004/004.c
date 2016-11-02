#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int i;
int j;
int product;
int greatest = 0;

int main(){
    for (i=999; i>=100; i--){
        for (j=999; j>=i; j--){
            product = i * j;
            if (product > greatest){
                if (palindrome(product)){
                    greatest = product;
                }
            }
        }
    }
    printf("%i\n", greatest);
}

int palindrome(int x){

    char buffer [33];
    int length;
    int k;

    snprintf(buffer, 33, "%i", x);
    length = strlen(buffer);
    for (k=0; buffer[k]; k++){
        if (buffer[k] != buffer[length-i-1]) {
            return 0;
        }
    }
    return 1;
};

// def ispal(x):
//     x = str(x)
//     for i in range(len(x)):
//         if not x[i-1] == x[-i]:
//             return False
//     return True

// greatest = 0;
// for i in range(999, 100, -1):
//     for j in range(999, i, -1):
//         product = i*j
//         if product > greatest:
//             if ispal(product):
//                 greatest = product
//         else:
//             break
// print(greatest)
