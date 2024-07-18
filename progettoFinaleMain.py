import progettoFinale as pf

def menu():
    # Caricamento dei dati
    file_path = 'Progetto/clienti.csv'
    df = pf.carica_dati(file_path)

    while True:
        print("\nMenu:")
        print("1. Mostra informazioni sul dataset")
        print("2. Mostra descrizione del dataset")
        print("3. Gestisci valori mancanti")
        print("4. Pulisci dati")
        print("5. Correggi anomalie nei dati")
        print("6. Crea colonne aggiuntive")
        print("7. Analizza relazioni con Churn")
        print("8. Analizza relazioni con Età")
        print("9. Analizza relazioni con Durata Abbonamento")
        print("10. Analizza relazioni con Tariffa Mensile")
        print("11. Identifica correlazioni")
        print("12. Converti Churn in formato numerico")
        print("13. Normalizza colonne numeriche preparandole alla modellazione")
        print("0. Esci")

        try:
            scelta = int(input("Scegli un'opzione: "))
            
            if scelta == 1:
                pf.info(df)
            elif scelta == 2:
                pf.descrizione(df)
            elif scelta == 3:
                pf.valori_mancanti(df)
            elif scelta == 4:
                df = pf.pulisci_dati(df)
                print("Dati puliti.")
            elif scelta == 5:
                df = pf.correggi_anomalie(df)
                print("Anomalie corrette.")
            elif scelta == 6:
                df = pf.crea_colonne(df)
                print("Colonne aggiuntive create.")
            elif scelta == 7:
                pf.relazioni_churn(df)
            elif scelta == 8:
                pf.relazioni_eta(df)
            elif scelta == 9:
                pf.relazioni_abbonamento(df)
            elif scelta == 10:
                pf.relazioni_tariffa(df)
            elif scelta == 11:
                pf.identifica_correlazioni(df)
            elif scelta == 12:
                pf.converti_churn(df)
            elif scelta == 13:
                pf.normalizza_colonne_numeriche(df)
                print("Hai normalizzato le colonne")
            elif scelta == 0:
                print("Arrivederci")
                break
            else:
                print("Scelta non valida. Riprova.")
        
        except ValueError:
            print("Errore: inserisci un numero valido.")

menu()