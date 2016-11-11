#include <stdio.h>

char character=1;

int main(){

  FILE *fp;
  fp = fopen ("008.txt","r");
  if (fp!=NULL) {
    while (character!=EOF) {
      character = fgetc(fp);
      printf("%c", character);
    }
    fclose (fp);
  }
  return 0;
}
