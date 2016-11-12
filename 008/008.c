#include <stdio.h>
#include <stdlib.h>

const int n = 13;
int i=0;
char character=1;
int buffer[n] = {0};
long current = 0;
long store = 0;

int main(){

  // Open the file.
  FILE *fp;
  fp = fopen ("008.txt","r");
  if (fp!=NULL) {
    // Iterate through the file.
    while ((character = fgetc(fp))) {
      if (character=='\n'){
        break;
      }
      buffer[i] = atoi(&character);
      i++; i%=n;
      current = 1;
      for (size_t j = 0; j < n; j++) {
        current *= buffer[j];
      }
      if (current>store){
        store=current;
      }
    }
    fclose (fp);
    printf("%li\n", store);
  }
  return 0;
}
