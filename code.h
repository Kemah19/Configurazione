#ifndef CODE_H
#define CODE_H

//configurazione mapping_info_sensors da file.txt
int config_sens(float*** mapping,int num_sens);

//libera la memoria allocatta per mapping_info
void free_mapping(float*** mapping,int num_sens);

#endif