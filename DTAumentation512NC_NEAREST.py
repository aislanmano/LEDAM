# Processamento de Imagens com as Imagens de Treino e Teste - Normalizaço de Cores Aplicando a Técnica de melhora da imagem INTER_NEAREST
# Aplicado em imagens 512x512 e já classificadas pela Eloisa - 06-11-2022
import cv2
import os
import numpy as np
from scipy import ndimage

def getIMG512Lagarta(input_dir, output_dir):
    caminhos = [os.path.join(input_dir, f) for f in os.listdir(input_dir)]
    
    id = 1 
    print('INICIO: LAGARTA - Processamento de Imagens Dimensao 512x512.\n')    
    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho512, interpolation = cv2.INTER_NEAREST)
        imagemresultadonc = np.zeros((tamanho512))
        imagem = cv2.normalize(imagemredimensionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1
        
    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho512, interpolation = cv2.INTER_NEAREST)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, 90)
        imagemresultadonc = np.zeros((tamanho512))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho512, interpolation = cv2.INTER_NEAREST)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, 180)
        imagemresultadonc = np.zeros((tamanho512))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho512, interpolation = cv2.INTER_NEAREST)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, 270)
        imagemresultadonc = np.zeros((tamanho512))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho512, interpolation = cv2.INTER_NEAREST)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, -90)
        imagemresultadonc = np.zeros((tamanho512))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho512, interpolation = cv2.INTER_NEAREST)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, -180)
        imagemresultadonc = np.zeros((tamanho512))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho512, interpolation = cv2.INTER_NEAREST)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, -270)
        imagemresultadonc = np.zeros((tamanho512))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGLagarta_" + str(id) + ".jpg", imagem)
        id = id + 1
    print('TERMINO: LAGARTA - Processamento de Imagens Dimensao 512x512.\n\n')

def getIMG512Vaquinha(input_dir, output_dir):
    caminhos = [os.path.join(input_dir, f) for f in os.listdir(input_dir)]

    id = 1
    print('INICIO: VAQUINHA - Processamento de Imagens Dimensao 512x512.\n')    
    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho512, interpolation = cv2.INTER_NEAREST)
        imagemresultadonc = np.zeros((tamanho512))
        imagem = cv2.normalize(imagemredimensionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho512, interpolation = cv2.INTER_NEAREST)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, 90)
        imagemresultadonc = np.zeros((tamanho512))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho512, interpolation = cv2.INTER_NEAREST)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, 180)
        imagemresultadonc = np.zeros((tamanho512))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho512, interpolation = cv2.INTER_NEAREST)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, 270)
        imagemresultadonc = np.zeros((tamanho512))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho512, interpolation = cv2.INTER_NEAREST)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, -90)
        imagemresultadonc = np.zeros((tamanho512))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho512, interpolation = cv2.INTER_NEAREST)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, -180)
        imagemresultadonc = np.zeros((tamanho512))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho512, interpolation = cv2.INTER_NEAREST)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, -270)
        imagemresultadonc = np.zeros((tamanho512))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGVaquinha_" + str(id) + ".jpg", imagem)
        id = id + 1
    print('TERMINO: VAQUINHA - Processamento de Imagens Dimensao 512x512.\n\n')   

def getIMG512Neutra(input_dir, output_dir):
    caminhos = [os.path.join(input_dir, f) for f in os.listdir(input_dir)]
    id = 1
    print('INICIO: NEUTRA - Processamento de Imagens Dimensao 512x512.\n')    
    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho512, interpolation = cv2.INTER_NEAREST)
        imagemresultadonc = np.zeros((tamanho512))
        imagem = cv2.normalize(imagemredimensionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho512, interpolation = cv2.INTER_NEAREST)
        imagemrotacionada = ndimage.rotate(imagemredimensionada,90)
        imagemresultadonc = np.zeros((tamanho512))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho512, interpolation = cv2.INTER_NEAREST)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, 180)
        imagemresultadonc = np.zeros((tamanho512))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho512, interpolation = cv2.INTER_NEAREST)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, 270)
        imagemresultadonc = np.zeros((tamanho512))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho512, interpolation = cv2.INTER_NEAREST)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, -90)
        imagemresultadonc = np.zeros((tamanho512))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho512, interpolation = cv2.INTER_NEAREST)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, -180)
        imagemresultadonc = np.zeros((tamanho512))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1

    for CaminhoImagem in caminhos:
        imagem = cv2.imread(CaminhoImagem)        
        imagemredimensionada = cv2.resize(imagem, tamanho512, interpolation = cv2.INTER_NEAREST)
        imagemrotacionada = ndimage.rotate(imagemredimensionada, -270)
        imagemresultadonc = np.zeros((tamanho512))
        imagem = cv2.normalize(imagemrotacionada, imagemresultadonc, 0, 100, cv2.NORM_MINMAX)
        cv2.imwrite(output_dir + "IMGNeutra_" + str(id) + ".jpg", imagem)
        id = id + 1
    print('TERMINO: NEUTRA - Processamento de Imagens Dimensao 512x512.\n\n')    


if __name__ == "__main__":
    tamanho512 = (512,512)

    # Teste
    diretorio_origem_lagarta_teste = '/home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas512/ImgTeste/lagarta'
    diretorio_origem_neutra_teste = '/home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas512/ImgTeste/saudaveis'
    diretorio_origem_vaquinha_teste = '//home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas512/ImgTeste/vaquinha'

    diretorio_saida_512_teste = '/home/administrador/Documents/ProjetosPython/VersaoFinal/ImgAumentationClassificadas512/NormalizeComTecnica/INTER_NEAREST_Teste/'

    # Treino
    diretorio_origem_lagarta_treino = '/home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas512/ImgTreino/lagarta'
    diretorio_origem_neutra_treino = '/home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas512/ImgTreino/saudaveis'
    diretorio_origem_vaquinha_treino = '/home/administrador/Documents/ProjetosPython/Imagens/ImgClassificadas512/ImgTreino/vaquinha'

    diretorio_saida_512_treino = '/home/administrador/Documents/ProjetosPython/VersaoFinal/ImgAumentationClassificadas512/NormalizeComTecnica/INTER_NEAREST_Treino/'
  
    # IMAGENS DE TESTE - ABAIXO REDIMENSIONAMENTO SEM TÉCNICA - 512 X 512
    # Processamento de Imagens com as Imagens de Treino - Sem Técnica de melhora da imagem
    getIMG512Lagarta(diretorio_origem_lagarta_treino, diretorio_saida_512_treino)
    getIMG512Vaquinha(diretorio_origem_neutra_treino, diretorio_saida_512_treino)
    getIMG512Neutra(diretorio_origem_vaquinha_treino, diretorio_saida_512_treino)

    # Processamento de Imagens com as Imagens de Teste - Sem Técnica de melhora da imagem
    getIMG512Lagarta(diretorio_origem_lagarta_teste, diretorio_saida_512_teste)
    getIMG512Vaquinha(diretorio_origem_neutra_teste, diretorio_saida_512_teste)
    getIMG512Neutra(diretorio_origem_vaquinha_teste, diretorio_saida_512_teste)
