import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import subprocess

import csv

def save_config():
    # Lista per contenere i dati
    list_data = []
    
    for i in range(0, 10):
        nome_sensore = entry_name[i].get()
        min_valore = float(entry_min[i].get())
        max_valore = float(entry_max[i].get())

        
        if nome_sensore and isinstance(min_valore,float) and isinstance(max_valore,float):
     
            list_data.append([nome_sensore, min_valore, max_valore])
        else:
            
            label_conferma.config(text="Non sono stati inseriti tutti i campi o formato non consentito.")

    
    with open("configurazioni_sensori.txt", mode="w", newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["name_sensors", "Range_Min", "Range_Max"])
        csv_writer.writerows(list_data)

    label_conferma.config(text="Dati salvati correttamente.")


def load_file():
    for j in range(0,10):
        entry_name[j].delete(0, tk.END)
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
                    range_min = row[1]
                    range_max = row[2]

                    entry_name[i].insert(0, name_sensors)
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
min = tk.Label(root, text="Min_value:")
max = tk.Label(root, text="Max_value:")
label_conferma = tk.Label(root, text="")
button_save = tk.Button(root, text="Save", command=save_config)
carica_pulsante = tk.Button(root, text="Carica File", command=load_file)
button_finish = tk.Button(root, text="Finish", command=finish)
button_close = tk.Button(root, text="Close", command=close)

name.grid(row=0, column=0, padx=10, pady=10, sticky="w")
min.grid(row=0, column=1, padx=10, pady=10, sticky="w")
max.grid(row=0, column=2, padx=10, pady=10, sticky="w")
button_save.grid(row=12, column=0, columnspan=1, pady=10)
carica_pulsante.grid(row = 12,column = 0,columnspan=2,pady=10)
label_conferma.grid(row=11, column=0, columnspan=2, pady=10)
button_finish.grid(row = 12, column = 3, columnspan=1, pady=5)
button_close.grid(row = 12, column = 2, columnspan=1, pady=5,padx =10)

entry_name = [tk.Entry(root) for _ in range(10)]
entry_min = [tk.Entry(root) for _ in range(10)]
entry_max = [tk.Entry(root) for _ in range(10)]


for i in range(1, 11):
    entry_name[i-1].grid(row=i, column=0, padx=10, pady=10)
    entry_min[i-1].grid(row=i, column=1, padx=10, pady=10)
    entry_max[i-1].grid(row=i, column=2, padx=10, pady=10)

root.mainloop()