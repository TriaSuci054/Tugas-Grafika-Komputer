import sys
import time
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window = 0

width, height = 800, 600


def bresAlgo(x1, y1, x2, y2):
    #menentukan delta X dan delta Y
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = dy/float(dx)
    
    x, y = x1, y1 

    if slope > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2 * dy - dx
    
    glVertex2f(x, y)
    
    
    for k in range(2, dx):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2*(dy - dx)
        else:
            p = p + 2*dy
 
        x = x + 1 if x < x2 else x - 1


        time.sleep(0.01)
        glVertex2f(x, y)
            
#memulai menggabar menggunakan bressenham
def lineBres():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_LINES)
    #menentukan warna
    glColor(1.0, 1.0, 0.0)
    bresAlgo(50, 50, 60, 60)   
    glEnd()
    glutSwapBuffers()

def main():
    #inisialisasi glut
    glutInit(sys.argv)
    #inisialisasi type display glut
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE|GLUT_ALPHA|GLUT_DEPTH)
    #inisialisasi ukuran layar glut
    glutInitWindowSize(width, height)
    #inisialisasi ukuran layar glut
    glutInitWindowPosition(0,0)
    #inisialisasi window
    glutCreateWindow("Bressenham")
    #membersihkan layar dan memberikan warna
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0.0, 100.0, 0.0, 100.0)
    glutDisplayFunc(lineBres)
    glutIdleFunc(lineBres)
    glutMainLoop()

main()
        
        

   
