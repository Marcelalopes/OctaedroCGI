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

faces = (
    (0,1,4),
    (1,2,4),
    (2,3,4),
    (3,0,4),
    (0,1,5),
    (1,2,5),
    (2,3,5),
    (3,0,5),
)

cores = (
    (0, 0, 1),
    (0, 1, 0),
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 1),
    (0, 0, 1),
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 1),
    (0, 0, 1)
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
textureCoordinates = (
  (0, 0), (0, 1), (1, 1), (1, 0), (1,2), (1,4),
    (0, 2), (2, 1), (2, 2), (2,0), (2,3), (2,4),
    (0, 3),(3, 1), (3, 2), (3, 0), (3,4), (3,3),
    (0, 4),(4, 1), (4, 2), (4, 0), (4,3), (4,4)
)

def carregaTextura():
    textureSurface = pygame.image.load('textura.jpg')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid

def Octaedro():
    # glColor3f(1,1,1)
    glBegin(GL_TRIANGLES)
    for i_surface, surface in enumerate(faces):
        x = 0
        glNormal3fv(normals[i_surface])
        for i_vertex, vertex in enumerate(surface):
            x += 1
            glColor3fv(cores[x])
            glTexCoord2fv(textureCoordinates[i_vertex])
            glVertex3fv(vertices[vertex])
    glEnd()

    # glColor3fv(cores[0])
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

            if event.key == pygame.K_g:
                gluLookAt(0, 0, 0, 1, 0, 1, 0, 0, 1)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

        carregaTextura()
        Octaedro()

        glDisable(GL_LIGHT0)
        glDisable(GL_LIGHTING)
        glDisable(GL_COLOR_MATERIAL)

        pygame.display.flip()
        clock.tick(60)
main()