#include <stdlib.h>
#include <stdio.h>
#include <string.h>

const int n = 20;
int m = 4;
int array [n] [n] = {0};
long product = 0;
long temp = 0;

int main(){

  char * line = NULL;
  size_t len = 0;
  ssize_t read;
  char * token;
  int i=0; int j=0;

  FILE *fp;
  fp = fopen ("011.dlm","r");
  if (fp==NULL){
    exit(EXIT_FAILURE);
  }

  //Read in array
  while ((read = getline(&line, &len, fp)) != -1) {
        token = strtok(line, " \n");
        for (int j=0; j<n; j++){
          array[i][j]=atoi(token);
          token = strtok(NULL," ");
        }
        i++;
  }

  fclose(fp);

  //check horizontal
  for (size_t i = 0; i < n; i++) {
    for (size_t j = 0; j < n-m; j++) {
      temp = 1;
      for (size_t k = 0; k < m; k++) {
        temp *= array[i][j+k];
        if (temp>product){
          product = temp;
        }
      }
    }
  }

  //check vertical
  for (size_t i = 0; i < n-m; i++) {
    for (size_t j = 0; j < n; j++) {
      temp = 1;
      for (size_t k = 0; k < m; k++) {
        temp *= array[i+k][j];
        if (temp>product){
          product = temp;
        }
      }
    }
  }

  //check upper-left diagonial
  for (size_t i = 0; i < n-m; i++) {
    for (size_t j = 0; j < n-m; j++) {
      temp = 1;
      for (size_t k = 0; k < m; k++) {
        temp *= array[i+k][j+m-k];
        if (temp>product){
          product = temp;
        }
      }
    }
  }
  //check lower-right diagonal
  for (size_t i = 0; i < n-m; i++) {
    for (size_t j = 0; j < n-m; j++) {
      temp = 1;
      for (size_t k = 0; k < m; k++) {
        temp *= array[i+k][j+k];
        if (temp>product){
          product = temp;
        }
      }
    }
  }

  // print result
  printf("%li\n", product);
  return 0;
}
