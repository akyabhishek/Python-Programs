import pygame,sys
from pygame.locals import *
import numpy as np
from keras.models import load_model
import cv2

WINDOWSIZEX=640
WINDOWSIZEY=480

#pygame initiliaze
pygame.init()

FONT=pygame.font.Font("freesansbold.ttf",18)

pygame.display.set_mode((WINDOWSIZEX,WINDOWSIZEY))

while True:
    for even in pygame.event.get():
        if even.type==QUIT:
            pygame.quit()
            sys.exit()
    