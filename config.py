import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Esecuzione del ciclo principale di Tkinter
def carica_file():
    file_path = filedialog.askopenfilename()
    # Fai qualcosa con il percorso del file, ad esempio visualizzalo a console
    print("File selezionato:", file_path)

def salva_configurazione():
    nome_sensore = entry_nome_sensore.get()
    min_valore = entry_min_valore.get()
    max_valore = entry_max_valore.get()

    # Verifica che siano stati inseriti tutti i campi
    if nome_sensore and min_valore and max_valore:
        # Formatta i dati e salva su file di testo
        dati_configurazione = f"Nome Sensore: {nome_sensore}Range min : {min_valore} Range Max : {max_valore}\n"
        with open("configurazioni_sensori.txt", "a") as file:
            file.write(dati_configurazione)
            entry_nome_sensore.delete(0, tk.END)
            entry_min_valore.delete(0, tk.END)
            entry_max_valore.delete(0, tk.END)
        
        #Aggiorna l'etichetta di conferma
        #label_conferma.config(text="Configurazione salvata")
    else:
        # Mostra un messaggio di errore se mancano campi
        label_conferma.config(text="Non sono stati inseriti tutti i campi.")
        

# Creazione della finestra principale
root = tk.Tk()
root.title("Configurazione Sensori")

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

button_salva = tk.Button(root, text="Salva", command=salva_configurazione)
label_conferma = tk.Label(root, text="")

carica_pulsante = tk.Button(root, text="Carica File", command=carica_file)
#carica_pulsante.pack(pady=20)

# Posizionamento dei widget
label_nome_sensore.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_nome_sensore.grid(row=1, column=0, padx=10, pady=10)

label_min_valore.grid(row=0, column=1, padx=10, pady=10, sticky="w")
entry_min_valore.grid(row=1, column=1, padx=10, pady=10)

label_max_valore.grid(row=0, column=2, padx=10, pady=10, sticky="w")
entry_max_valore.grid(row=1, column=2, padx=10, pady=10)

button_salva.grid(row=4, column=0, columnspan=1, pady=10)
label_conferma.grid(row=4, column=0, columnspan=2, pady=10)

carica_pulsante.grid(row = 4,column = 0,columnspan=2,pady=10)


#Creazione di un pulsante per caricare il file


#Esegui il loop principale dell'applicativo
root.mainloop()

