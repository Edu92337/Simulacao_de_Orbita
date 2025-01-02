import pygame 
import math
import numpy as np
from collections import deque


simulacao_ativa = True
pygame.init()
screen = pygame.display.set_mode((1200, 650))
clock = pygame.time.Clock()
running = True
dt = 1/60

G = 600
M = 1000
m = 40


estrela = pygame.Vector2(screen.get_width()/2,screen.get_height()/2)
corpo = pygame.Vector2(np.random.randint(screen.get_width() // 3, 2 * screen.get_width() // 3),np.random.randint(screen.get_height() // 3, 2 * screen.get_height() // 3))
r = math.dist(corpo,estrela)
versor_r = (estrela - corpo).normalize()
v = versor_r.rotate(90).normalize() * math.sqrt(G * M / r)
trajetoria = deque()
corpo_anterior = corpo - v * dt
estrela_anterior = estrela
v_estrela = pygame.Vector2(0,0)


def calcula_forca(pos1, pos2,massa):
    r = math.dist(pos1, pos2)
    if r != 0:
        versor_r = (pos2 - pos1).normalize()
        forca = G * M * m / (r**2)
        return versor_r * (forca / massa)
    return pygame.Vector2(0, 0)

#MÉTODO DE VERLET
def atualizaMovimento(astro, astro_anterior, a, dt=dt):
    nova_posicao = 2 * astro - astro_anterior + a * (dt ** 2)
    astro_anterior = astro.copy() 
    astro = nova_posicao
    return astro, astro_anterior
    
def verificaColisao(astro,screen,raio):
    if astro.x - raio < 0 or astro.x + raio > screen.get_width() or astro.y - raio < 0 or  astro.y + raio > screen.get_height():
        return False
    return True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")

    if simulacao_ativa:
        raio_corpo = 5
        r = math.dist(corpo,estrela)
        versor_r = (estrela - corpo).normalize()
        a = calcula_forca(corpo,estrela,m)
        a_estrela = calcula_forca(corpo,estrela,M)
        corpo, corpo_anterior = atualizaMovimento(corpo, corpo_anterior, a, dt)
        estrela,estrela_anterior = atualizaMovimento(estrela, estrela_anterior, a_estrela, dt)

        trajetoria.append(corpo.xy[:])
        
        if len(trajetoria) > 1:
            pygame.draw.lines(screen, "white", False, trajetoria, 2)
        
        pygame.draw.circle(screen, "orange", estrela, raio_corpo)
        pygame.draw.circle(screen,'white',corpo,raio_corpo)
        simulacao_ativa = verificaColisao(corpo,screen,raio_corpo)

        pygame.display.flip()
        dt = clock.tick(60)/1000
        
pygame.quit()