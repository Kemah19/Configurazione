import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import subprocess

import csv

def save_config():
    # Lista per contenere i dati
    list_data = []
    
    for i in range(0, 11):
        if (entry_name[i].get() != '' and 
            entry_in_min[i].get() != '' and 
            entry_in_max[i].get() != '' and
            entry_min[i].get() != '' and
            entry_max[i].get() != ''):
            
            try:
                nome_sensore = int(entry_name[i].get())
                in_min = int(entry_in_min[i].get())
                in_max = int(entry_in_max[i].get())
                min_valore = float(entry_min[i].get())
                max_valore = float(entry_max[i].get())
            except:
                label_conferma.config(text="caratteri non consentiti")
            else:
                if (isinstance(nome_sensore, int) and isinstance(in_min, int) and isinstance(in_max, int) and isinstance(min_valore, float) and isinstance(max_valore, float)):
                    list_data.append([nome_sensore, in_min,in_max,min_valore, max_valore])
        
        else:
            label_conferma.config(text="non sono stati inseriti tutti i valori")
    if (len(list_data)==11):
        with open("configurazioni_sensori1.txt", mode="w", newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["name_sensors","in_min","in_max", "Range_Min", "Range_Max"])
            csv_writer.writerows(list_data)

        label_conferma.config(text="Dati salvati correttamente.")

    else:
        pass
        #label_conferma.config(text="Non sono stati inseriti tutti i valori")

def load_file():
    for j in range(0,11):
        entry_name[j].delete(0, tk.END)
        entry_in_min[j].delete(0, tk.END)
        entry_in_max[j].delete(0, tk.END)
        entry_min[j].delete(0, tk.END)
        entry_max[j].delete(0, tk.END)
    file_path = filedialog.askopenfilename(filetypes=[("File di testo", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'r', newline='') as file:
              
                csv_reader = csv.reader(file)
                next(csv_reader, None)

                for i, row in enumerate(csv_reader):
                    name_sensors = row[0]
                    in_min = row[1]
                    in_max = row[2]
                    range_min = row[3]
                    range_max = row[4]

                    entry_name[i].insert(0, name_sensors)
                    entry_in_min[i].insert(0, in_min)
                    entry_in_max[i].insert(0, in_max)
                    entry_min[i].insert(0, range_min)
                    entry_max[i].insert(0, range_max)

        except csv.Error as e:
            print(f"Errore durante l'analisi del file CSV: {e}")

def close ():
    root.destroy()

def finish():
    save_config()
    script_path = "script.sh"
    try:
        subprocess.run(['bash',script_path],check=True)
        print("Success")
        root.destroy()
    except subprocess.CalledProcessError as error:
        print(f"Error:{error}")

root = tk.Tk()
root.title("Configurazione Sensori")
name = tk.Label(root, text="Nome Sensore:")
in_min = tk.Label(root, text="In_min:")
in_max = tk.Label(root, text="In_max:")
min = tk.Label(root, text="Min_value:")
max = tk.Label(root, text="Max_value:")
label_conferma = tk.Label(root, text="")
button_save = tk.Button(root, text="Save", command=save_config)
carica_pulsante = tk.Button(root, text="Carica File", command=load_file)
button_finish = tk.Button(root, text="Finish", command=finish)
button_close = tk.Button(root, text="Close", command=close)

name.grid(row=0, column=0, padx=10, pady=10, sticky="w")
in_min.grid(row=0, column=1, padx=10, pady=10, sticky="w")
in_max.grid(row=0, column=2, padx=10, pady=10, sticky="w")
min.grid(row=0, column=3, padx=10, pady=10, sticky="w")
max.grid(row=0, column=4, padx=10, pady=10, sticky="w")
button_save.grid(row=13, column=0, columnspan=1, pady=10)
carica_pulsante.grid(row = 13,column = 0,columnspan=2,pady=10)
label_conferma.grid(row=12, column=0, columnspan=2, pady=10)
button_finish.grid(row = 13, column = 3, columnspan=1, pady=5)
button_close.grid(row = 13, column = 2, columnspan=1, pady=5,padx =10)

entry_name = [tk.Entry(root) for _ in range(11)]
entry_in_min = [tk.Entry(root) for _ in range(11)]
entry_in_max = [tk.Entry(root) for _ in range(11)]
entry_min = [tk.Entry(root) for _ in range(11)]
entry_max = [tk.Entry(root) for _ in range(11)]



for i in range(1, 12):
    entry_name[i-1].grid(row=i, column=0, padx=10, pady=10)
    entry_in_min[i-1].grid(row=i, column=1, padx=10, pady=10)
    entry_in_max[i-1].grid(row=i, column=2, padx=10, pady=10)
    entry_min[i-1].grid(row=i, column=3, padx=10, pady=10)
    entry_max[i-1].grid(row=i, column=4, padx=10, pady=10)

root.mainloop()