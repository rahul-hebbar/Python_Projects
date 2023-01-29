import pygame as py
import time
import random

red = (255,0,0)
black = (0,0,0)
col = (0,255,255)
white = (255,255,255)

py.init()
disp = py.display.set_mode((800,600))
py.display.set_caption("Slither")
py.display.update()

font = py.font.SysFont(None,25)

clock = py.time.Clock()

def print_text(msg,color):
    screen_text = font.render(msg,True,color)
    disp.blit(screen_text,[100,100])
#    py.display.update()

def gamestart():
    g_start = True
    while g_start:
        disp.fill(white)
        print_text("To start press s",red)
        py.display.update()
        
        for event in py.event.get():
            if event.type == py.QUIT:
                g_start = False
            if event.type == py.KEYDOWN:
                if event.key == py.K_s:
                    gameLoop()
    py.quit()
    quit()
    
def gameend():
    g_end = True
    while g_end: 
        disp.fill(white)
        print_text("Game Over, c to restart and q to quit",black)
        py.display.update()
                
        for event in py.event.get():
            if event.type == py.QUIT:
                g_end = False
            if event.type == py.KEYDOWN:
                if event.key == py.K_q:
                    py.quit()
                    quit()
                elif event.key == py.K_c:
                    gameLoop()
    py.quit()
    quit()
                        
def gameLoop():
    g_exit = False
    lead_x = 400
    lead_y = 300
    lead_x_change = 0
    lead_y_change = 1
    randX = round(random.randrange(0,790)//10)*10
    randY = round(random.randrange(0,590)//10)*10
    while not g_exit:                   
        for event in py.event.get():
            if event.type == py.QUIT:
                g_exit = True
            if event.type == py.KEYDOWN:
                if event.key == py.K_LEFT:
                    lead_x_change = -1
                    lead_y_change = 0
                elif event.key == py.K_RIGHT:
                    lead_x_change = 1
                    lead_y_change = 0
                elif event.key == py.K_UP:
                    lead_y_change = -1
                    lead_x_change = 0
                elif event.key == py.K_DOWN:
                    lead_y_change = 1
                    lead_x_change = 0
    #        if event.type == py.KEYUP:
    #            if event.key == py.K_LEFT or event.key == py.K_RIGHT:
    #                lead_x_change = 0
        if lead_x >= 800 or lead_x < 0 or lead_y >=600 or lead_y < 0:
            gameend()
        if randX<lead_x<randX+10 and randY<lead_y<randY+10:
            randX = round(int(random.randrange(0,790))/10)*10
            randY = round(int(random.randrange(0,590))/10)*10
        lead_x += lead_x_change
        lead_y += lead_y_change
        disp.fill(red)
        disp.fill(black,rect = [lead_x,lead_y,10,10])
        disp.fill(col,rect = [randX,randY,10,10])
        py.display.update()
        clock.tick(100)

#    print_text("Game over",white)
#    py.display.update() 
#    time.sleep(2)
    py.quit()
    quit()
   
gamestart()
