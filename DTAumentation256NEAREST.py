# Processamento de Imagens com as Imagens de Treino e Teste - Aplicando a Técnica de melhora da imagem INTER_NEAREST
# Aplicado em imagens 256x256 e já classificadas pela Eloisa - 07-11-2022
import cv2
import os
from scipy import ndimage

def getIMG256Lagarta(input_dir, output_dir):
    caminhos = [os.path.join(input_dir, f) for f in os.listdir(input_dir)]
    
    id = 1 
    print('INICIO: LAGARTA - Processamento de Imagens Dimensao 256x256.\n')    
    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256, interpolation = cv2.INTER_NEAREST)
        imagem = imagemredimensionada
        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1
        
    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256, interpolation = cv2.INTER_NEAREST)
        imagem = ndimage.rotate(imagemredimensionada, 90)
        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256, interpolation = cv2.INTER_NEAREST)
        imagem = ndimage.rotate(imagemredimensionada, 180)
        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256, interpolation = cv2.INTER_NEAREST)
        imagem = ndimage.rotate(imagemredimensionada, 270)
        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256, interpolation = cv2.INTER_NEAREST)
        imagem = ndimage.rotate(imagemredimensionada, -90)
        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256, interpolation = cv2.INTER_NEAREST)
        imagem = ndimage.rotate(imagemredimensionada, -180)
        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256, interpolation = cv2.INTER_NEAREST)
        imagem = ndimage.rotate(imagemredimensionada, -270)
        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1
    print('TERMINO: LAGARTA - Processamento de Imagens Dimensao 256x256.\n\n')

def getIMG256Vaquinha(input_dir, output_dir):
    caminhos = [os.path.join(input_dir, f) for f in os.listdir(input_dir)]

    id = 1
    print('INICIO: VAQUINHA - Processamento de Imagens Dimensao 256x256.\n')    
    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256, interpolation = cv2.INTER_NEAREST)
        imagem = imagemredimensionada
        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256, interpolation = cv2.INTER_NEAREST)
        imagem = ndimage.rotate(imagemredimensionada, 90)
        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256, interpolation = cv2.INTER_NEAREST)
        imagem = ndimage.rotate(imagemredimensionada, 180)
        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256, interpolation = cv2.INTER_NEAREST)
        imagem = ndimage.rotate(imagemredimensionada, 270)
        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256, interpolation = cv2.INTER_NEAREST)
        imagem = ndimage.rotate(imagemredimensionada, -90)
        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256, interpolation = cv2.INTER_NEAREST)
        imagem = ndimage.rotate(imagemredimensionada, -180)
        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256, interpolation = cv2.INTER_NEAREST)
        imagem = ndimage.rotate(imagemredimensionada, -270)
        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1
    print('TERMINO: VAQUINHA - Processamento de Imagens Dimensao 256x256.\n\n')   

def getIMG256Neutra(input_dir, output_dir):
    caminhos = [os.path.join(input_dir, f) for f in os.listdir(input_dir)]
    id = 1
    print('INICIO: NEUTRA - Processamento de Imagens Dimensao 256x256.\n')    
    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256, interpolation = cv2.INTER_NEAREST)
        imagem = imagemredimensionada
        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256, interpolation = cv2.INTER_NEAREST)
        imagem = ndimage.rotate(imagemredimensionada, 90)
        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256, interpolation = cv2.INTER_NEAREST)
        imagem = ndimage.rotate(imagemredimensionada, 180)
        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256, interpolation = cv2.INTER_NEAREST)
        imagem = ndimage.rotate(imagemredimensionada, 270)
        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256, interpolation = cv2.INTER_NEAREST)
        imagem = ndimage.rotate(imagemredimensionada, -90)
        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256, interpolation = cv2.INTER_NEAREST)
        imagem = ndimage.rotate(imagemredimensionada, -180)
        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256, interpolation = cv2.INTER_NEAREST)
        imagem = ndimage.rotate(imagemredimensionada, -270)
        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1
    print('TERMINO: NEUTRA - Processamento de Imagens Dimensao 256x256.\n\n')    


if __name__ == "__main__":
    tamanho256 = (256,256)

    # Teste
    diretorio_origem_lagarta_teste = '/home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas256/ImgTeste/lagarta'
    diretorio_origem_neutra_teste = '/home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas256/ImgTeste/saudaveis'
    diretorio_origem_vaquinha_teste = '//home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas256/ImgTeste/vaquinha'

    diretorio_saida_256_teste = '/home/administrador/Documents/ProjetosPython/VersaoFinal/Teste/256INTER_NEAREST/'

    # Treino
    diretorio_origem_lagarta_treino = '/home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas256/ImgTreino/lagarta'
    diretorio_origem_neutra_treino = '/home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas256/ImgTreino/saudaveis'
    diretorio_origem_vaquinha_treino = '/home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas256/ImgTreino/vaquinha'

    diretorio_saida_256_treino = '/home/administrador/Documents/ProjetosPython/VersaoFinal/Treino/256INTER_NEAREST/'
  
    # IMAGENS DE TESTE - ABAIXO REDIMENSIONAMENTO SEM TÉCNICA - 256 X 256
    # Processamento de Imagens com as Imagens de Treino - Aplicando Técnica de melhora da imagem INTER_NEAREST
    getIMG256Lagarta(diretorio_origem_lagarta_treino, diretorio_saida_256_treino)
    getIMG256Vaquinha(diretorio_origem_neutra_treino, diretorio_saida_256_treino)
    getIMG256Neutra(diretorio_origem_vaquinha_treino, diretorio_saida_256_treino)

    # Processamento de Imagens com as Imagens de Teste - Aplicando Técnica de melhora da imagem INTER_NEAREST
    getIMG256Lagarta(diretorio_origem_lagarta_teste, diretorio_saida_256_teste)
    getIMG256Vaquinha(diretorio_origem_neutra_teste, diretorio_saida_256_teste)
    getIMG256Neutra(diretorio_origem_vaquinha_teste, diretorio_saida_256_teste)
