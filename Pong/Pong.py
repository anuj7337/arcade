import pygame
from Paddle import paddle
from Ball import ball
pygame.init()
Black = (0,0,0)
White = (255,255,255)
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
icon=pygame.image.load("pongicon.png")
pygame.display.set_icon(icon)

paddle1 = paddle(White,10,100)
paddle1.rect.x = 25
paddle1.rect.y = 200

paddle2 = paddle(White,10,100)
paddle2.rect.x = 765
paddle2.rect.y = 200

ball = ball(White,10,10)
ball.rect.x = 349
ball.rect.y = 299

sprites = pygame.sprite.Group()
sprites.add(paddle1)
sprites.add(paddle2)
sprites.add(ball)

run = True
clock = pygame.time.Clock()

score1 = 0
score2 = 0

while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.moveUp(5)
    if keys[pygame.K_s]:
        paddle1.moveDown(5)
    if keys[pygame.K_UP]:
        paddle2.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddle2.moveDown(5)

    if ball.rect.x>=790:
        score1+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        score2+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>590:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<69:
        ball.velocity[1] = -ball.velocity[1]
    if pygame.sprite.collide_mask(ball, paddle1) or pygame.sprite.collide_mask(ball, paddle2):
        ball.bounce()
    
    sprites.update()
    screen.fill(Black)
    pygame.draw.line(screen, White, [398,0], [398,600], 5)
    pygame.draw.line(screen, White, [0,69] , [800,69], 5)
    sprites.draw(screen)
    font = pygame.font.Font(None, 74)
    text = font.render(str(score1), 1, White)
    screen.blit(text, (198,10))
    text = font.render(str(score2), 1, White)
    screen.blit(text, (596,10))
    pygame.display.flip()
    clock.tick(60)
    if score1 == 1 or score2 == 1:
        screen.fill(Black)
pygame.quit()
