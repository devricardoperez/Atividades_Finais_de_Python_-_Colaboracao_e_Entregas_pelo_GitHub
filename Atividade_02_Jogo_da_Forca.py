import random

def escolher_palavra():
    palavras = ['desenvolvimento', 'tecnologia', 'lógica', 'programação', 'tendências', 'blockchain', 'cibersegurança', 'robótica', 'automação', 'software' 'hardware']
    return random.choice(palavras)

def exibir_forca(tentativas):
    etapas = ['''
   +---+
   |   |
       |
       |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
       |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
   |   |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\\  |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
=========''']
    print(etapas[6-tentativas])

def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ['_' for _ in palavra]
    tentativas = 0
    tentadas = []

    print("Bienvenido al juego del ahorcado!")
    print("Tienes 6 intentos para adivinar la palabra.")
    exibir_forca(tentativas)
    print(" ".join(palavra_oculta))

    while tentativas < 6:
        letra = input("\nPor favor, introduce una letra: ").lower()
        if letra in tentadas:
            print("Ya has intentado esa letra. Por favor, intenta con otra.")
            continue
        elif letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
            print(" ".join(palavra_oculta))
        else:
            tentativas += 1
            exibir_forca(tentativas)

        tentadas.append(letra)

        if "_" not in palavra_oculta:
            print("¡Felicidades! Has adivinado la palabra.")
            return
        elif tentativas >= 6:
            print("Lo siento, has perdido. La palabra era " + palavra + ".")
            return
jogar()

print("¡Gracias por jugar!")