# Cài đặt pygame
import pygame, sys, os, random

# Tạo hàm cho trò chơi
def draw_floor():
    screen.blit(floor, (floor_x_pos,650))         # chèn hình vào
    screen.blit(floor, (floor_x_pos + 432,650))         # chèn hình vào

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (500, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop = (500, random_pipe_pos - 650))
    return bottom_pipe, top_pipe

def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5   # di chuyển ống về bên trái
    return pipes    # trả về list ống đã dịch

def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)    # lật trục nào để true trục đó (x,y)
            screen.blit(flip_pipe, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):     # va chạm xảy ra
            hit_sound.play()
            return False
    if bird_rect.top <= -75 or bird_rect.bottom >= 650:
        return False        
    return True

def rotate_bird(bird1):
    new_bird = pygame.transform.rotozoom(bird1, -bird_movement*2.5, 1)
    return new_bird

def bird_animation():
    new_bird = bird_list[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100, bird_rect.centery))
    return new_bird, new_bird_rect

def score_display(game_state):
    if game_state == 'main game':
        score_surface = game_font.render(f"Score: {int(score)}", True, (255,255,255))
        score_rect = score_surface.get_rect(center = (216, 100))
        screen.blit(score_surface, score_rect)
    elif game_state == 'game_over':
        score_surface = game_font.render(f"Score: {int(score)}", True, (255,255,255))
        score_rect = score_surface.get_rect(center = (216, 100))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f"High score: {int(high_score)}", True, (255,255,255))
        high_score_rect = score_surface.get_rect(center = (216, 630))
        screen.blit(high_score_surface, high_score_rect)

def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

os.chdir(r"C:\Users\DELL\Documents\Python3\Pygame_Intro")
# Khởi tạo
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512) # tiền khởi tạo âm thanh, căn chỉnh phù hợp giảm độ trễ so với code
pygame.init()
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock()     # tan so quet fps
game_font = pygame.font.Font('04B_19.ttf', 40)

# Tạo biến cho trò chơi
gravity = 0.25
bird_movement = 0
game_active = True  # thắng thua
score = 0
high_score = 0

# Chèn bg
bg = pygame.image.load('assets/background-night.png').convert()
bg = pygame.transform.scale2x(bg)
# Chèn sàn
floor = pygame.image.load('assets/floor.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
# Tạo chim
bird_down = pygame.transform.scale2x(pygame.image.load('assets/yellowbird-downflap.png').convert_alpha())
bird_mid = pygame.transform.scale2x(pygame.image.load('assets/yellowbird-midflap.png').convert_alpha())
bird_up = pygame.transform.scale2x(pygame.image.load('assets/yellowbird-upflap.png').convert_alpha())
# bird = pygame.image.load('assets/yellowbird-midflap.png').convert_alpha()   # do dùng rotozoom nên đổi thành alpha
bird_list = [bird_down, bird_mid, bird_up]
bird_index = 2
bird = bird_list[bird_index]
bird_rect = bird.get_rect(center = (100, 384))

# Tạo timer cho bird
birdflap = pygame.USEREVENT + 1 # event thứ 2 cho chim
pygame.time.set_timer(birdflap, 200)    # sau 200s đập cánh   

# Tạo ống
pipe_surface = pygame.image.load('assets/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
# Tạo timer
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)  # sau 1200ms tạo ống mới
pipe_height = [200, 300, 400]
# Tạo màn hình kết thúc
game_over_surface = pygame.transform.scale2x(pygame.image.load('assets/message.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center = (216, 384))
# Chèn âm thanh
flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
hit_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
score_sound_countdown = 100
# Vòng lặp trò chơi
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()               # sự kiện là QUIT => gọi hàm quit
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement =- 8
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True 
                pipe_list.clear()
                bird_rect.center = (100,384)
                bird_movement = 0
                score = 0
        if event.type == spawnpipe:
            pipe_list.extend(create_pipe()) # tạo ống mới
        if event.type == birdflap:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
            bird, bird_rect = bird_animation()
    screen.blit(bg, (0,0))         # chèn hình vào
    if game_active:
        # chim
        bird_movement += gravity
        rotated_bird = rotate_bird(bird)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)       # chèn hình chữ nhật
        game_active = check_collision(pipe_list)
        # ống
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        score += 0.01
        score_display('main game')
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100
    else:
        screen.blit(game_over_surface, game_over_rect)
        high_score = update_score(score, high_score)
        score_display('game_over')
    # sàn
    floor_x_pos -= 1            # cho hình lùi lại
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)