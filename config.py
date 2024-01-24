import tkinter as tk
from tkinter import ttk

def salva_configurazione():
    nome_sensore = entry_nome_sensore.get()
    min_valore = entry_min_valore.get()
    max_valore = entry_max_valore.get()

    # Verifica che siano stati inseriti tutti i campi
    if nome_sensore and min_valore and max_valore:
        # Formatta i dati e salva su file di testo
        dati_configurazione = f"Nome Sensore: {nome_sensore}\nRange min : {min_valore}\nRange Max :{max_valore}\n"
        with open("configurazioni_sensori.txt", "a") as file:
            file.write(dati_configurazione)
        
        # Aggiorna l'etichetta di conferma
        label_conferma.config(text="Configurazione salvata")
    else:
        # Mostra un messaggio di errore se mancano campi
        label_conferma.config(text="Non sono stati inseriti tutti i campi.")
        

# Creazione della finestra principale
root = tk.Tk()
root.title("Configurazione Sensori Moto")

larghezza_finestra = 800
altezza_finestra = 600
dimensioni_finestra = f"{larghezza_finestra}x[altezza_finestra]"


# Creazione di widget
label_nome_sensore = tk.Label(root, text="Nome Sensore:")
entry_nome_sensore = tk.Entry(root)

label_min_valore = tk.Label(root, text="Valore Minimo:")
entry_min_valore = tk.Entry(root)

label_max_valore = tk.Label(root, text="Valore Massimo:")
entry_max_valore = tk.Entry(root)

button_salva = tk.Button(root, text="Salva Configurazione", command=salva_configurazione)
label_conferma = tk.Label(root, text="")

# Posizionamento dei widget
label_nome_sensore.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_nome_sensore.grid(row=0, column=1, padx=10, pady=10)

label_min_valore.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_min_valore.grid(row=1, column=1, padx=10, pady=10)

label_max_valore.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_max_valore.grid(row=2, column=1, padx=10, pady=10)

button_salva.grid(row=3, column=0, columnspan=2, pady=10)
label_conferma.grid(row=4, column=0, columnspan=2, pady=10)

# Esecuzione del ciclo principale di Tkinter
root.mainloop()