import socket

def handle_client(client_socket):   #Funktion zur Kommunikation mit thunkable, 
                            #empfänt rollenauswahl für fahrer/nichtfahrer
    try: 
        #Rollenauswahl Empfang
        role_selection = client_socket.recv(1024).decode('utf-8')
        print(f"Rollenauswahl erhalten: {role_selection}")
        
        #Verarbeitung Rollenauswahl
        if role_selection == "Fahrer":
            print("Du hast die Rolle Fahrer ausgewählt.")
        #print("Bitte nenne deine verfügbaren Fahrplätze:")
        #verfügbare_fahrplätze = int(input("Bitte nenne deine verfügbaren Fahrplätze:"))
        #print(f"Du hast {verfügbare_fahrplätze}.")
        #
        elif role_selection == "Nichtfahrer":
            print("Du hast die Rolle Nichtfahrer ausgewählt.")
        elif role_selection == "Beides":
            print("Du hast die Rolle Beides ausgewählt.")
        #print("Bitte nenne deine verfügbaren Fahrplätze:")
        #verfügbare_fahrplätze = int(input("Bitte nenne deine verfügbaren Fahrplätze:"))
        #print(f"Du hast {verfügbare_fahrplätze}.")
        
        #Antwort Rückversendung
        client_socket.send(response.encode('utf-8'))
        
    except Exception as e: 
        print(f"Fehler: {e}")
    finally: 
        client_socket.close()