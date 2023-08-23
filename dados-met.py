def obter_temperatura_valida():
    while True:
        try:
            temperatura_str = input("Informe a temperatura (insira apenas números):").replace(",", ".")
            temperatura = float(temperatura_str)
            if -60 <= temperatura <= 50:
                return temperatura
            else:
                print("Temperatura fora do intervalo válido (-60°C a 50°C). Tente novamente.")
        except ValueError:
            print("Valor inválido! Tente novamente.")


def obter_mes_valido():
    while True:
        try:
            mes = int(input("Informe o número do mês (1 a 12): "))
            if 1 <= mes <= 12:
                return mes
            else:
                print("Mês fora do intervalo válido (1 a 12). Tente novamente.")
        except ValueError:
            print("Valor inválido. Tente novamente.")

def main():
    temperaturas_maximas = []
    meses_escaldantes = 0
    mes_escaldante = None
    mes_menos_quente = None

    for _ in range(12):
        mes = obter_mes_valido()
        temperatura = obter_temperatura_valida()
        temperaturas_maximas.append(temperatura)
        
        if temperatura > 38:
            meses_escaldantes += 1
            if mes_escaldante is None:
                mes_escaldante = mes

        if mes_menos_quente is None or temperatura < temperaturas_maximas[mes_menos_quente - 1]:
            mes_menos_quente = mes

    media_anual = sum(temperaturas_maximas) / len(temperaturas_maximas)
    
    nomes_meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    
    print(f"Temperatura média máxima anual: {media_anual:.2f}°C")
    print(f"Quantidade de meses escaldantes: {meses_escaldantes}")
    
    if mes_escaldante:
        print(f"Mês mais escaldante do ano: {nomes_meses[mes_escaldante - 1]}")
    
    if mes_menos_quente:
        print(f"Mês menos quente do ano: {nomes_meses[mes_menos_quente - 1]}")

if __name__ == "__main__":
    main()

