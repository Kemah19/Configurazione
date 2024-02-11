#include <stdio.h>
#include <stdlib.h>
#include "code.h"

#define MAX_VAL 100

int config_sens(float*** mapping, int num_sens) {
    *mapping = (float**)malloc(num_sens * sizeof(float*));
    if (*mapping == NULL) {
        printf("memory allocation error");
        return 1;
    }

    for (int i = 0; i < num_sens; i++) {
        (*mapping)[i] = (float*)malloc(4 * sizeof(float));
        if ((*mapping)[i] == NULL) {
            printf("memory allocation error");
            for (int j = 0; j < i; j++) {
                free((*mapping)[j]);
            }
            free(*mapping);
            return 1;
        }
    }

    FILE* file = fopen("configurazioni_sensori.txt", "r");
    if (file == NULL) {
        printf("Error in file opening");
        for (int i = 0; i < num_sens; i++) {
            free((*mapping)[i]);
        }
        free(*mapping);
        return 1;
    }

    char line[MAX_VAL];
    fgets(line, sizeof(line), file);
    //int name=0;
    int i = 0;
    while (fscanf(file, "%*d,%f,%f,%f,%f\n",&(*mapping)[i][0], &(*mapping)[i][1], &(*mapping)[i][2], &(*mapping)[i][3]) != EOF) {
        i++;
    }

    fclose(file);
    return 0;
}

void free_mapping(float*** mapping,int num_sens) {
    for (int i = 0; i < num_sens; i++) {
        free((*mapping)[i]);
    }
    free(*mapping);
}
