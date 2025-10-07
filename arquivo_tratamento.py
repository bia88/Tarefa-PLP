# Programa de leitura e gravação de arquivos com tratamento de erros

try:
    # Solicita ao usuário o nome do arquivo de entrada
    input_file = input("Digite o nome do arquivo de entrada (ex: input.txt): ")
    output_file = "output.txt"

    # Lê o conteúdo do arquivo
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Processa o conteúdo
    word_count = len(text.split())      # Conta palavras
    upper_text = text.upper()           # Converte para maiúsculas

    # Grava o resultado em um novo arquivo
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(upper_text)
        f.write(f"\nNúmero total de palavras: {word_count}\n")

    print(f"Arquivo '{output_file}' criado com sucesso! ")

except FileNotFoundError:
    print(f"Erro: O arquivo '{input_file}' não foi encontrado. ")
except PermissionError:
    print(f"Erro: Sem permissão para ler o arquivo '{input_file}'. ")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e} ")
