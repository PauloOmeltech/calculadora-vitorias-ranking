# Determinar o nível baseado na quantidade de vitórias
def calcular_nivel(vitorias):
    
    if vitorias < 10:
        return "Ferro"
    elif vitorias <= 20:
        return "Bronze"
    elif vitorias <= 50:
        return "Prata"
    elif vitorias <= 80:
        return "Ouro"
    elif vitorias <= 90:
        return "Diamante"
    elif vitorias <= 100:
        return "Lendário"
    else:
        return "Imortal"

# Calcular o saldo e o nível do jogador
def calcular_saldo_rankeadas(vitorias, derrotas):
    saldo = vitorias - derrotas
    
# Determinação do nível baseado nas vitórias
    nivel = calcular_nivel(vitorias)
    return saldo, nivel

# Função principal para executar a calculadora
def main():
    print("=== CALCULADORA DE PARTIDAS RANQUEADAS ===\n")
    
# Entrada de dados com validação
    while True:
        try:
            vitorias = int(input("Digite a quantidade de vitórias: "))
            if vitorias < 0:
                print("Por favor, digite um número não negativo!")
                continue
            break
        except ValueError:
            print("Por favor, digite um número válido!")
    
    while True:
        try:
            derrotas = int(input("Digite a quantidade de derrotas: "))
            if derrotas < 0:
                print("Por favor, digite um número não negativo!")
                continue
            break
        except ValueError:
            print("Por favor, digite um número válido!")
    
# Chamada da função principal
    saldo, nivel = calcular_saldo_rankeadas(vitorias, derrotas)
    
# Mensagem de saída formatada
    print(f"\nO Herói tem de saldo de {saldo} está no nível de {nivel} do Ranking")
    
# Opção para repetir (laço de repetição)
    print("\n" + "="*40)
    while True:
        continuar = input("\nDeseja calcular novamente? (s/n): ").lower()
        if continuar in ['s', 'n', 'sim', 'não', 'nao']:
            if continuar in ['s', 'sim']:
                main()  # Recursão para repetir
                break
            else:
                print("\nObrigado por usar a Calculadora de Partidas Rankeadas!")
                break
        else:
            print("Opção inválida! Digite 's' para sim ou 'n' para não.")

# Execução do programa
if __name__ == "__main__":
    main()
    print("\n")
    