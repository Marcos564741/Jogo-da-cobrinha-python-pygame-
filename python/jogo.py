import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.display.set_caption("Jogo snake python")
relogio = pygame.time.Clock()

pontos = 0

velocidade = 10
x_controle = 0
y_controle = 0
largura = 640
altura = 480
x_cobra = largura/2
y_cobra = altura/2

x_maca = randint(40, 600)
y_maca = randint(50,  430)

fonte = pygame.font.SysFont("arial", 40, True, True)

tela = pygame.display.set_mode((largura, altura))

lista_cobra = []
comprimento_inicial = 5

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))

while True:
    relogio.tick(30)
    tela.fill((255,255,255))
    mensagem = f'Pontos:{pontos}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca, y_maca, 20, 20))
    if event.type == KEYDOWN:
            if event.key == K_LEFT and x_controle == 0:
                x_controle = -velocidade
                y_controle = 0
            elif event.key == K_RIGHT and x_controle == 0:
                x_controle = velocidade
                y_controle = 0
            elif event.key == K_UP and y_controle == 0:
                y_controle = -velocidade
                x_controle = 0
            elif event.key == K_DOWN and y_controle == 0:
                y_controle = velocidade
                x_controle = 0
    x_cobra += x_controle
    y_cobra += y_controle

    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50,  430)
        pontos += 1
        comprimento_inicial +=1
        

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    
    lista_cobra.append(lista_cabeca)

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (450, 40))
    pygame.display.update()