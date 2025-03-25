import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Configuração inicial do OpenGL
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, 800.0 / 600.0, 0.1, 100.0)  # Ajuste da tela para 800x600
    glMatrixMode(GL_MODELVIEW)

# Função para desenhar um quadrado com linhas
def draw_square_lines():
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -6.0)  # Posição fixa
    glColor3f(1.0, 1.0, 1.0)  # Branco
    glBegin(GL_LINE_LOOP)
    glVertex3f(-1.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glEnd()

# Função principal
def main():
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)  # Ajuste para 800x600
    init()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_square_lines()
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
