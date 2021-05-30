import pygame
import subprocess
from pygame.locals import *
from time import sleep
from random import randrange
#inicia el juego
pygame.init()
#Cargando Variables
width = pygame.display.Info().current_w #1920
heigth  = pygame.display.Info().current_h #1080
x = 900
y = 950
char_w = 80
char_h = 80
velN = 10
velC = 30
isJump = False
jumpCount = 10
left = False
right = False
trans =False
Jumping = False
Falling = False
ToggleFrame  = True
BanderaWC = True
walkCount = 0
CargarCCount = 0
CorrerSCount = 0
ChangeS = 0
clock = pygame.time.Clock()

#Cargando Imagenes
#Fondo 
screen = pygame.display.set_mode((width, heigth))
Fondo = pygame.image.load('FondoKonoha.png')
Fondo = pygame.transform.scale(Fondo,(width,heigth))

# Imagenes de Movimiento
walkRight = [pygame.transform.scale(pygame.image.load('Camina/RC1.png'),(48,75)),
                     pygame.transform.scale(pygame.image.load('Camina/RC2.png'),(36,75)),
                     pygame.transform.scale(pygame.image.load('Camina/RC3.png'),(38,75)),
                     pygame.transform.scale(pygame.image.load('Camina/RC4.png'),(36,75)),
                     pygame.transform.scale(pygame.image.load('Camina/RC5.png'),(33,75)),
                     pygame.transform.scale(pygame.image.load('Camina/RC6.png'),(35,75))] 
walkLeft =  [pygame.transform.scale(pygame.image.load('Camina/LC1.png'),(48,75)),
                    pygame.transform.scale(pygame.image.load('Camina/LC2.png'),(36,75)),
                    pygame.transform.scale(pygame.image.load('Camina/LC3.png'),(38,75)),
                    pygame.transform.scale(pygame.image.load('Camina/LC4.png'),(36,75)),
                    pygame.transform.scale(pygame.image.load('Camina/LC5.png'),(33,75)),
                    pygame.transform.scale(pygame.image.load('Camina/LC6.png'),(35,75))]
ChakraC = [ pygame.transform.scale(pygame.image.load('Chakra/1.png'),(46,84)),
                    pygame.transform.scale(pygame.image.load('Chakra/2.png'),(42,84)),
                    pygame.transform.scale(pygame.image.load('Chakra/3.png'),(36,84)),
                    pygame.transform.scale(pygame.image.load('Chakra/4.png'),(36,84)),
                    pygame.transform.scale(pygame.image.load('Chakra/5.png'),(74,101)),
                    pygame.transform.scale(pygame.image.load('Chakra/6.png'),(76,101)),
                    pygame.transform.scale(pygame.image.load('Chakra/7.png'),(65,101)),
                    pygame.transform.scale(pygame.image.load('Chakra/8.png'),(74,101))]
Stand = [ pygame.transform.scale(pygame.image.load('Parado/1.png'),(53,74)),
              pygame.transform.scale(pygame.image.load('Parado/2.png'),(53,74)),
              pygame.transform.scale(pygame.image.load('Parado/3.png'),(51,74)),
              pygame.transform.scale(pygame.image.load('Parado/4.png'),(51,74))]

Jump = [pygame.transform.scale(pygame.image.load('Salto/1.png'),(66,75)),
                pygame.transform.scale(pygame.image.load('Salto/2.png'),(66,74)),]

Fall = [pygame.transform.scale(pygame.image.load('Salto/3.png'),(45,80)),
            pygame.transform.scale(pygame.image.load('Salto/4.png'),(45,80)),]

#Cargando sonidos
JumpS = pygame.mixer.Sound('Sonido/Jump.wav')
Music = pygame.mixer.Sound('Sonido/Music.wav')
CargarC = pygame.mixer.Sound('Sonido/CargarC.wav')
CorrerS = pygame.mixer.Sound('Sonido/Pasos.wav')

#Corriendo a 24 Fps lo cual da 1 F cada 0.0417 seg

# Definicion de funciones
        

def Refresh():
    global walkCount
    global CargarCCount
    global CorrerSCount
    global ToggleFrame
    screen.blit(Fondo,(0,0))
    if walkCount + 1 > 24:
        walkCount = 0
        
    if right:
        screen.blit(walkRight[walkCount//4], (x,y))
        walkCount += 1
    elif left:
        screen.blit(walkLeft[walkCount//4], (x,y))
        walkCount += 1
    elif trans:
        if(walkCount > 5):
            if ToggleFrame:
                screen.blit(ChakraC[6], (x,y))
            else:
                screen.blit(ChakraC[7], (x,y))
            ToggleFrame = not(ToggleFrame)
        else:
            screen.blit(ChakraC[walkCount//3], (x,y))
            walkCount += 1
    elif Jumping:
        CorrerSCount = 0
        CorrerS.stop()
        screen.blit(Jump[walkCount//12], (x,y))
        walkCount += 1
    elif Falling:
        CorrerSCount = 0
        CorrerS.stop()
        screen.blit(Fall[walkCount//12], (x,y))
        walkCount += 1
    else:
        CorrerSCount = 0
        CorrerS.stop()
        CargarCCount = 0
        CargarC.stop()
        screen.blit(Stand[walkCount//6], (x,y))
        walkCount += 1
    pygame.display.update()
    
def execute_unix(inputcommand):
    p = subprocess.Popen(inputcommand, stdout = subprocess.PIPE,shell = True)
    (output,err) = p.communicate()
    return output
    
Lenguaje = 0
LineasEs = ["Hola soy Naruto","Me esforzare","Seré Hokage","Soy un Ninja"]
LineasEn = ["Hi I am Naruto","I will give my best","I will  be Hokage","I am Ninja"]
print("Seleccione un idioma\n")
print("1. Español\n")
print("2. English\n")
Lenguaje = int(input())
if(Lenguaje == 1):
    LineaS = ['espeak -ves+m1 -k5 -s150 -w L1.wav "%s" 2>>/dev/null' %LineasEs[0],
                      'espeak -ves+m1 -k5 -s150 -w L2.wav "%s" 2>>/dev/null' %LineasEs[1],
                      'espeak -ves+m1 -k5 -s150 -w L3.wav "%s" 2>>/dev/null' %LineasEs[2],
                      'espeak -ves+m1 -k5 -s150 -w L4.wav "%s" 2>>/dev/null' %LineasEs[3]]
else:
    LineaS = ['espeak -ves+m1 -k5 -s150 -w L1.wav "%s" 2>>/dev/null' %LineasEn[0],
                      'espeak -ves+m1 -k5 -s150 -w L2.wav "%s" 2>>/dev/null' %LineasEn[1],
                      'espeak -ves+m1 -k5 -s150 -w L3.wav "%s" 2>>/dev/null' %LineasEn[2],
                      'espeak -ves+m1 -k5 -s150 -w L4.wav "%s" 2>>/dev/null' %LineasEn[3]]
for i in range (4):
    execute_unix(LineaS[i])   

FrasesS = [ pygame.mixer.Sound('L1.wav'),
                   pygame.mixer.Sound('L2.wav'),
                    pygame.mixer.Sound('L3.wav'),
                    pygame.mixer.Sound('L4.wav')]



#Main loop
Music.play(-1)
notaltf4 = True
while (notaltf4):
    clock.tick(24)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            notaltf4 = False
            
    keys = pygame.key.get_pressed()
    
    # Moverse a la izquierda
    if keys[pygame.K_LEFT] and x > velN:
        if CorrerSCount == 0:
            CorrerS.play()
        if CorrerSCount < 11:
            CorrerSCount += 1
        else:
            CorrerS.stop()
            CorrerSCount = 0
        x -= velN
        left = True
        right = False
        trans = False
        Jumping = False
        Falling = False
    #Moverse a la derecha caminar
    elif keys[pygame.K_RIGHT] and x < 1920 - char_w - velN:
        if CorrerSCount == 0:
            CorrerS.play()
        if CorrerSCount < 11:
            CorrerSCount += 1
        else:
            CorrerS.stop()
            CorrerSCount = 0
        x += velN
        left = False
        right = True
        trans = False
        Jumping = False
        Falling = False
    # Se pone a cargar Chakra
    elif keys[pygame.K_t]:
        #Checa si es la primera vez que se presiona
        if BanderaWC:
            walkCount = 0
            BanderaWC = not(BanderaWC)
        #Sonido
        if CargarCCount == 0:
            CargarC.play()
        if CargarCCount < 63:
            CargarCCount += 1
        else:
            walkCount = 0
            CargarC.stop()
            CargarCCount = 0
            
        right = False
        left = False
        trans = True
        Jumping = False
        Falling = False
        
    elif keys[pygame.K_s]:
        if ChangeS == 0:
            FrasesS[randrange(0,3)].play()
        if ChangeS < 13:
            ChangeS += 1
        else:
            ChangeS = 0
        
    # No esta haciendo nada
    else:
        BanderaWC = True
        right = False
        left = False
        trans = False
        Jumping = False
        Falling = False
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            JumpS.play()
            isJump = True
            right = False
            left = False
            Jumping = False
            Falling = False
    else:  
        if jumpCount >= -10:
            left = False
            right = False
            trans = False
            Jumping = True
            Falling = False
            neg = 1
            if jumpCount < 0:
                left = False
                right = False
                trans = False
                Jumping = False
                Falling = True
                neg = -1
            y -= (jumpCount**2)*0.5*neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    
    Refresh()
Music.stop()
pygame.quit()
            