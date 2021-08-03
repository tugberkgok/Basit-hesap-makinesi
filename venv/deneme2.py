import pygame
import pygame.camera
import keyboard

pygame.camera.init()
pygame.camera.list_cameras() #Camera detected or not
cam = pygame.camera.Camera()
cam.start()
img = cam.get_image()

img = cam.get_image()
pygame.image.save(img,"filename.jpg")