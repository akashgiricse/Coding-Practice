#include<stdio.h>

/* print fahrenheit to celsius table
    for fahr = 0, 20, 40, ... , 200 */

main(){

        // int fahr, celsius;
        float fahr, celsius; /* using float instead of int */
        int lower, upper, step;
        lower = 0;  /* lower limit of temp */
        upper = 300; /* upper limit of temp */
        step = 20;  /* step size */
        fahr = lower;

        printf("Table to convert fahrenheit to celsius \n\n");
        while(fahr<=upper){
                // celsius = 5*(fahr - 32)/ 9;  /* can not use 5/9 as the int will truncate it to zero */
                // printf("%d\t%d\n", fahr, celsius);
                // printf("%3d %6d \n", fahr, celsius);

                celsius = (5.0/9.0)*(fahr - 32.0);
                printf("%3.0f %6.1f\n", fahr, celsius);
                fahr = fahr + step;
        }

}
