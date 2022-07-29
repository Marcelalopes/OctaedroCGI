import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (

    (-1,0,0),#0
    (0,1,0),#1
    (1,0,0),#2
    (0,-1,0),#3
    (0,0,1),#4
    (0,0,-1),#5
)

arestas = (
    (0,1),
    (1,2),
    (0,3),
    (2,3),
    (0,4),
    (1,4),
    (2,4),
    (3,4),
    (5,0),
    (5,1),
    (5,2),
    (5,3),
)


def Octaedro():
    glBegin(GL_LINES)
    for aresta in arestas:
        for vertex in aresta:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():

    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    clock = pygame.time.Clock()
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                glTranslatef(-0.1, 0, 0)
            if event.key == pygame.K_RIGHT:
                glTranslatef(0.1, 0, 0)

            if event.key == pygame.K_UP:
                glTranslatef(0, 0.2, 0)
            if event.key == pygame.K_DOWN:
                glTranslatef(0, -0.2, 0)

            if event.key == pygame.K_s:
                glRotatef(5, 5, 0, 0)
            if event.key == pygame.K_w:
                glRotatef(-5, 5, 0, 0)
            if event.key == pygame.K_d:
                glRotatef(-5, 0, -5, 0)
            if event.key == pygame.K_a:
                glRotatef(5, 0, -5, 0)

            if event.key == pygame.K_p:
                glScalef(0.9, 0.9, 0.9)
            if event.key == pygame.K_l:
                glScalef(1.1, 1.1, 1.1)

            if event.key == pygame.K_g:
                gluLookAt(0, 0, 0, 1, 0, 1, 0, 0, 1)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Octaedro()

        pygame.display.flip()
        clock.tick(60)
main()