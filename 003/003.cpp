#include <iostream>
using namespace std;

long n = 600851475143;
int i = 2;

int main(){
    while (i*i < n){
        while (n % i == 0){
            n /= i;
        }
        i++;
    }
    cout << n << "\n";
}
