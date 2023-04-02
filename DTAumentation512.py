# Processamento de Imagens com as Imagens de Treino e Teste - Sem aplicar Técnica de melhora da imagem
# Aplicado em imagens 512x512 e já classificadas pela Eloisa - 22-10-2022
import cv2
import os
from scipy import ndimage

def getIMG512Lagarta(input_dir, output_dir):
    caminhos = [os.path.join(input_dir, f) for f in os.listdir(input_dir)]
    
    id = 1 
    print('INICIO: LAGARTA - Processamento de Imagens Dimensao 512x512.\n')    
    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)
        
        imagemredimensionada = cv2.resize(imagem, tamanho512)
        imagem = imagemredimensionada
        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1
        
    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)
        
        imagemredimensionada = cv2.resize(imagem, tamanho512)
        imagem = ndimage.rotate(imagemredimensionada, 90)

        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)
        
        imagemredimensionada = cv2.resize(imagem, tamanho512)
        imagem = ndimage.rotate(imagemredimensionada, 180)

        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)
        
        imagemredimensionada = cv2.resize(imagem, tamanho512)
        imagem = ndimage.rotate(imagemredimensionada, 270)

        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)
        
        imagemredimensionada = cv2.resize(imagem, tamanho512)
        imagem = ndimage.rotate(imagemredimensionada, -90)

        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)
        
        imagemredimensionada = cv2.resize(imagem, tamanho512)
        imagem = ndimage.rotate(imagemredimensionada, -180)

        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)
        
        imagemredimensionada = cv2.resize(imagem, tamanho512)
        imagem = ndimage.rotate(imagemredimensionada, -270)

        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1

    print('TERMINO: LAGARTA - Processamento de Imagens Dimensao 512x512.\n\n')

def getIMG512Vaquinha(input_dir, output_dir):
    caminhos = [os.path.join(input_dir, f) for f in os.listdir(input_dir)]

    id = 1
    print('INICIO: VAQUINHA - Processamento de Imagens Dimensao 512x512.\n')    
    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)
        
        imagemredimensionada = cv2.resize(imagem, tamanho512)
        imagem = imagemredimensionada

        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)
        
        imagemredimensionada = cv2.resize(imagem, tamanho512)
        imagem = ndimage.rotate(imagemredimensionada, 90)

        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)
        
        imagemredimensionada = cv2.resize(imagem, tamanho512)
        imagem = ndimage.rotate(imagemredimensionada, 180)

        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)
        
        imagemredimensionada = cv2.resize(imagem, tamanho512)
        imagem = ndimage.rotate(imagemredimensionada, 270)

        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)
        
        imagemredimensionada = cv2.resize(imagem, tamanho512)
        imagem = ndimage.rotate(imagemredimensionada, -90)

        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)
        
        imagemredimensionada = cv2.resize(imagem, tamanho512)
        imagem = ndimage.rotate(imagemredimensionada, -180)

        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)
        
        imagemredimensionada = cv2.resize(imagem, tamanho512)
        imagem = ndimage.rotate(imagemredimensionada, -270)

        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1       

    print('TERMINO: VAQUINHA - Processamento de Imagens Dimensao 512x512.\n\n')   

def getIMG512Neutra(input_dir, output_dir):
    caminhos = [os.path.join(input_dir, f) for f in os.listdir(input_dir)]
    id = 1
    print('INICIO: NEUTRA - Processamento de Imagens Dimensao 512x512.\n')    
    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)
        
        imagemredimensionada = cv2.resize(imagem, tamanho512)
        imagem = imagemredimensionada

        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)
        
        imagemredimensionada = cv2.resize(imagem, tamanho512)
        imagem = ndimage.rotate(imagemredimensionada, 90)

        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)
        
        imagemredimensionada = cv2.resize(imagem, tamanho512)
        imagem = ndimage.rotate(imagemredimensionada, 180)

        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)
        
        imagemredimensionada = cv2.resize(imagem, tamanho512)
        imagem = ndimage.rotate(imagemredimensionada, 270)

        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)
        
        imagemredimensionada = cv2.resize(imagem, tamanho512)
        imagem = ndimage.rotate(imagemredimensionada, -90)

        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)
        
        imagemredimensionada = cv2.resize(imagem, tamanho512)
        imagem = ndimage.rotate(imagemredimensionada, -180)

        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)
        
        imagemredimensionada = cv2.resize(imagem, tamanho512)
        imagem = ndimage.rotate(imagemredimensionada, -270)

        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    print('TERMINO: NEUTRA - Processamento de Imagens Dimensao 512x512.\n\n')    


if __name__ == "__main__":
    tamanho512 = (512,512)

    # Teste
    diretorio_origem_lagarta_teste = '/home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas/ImgTeste/lagarta'
    diretorio_origem_neutra_teste = '/home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas/ImgTeste/saudaveis'
    diretorio_origem_vaquinha_teste = '//home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas/ImgTeste/vaquinha'

    diretorio_saida_512_teste = '/home/administrador/Documents/ProjetosPython/VersaoFinal/ImgAumentationClassificadas/Teste/'

    # Treino
    diretorio_origem_lagarta_treino = '/home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas/ImgTreino/lagarta'
    diretorio_origem_neutra_treino = '/home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas/ImgTreino/saudaveis'
    diretorio_origem_vaquinha_treino = '/home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas/ImgTreino/vaquinha'

    diretorio_saida_512_treino = '/home/administrador/Documents/ProjetosPython/VersaoFinal/ImgAumentationClassificadas/Treino/'
  
    # IMAGENS DE TESTE - ABAIXO REDIMENSIONAMENTO SEM TÉCNICA - 512 X 512
    # Processamento de Imagens com as Imagens de Treino - Sem Técnica de melhora da imagem
    getIMG512Lagarta(diretorio_origem_lagarta_treino, diretorio_saida_512_treino)
    getIMG512Vaquinha(diretorio_origem_neutra_treino, diretorio_saida_512_treino)
    getIMG512Neutra(diretorio_origem_vaquinha_treino, diretorio_saida_512_treino)

    # Processamento de Imagens com as Imagens de Teste - Sem Técnica de melhora da imagem
    getIMG512Lagarta(diretorio_origem_lagarta_teste, diretorio_saida_512_teste)
    getIMG512Vaquinha(diretorio_origem_neutra_teste, diretorio_saida_512_teste)
    getIMG512Neutra(diretorio_origem_vaquinha_teste, diretorio_saida_512_teste)
