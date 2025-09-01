# 🐭🐇 Raton y Conejo vs Culebras

Un juego en **Python con Pygame** en el que puedes elegir entre dos
personajes:\
- 🐭 **Ratón** → más rápido y dispara **quesos**.\
- 🐇 **Conejo** → velocidad normal y dispara **zanahorias**.

Ambos pueden usar **escudo protector** y lanzar **huevos explosivos** 💥
para derrotar a las culebras 🐍.
Cada jugador cuenta con 2 vidas

------------------------------------------------------------------------

## 🎮 Controles del juego

-   **F** → Disparar proyectil (queso/zanahoria según personaje).\
-   **E** → Lanzar huevo explosivo.\
-   **ESPACIO** → Activar escudo temporal.\
-   **Flechas** → Mover al personaje.

------------------------------------------------------------------------

## 📋 Instrucciones

1.  Al iniciar el juego, aparecerá un **menú principal**.\
2.  Selecciona tu personaje (Ratón o Conejo).\
3.  Lee las **indicaciones de los controles** (también visibles en
    pantalla durante la partida).\
4.  Derrota a las culebras que aparecen en el mapa.
    -   Si una culebra te atrapa sin escudo → pierdes.\
    -   Si explotas huevos cerca de ellas o disparas → se destruyen y
        aparecen nuevas.

------------------------------------------------------------------------

## 🚀 Instalación y ejecución

1.  Asegúrate de tener instalado **Python 3.x**.\
2.  Instala **Pygame** si no lo tienes:

``` bash
pip install pygame
```

3.  Clona este repositorio o descarga los archivos.\
4.  Ejecuta el juego con:

``` bash
python main.py
```

------------------------------------------------------------------------

## 📂 Estructura del proyecto

    .
    ├── main.py
    ├── assets/
    │   ├── raton.jpg
    │   ├── conejo.jpg
    │   ├── culebras.jpg
    │   ├── queso.jpg
    │   ├── zanahoria.jpg
    │   ├── huevo.png
    │   └── explosion.png
    └── README.md

------------------------------------------------------------------------

## ✨ Mejoras futuras

-   puntuación.\
-   Animaciones más detalladas para las culebras.
