#include <iostream>
using namespace std;

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
  cout << total << "\n";
  return 0;
}
