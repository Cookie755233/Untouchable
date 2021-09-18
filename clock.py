import sys, pygame, random, time
from constants import WHITE, image_const

pygame.init()

size = width, height = 300, 200
screen = pygame.display.set_mode(size)

done = False

Black=0,0,0
White=255,255,255

Time = 0
Second = 0
Minute = 0
Hour = 0
Day = 0

numbers= ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
scale = (50,75)

tens = [pygame.transform.scale(image_const(num), scale) for num in numbers[0:6]]
singles = [pygame.transform.scale(image_const(num), scale) for num in numbers]


seconds_tens = [pygame.transform.scale(image_const(num), scale) for num in numbers[0:6]]
seconds_singles = [pygame.transform.scale(image_const(num), scale) for num in numbers]
minutes_tens = [pygame.transform.scale(image_const(num), scale) for num in numbers[0:6]]
minutes_singles = [pygame.transform.scale(image_const(num), scale) for num in numbers]
hours_tens = [pygame.transform.scale(image_const(num), scale) for num in numbers[0:6]]
hours_singles = [pygame.transform.scale(image_const(num), scale) for num in numbers]
colon = pygame.transform.scale(image_const('colon'), scale)

Clock = pygame.time.Clock()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    time.sleep(1)
    Second += 1
    
    screen.fill(WHITE)
    screen.blit(singles[Second%10-1], (170, 100))
    screen.blit(tens[(Second-1)//10], (150, 100))
    screen.blit(colon,(130,100))
    screen.blit(singles[Minute%10], (110, 100))
    screen.blit(tens[(Minute)//10], (90, 100))
    screen.blit(colon,(70,100))
    screen.blit(singles[Hour%10], (50, 100))
    screen.blit(tens[(Hour)//10], (30, 100))

    if Second == 60:
        Second = 0
        Minute=Minute+1
    if Minute == 60:
        Minute = 0
        Second = 0
        Hour=Hour+1
    if Hour==24:
        Hour=0
        Second = 0
        Minutes=0
        Day=Day+1

    pygame.display.flip()

    Clock.tick(60)

pygame.quit()