# Nomes dos arquivos
input_file = "input.txt"
output_file = "output.txt"

try:
   
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

  
    word_count = len(text.split())

   
    upper_text = text.upper()

    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(upper_text)
        f.write(f"\nNúmero total de palavras: {word_count}\n")

    
    print(f"Arquivo '{output_file}' criado com sucesso!")

except FileNotFoundError:
    print(f"Erro: O arquivo '{input_file}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
