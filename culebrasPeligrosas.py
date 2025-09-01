import pygame
import random
import sys

pygame.init()

ANCHO, ALTO = 1000, 700
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Raton y Conejo vs Culebras")

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (200, 0, 0)
FUENTE = pygame.font.SysFont("Arial", 28)

personajes = [
    {"nombre": "Raton", "velocidad": 7, "proyectil": "assets/queso.jpg"},
    {"nombre": "Conejo", "velocidad": 5, "proyectil": "assets/zanahoria.jpg"},
]

class Jugador:
    def __init__(self, x, y, personaje):
        self.x = x
        self.y = y
        self.velocidad = personaje["velocidad"]
        self.radio = 30
        self.vidas = 2
        self.escudo_activo = False
        self.escudo_tiempo = 0
        self.duracion_escudo = 2000
        self.proyectil = pygame.image.load(personaje["proyectil"])
        self.proyectil = pygame.transform.scale(self.proyectil, (25, 25))

        if personaje["nombre"] == "Raton":
            self.imagen = pygame.image.load("assets/raton.jpg")
        else:
            self.imagen = pygame.image.load("assets/conejo.jpg")
        self.imagen = pygame.transform.scale(self.imagen, (70, 70))

    def mover(self, teclas):
        if teclas[pygame.K_LEFT] and self.x - self.velocidad > 0:
            self.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.x + self.velocidad < ANCHO:
            self.x += self.velocidad
        if teclas[pygame.K_UP] and self.y - self.velocidad > 0:
            self.y -= self.velocidad
        if teclas[pygame.K_DOWN] and self.y + self.velocidad < ALTO:
            self.y += self.velocidad

    def activar_escudo(self):
        self.escudo_activo = True
        self.escudo_tiempo = pygame.time.get_ticks()

    def dibujar(self):
        VENTANA.blit(self.imagen, (self.x - 35, self.y - 35))
        if self.escudo_activo:
            tiempo_pasado = pygame.time.get_ticks() - self.escudo_tiempo
            if tiempo_pasado < self.duracion_escudo:
                pygame.draw.circle(VENTANA, (0, 200, 255), (self.x, self.y), 45, 3)
            else:
                self.escudo_activo = False

class Culebra:
    def __init__(self, jugador, vel_min, vel_max):
        distancia_segura = 200
        while True:
            self.x = random.randint(0, ANCHO)
            self.y = random.randint(0, ALTO)
            dx = self.x - jugador.x
            dy = self.y - jugador.y
            if (dx**2 + dy**2) ** 0.5 > distancia_segura:
                break
        self.velocidad = random.uniform(vel_min, vel_max)
        self.imagen = pygame.image.load("assets/culebras.jpg")
        self.imagen = pygame.transform.scale(self.imagen, (80, 40))

    def mover(self, jugador):
        if self.x < jugador.x:
            self.x += self.velocidad
        if self.x > jugador.x:
            self.x -= self.velocidad
        if self.y < jugador.y:
            self.y += self.velocidad
        if self.y > jugador.y:
            self.y -= self.velocidad

    def dibujar(self):
        VENTANA.blit(self.imagen, (int(self.x), int(self.y)))

class Proyectil:
    def __init__(self, x, y, imagen):
        self.x = x
        self.y = y
        self.imagen = imagen
        self.velocidad = 10

    def mover(self):
        self.y -= self.velocidad

    def dibujar(self):
        VENTANA.blit(self.imagen, (self.x - 12, self.y - 12))

class Huevo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radio = 20
        self.exploto = False
        self.imagen = pygame.image.load("assets/huevo.png")
        self.imagen = pygame.transform.scale(self.imagen, (40, 40))

    def explotar(self):
        self.exploto = True
        self.explosion_time = pygame.time.get_ticks()

    def dibujar(self):
        if not self.exploto:
            VENTANA.blit(self.imagen, (self.x - 20, self.y - 20))
        else:
            pygame.draw.circle(VENTANA, ROJO, (self.x, self.y), 60, 5)

def mostrar_texto(texto, y):
    render = FUENTE.render(texto, True, NEGRO)
    rect = render.get_rect(center=(ANCHO // 2, y))
    VENTANA.blit(render, rect)

def seleccion_dificultad():
    while True:
        VENTANA.fill(BLANCO)
        mostrar_texto("Selecciona dificultad:", 150)
        mostrar_texto("1 - Fácil", 250)
        mostrar_texto("2 - Normal", 300)
        mostrar_texto("3 - Difícil", 350)
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    return {"enemigos": 3, "vel_min": 0.3, "vel_max": 0.6, "nombre": "Fácil"}
                if evento.key == pygame.K_2:
                    return {"enemigos": 5, "vel_min": 0.5, "vel_max": 1.0, "nombre": "Normal"}
                if evento.key == pygame.K_3:
                    return {"enemigos": 8, "vel_min": 1.0, "vel_max": 1.5, "nombre": "Difícil"}

def seleccion_personaje():
    while True:
        VENTANA.fill(BLANCO)
        mostrar_texto("Elige tu personaje (1 = Ratón, 2 = Conejo):", 150)
        for i, p in enumerate(personajes):
            img = pygame.image.load(f"assets/{p['nombre'].lower()}.jpg")
            img = pygame.transform.scale(img, (100, 100))
            VENTANA.blit(img, (ANCHO//2 - 150 + i*200, 250))
            mostrar_texto(p["nombre"], 400 + i*50)
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    return personajes[0]
                if evento.key == pygame.K_2:
                    return personajes[1]

def menu():
    while True:
        VENTANA.fill(BLANCO)
        mostrar_texto("🐭🐇 RATON Y CONEJO VS CULEBRAS 🐍", 150)
        mostrar_texto("Presiona ENTER para comenzar", 300)
        mostrar_texto("Presiona ESC para salir", 350)
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def juego():
    dificultad = seleccion_dificultad()
    personaje = seleccion_personaje()
    jugador = Jugador(ANCHO//2, ALTO//2, personaje)

    enemigos = [Culebra(jugador, dificultad["vel_min"], dificultad["vel_max"]) for _ in range(dificultad["enemigos"])]
    balas = []
    huevos = []
    reloj = pygame.time.Clock()

    while True:
        reloj.tick(60)
        VENTANA.fill(BLANCO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_f:
                    balas.append(Proyectil(jugador.x, jugador.y, jugador.proyectil))
                if evento.key == pygame.K_e:
                    huevos.append(Huevo(jugador.x, jugador.y))
                if evento.key == pygame.K_SPACE:
                    jugador.activar_escudo()

        teclas = pygame.key.get_pressed()
        jugador.mover(teclas)

        jugador.dibujar()

        for bala in balas[:]:
            bala.mover()
            bala.dibujar()
            if bala.y < 0:
                balas.remove(bala)

        for huevo in huevos[:]:
            huevo.dibujar()
            if huevo.exploto and pygame.time.get_ticks() - huevo.explosion_time > 500:
                huevos.remove(huevo)

        for enemigo in enemigos[:]:
            enemigo.mover(jugador)
            enemigo.dibujar()

            dx = jugador.x - enemigo.x
            dy = jugador.y - enemigo.y
            distancia = (dx**2 + dy**2) ** 0.5
            if distancia < jugador.radio + 20:
                if jugador.escudo_activo and pygame.time.get_ticks() - jugador.escudo_tiempo < 2000:
                    pass
                else:
                    jugador.vidas -= 1
                    if jugador.vidas > 0:
                        jugador.x, jugador.y = ANCHO//2, ALTO//2
                        mostrar_texto("¡Te atraparon! Pierdes una vida", ALTO//2)
                        pygame.display.update()
                        pygame.time.delay(1500)
                    else:
                        mostrar_texto("GAME OVER", ALTO//2)
                        pygame.display.update()
                        pygame.time.delay(2000)
                        return

            for bala in balas[:]:
                dx = bala.x - enemigo.x
                dy = bala.y - enemigo.y
                if (dx**2 + dy**2) ** 0.5 < 30:
                    enemigos.remove(enemigo)
                    balas.remove(bala)
                    enemigos.append(Culebra(jugador, dificultad["vel_min"], dificultad["vel_max"]))
                    break

            for huevo in huevos:
                if not huevo.exploto:
                    dx = huevo.x - enemigo.x
                    dy = huevo.y - enemigo.y
                    if (dx**2 + dy**2) ** 0.5 < 30:
                        huevo.explotar()
                else:
                    dx = huevo.x - enemigo.x
                    dy = huevo.y - enemigo.y
                    if (dx**2 + dy**2) ** 0.5 < 60:
                        if enemigo in enemigos:
                            enemigos.remove(enemigo)
                            enemigos.append(Culebra(jugador, dificultad["vel_min"], dificultad["vel_max"]))


        vidas_texto = FUENTE.render(f"Vidas: {jugador.vidas}", True, NEGRO)
        VENTANA.blit(vidas_texto, (20, 20))
        nivel_texto = FUENTE.render(f"Dificultad: {dificultad['nombre']}", True, NEGRO)
        VENTANA.blit(nivel_texto, (20, 50))

        controles = ["F = Disparar", "E = Huevo explosivo", "ESPACIO = Escudo", "Flechas = Mover"]
        for i, c in enumerate(controles):
            c_texto = FUENTE.render(c, True, NEGRO)
            VENTANA.blit(c_texto, (ANCHO - 300, 20 + i*30))

        pygame.display.update()

if __name__ == "__main__":
    menu()
    juego()
