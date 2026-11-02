# Array de dicionários contendo possíveis mensagens do usuário e respostas adequadas
dialogo = [ {"saudacao" : ["oi", "ola", "olá", "eae", "eai", "bom dia", "bomdia", "bom-dia", "boa tarde", "boatarde", "boa-tarde", "boa noite", "boanoite", "boa-noite"],
             "resposta" : "Olá! Sou a Paimon, sua companheira de viagem\nComo posso ajudar?"},
            
            {"despedida" : ["tchau"],
             "resposta" : "Até mais Viajante!"},
             
            {"elementos" : ["elementos", "elemento", "anemo", "geo", "electro", "dendro", "hydro", "pyro", "cryo"],
             "resposta" : "Oque exatamente você quer saber sobre esse elemento?"},
             
            {"armas" : ["armas", "arma", "espada", "espadão", "espadao", "catalisador", "lança", "arco"],
             "resposta" : "Oque você quer saber sobre essa arma?"},
             
            {"artefatos" : ["artefato", "artefatos", "flor", "flor da vida", "pena", "pluma", "pluma da morte", "relógio", "relógio", "ampulheta", "areia do tempo", "copo", "calice", "cálice", "cálice de erátema", "capacete", "coroa", "tiara", "tiara de logos"],
             "resposta" : "Oque você quer saber sobre artefatos?"}]

mensagemUsuario = str(input("Usuário: ")).strip().lower()

if any(saudacao in mensagemUsuario for saudacao in dialogo[0]["saudacao"]):
    print("INTENÇÃO: Saudação")
    print(dialogo[0]["resposta"])

elif any(despedida in mensagemUsuario for despedida in dialogo[1]["despedida"]):
    print("INTENÇÃO: Despedida")
    print(dialogo[1]["resposta"])

elif any(elementos in mensagemUsuario for elementos in dialogo[2]["elementos"]):
    print("INTENÇÃO: Elementos")
    print(dialogo[2]["resposta"])

elif any(armas in mensagemUsuario for armas in dialogo[3]["armas"]):
    print("INTENÇÃO: Armas")
    print(dialogo[3]["resposta"])

elif any(artefatos in mensagemUsuario for artefatos in dialogo[4]["artefatos"]):
    print("INTENÇÃO: Artefatos")
    print(dialogo[4]["resposta"])

else:
    print("Não entendi")