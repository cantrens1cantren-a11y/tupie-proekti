
import pygame
import random



pygame.init()

W = 450
H = 650
FPS = 100
sc = pygame.display.set_mode((W,H)) #экран


def ggame():


    score = 0

    hounou = pygame.mixer.Sound("sounds\hou nou.mp3")
    ballsound = pygame.mixer.Sound("sounds\ga.mp3")
    hounou.set_volume(0.09)


    clock = pygame.time.Clock()
    pygame.display.set_caption("Python File")




    class Ball: #класс мяча
        def __init__(self,bx,by):
            self.bx = bx
            self.by = by
            self.bw = 150
            self.bh = 400
            self.y_speed = 2
            self.x_speed = 2
            self.dir_x = random.choice([-1,0,1,])
            self.dir_y = 1

        def drw_ball(self):# отрисовка мяча
            pygame.draw.circle(sc, 'Black', (self.bx, self.by,), 20)

        def move_ball(self): # движение мяча
            self.by += self.y_speed * self.dir_y
            self.bx += self.x_speed * self.dir_x
            if self.bx == W:
                self.dir_x = -1
                ballsound.play()

            if self.bx == 0:
                self.dir_x = 1
                ballsound.play()




    class Player: #класс платформы
        def __init__(self,x,y,):
            self.x = x
            self.y = y
            self.w = 100
            self.h = 10
            self.x_speed = 0

        def draw(self):
            pygame.draw.rect(sc,'Blue',(self.x,self.y,self.w,self.h))




        def update(self):
             #self.x -= 1
             self.x += self.x_speed
             if self.x > W - self.w:
                 self.x = 450 - self.w



             if self.x < 0:
                 self.x = 0


    player = Player(155,570)
    ball = Ball(200,80)


    game_over = False
    running = True
    while running: #Главный цикл
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.x_speed = -5
                if event.key == pygame.K_d:
                    player.x_speed = 5
                if event.key == pygame.K_F4:
                    if game_over:
                        ggame()
                        game_over = False


        font = pygame.font.SysFont('Comic Sans MS', 50)
        text_surface = font.render(f'счет : {score} ', True, (0, 0, 0))



        sc.fill((255, 255, 255))

        sc.blit(text_surface, (W // 2 - text_surface.get_width() // 2, 10))

        player.draw()
        if not game_over:

            player.update()

        ball.drw_ball()
        ball.move_ball()


        if game_over:
            overlay = pygame.Surface((W, H))
            overlay.set_alpha(180)
            overlay.fill((0, 0, 0))
            sc.blit(overlay, (0, 0))
            text_surface77 = font.render(f'Game over ', True, (255, 255, 255))
            text_surface778 = font.render(f'f4 перезапуск ', True, (255, 255, 255))
            sc.blit(text_surface778, (W // 2 - text_surface778.get_width() // 2, H // 2))
            sc.blit(text_surface77, (W // 2 - text_surface77.get_width() // 2, H // 3))
            hounou.play()

        #чтобы игрок не выходил за границы
        ball_hb = pygame.Rect(ball.bx,ball.by,20,20)
        player_hb = pygame.Rect(player.x,player.y,100,10)
        if ball_hb.colliderect(player_hb):
            ball.dir_y= -1
            score += 1
            ball.dir_x = random.choice([-1,0,1])
            ballsound.play()
            if score > 0 and score % 5 == 0:
                ball.y_speed += 0.2
                print(ball.y_speed)
        if ball.by <= 0:
            ball.dir_y = 1
            ballsound.play()

        if ball.by >= 650:
            game_over = True
        clock.tick(FPS)
        pygame.display.flip()



ggame()








