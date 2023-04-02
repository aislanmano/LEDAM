# Processamento de Imagens com as Imagens de Treino e Teste - Normalização de Cores Sem aplicar Técnica de melhora da imagem
# Aplicado em imagens 256x256 e já classificadas pela Eloisa - 06-11-2022
import cv2
import os
import numpy as np
from scipy import ndimage

def getIMG256Lagarta(input_dir, output_dir):
    caminhos = [os.path.join(input_dir, f) for f in os.listdir(input_dir)]
    
    id = 1 
    print('INICIO: LAGARTA - Processamento de Imagens Dimensao 256x256.\n')    
    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256)
        imagemresultadonc = np.zeros((tamanho256))
        imagem = cv2.normalize(imagemredimensionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1
        
    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, 90)
        imagemresultadonc = np.zeros((tamanho256))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, 180)
        imagemresultadonc = np.zeros((tamanho256))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, 270)
        imagemresultadonc = np.zeros((tamanho256))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, -90)
        imagemresultadonc = np.zeros((tamanho256))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, -180)
        imagemresultadonc = np.zeros((tamanho256))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, -270)
        imagemresultadonc = np.zeros((tamanho256))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1

    print('TERMINO: LAGARTA - Processamento de Imagens Dimensao 256x256.\n\n')

def getIMG256Vaquinha(input_dir, output_dir):
    caminhos = [os.path.join(input_dir, f) for f in os.listdir(input_dir)]

    id = 1
    print('INICIO: VAQUINHA - Processamento de Imagens Dimensao 256x256.\n')    
    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256)
        imagemresultadonc = np.zeros((tamanho256))
        imagem = cv2.normalize(imagemredimensionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, 90)
        imagemresultadonc = np.zeros((tamanho256))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, 180)
        imagemresultadonc = np.zeros((tamanho256))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)  

        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, 270)
        imagemresultadonc = np.zeros((tamanho256))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)  

        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, -90)
        imagemresultadonc = np.zeros((tamanho256))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)  

        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, -180)
        imagemresultadonc = np.zeros((tamanho256))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)          

        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, -270)
        imagemresultadonc = np.zeros((tamanho256))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)  

        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1       

    print('TERMINO: VAQUINHA - Processamento de Imagens Dimensao 256x256.\n\n')   

def getIMG256Neutra(input_dir, output_dir):
    caminhos = [os.path.join(input_dir, f) for f in os.listdir(input_dir)]
    id = 1
    print('INICIO: NEUTRA - Processamento de Imagens Dimensao 256x256.\n')    
    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256)
        imagemresultadonc = np.zeros((tamanho256))
        imagem = cv2.normalize(imagemredimensionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256)
        imagemrotacionada = ndimage.rotate(imagemredimensionada,90)
        imagemresultadonc = np.zeros((tamanho256))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, 180)
        imagemresultadonc = np.zeros((tamanho256))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, 270)
        imagemresultadonc = np.zeros((tamanho256))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, -90)
        imagemresultadonc = np.zeros((tamanho256))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, -180)
        imagemresultadonc = np.zeros((tamanho256))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho256)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, -270)
        imagemresultadonc = np.zeros((tamanho256))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    print('TERMINO: NEUTRA - Processamento de Imagens Dimensao 256x256.\n\n')    


if __name__ == "__main__":
    tamanho256 = (256,256)

    # Teste
    diretorio_origem_lagarta_teste = '/home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas256/ImgTeste/lagarta'
    diretorio_origem_neutra_teste = '/home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas256/ImgTeste/saudaveis'
    diretorio_origem_vaquinha_teste = '//home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas256/ImgTeste/vaquinha'

    diretorio_saida_256_teste = '/home/administrador/Documents/ProjetosPython/VersaoFinal/ImgAumentationClassificadas256/NormalizeSemTecnica/Teste/'

    # Treino
    diretorio_origem_lagarta_treino = '/home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas256/ImgTreino/lagarta'
    diretorio_origem_neutra_treino = '/home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas256/ImgTreino/saudaveis'
    diretorio_origem_vaquinha_treino = '/home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas256/ImgTreino/vaquinha'

    diretorio_saida_256_treino = '/home/administrador/Documents/ProjetosPython/VersaoFinal/ImgAumentationClassificadas256/NormalizeSemTecnica/Treino/'
  
    # IMAGENS DE TESTE - ABAIXO REDIMENSIONAMENTO SEM TÉCNICA - 256 X 256
    # Processamento de Imagens com as Imagens de Treino - Sem Técnica de melhora da imagem
    getIMG256Lagarta(diretorio_origem_lagarta_treino, diretorio_saida_256_treino)
    getIMG256Vaquinha(diretorio_origem_neutra_treino, diretorio_saida_256_treino)
    getIMG256Neutra(diretorio_origem_vaquinha_treino, diretorio_saida_256_treino)

    # Processamento de Imagens com as Imagens de Teste - Sem Técnica de melhora da imagem
    getIMG256Lagarta(diretorio_origem_lagarta_teste, diretorio_saida_256_teste)
    getIMG256Vaquinha(diretorio_origem_neutra_teste, diretorio_saida_256_teste)
    getIMG256Neutra(diretorio_origem_vaquinha_teste, diretorio_saida_256_teste)
