#include<stdio.h>

main(){

    int c , nl, tab, blank;
    nl = 0;
    tab = 0;
    blank = 0;

    while((c= getchar()) != EOF){

            if(c=='\n'){
                    ++nl;
            }
            else if (c =='\t'){
                ++tab;
            }
            else if (c ==' '){
                ++blank;
            }

    }
    printf("\nNew lines: %d \n Tabs: %d \n Blanks: %d\n", nl, tab, blank);

}
