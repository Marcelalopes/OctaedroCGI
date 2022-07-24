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
    (-0.5,-0.5,0),
    (0.5,-0.5,0),
    (0.5,0.5,0),
    (-0.5,0.5,0),
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

faces = (
    (0,1,6,4),
    (1,2,7,4),
    (2,3,8,4),
    (3,0,9,4),
    (0,1,6,5),
    (1,2,7,5),
    (2,3,8,5),
    (3,0,9,5),
)

cores = (
    (0,0,1),
    (0,0,0),
    (0,0,1),
    (0,0,0),
    (0,0,1),
    (0,0,0),
)

normals = [
    (0,  1,  0),
    (0, -1,  0),
    (0,  0,  1),
    (1,  0,  0),
    (0,  1,  0),
    (0,  0, -1),
    (-1,  0,  0),
    (0,  0,  1),
    (1,  0,  0),
    (0, -1,  0)
]

def Octaedro():
    glBegin(GL_QUADS)
    for surface in faces:
        x = 0
        for vertex in surface:
            x+=1
            glColor3fv(cores[x])
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for aresta in arestas:
        for vertex in aresta:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():

    global faces

    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    clock = pygame.time.Clock()

    glMatrixMode(GL_MODELVIEW)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0.0,0.0, -5)

    glLight(GL_LIGHT0, GL_POSITION, (5,5,5,1))
    glLight(GL_LIGHT0, GL_AMBIENT, (10,0,0,1))
    glLight(GL_LIGHT0, GL_DIFFUSE, (1,1,1,1))

    glEnable(GL_DEPTH_TEST)

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

            if event.key == pygame.K_c:
                gluLookAt(0, 0, 0, 1, 0, 1, 0, 0, 1)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

        Octaedro()

        glDisable(GL_LIGHT0)
        glDisable(GL_LIGHTING)
        glDisable(GL_COLOR_MATERIAL)

        pygame.display.flip()
        clock.tick(60)
main()