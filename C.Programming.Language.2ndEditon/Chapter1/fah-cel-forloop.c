#include<stdio.h>

#define LOWER 0   // LOWER, UPPER and STEP are symbolic constant and not variable
#define UPPER 300
#define STEP 30

main(){

    /*
    int fahr;
    printf("Print fahr to cels in reverse order using for loop");
    for(fahr=300; fahr>=0; fahr= fahr-30 ){
            printf("%3d%6.1f\n", fahr, (5.0/9.0)*(fahr - 32.0));
    }
    */

    int fahr;
    for(fahr = LOWER; fahr<=UPPER; fahr+= STEP){
            printf("%3d%6.1f\n", fahr, (5.0/9.0)*(fahr - 32.0));
    }

}
