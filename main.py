import speech_recognition as sr
from datetime import datetime

# Inicializa o reconhecedor de fala
r = sr.Recognizer() 

# Usa o microfone como fonte de entrada
with sr.Microphone() as source:
    print("Ajustando o ruído ambiente... Aguarde.")
    r.adjust_for_ambient_noise(source)  # Ajusta o nível de ruído ambiente
    print("Pode falar agora...")
    
    # Captura o áudio do microfone
    audio = r.listen(source)

    try:
        # Usa o reconhecedor para converter fala em texto
        texto = r.recognize_google(audio, language='pt-BR')
        texto = texto.title()
        print(f"Você disse: {texto}")
        
        # Obtém a data e hora atual
        data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M")

        # Abre o arquivo no modo de adição e salva o texto com a data
        with open("fala_capturada.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{data_hora_atual} - {texto}\n\n ------------------------ || ----------------- \n\n")
        print("Texto salvo no arquivo com sucesso!")

    except sr.UnknownValueError:
        print("Não consegui entender o que você disse.")
    except sr.RequestError:
        print("Não consegui solicitar os resultados do serviço de reconhecimento de fala.")