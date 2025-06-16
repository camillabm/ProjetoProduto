from PIL import Image
import os

# Definindo as classes e a ordem de sobreposição (fundo para o topo)
ordem_classes = ['C', 'B', 'A', 'D']  # C é o fundo, D é o topo

# Gerar todas as combinações possíveis de opções (1, 2, 3) para cada classe
for a in range(1, 4):
    for b in range(1, 4):
        for c in range(1, 4):
            for d in range(1, 4):
                # Criar um dicionário com as opções para cada classe
                opcoes = {
                    'A': a,
                    'B': b,
                    'C': c,
                    'D': d
                }
                
                # Iniciar com uma imagem transparente
                # Assumindo que todas as imagens têm o mesmo tamanho
                # Pegamos o tamanho da primeira imagem encontrada
                primeira_imagem = None
                for classe in ordem_classes:
                    img_path = f"{classe}_{opcoes[classe]}.png"
                    if os.path.exists(img_path):
                        primeira_imagem = Image.open(img_path)
                        break
                
                if primeira_imagem is None:
                    print("Nenhuma imagem encontrada. Verifique os arquivos.")
                    exit()
                
                imagem_combinada = Image.new("RGBA", primeira_imagem.size)
                
                # Combinar as imagens na ordem especificada
                for classe in ordem_classes:
                    img_path = f"{classe}_{opcoes[classe]}.png"
                    try:
                        img = Image.open(img_path)
                        imagem_combinada = Image.alpha_composite(imagem_combinada, img)
                    except FileNotFoundError:
                        print(f"Arquivo não encontrado: {img_path}")
                        continue
                
                # Salvar a imagem combinada
                nome_arquivo = f"jogador_{a}_{b}_{c}_{d}.png"
                imagem_combinada.save(nome_arquivo)
                print(f"Imagem salva: {nome_arquivo}")

print("Todas as combinações foram processadas!")