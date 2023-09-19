import pygame
import random
import math
from sys import exit
from random import randint, choice
class Player(pygame.sprite.Sprite):   #classe sprite para o player, sprite = surface ( imagem) e retângulos combinados
                                      # para usarmos a sprite precisamos colocá-las em um grupo ou em um GroupSingle
                                      # e esse grupo pode desenhar (draw) as sprites dentro dele e pode fazer um update das sprites
                                      # pygame tem dois tipos de grupo, um grupo (group) para múltiplos sprites ( um grupo grande que n vai interagir entre si)
                                      # já o groupsingle é um grupo para apenas uma sprite (perfeito para a classe Player)
    def __init__(self):
        super().__init__()
        macaco2 = pygame.image.load('macaco/macaco2.png').convert_alpha()  ### animações do macaco correndo
        macaco3 = pygame.image.load('macaco/macaco3.png').convert_alpha()
        macaco4 = pygame.image.load('macaco/macaco4.png').convert_alpha()
        macaco5 = pygame.image.load('macaco/macaco5.png').convert_alpha()
        macaco6 = pygame.image.load('macaco/macaco6.png').convert_alpha()
        macaco7 = pygame.image.load('macaco/macaco7.png').convert_alpha()
        self.player_walk = [macaco2, macaco3, macaco4, macaco5, macaco6, macaco7]  # colocar todos os frames dentro precisa usar (self) por que vamos acessar ele fora desse init
        self.player_jump = pygame.image.load('macaco/macacojump.png').convert_alpha()  # frame jump
        self.player_voando = pygame.image.load('macaco/macacovoando.png').convert_alpha() # frame voando
        self.player_desviar = pygame.image.load('macaco/desviar.png').convert_alpha() # frame desviar
        self.player_desviar = pygame.transform.scale2x(self.player_desviar)
        self.player_index = 0  # numero da imagem (frame) que vai aparecer no self image
        self.image = macaco2  # imagem incial
        self.rect = self.image.get_rect(topleft = (20, 400))  ## o retângulo da imagem
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound('sound/jump.mp3')
        self.lose_sound = pygame.mixer.Sound('sound/lose.mp3')
        self.jump_sound.set_volume(0.5)
    def player_controle(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.bottom < 400:  # verifica se a tecla w está sendo precionada e se o peronsgame está voando
                if keys[pygame.K_s]: # se eu aperto w ( estou pulando) e aperto s, minha gravidade começa a aumentar e meu personagem cai
                    self.gravity += 2
                else:  # caso o contrário
                     self.gravity = 2    # gravidade recebe dois  e meu personagem começa a cair devagar
                     self.image = self.player_voando   # imagem muda para o player_voando 
        if self.rect.bottom == 400:
            if jogador_pula:
                self.jump_sound.play()
                self.gravity = -15
        if 260 <= self.rect.bottom < 400:
            if jogador_pula:
                self.jump_sound.play()
                self.gravity = -14
    def apply_gravity(self):
        self.gravity += 1  # Incrementa o valor da variável gravity em 1. Isso aumenta a intensidade da força de gravidade aplicada ao objeto representado pela classe.
        self.rect.y += self.gravity   #Incrementa a posição vertical (y) do retângulo representado pelo player, # Isso faz com que o objeto se mova para baixo, simulando a queda devido à gravidade.
        if self.rect.bottom >= 400:  # verifica se o retângulo do player está abaixo do solo se n houver isso, o player cai para debaixo da terra, por causa do self.rect.y += self.gravity
            self.rect.bottom = 400  # se estiver ele vai para a posição do solo
    def animacao(self):   # animacao do macaco
        keys = pygame.key.get_pressed()
        if self.rect.bottom < 400 and not keys[pygame.K_w]:  ### macaco pulando ( quando tá pulando e eu n tou apertando w)
            self.image = self.player_jump
        elif keys[pygame.K_s] and not keys[pygame.K_w] :    ### macaco deitado
            self.image = self.player_desviar
            self.rect.y = 404 - self.image.get_height()
        if self.rect.bottom == 400:  ###animação do macaco correndo
            self.player_index += 0.2  ## acrescer o player_index 
            if self.player_index >= len(self.player_walk): # chegar se o index ainda está dentro da lista
                self.player_index = 0  #voltar para o index inicial
            self.image = self.player_walk[int(self.player_index)] # mudar o frame do macaco
    def update(self):
        self.player_controle()
        self.apply_gravity()
        self.animacao()
class Obstacle(pygame.sprite.Sprite):  ## classe de obstáculos
    def __init__(self,type):
        super().__init__()
        if type == 'passaro':
            passaro1 = pygame.image.load('passaro/passaro.png').convert_alpha()
            passaro2 = pygame.image.load('passaro/passaro1.png').convert_alpha()
            passaro3 = pygame.image.load('passaro/passaro2.png').convert_alpha()
            passaro1 = pygame.transform.scale2x(passaro1)
            passaro2 = pygame.transform.scale2x(passaro2)
            passaro3 = pygame.transform.scale2x(passaro3)
            self.frames = [passaro1, passaro2, passaro3]
            y_pos = 294
        if type == 'urso':
            urso1 = pygame.image.load('urso/ursofinal/urso1.png').convert_alpha()
            urso2 = pygame.image.load('urso/ursofinal/urso2.png').convert_alpha()
            urso3 = pygame.image.load('urso/ursofinal/urso3.png').convert_alpha()
            urso1 = pygame.transform.scale2x(urso1)
            urso2 = pygame.transform.scale2x(urso2)
            urso3 = pygame.transform.scale2x(urso3)
            self.frames = [urso1, urso2, urso3]
            y_pos = 313
        if type == 'passaro2':
            passaro1 = pygame.image.load('passaro/passaro.png').convert_alpha()
            passaro2 = pygame.image.load('passaro/passaro1.png').convert_alpha()  
            passaro3 = pygame.image.load('passaro/passaro2.png').convert_alpha()
            passaro1 = pygame.transform.scale2x(passaro1)
            passaro2 = pygame.transform.scale2x(passaro2)
            passaro3 = pygame.transform.scale2x(passaro3)
            self.frames = [passaro1, passaro2, passaro3]
            y_pos = 190
        if type == 'banana':
            banana = pygame.image.load('banana/banana.png').convert_alpha()
            banana1 = pygame.image.load('banana/banana1.png').convert_alpha()
            banana = pygame.transform.scale2x(banana)
            banana1 = pygame.transform.scale2x(banana1)
            self.frames = [banana, banana1]
            y_pos = 290
        if type == 'melancia':
            melanciama = pygame.image.load('melancia/melanciama.png').convert_alpha()
            melanciama2 = pygame.image.load('melancia/melanciama2.png').convert_alpha()
            melanciama = pygame.transform.scale2x(melanciama)
            melanciama2 = pygame.transform.scale2x(melanciama2)
            self.frames = [melanciama, melanciama2]
            y_pos = 294
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(topleft = (random.randint(900,1100),y_pos))   ## usando o random para gerar o obstaculo em x entre o intervalo 900, 1100
    def animacao(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]   
    def destroy(self):
        if self.rect.x <= -100:  ## destroir objetos que passam para fora da tela
            self.kill()
    def update(self):
        self.animacao()
        self.rect.x -= 6  # decrescendo o x para se movimentar na tela
        self.destroy()
def collision_sprite():   # colisão do macaco com o  grupo de obstáculos
    lose_sound = pygame.mixer.Sound('sound/lose.mp3')
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False): # pygame.sprite.spritecollide() retorna uma lista contendo os sprites colididos com um determinado sprite de referência.
        pygame.mixer.Channel(Ccanal_efeitos_sonoros2).play(lose_sound)
        obstacle_group.empty()
        obstacle_group2.empty()
        obstacle_group3.empty()
        obstacle_group4.empty()
        return 2
    return 1
class Banana(pygame.sprite.Sprite): ## bananas
    def __init__(self,type):
        super().__init__()
        if type == 'banana':
            bananaboa = pygame.image.load('banana/bananaboa.png').convert_alpha()
            bananaboa1 = pygame.image.load('banana/bananaboa1.png').convert_alpha()
            bananaboa = pygame.transform.scale2x(bananaboa)
            bananaboa1 = pygame.transform.scale2x(bananaboa1)
            self.frames = [bananaboa, bananaboa1]
            y_pos = 293
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(topleft = (random.randint(900,1100),y_pos))
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()
def collision2_sprite():  #colisão macaco e a banana boa
    coin_sound = pygame.mixer.Sound('sound/coin.mp3')
    collisions = pygame.sprite.spritecollide(player.sprite, obstacle_group2, False)  # pygame.sprite.spritecollide() retorna uma lista contendo os sprites colididos com um determinado sprite de referência
    for banana in collisions: # itero sobre os sprites colidos do grupo de banana(obstacle_group2)
        banana.kill()
        pygame.mixer.Channel(Ccanal_efeitos_sonoros3).play(coin_sound)
        
    return bool(collisions)
class Melancia(pygame.sprite.Sprite):  ##melancias
    def __init__(self,type):
        super().__init__()
        if type == 'melancia':
            melancia = pygame.image.load('melancia/melancia.png').convert_alpha()
            melancia1 = pygame.image.load('melancia/melancia1.png').convert_alpha()
            melancia = pygame.transform.scale2x(melancia)
            melancia1 = pygame.transform.scale2x(melancia1)
            self.frames = [melancia, melancia1]
            y_pos = 330
        if type == 'melancia2':
            melancia = pygame.image.load('melancia/melancia.png').convert_alpha()
            melancia1 = pygame.image.load('melancia/melancia1.png').convert_alpha()
            melancia = pygame.transform.scale2x(melancia)
            melancia1 = pygame.transform.scale2x(melancia1)
            self.frames = [melancia, melancia1]
            y_pos = 230
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(topleft = (random.randint(900,1100),y_pos))
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()
def collision3_sprite(): # colisão macaco e melancia
    coin_sound = pygame.mixer.Sound('sound/coin.mp3')  # false, os sprits colididos n seram removidos após a colisão.
    collisions = pygame.sprite.spritecollide(player.sprite, obstacle_group3, False) #pygame.sprite.spritecollide() retorna uma lista contendo os sprites colididos com um determinado sprite de referência
    for melancia in collisions: # itero sobre os sprites colidos
        melancia.kill()
        pygame.mixer.Channel(Ccanal_efeitos_sonoros).play(coin_sound)
    return bool(collisions)
class Neve(pygame.sprite.Sprite): # bola de neve 
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('neve/neve.png').convert_alpha()
        for i in player:
            x = i.rect.x
            y = i.rect.y
            y_pos = y
        self.rect = self.image.get_rect(topleft = (30 ,y_pos))
    def update(self):
        self.rect.x += 6
        if self.rect.x >= WIDTH + 200:   # se a posição da bola estiver muito a esquerda, ela some, para n lagar o jogo
            self.kill
def collision4_sprite(): # colisão bola de neve e obstaculos
    killsound = pygame.mixer.Sound('sound/kill.mp3')
    collisions = pygame.sprite.groupcollide(obstacle_group4, obstacle_group, True, True)  # A função pygame.sprite.groupcollide() é usada para verificar colisões entre dois grupos de sprites.
    if collisions:
        pygame.mixer.Channel(Ccanal_efeitos_sonoros6).play(killsound)
        
    return bool(collisions)

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Macaco do Ártico")
Clock = pygame.time.Clock()
jogo_ativo = 0 # condição para o jogo iniciar
player = pygame.sprite.GroupSingle()  # criação do gruposingle para a sprite do player
player.add(Player()) # adicionando a instância da classe Player ao grupo  
obstacle_group = pygame.sprite.Group()  #   grupo dos obstaculos, mas n podemos adicionar os obstaculos no grupo agora, somente quando o timer começar
obstacle_group2 = pygame.sprite.Group() #   grupo de bananas, mas n podemos adicionar os obstaculos no grupo agora, somente quando o timer começar
obstacle_group3 = pygame.sprite.Group() #   grupo dos melancias, mas n podemos adicionar os obstaculos no grupo agora, somente quando o timer começar
obstacle_group4 = pygame.sprite.Group() #   grupo  de bolas de neve
# carregar imagens
telainicial = pygame.image.load('telainicial/background.png').convert_alpha()
bg = pygame.image.load('fundo/bg.png').convert_alpha()
telainicial = pygame.transform.scale(telainicial, (800, 400))
score1 = pygame.image.load('score/score.png').convert_alpha()
boladeneve = pygame.image.load('neve/neve.png').convert_alpha()
boladeneve = pygame.transform.scale2x(boladeneve)   
Ccanal_efeitos_sonoros = 1
Ccanal_efeitos_sonoros2 = 2
Ccanal_efeitos_sonoros3 = 3
Ccanal_efeitos_sonoros4 = 4
Ccanal_efeitos_sonoros5 = 5
Ccanal_efeitos_sonoros6 = 6
Ccanal_efeitos_sonoros7 = 7


#intro do jogo
jogar = pygame.image.load('telainicial/JOGAR.png').convert_alpha()
sair = pygame.image.load('telainicial/SAIR.png').convert_alpha()
background = pygame.image.load('telainicial/background.png').convert_alpha()
jogar = pygame.transform.scale2x(jogar)
sair = pygame.transform.scale2x(sair)
# gameover
gameover = pygame.image.load('gameover/gameover.png').convert_alpha()
gameover = pygame.transform.scale(gameover, (800, 400))
gameovermsg = pygame.image.load('gameover/gameovermsg.png').convert_alpha()
gameovermsg = pygame.transform.scale2x(gameovermsg)
menu = pygame.image.load('gameover/MENU.png').convert_alpha()
novamente = pygame.image.load('gameover/novamente.png').convert_alpha()
novamente = pygame.transform.scale2x(novamente)
SCORE = pygame.image.load('gameover/SCORE.png').convert_alpha()
SCORE = pygame.transform.scale2x(SCORE)
HEIGHT = 400
WIDTH = 800
background_width = bg.get_width()
bg = pygame.transform.scale(bg, (background_width, HEIGHT))
bg_rect = bg.get_rect()
scroll = 0
panels = math.ceil(WIDTH / background_width) + 2
# retângulo dos itens do gameover
menu_rect = menu.get_rect(topleft = (320, 260))
menu_rect2 = menu.get_rect(topleft = (311, 260))
novamente_rect = novamente.get_rect(topleft = (250, 200))
# retângulo itens do iniciar/menu
jogar_rect = jogar.get_rect(topleft = (310, 190))
sair_rect = sair.get_rect(topleft = (317, 270))
contadorbolas1 = 0
# timer
obstacle_timer = pygame.USEREVENT + 1  # melhor spawn de obstáculos adicionar +1 para n dar conflito com os eventos do pygame ( custom user event)
dificuldade = 1150  
pygame.time.set_timer(obstacle_timer,dificuldade) #aumenta a dificuldade ( executar o evento custom do obstacle_timer em um certo intervalo) (evento que quero executar, e quantas vezes quero executar em milisegundos)

# menu de pause
pause = pygame.image.load('pause/pause.png').convert_alpha()
voltar = pygame.image.load('pause/voltar.png').convert_alpha()
voltar = pygame.transform.scale2x(voltar)
voltar_rect = voltar.get_rect(topleft = (287, 170))

#level
level = pygame.image.load('score/level.png').convert_alpha()




contador = 0
valor = 0
reserva = 0
reserva2 = 0
monkeysound = pygame.mixer.Sound('sound/monkey.mp3')
snowball = pygame.mixer.Sound('sound/snowball.mp3')
fatality = pygame.mixer.Sound('sound/fatality.mp3')
fonte_contador = pygame.font.Font(None, 45)
contadorbolas = False
pygame.mixer.music.load('sound/background.mp3')
pygame.mixer_music.play(-1)
pygame.mixer.music.set_volume(0.1)
levelcont = 1

while True: 
    if jogo_ativo ==1:
        for i in range(panels):  # loop no background
            screen.blit(bg, (i * background_width + scroll - background_width, 0))
        scroll -= 5 
        if abs(scroll) > background_width:
            scroll = 0
    jogador_pula = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if jogo_ativo == 1:
            if event.type == pygame.KEYDOWN: 
                if contadorbolas1 <= 1:
                    if event.key == pygame.K_d and contadorbolas == True:  ### adicionar as bolas de neves ao apertar a tecla d
                        obstacle_group4.add(Neve())
                        contadorbolas1 += 1
                        ## adicionando a bola de neve ao grupo de obstaculos4
                        pygame.mixer.Channel(Ccanal_efeitos_sonoros3).play(snowball)
                else:
                    contadorbolas = False
                    contadorbolas1 = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jogador_pula = True
        if jogo_ativo == 0:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  #reiniciar o jogo depois de perder apertando espaço
                jogo_ativo = 1
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if jogar_rect.collidepoint(event.pos):
                        jogo_ativo = 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if sair_rect.collidepoint(event.pos):
                        pygame.quit()
                        exit()
        if jogo_ativo == 2:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  #reiniciar o jogo depois de perder apertando espaço
                jogo_ativo = 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                 if menu_rect.collidepoint(event.pos):
                     jogo_ativo = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if novamente_rect.collidepoint(event.pos):
                    jogo_ativo = 1
        if event.type == pygame.KEYDOWN:  ### inciair tela pause
            if event.key == pygame.K_ESCAPE:
                if jogo_ativo == 1:
                    jogo_ativo = 3
                elif jogo_ativo == 3:
                    jogo_ativo = 1
        if jogo_ativo == 3:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_rect.collidepoint(event.pos):
                    jogo_ativo = 0
                    obstacle_group.empty()
                    obstacle_group2.empty()
                    obstacle_group3.empty()
                    obstacle_group4.empty()  #### limpando o grupo de obstáculos para os obstaculos n continuarem no mesmo lugar
            if event.type == pygame.MOUSEBUTTONDOWN:
                if voltar_rect.collidepoint(event.pos):
                    jogo_ativo = 1

                      
        if jogo_ativo == 1:  ## todo vez que o meu timer é executado, eu adiciono uma sprite dentro do grupo
            if event.type == obstacle_timer: ## adicionar os sprites ao obstacle_group quando o timer começa ## executar o evento customizado
                obstacle_group2.add(Banana(choice(['banana'])))    ## choice para pegar um item aleatório da lista, sempre que chamamos o obstacle, o choice vai escolher 1 item random da lista
                obstacle_group.add(Obstacle(choice(['passaro','urso','passaro2','banana','melancia'])))
                obstacle_group3.add(Melancia(choice(['melancia', 'melancia2'])))
    if jogo_ativo == 1:
        contadorbolas == False
        if contadorbolas == True:
            screen.blit(boladeneve, (700, 5))
                        
        player.draw(screen)  #mostrar o gruposingle Player na tela que possui a Sprite 
        player.update()  # update player
        obstacle_group4.update()  ## neve
        obstacle_group4.draw(screen) ##update neve
        obstacle_group3.update() ## melancia 
        obstacle_group3.draw(screen)# update melancia
        obstacle_group2.update()# banana
        obstacle_group2.draw(screen) # update banana
        obstacle_group.draw(screen) # obstaculos    
        obstacle_group.update() # update obstaculos
        screen.blit(score1, (0,0))
        screen.blit(level, (0,80))
        jogo_ativo = collision_sprite()
        if (collision2_sprite()): # colisão entre macaco e banana
            contador += 1
            valor = int(contador)
            reserva = valor
            reserva2 += 1
            if valor % 10 == 0:
                pygame.mixer.Channel(Ccanal_efeitos_sonoros5).play(monkeysound)
        if (collision3_sprite()):   # colisão com a melanciaboa
            contador += 5
            valor = int(contador)
            reserva = valor
            reserva2 += 1
            contadorbolas = True
            if valor % 10 == 0:
                pygame.mixer.Channel(Ccanal_efeitos_sonoros5).play(monkeysound)
        if collision4_sprite(): # colisão entre bola de neve e obstáculos
            contador += 20
            valor = int(contador)
            reserva = valor
            reserva2 += 1
        if reserva2 == 20:
            pygame.mixer.Channel(Ccanal_efeitos_sonoros7).play(fatality)
            if dificuldade > 400:
                dificuldade -= 10
                levelcont += 1
                pygame.time.set_timer(obstacle_timer,dificuldade)
                reserva2 = 0
            else:
                dificuldade == 400
        print(dificuldade)
        print(reserva2)
        print(levelcont)


        
        contador_texto = fonte_contador.render(f' {valor}', True, (255, 255, 255))
        screen.blit(contador_texto, (140, 24))
        contador_texto3 = fonte_contador.render(f' {levelcont}', True, (0, 0, 0))
        screen.blit(contador_texto3, (98, 87))

            
    if jogo_ativo == 0:
        contadorbolas1 = 0
        levelcont = 1
        reserva2 = 0
        dificuldade = 1150
        valor = 0
        contador = 0
        contadorbolas = False
        screen.blit(telainicial,(0,0))
        screen.blit(jogar, jogar_rect)
        screen.blit(sair, sair_rect)
    if jogo_ativo == 2:
        contadorbolas1 = 0
        levelcont = 1
        dificuldade = 1150
        contadorbolas = False
        screen.blit(gameover,(0,0))
        screen.blit(gameovermsg,(240,10))
        screen.blit(menu, menu_rect)
        screen.blit(novamente, novamente_rect)
        fonte_contador2 = pygame.font.Font(None, 70)
        contador_texto2 = fonte_contador2.render(f' {reserva}', True, (0, 0, 128))
        screen.blit(contador_texto2, (520, 350))
        screen.blit(SCORE,(240,300))
        valor = 0
        contador = 0
        reserva2 = 0
    if jogo_ativo == 3:
        screen.blit(pause,(0,0))
        screen.blit(menu, menu_rect2)
        screen.blit(voltar, voltar_rect)
        




    FPS = 60
    pygame.display.update()
    Clock.tick(FPS)