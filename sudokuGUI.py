import pygame

pygame.init()
pygame.font.init()

sdk= [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]


WIDTH,HEIGHT=450,450
WIND= pygame.display.set_mode((WIDTH, HEIGHT))
ROWS, COLS=9,9
BLOCKSZ= WIDTH//COLS
FPS=60
WHITE = (255, 255, 255)
BLACK=(0, 0, 0)
BLUE=(0,0,128)
WIND.fill(WHITE)


pygame.display.set_caption('SUDOKU')
def drawgrd(sdk):
    fontt= pygame.font.SysFont("comicsans", 40)
    for i in range(9):
        for j in range(9):
            if (sdk[i][j]!=0):
                text1 = fontt.render(str(sdk[i][j]), 1, (0, 0, 0))
                WIND.blit(text1, (i*BLOCKSZ+15, j*BLOCKSZ+15))

    for x in range(WIDTH):
        for y in range(HEIGHT):
            bx=pygame.Rect(x*WIDTH,y*HEIGHT,BLOCKSZ,BLOCKSZ)
            pygame.draw.rect(WIND,(255,0,0),pygame.Rect(x*BLOCKSZ,y*BLOCKSZ,BLOCKSZ,BLOCKSZ),2)
            pygame.display.flip()

#def drawnew(m):
 #   fnt = pygame.font.SysFont("comicsans", 40)
    
 #   gap = WIDTH / 9
 #   x = COLS * gap
 #   y = ROWS* gap

 #   pygame.draw.rect(WIND, (255, 255, 255), (x, y, gap, gap), 2)

 #   text = fnt.render(str(m), 1, (0, 0, 128))
 #   WIND.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))


##-----------------------------------------SUDOKU BACKTRACK SOLVING-----------------------------------
def emtsq(sudobrd):
    for i in range(len(sudobrd)):
        for j in range(len(sudobrd[0])):
            if sudobrd[i][j]==0:
                return (i,j)

def isval(nu,sudobrd,pos):
    for j in range(len(sudobrd[0])):
        if(nu==sudobrd[pos[0]][j] and pos[1]!=j):
            return False
    for i in range(len(sudobrd)):
        if(sudobrd[i][pos[1]]==nu and pos[0]!=i):
            return False
    bx= pos[1]//3
    by=pos[0]//3          #in matrix we have 00, 01 and so on, so second one is x loc and first digit is y, just like that we consider these 3 by 3 boxes as one, so whole matrix of 3*3, and therefore 1st box would be 0,0 and so
    # say element is at  1,4, so bx=4//3 =1, by=1//3=0, therefore box 0,1 which is 2nd box 
    for k in range(by*3,by*3+3):
        for l in range(bx*3,bx*3+3):
            if(sudobrd[k][l]==nu and k!=pos[0] and l!=pos[1]):
                return False
    return True

def sudokusol(sudobrd):
    emp=emtsq(sudobrd)
    #print("here")
    if not emp:
        drawgrd(sdk)  #final
        return True
    else:
        i,j=emp
    
    for m in range(1,10):
        if isval(m,sudobrd,emp):
            sudobrd[i][j]=m
            fontt= pygame.font.SysFont("comicsans", 40)
            for a in range(9):
                for b in range(9):
                    if (sdk[a][b]!=0):
                        text1 = fontt.render(str(sdk[a][b]), 1, (0, 0, 0))
                        WIND.blit(text1, (a*BLOCKSZ+15, b*BLOCKSZ+15))
            fnt = pygame.font.SysFont("comicsans", 40)
            text = fnt.render(str(m), 1, (255, 255, 0))
            WIND.blit(text, (i*BLOCKSZ+15, j*BLOCKSZ+15))
            bx=pygame.Rect(i*WIDTH,j*HEIGHT,BLOCKSZ,BLOCKSZ)
            pygame.draw.rect(WIND,(255,255,0),pygame.Rect(i*BLOCKSZ,j*BLOCKSZ,BLOCKSZ,BLOCKSZ),2)
            pygame.time.delay(1)
            pygame.display.flip()
            #drawnew(m)
            if sudokusol(sudobrd):
                return True
            else: 
                sudobrd[i][j]=0
                WIND.fill((255, 255, 255))
    return False

#-------------------------------------------------------------------------------------------------------


def main():
    run=True
    clock=pygame.time.Clock()
    while run:
        sudokusol(sdk)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
    pygame.quit() 
main() 