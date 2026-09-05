# Hecho por MarBano

import pygame
import math
import random

pygame.init()

# -------------------------
# Configuración
# -------------------------
ANCHO = 1000
ALTO = 600

VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Copa Mundial 2026")

FPS = 60
clock = pygame.time.Clock()

# Colores
VERDE = (30, 150, 30)
BLANCO = (255,255,255)
ROJO = (220,50,50)
AZUL = (50,50,220)
NEGRO = (0,0,0)

# Marcador
goles_mexico = 0
goles_argentina = 0

# -------------------------
# Jugador
# -------------------------
class Jugador:

    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.radio = 20
        self.velocidad = 5
        self.color = color

    def mover(self,teclas):

        if teclas[pygame.K_w]:
            self.y -= self.velocidad

        if teclas[pygame.K_s]:
            self.y += self.velocidad

        if teclas[pygame.K_a]:
            self.x -= self.velocidad

        if teclas[pygame.K_d]:
            self.x += self.velocidad

        self.x = max(self.radio,min(ANCHO-self.radio,self.x))
        self.y = max(self.radio,min(ALTO-self.radio,self.y))

    def dibujar(self):
        pygame.draw.circle(VENTANA,self.color,(int(self.x),int(self.y)),self.radio)

# -------------------------
# IA
# -------------------------
class IA:

    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.radio = 20
        self.velocidad = 3
        self.color = color

    def mover(self,balon):

        if self.x < balon.x:
            self.x += self.velocidad
        elif self.x > balon.x:
            self.x -= self.velocidad

        if self.y < balon.y:
            self.y += self.velocidad
        elif self.y > balon.y:
            self.y -= self.velocidad

    def dibujar(self):
        pygame.draw.circle(VENTANA,self.color,(int(self.x),int(self.y)),self.radio)

# -------------------------
# Balón
# -------------------------
class Balon:

    def __init__(self):
        self.x = ANCHO//2
        self.y = ALTO//2
        self.radio = 12
        self.vx = 0
        self.vy = 0

    def actualizar(self):

        self.x += self.vx
        self.y += self.vy

        self.vx *= 0.98
        self.vy *= 0.98

        if self.y-self.radio <=0 or self.y+self.radio>=ALTO:
            self.vy *= -1

        if self.x-self.radio<=0:
            self.vx *= -1

        if self.x+self.radio>=ANCHO:
            self.vx *= -1

    def dibujar(self):
        pygame.draw.circle(VENTANA,BLANCO,(int(self.x),int(self.y)),self.radio)

# -------------------------
# Colisión
# -------------------------
def golpear(jugador,balon):

    dx = balon.x-jugador.x
    dy = balon.y-jugador.y

    distancia = math.sqrt(dx*dx+dy*dy)

    if distancia < jugador.radio+balon.radio:

        if distancia == 0:
            distancia = 1

        balon.vx = dx/distancia*8
        balon.vy = dy/distancia*8

# -------------------------
# Crear objetos
# -------------------------
mexico = Jugador(200,300,BLANCO)
argentina = IA(800,300,AZUL)
balon = Balon()

fuente = pygame.font.SysFont("Arial",30)

# -------------------------
# Juego
# -------------------------
while True:

    clock.tick(FPS)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    teclas = pygame.key.get_pressed()

    mexico.mover(teclas)
    argentina.mover(balon)

    golpear(mexico,balon)
    golpear(argentina,balon)

    balon.actualizar()

    # Goles
    if balon.x < 15 and 220 < balon.y < 380:

        goles_argentina += 1

        balon = Balon()

        mexico.x = 200
        mexico.y = 300

        argentina.x = 800
        argentina.y = 300

    if balon.x > ANCHO-15 and 220 < balon.y < 380:

        goles_mexico += 1

        balon = Balon()

        mexico.x = 200
        mexico.y = 300

        argentina.x = 800
        argentina.y = 300

    # Dibujar campo
    VENTANA.fill(VERDE)

    pygame.draw.rect(VENTANA,BLANCO,(0,220,10,160))
    pygame.draw.rect(VENTANA,BLANCO,(ANCHO-10,220,10,160))

    pygame.draw.line(VENTANA,BLANCO,(ANCHO//2,0),(ANCHO//2,ALTO),3)

    pygame.draw.circle(VENTANA,BLANCO,(ANCHO//2,ALTO//2),80,3)

    mexico.dibujar()
    argentina.dibujar()
    balon.dibujar()

    texto = fuente.render(f"México {goles_mexico} - {goles_argentina} Argentina",True,NEGRO)

    VENTANA.blit(texto,(280,20))

    pygame.display.update()