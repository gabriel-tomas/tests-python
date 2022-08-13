import math

import pygame
from math import sqrt
pygame.init()

tela = pygame.display.set_mode((1280, 720))

jogador = pygame.image.load('mario.png')
pox = 70
poy = 123
pos_x_escolha = 0
pos_y_escolha = 0

inimigo_do_mal = pygame.image.load('mal.png')
pox_enemy = 800
poy_enemy = 123
po_aleatorio = 1

bala = pygame.image.load('bullet.png')
poy_bullet = 123
pox_bullet = 70
pos_xbullet = 10
pos_ybullet = 0
estado = 'preparado'

def atirar(x, y):
    global estado
    estado = 'atirar'
    tela.blit(bala, (x, y))


back = pygame.image.load('back3.jpg')
movement = 0
def player(x, y):
    tela.blit(jogador, (x, y))

def inimigo(x, y):
    tela.blit(inimigo_do_mal, (x, y))
def colisao(pox_enemy, poy_enemy, pox_bullet, poy_bullet):
    distance = sqrt((math.pow(pox_enemy - pox_bullet, 2)) + (math.pow(poy_enemy - poy_bullet, 2)))
    if distance <= 80:
        return True
    else:
        return False

rodando = True
pontos = 0
while rodando:
    tela.blit(back, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                pos_x_escolha = 4
            if event.key == pygame.K_a:
                pos_x_escolha = -4
            if event.key == pygame.K_w:
                pos_y_escolha = -4
            if event.key == pygame.K_s:
                pos_y_escolha = 4
            if event.key == pygame.K_SPACE:
                atirar(0, 0)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                pos_x_escolha = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                pos_y_escolha = 0
    pox += pos_x_escolha
    poy += pos_y_escolha
    if pox <= -59:
        pox = -30
    if pox >= 1060:
        pox = 1030
    if poy <= -10:
        poy = 0
    if poy >= 550:
        poy = 550
    player(pox, poy)
    inimigo(pox_enemy, poy_enemy)
    poy_enemy += po_aleatorio
    colissao = colisao(pox_enemy, poy_enemy, pox_bullet, poy_bullet)
    if colissao:
        pox_bullet = 0
        estado = 'preparado'
        pontos += 1
        print(pontos)

    if poy_enemy <= -10:
        po_aleatorio = 1
    if poy_enemy >= 260:
        po_aleatorio = -1
    if estado == 'atirar':
        atirar(pox_bullet, poy)
        pox_bullet += pos_xbullet
    if pox_bullet >= 1280:
        pox_bullet = 0
        estado = 'preparado'
    pygame.display.update()
