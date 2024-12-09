def separa_colonne_da_file(file_path):

    lista_colonna1 = []
    lista_colonna2 = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                valori = line.strip().split()
                if len(valori) == 2:  
                    col1, col2 = map(int, valori)  
                    lista_colonna1.append(col1)
                    lista_colonna2.append(col2)
                else:
                    print(f"Riga ignorata: {line.strip()}") 

        return lista_colonna1, lista_colonna2
    except FileNotFoundError:
        print(f"Errore: Il file {file_path} non è stato trovato.")
        return [], []
    except ValueError as e:
        print(f"Errore nel convertire i valori in interi: {e}")
        return [], []


def calcla_minimo(col1[], col2[])