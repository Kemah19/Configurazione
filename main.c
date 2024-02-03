#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "code.h"


int main(){
    float** mapping_sensors = NULL;
    config_sens(&mapping_sensors,11);

    for (int i = 0; i < 11; i++) {
        for (int j = 0; j < 4; j++) {
            printf("%f ", mapping_sensors[i][j]);
        }
        printf("\n");
    }

    free_mapping(&mapping_sensors,11);
    
}