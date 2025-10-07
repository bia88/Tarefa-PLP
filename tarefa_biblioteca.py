import os
import requests
from urllib.parse import urlparse
from pathlib import Path
from hashlib import md5

def baixar_imagem(url, save_dir="Fetched_Images"):
    """
    Baixa uma imagem do URL e salva no diretório especificado.
    Evita duplicatas usando hash do conteúdo.
    """
    try:
        # Cria diretório se não existir
        os.makedirs(save_dir, exist_ok=True)

        # Faz a requisição HTTP com timeout e cabeçalhos básicos
        headers = {"User-Agent": "UbuntuImageFetcher/1.0 (+https://example.com)"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Lança erro se HTTP inválido

        # Gera hash do conteúdo para evitar duplicatas
        file_hash = md5(response.content).hexdigest()

        # Extrai nome do arquivo da URL ou cria nome baseado no hash
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename or '.' not in filename:
            filename = f"image_{file_hash[:8]}.jpg"

        filepath = Path(save_dir) / filename

        # Se arquivo já existe com mesmo hash, pula
        if filepath.exists():
            print(f"✗ Imagem duplicada detectada, pulando: {filename}")
            return

        # Salva a imagem em binário
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Obtido com sucesso: {filename}")
        print(f"✓ Imagem salva em {filepath}")
    
    except requests.exceptions.MissingSchema:
        print(f"✗ URL inválida: {url}")
    except requests.exceptions.HTTPError as e:
        print(f"✗ Erro HTTP {e.response.status_code} ao acessar {url}")
    except requests.exceptions.RequestException as e:
        print(f"✗ Erro de conexão: {e}")
    except Exception as e:
        print(f"✗ Erro inesperado: {e}")

def main():
    print("Bem-vindo ao Ubuntu Image Fetcher")
    print("Uma ferramenta para coletar imagens da web de forma consciente\n")

   
    urls_input = input("Digite URLs das imagens (separadas por vírgula): ")
    urls = [u.strip() for u in urls_input.split(",") if u.strip()]

    if not urls:
        print("Nenhum URL fornecido. Encerrando.")
        return

    for url in urls:
        baixar_imagem(url)

    print("\nConexão fortalecida. Comunidade enriquecida. 🌍")

if __name__ == "__main__":
    main()
