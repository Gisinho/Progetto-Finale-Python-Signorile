import progettoFinale as pf

def menu():
    # Caricamento dei dati
    file_path = 'Progetto/clienti.csv'
    df = pf.carica_dati(file_path)

    while True:
        print("\nMenu:")
        print("1. Mostra dataset")
        print("2. Mostra informazioni sul dataset")
        print("3. Mostra descrizione del dataset")
        print("4. Distribuzione valori")
        print("5. Gestisci valori mancanti")
        print("6. Pulisci dati")
        print("7. Correggi anomalie nei dati")
        print("8. Crea colonne aggiuntive")
        print("9. Analizza relazioni con Età")
        print("10. Analizza relazioni con Durata Abbonamento")
        print("11. Analizza relazioni con Tariffa Mensile")
        print("12. Analizza relazioni Churn")
        print("13. Identifica correlazioni")
        print("14. Converti Churn in formato numerico")
        print("15. Normalizza colonne numeriche preparandole alla modellazione")
        print("0. Esci")

        try:
            scelta = int(input("\nScegli un'opzione: "))
            if scelta == 1:
                print(df)
            if scelta == 2:
                pf.info(df)
            elif scelta == 3:
                pf.descrizione(df)
            elif scelta == 4:
                pf.distribuzione_val(df)
            elif scelta == 5:
                pf.valori_mancanti(df)
            elif scelta == 6:
                df = pf.pulisci_dati(df)
                print("Dati puliti.")
            elif scelta == 7:
                df = pf.correggi_anomalie(df)
                print("Anomalie corrette.")
            elif scelta == 8:
                df = pf.crea_colonne(df)
                print("Colonne aggiuntive create.")
            elif scelta == 9:
                pf.relazioni_eta(df)
            elif scelta == 10:
                pf.relazioni_abbonamento(df)
            elif scelta == 11:
                pf.relazioni_tariffa(df)
            elif scelta == 12:
                pf.relazioni_churn(df)
            elif scelta == 13:
                pf.identifica_correlazioni(df)
            elif scelta == 14:
                pf.converti_churn(df)
            elif scelta == 15:
                pf.normalizza_colonne_numeriche(df)
            elif scelta == 0:
                print("Arrivederci")
                break
            else:
                print("Scelta non valida. Riprova.")
        
        except ValueError:
            print("Errore: inserisci un numero valido.")

menu()