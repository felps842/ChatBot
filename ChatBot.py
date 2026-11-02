# Array de dicionários contendo possíveis mensagens do usuário e respostas adequadas
dialogo = [ {"saudacao" : ["oi", "ola", "olá", "eae", "eai", "bom dia", "bomdia", "bom-dia", "boa tarde", "boatarde", "boa-tarde", "boa noite", "boanoite", "boa-noite"],
             "resposta" : "Olá! Sou a Paimon, sua companheira de viagem\nComo posso ajudar?"},
            
            {"despedia" : ["tchau"],
             "resposta" : "Até mais Viajante!"}]

mensagemUsuario = str(input("Usuário: ")).strip().lower()

if any(saudacao in mensagemUsuario for saudacao in dialogo[0]["saudacao"]):
    print(dialogo[0]["resposta"])

elif any(despedida in mensagemUsuario for despedida in dialogo[1]["despedida"]):
    print(dialogo[1]["resposta"])

else:
    print("Não entendi")