"""
Obiettivo: Utilizzare pandas e numpy per esplorare, pulire, trasformare e analizzare un dataset di clienti della compagnia di
telecomunicazioni. L'esercizio mira a costruire un modello predittivo di base per la churn rate e scoprire correlazioni tra
vari attributi del cliente e la loro fedeltà.
Dataset: 
ID_Cliente: Identificativo unico per ogni cliente
Età: Età del cliente
Durata_Abonnamento: Quanti mesi il cliente è stato abbonato
Tariffa_Mensile: Quanto il cliente paga al mese
Dati_Consumati: GB di dati consumati al mese
Servizio_Clienti_Contatti: Quante volte il cliente ha contattato il servizio clienti
Churn: Se il cliente ha lasciato la compagnia (Sì/No)
Caricamento e Esplorazione Iniziale:
Caricare i dati da un file CSV.
Utilizzare info(), describe(), e value_counts() per esaminare la distribuzione dei dati e identificare colonne con
valori mancanti.
Pulizia dei Dati:
Gestire i valori mancanti in modo appropriato, considerando l'imputazione o la rimozione delle righe.
Verificare e correggere eventuali anomalie nei dati (es. età negative, tariffe mensili irrealistiche).
Analisi Esplorativa dei Dati (EDA):
Creare nuove colonne che potrebbero essere utili, come Costo_per_GB (tariffa mensile divisa per i dati consumati).
Utilizzare groupby() per esplorare la relazione tra Età, Durata_Abonnamento, Tariffa_Mensile e la Churn.
Utilizzare metodi come corr() per identificare possibili correlazioni tra le variabili.
Preparazione dei Dati per la Modellazione:
Convertire la colonna Churn in formato numerico (0 per "No", 1 per "Sì").
Normalizzare le colonne numeriche usando numpy per prepararle per la modellazione.
"""

import pandas as pd


def carica_dati(file_path):
    df = pd.read_csv(file_path)
    return df

def info(df):
    print("\nInfo sul dataset:")
    print(df.info())

def descrizione(df):
    print("\nDescrizione:")
    print(df.describe())
    
def valori_mancanti(df):    
    print("\nValori per colonna:")
    print(df.value_counts())
    # valori mancanti (media delle tariffe mensili)
    df['Tariffa_Mensile'].fillna(df['Tariffa_Mensile'].mean(), inplace=True)
    print("Valori mancanti gestiti con inplace.")


def pulisci_dati(df):
    # Gestire i valori mancanti
    df = df.dropna()  # Rimuove le righe con valori mancanti
    return df

def correggi_anomalie(df):
    # Correggere anomalie nei dati(valori negativi e 0)
    df = df[df['Età'] >= 0]
    df = df[df['Tariffa_Mensile'] > 0]
    return df

# Analisi Esplorativa dei Dati (EDA)
def crea_colonne(df):
    df['Costo_per_GB'] = df['Tariffa_Mensile'] / df['Dati_Consumati']
    return df

def relazioni_churn(df):
    print("Relazione tra variabili e Churn:")
    print(df.groupby('Churn')[['ID_Cliente']].count())

def relazioni_eta(df):
    print("Relazione tra variabili e Età:")
    print(df.groupby('Età')[['ID_Cliente']].count())  

def relazioni_abbonamento(df):
    print("Relazione tra variabili e Abbonamento:")
    print(df.groupby('Durata_Abbonamento')[['ID_Cliente']].count()) 

def relazioni_tariffa(df):
    print("Relazione tra variabili e Tariffe:")
    print(df.groupby('Tariffa_Mensile')[['ID_Cliente']].count())      
    

def identifica_correlazioni(df):
    print("\nCorrelazioni tra le variabili:")
    correlazione = df.corr()
    print(correlazione)

def converti_churn(df):
    #funzione che prende un valore(x elemntocolonna churn)
    #La lambda function restituisce 1 se x è uguale a 'Yes', altrimenti restituisce 0
    df['Churn'] = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0) 
    print("Churn convertita in numerico.")
