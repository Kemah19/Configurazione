#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "code.h"


int main(){
    float** mapping_sensors = NULL;
    config_sens(&mapping_sensors,11);

    free_mapping(&mapping_sensors,11);
    
}