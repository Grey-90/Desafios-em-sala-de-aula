def calcular_velocidade_media():

    try:
        distancia = float(input("Digite a distância em Km: "))
        tempo = float(input("Digite o tempo em horas: "))

        if tempo <= 0:
            print("O tempo não pode ser zero ou negativo.")
            return
        
        velocidade_media = distancia / tempo
        print(f"A velocidade média é: {velocidade_media} km/h")

    except ValueError:
        print("Por favor, insira valores numéricos válidos para distância e tempo.")