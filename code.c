#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_CHAR 100

typedef struct {
    char name_sensors[MAX_CHAR];
    float Range_Min;
    float Range_Max;
} SensorData;

int main() {
    FILE *file = fopen("configurazioni_sensori.txt", "r");

    if (file == NULL) {
        perror("Errore nell'apertura del file");
        return 1;
    }

    // Ignora l'intestazione
    char line[MAX_CHAR];
    fgets(line, sizeof(line), file);

    // Leggi i dati
    SensorData sensors[10];
    int i = 0;
    while (fscanf(file, "%[^,],%f,%f\n", sensors[i].name_sensors, &sensors[i].Range_Min, &sensors[i].Range_Max) == 3 && i < 10) {
        i++;
    }

    // Stampa i dati letti
    for (int j = 0; j < i; j++) {
        printf("Nome: %s Range_Min: %.2f Range_Max: %.2f\n", sensors[j].name_sensors, sensors[j].Range_Min, sensors[j].Range_Max);
    }

    fclose(file);
    return 0;
}

