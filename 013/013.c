#include <stdio.h>
#include <stlib.h>

# include <readline/readline.h>

int main(){
    char *line = malloc(50);
    for(i=0; i<50; i++){
        printf(readline(line));
    }
    return 0;
}