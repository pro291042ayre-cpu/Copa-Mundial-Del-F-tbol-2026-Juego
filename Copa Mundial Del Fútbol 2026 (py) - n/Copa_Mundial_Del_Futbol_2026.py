# Hecho por MarBano

import pygame, sys
from pygame.locals import *

# Pantalla del displaysurf
FPS = 30
DISPLAYSURFX = 900
DISPLAYSURFY = 700

MITADDISPLAYSURFX = int(DISPLAYSURFX / 2)
MITADDISPLAYSURFY = int(DISPLAYSURFY / 2)

# Poner colores
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255,  0,  0)
DARKRED = (195, 33, 72)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Verde de México (más oscuro)
GREEN_MEXICO = (0, 104, 71)

# Azul de Brasil
BLUE_BRAZIL = (0, 39, 118)

# Tamano de los bloques
BLOQUETAMANOX = 50
BLOQUETAMANOY = 50

MITADBLOQUETAMANO = int(BLOQUETAMANOX / 2)

# Mapa
MAPA = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

MAPA_HORIZONTAL = 50
MAPA_VERTICAL = 50

paisSeleccionado = ""

def main():
    global FPSCLOCK, DISPLAYSURF, FONDOOBJETO, FONDOOBJETOTITULO, FONDOOBJETOGAMEOVER, paisSeleccionado
    pygame.init()
    pygame.mixer.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((DISPLAYSURFX, DISPLAYSURFY), 0, 32)
    pygame.display.set_caption("Copa Mundial Del Fútbol 2026")
    FONDOOBJETO = pygame.font.Font('freesansbold.ttf', 32)
    FONDOOBJETOTITULO = pygame.font.Font('freesansbold.ttf', 100)
    FONDOOBJETOGAMEOVER = pygame.font.Font('freesansbold.ttf', 90)
    paisSeleccionado = menuPais()

    while True:
        Juego()

def menuPais():

    Logo = pygame.image.load("Cara de MarBano MEJOR con edición.png")
    Logo = pygame.transform.scale(Logo, (150, 150))

    fuenteTitulo = pygame.font.SysFont("Arial", 60)
    fuente = pygame.font.SysFont("Arial", 40)

    opciones = ["MÉXICO", "ARGENTINA", "ESPAÑA", "BRASIL"]
    seleccion = 0

    pygame.mixer.music.load("HoliznaCC0 - Game BOI 2.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    while True:

        DISPLAYSURF.fill((40,120,40))

        titulo = fuenteTitulo.render("COPA MUNDIAL 2026", True, WHITE)
        DISPLAYSURF.blit(titulo, (190,80))

        # Mensaje de YouTube
        textoYT = fuente.render("¡Suscríbete a MarBano en YouTube!", True, RED)
        DISPLAYSURF.blit(textoYT, (170, 500))

        DISPLAYSURF.blit(Logo, (MITADDISPLAYSURFX - 85, DISPLAYSURFY - 150))

        for i, opcion in enumerate(opciones):

            if i == seleccion:
                color = YELLOW
            else:
                color = WHITE

            texto = fuente.render(opcion, True, color)
            DISPLAYSURF.blit(texto, (330,220+i*70))

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:

                if event.key == K_UP:
                    seleccion = (seleccion-1) % len(opciones)

                elif event.key == K_DOWN:
                    seleccion = (seleccion+1) % len(opciones)

                elif event.key == K_RETURN:
                    return opciones[seleccion]

# Función del Juego
def Juego():

    # Números
    golesJugador = 0
    golesCambiarTipo = 0
    
    # Booleano
    COSA = False

    # -------------------------
    # Jugador
    # -------------------------
    class Jugador:
    
        def __init__(self, x, y, color):
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
    
            self.x = max(self.radio, min(DISPLAYSURFX - self.radio, self.x))
            self.y = max(self.radio + 150, min(DISPLAYSURFY - (self.radio + 150), self.y))

        def dibujar(self):
            if paisSeleccionado == "MÉXICO":
                Personaje.color = GREEN_MEXICO
            elif paisSeleccionado == "ARGENTINA":
                Personaje.color = WHITE
            elif paisSeleccionado == "ESPAÑA":
                Personaje.color = RED
            elif paisSeleccionado == "BRASIL":
                Personaje.color = BLUE_BRAZIL

            pygame.draw.circle(DISPLAYSURF,self.color,(int(self.x),int(self.y)),self.radio)
    
    Personaje = Jugador(100, MITADDISPLAYSURFY, WHITE)

    class Pelota:
    
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.radio = 20
    
            # La pelota empieza pegada al jugador
            self.conJugador = True
    
            # Velocidad constante (MRU)
            self.velocidadX = 0

            # Tiempo constante (MRU)
            self.tiempoX = 1

    
        def mover(self, jugador):
    
            if self.conJugador:
                # La pelota sigue al jugador
                self.x = jugador.x + 30
                self.y = jugador.y
            else:
                # Movimiento Rectilíneo Uniforme
                self.x += self.velocidadX * self.tiempoX
    
        def disparar(self):
    
            if self.conJugador:
                self.conJugador = False
                self.velocidadX = 8   # Velocidad constante
    
        def dibujar(self):
            pygame.draw.circle(DISPLAYSURF, BLACK, (int(self.x), int(self.y)), self.radio)
        
        def getRect(self):
            return pygame.Rect(self.x - self.radio, self.y - self.radio, self.radio * 2, self.radio * 2)

    PelotaJuego = Pelota(Personaje.x + 30, Personaje.y)

    # -------------------------
    # IA
    # -------------------------
    class IA:
    
        def __init__(self, x, y, color, tiempo, tipo):
            self.x = x
            self.y = y
            self.xInicial = x
            self.yInicial = y
            self.radio = 20
            self.velocidad = 3
            self.color = color
            self.tiempo = tiempo   # ← Agrega esta línea
            self.tipo = tipo
    
        def mover(self):

            if self.tipo == 0:
                self.velocidad = 3
            elif self.tipo == 1:
                self.velocidad = 4
            elif self.tipo == 2:
                self.velocidad = 5
            elif self.tipo == 3:
                self.velocidad = 6
            elif self.tipo == 4:
                self.velocidad = 7
            elif self.tipo == 5:
                self.velocidad = 8
            elif self.tipo == 6:
                self.velocidad = 9
            elif self.tipo == 7:
                self.velocidad = 10
            elif self.tipo == 8:
                self.velocidad = 11
            elif self.tipo == 9:
                self.velocidad = 13
            elif self.tipo == 10:
                self.velocidad = 15
            elif self.tipo == 11:
                self.velocidad = 17
            elif self.tipo == 12:
                self.velocidad = 20
            elif self.tipo == 13:
                self.velocidad = 25

            #print(self.velocidad)
            self.y += self.velocidad * self.tiempo
    
            if self.y <= 175:
                self.tiempo = 1   # Baja

            if self.y >= 525:
                self.tiempo = -1  # Sube
        
        def dibujar(self):
            if paisSeleccionado == "MÉXICO":
                rival = "ARGENTINA"
                self.color = WHITE   # Blanco
            
            elif paisSeleccionado == "ARGENTINA":
                rival = "ESPAÑA"
                self.color = RED     # Rojo
            
            elif paisSeleccionado == "ESPAÑA":
                rival = "BRASIL"
                self.color = BLUE_BRAZIL      # Azul de Brasil
            
            elif paisSeleccionado == "BRASIL":
                rival = "MEXICO"
                self.color = GREEN_MEXICO     # Verde de México

            pygame.draw.circle(DISPLAYSURF,self.color,(int(self.x),int(self.y)),self.radio)
        
        def getRect(self):
            return pygame.Rect(self.x - self.radio, self.y - self.radio, self.radio * 2, self.radio * 2)
    
    Enemigo = IA(600, MITADDISPLAYSURFY, BLUE, -1, 0)
    Enemigo2 = IA(400, MITADDISPLAYSURFY, BLUE, 1, 0)
    Enemigo3 = IA(700, MITADDISPLAYSURFY, BLUE, 0, 0)

    enemigos = [Enemigo, Enemigo2, Enemigo3]

    SonidoGol = pygame.mixer.Sound("474683__the-sacha-rush__goal-point-reached-simple-sfx.wav")
    SonidoDisparo = pygame.mixer.Sound("171828__qubenzis__psy-kick-original-1.wav")
    SonidoGameOver = pygame.mixer.Sound("173859__jivatma07__j1game_over_mono.wav")

    pygame.mixer.music.load("HoliznaCC0 - Game BOI 2.mp3")
    pygame.mixer.music.play(-1)

    while True:
        
        DISPLAYSURF.fill(GREEN)

        drawBloque()
        BloqueRect = drawBloqueRect()
        

        teclas = pygame.key.get_pressed()

        Personaje.mover(teclas)
        PelotaJuego.mover(Personaje)

        PelotaRect = PelotaJuego.getRect()

        Personaje.dibujar()
        PelotaJuego.dibujar()

        Enemigo.dibujar()
        Enemigo2.dibujar()
        Enemigo3.dibujar()

        Enemigo.mover()
        Enemigo2.mover()

        # Salida del videojuego
        ChequearParaSalir()

        for event in pygame.event.get(): # event handling loop
            #Poner el click
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    PelotaJuego.disparar()
                    SonidoDisparo.play()
        
        for fila in BloqueRect:
            for bloque in fila:
                if PelotaRect.colliderect(bloque):
                    print("¡Gol!")
        
                    golesJugador += 1
                    golesCambiarTipo += 1
                    SonidoGol.play()
        
                    PelotaJuego.conJugador = True
                    PelotaJuego.velocidadX = 0
        
                    Personaje.x = 100
                    Personaje.y = MITADDISPLAYSURFY

                    break   # Sale del segundo for
            else:
                continue
            break           # Sale del primer for

        for enemigo in enemigos:

            if golesCambiarTipo == 1:
                enemigo.tipo = 1
            elif golesCambiarTipo == 2:
                enemigo.tipo = 2
            elif golesCambiarTipo == 3:
                enemigo.tipo = 3
            elif golesCambiarTipo == 4:
                enemigo.tipo = 4
            elif golesCambiarTipo == 5:
                enemigo.tipo = 5
            elif golesCambiarTipo == 6:
                enemigo.tipo = 6
            elif golesCambiarTipo == 7:
                enemigo.tipo = 7
            elif golesCambiarTipo == 8:
                enemigo.tipo = 8
            elif golesCambiarTipo == 9:
                enemigo.tipo = 9
            elif golesCambiarTipo == 10:
                enemigo.tipo = 10
            elif golesCambiarTipo == 11:
                enemigo.tipo = 11
            elif golesCambiarTipo == 12:
                enemigo.tipo = 12
            elif golesCambiarTipo == 13:
                enemigo.tipo = 13

            if PelotaJuego.getRect().colliderect(enemigo.getRect()):
        
                #print("GAME OVER")
                showTextScreenGAMEOVER('JUEGO TERMINADO', Personaje)
                showTextScreenFinalPunto('Tus goles son ', golesJugador, Personaje)
        
                for e in enemigos:
                    e.tipo = 0
                golesJugador = 0
                golesCambiarTipo = 0
                SonidoGameOver.play()
                
        
                Personaje.x = 100
                Personaje.y = MITADDISPLAYSURFY
        
                PelotaJuego.conJugador = True
                PelotaJuego.velocidadX = 0
                PelotaJuego.x = Personaje.x + 30
                PelotaJuego.y = Personaje.y

                pygame.display.update()
                pygame.time.delay(2000)
        
                break

        fuente = pygame.font.SysFont("Arial",30)
        
        texto = fuente.render(
            "País: " + paisSeleccionado,
            True,
            WHITE
        )
        
        DISPLAYSURF.blit(texto,(20,20))
        showTextScreenPunto('Goles', golesJugador, Personaje)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def ChequearParaSalir():
    for event in pygame.event.get(QUIT): # Obtener todas las salidas de eventos de QUIT
        terminate() # Terminar si los eventos de QUIT estan presentes
    for event in pygame.event.get(KEYUP): # Obtener todos los eventos de KEYUP
        if event.key == K_ESCAPE:
            terminate() # Terminar si el evento de KEYUP era el boton del Esc
        pygame.event.post(event) # Poner el otro evento de objetos de KEYUP atras

def terminate():
    pygame.quit()
    sys.exit()

def dibujar(self):
    pygame.draw.circle(DISPLAYSURF,self.color,(int(self.x),int(self.y)),self.radio)

def makeTextObjs(text, font, color, colorbackground):
    surf = font.render(text, True, color, colorbackground)
    return surf, surf.get_rect()

#Crear los textos
def showTextScreenMenu(text):
    titleSurf, titleRect = makeTextObjs('Seleccionar un país hispano', FONDOOBJETOTITULO, WHITE, BLUE)
    titleRect.center = MITADDISPLAYSURFX, 150
    DISPLAYSURF.blit(titleSurf, titleRect)

    titleSurf, titleRect = makeTextObjs('Iniciar Juego', FONDOOBJETO, WHITE, BLUE)
    titleRect.center = MITADDISPLAYSURFX, MITADDISPLAYSURFY
    DISPLAYSURF.blit(titleSurf, titleRect)

    titleSurf, titleRect = makeTextObjs('¡Suscríbete a MarBano en YouTube!', FONDOOBJETO, WHITE, None)
    titleRect.center = 225, MITADDISPLAYSURFY + 360
    DISPLAYSURF.blit(titleSurf, titleRect)

def showTextScreenPunto(text, Punto, Personaje):
    if Personaje.color == WHITE:
        titleSurf, titleRect = makeTextObjs('Goles ' + str(Punto), FONDOOBJETO, BLUE, Personaje.color)
        titleRect.center = DISPLAYSURFX - 100, 0 + 50
        DISPLAYSURF.blit(titleSurf, titleRect)
    else:
        titleSurf, titleRect = makeTextObjs('Goles ' + str(Punto), FONDOOBJETO, WHITE, Personaje.color)
        titleRect.center = DISPLAYSURFX - 100, 0 + 50
        DISPLAYSURF.blit(titleSurf, titleRect)

def showTextScreenGAMEOVER(text, Personaje):
    if Personaje.color == WHITE:
        titleSurf, titleRect = makeTextObjs('JUEGO TERMINADO', FONDOOBJETOGAMEOVER, BLUE, Personaje.color)
        titleRect.center = MITADDISPLAYSURFX, 150
        DISPLAYSURF.blit(titleSurf, titleRect)
    else:
        titleSurf, titleRect = makeTextObjs('JUEGO TERMINADO', FONDOOBJETOGAMEOVER, WHITE, Personaje.color)
        titleRect.center = MITADDISPLAYSURFX, 150
        DISPLAYSURF.blit(titleSurf, titleRect)

def showTextScreenFinalPunto(text, Punto, Personaje):
    if Personaje.color == WHITE:
        titleSurf, titleRect = makeTextObjs('Tus goles son ' + str(Punto), FONDOOBJETOGAMEOVER, BLUE, Personaje.color)
        titleRect.center = MITADDISPLAYSURFX, MITADDISPLAYSURFY
        DISPLAYSURF.blit(titleSurf, titleRect)
    else:
        titleSurf, titleRect = makeTextObjs('Tus goles son ' + str(Punto), FONDOOBJETOGAMEOVER, WHITE, Personaje.color)
        titleRect.center = MITADDISPLAYSURFX, MITADDISPLAYSURFY
        DISPLAYSURF.blit(titleSurf, titleRect)

def drawBloque():
    Posicionx = 0
    Posiciony = 0

    # Buscar en cada una de las 14 listas en y, dentro de cada uno de los 18 objetos en x.
    for y in range(len(MAPA)):
        for x in range(len(MAPA[y])):
            Posiciony = MAPA_VERTICAL * y
            Posicionx = MAPA_HORIZONTAL * x

            #print(Posiciony)
            
            # Si es 1 entonces añade una plataforma del tamaño de un bloque
            if MAPA[y][x] == 1:
                pygame.draw.rect(DISPLAYSURF, WHITE, (Posicionx, Posiciony, BLOQUETAMANOX, BLOQUETAMANOY))
                #pygame.rect

    #print(len(MAPA_DEL_PLATAFORMERO[y]))    
    #print(Posicionx, Posiciony, x, y)

def drawBloqueRect():
    PlataformeroRect = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

    #print(len(PlataformeroRect))

    Rectx = 0
    Recty = 0

    # Buscar en cada una de las 14 listas en y, dentro de cada uno de los 18 objetos en x.
    for y in range(len(MAPA)):
        for x in range(len(MAPA[y])):
            Recty = MAPA_VERTICAL * y
            Rectx = MAPA_HORIZONTAL * x

            # Si es 1 entonces añade un collider del tamaño de un bloque
            if MAPA[y][x] == 1:
                PlataformeroRect[y].append(pygame.Rect(Rectx, Recty, BLOQUETAMANOX, BLOQUETAMANOY))

    # Len es contar objetos de una lista.    
    #print(len(MAPA_DEL_PLATAFORMERO), len(MAPA_DEL_PLATAFORMERO[y]))
    
    return PlataformeroRect

if __name__ == '__main__':
    main()