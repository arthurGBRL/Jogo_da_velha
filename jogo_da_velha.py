import pygame
from pygame.locals import *
import os
caminho_atual = os.path.dirname(__file__) # localização deste arquivo
imagens = os.path.join(caminho_atual, "Imagens")
branco = (0,0,0)
altura = 600
largura = 800

class Quadro:
    def __init__(self,centro = (0,0)):
        self.centro = centro
    def __str__(self):
        return "{}".format(self.centro)
    largura = 266.66
    altura = 200
    __tipo = " "
    @property
    def estado(self):
        return self.__tipo

    def mudar_propriedade(self, nova_propriedade):
        self.__tipo = nova_propriedade

def background(x,y):
    gameDisplay.blit(backgroundImg, (x,y))

def botao(quadro, proximo_estado = " "):
    canto_esquerdo_x = quadro.centro[0] - quadro.largura/2
    canto_esquerdo_y = quadro.centro[1] - quadro.altura/2
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if canto_esquerdo_x + quadro.largura > mouse[0] > canto_esquerdo_x and canto_esquerdo_y + quadro.altura> mouse[1] > canto_esquerdo_y:
        if click[0] == 1 and quadro.estado == " " and proximo_estado == "x":
            quadro.mudar_propriedade("x")
        if click[0] == 1 and quadro.estado == " " and proximo_estado == "o":
            quadro.mudar_propriedade("o")

def cria_botoes(contador):
    for linha in range(len(quadros)):
        for quadro in range(len(quadros[linha])):
            botao(quadros[linha][quadro], "o" if contador%2 == 0 else "x") # Para mudar a ordem dos jogadores, é só inverter "o" e "x"

def checa_botoes(quadros):
    contador = 0
    for linha in quadros:
        for quadro in linha:
            if quadro.estado == " ":
                contador += 1
    return contador

def checador_horizontal(quadros):
    for i in range(len(quadros)):
        if quadros[i][0].estado == quadros[i][1].estado == quadros[i][2].estado:
            if quadros[i][0].estado != " ":
                return quadros[i][0].estado
    return " "

def checador_vertical(quadros):
    for i in range(len(quadros)):
        for j in range(len(quadros[i])):
            if i == 0:
                if quadros[i][j].estado == quadros[i+1][j].estado == quadros[i+2][j].estado:
                    if quadros[i][j].estado != " ":
                        print(quadros[i][j].estado)
                        return quadros[i][j].estado
    return " "

def checador_diagonal(quadros):
    if quadros[0][0].estado == quadros[1][1].estado == quadros[2][2].estado:
        if quadros[0][0].estado != " ":
            return quadros[0][0].estado
    if quadros[0][2].estado == quadros[1][1].estado == quadros[2][0].estado:
        if quadros[1][1].estado != " ":
            return quadros[1][1].estado
    return " "

def checador_ganhou(quadros):
    h = checador_horizontal(quadros)
    v = checador_vertical(quadros)
    d = checador_diagonal(quadros)
    if h != " ":
        return h
    if v != " ":
        return v
    if d != " ":
        return d
    return " "


posicoes = [
    [(133.33,100),(400.33,100),(666.99,100)],
    [(133.33,300),(400.33,300),(666.99,300)],
    [(133.33,500),(400.33,500),(666.99,500)]
]
quadros = [[Quadro(centro) for centro in linha] for linha in posicoes]
[[print(quadro) for quadro in linha] for linha in quadros]
x = 0
y = 0
pygame.init()
pygame.display.set_caption('Jogo da Velha')
backgroundImg = pygame.image.load(os.path.join(imagens, 'Base.png'))
XImg = pygame.image.load(os.path.join(imagens, 'Xis.png'))
OImg = pygame.image.load(os.path.join(imagens, 'Bola.png'))
gameDisplay = pygame.display.set_mode((largura,altura))
clock = pygame.time.Clock()
crashed = False


while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    
    background(x,y)
    cria_botoes(checa_botoes(quadros))
    for linha in quadros:
        for quadro in linha:
            if quadro.estado == "x":
                gameDisplay.blit(XImg, (int(quadro.centro[0] - quadro.largura/2),int(quadro.centro[1] - quadro.altura/2)))
            elif quadro.estado == "o":
                gameDisplay.blit(OImg, (int(quadro.centro[0] - quadro.largura/2),int(quadro.centro[1] - quadro.altura/2)))
    if checador_ganhou(quadros) != " ":
        print(checador_ganhou(quadros), "ganhou")
        
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()