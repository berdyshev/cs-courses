import pgzrun
import random

WIDTH = 640
HEIGHT = 480

speed = 5

fish = Actor('sea3')
shrimp = Actor('sea9')
shrimp.scale = 0.5
jellyfish = Actor('sea5')

def init():
    global timer, score, game_over
    timer = 30
    score = 0
    game_over = False
    fish.pos = (320, 200)
    shrimp.pos = (400, 150)
    jellyfish.pos = (600, 180)

init()

def draw():
    screen.fill("steelblue")
    screen.draw.filled_rect(Rect((0, 400), (640, 80)), "tan")

    if game_over:
        if score >= 20:
            screen.draw.text("ПЕРЕМОГА!", center=(320, 200), fontsize=60, color="yellow")
        else:
            screen.draw.text("GAME OVER", center=(320, 200), fontsize=60, color="orangered")
        screen.draw.text("Очки: " + str(score), center=(320, 260), fontsize=40)
        return

    fish.draw()
    shrimp.draw()
    jellyfish.draw()
    screen.draw.text("⭐: " + str(score), (10, 10), fontsize=30)

def update():
    global score, game_over

    if game_over:
        return

    if keyboard.right:
        fish.x += speed
        fish.flip_x = True
    if keyboard.left:
        fish.x -= speed
        fish.flip_x = False
    if keyboard.up:
        fish.y -= speed
    if keyboard.down:
        fish.y += speed

    if fish.x < 0:   fish.x = 0
    if fish.x > 640: fish.x = 640
    if fish.y < 0:   fish.y = 0
    if fish.y > 360: fish.y = 360

    if fish.colliderect(shrimp):
        score += 1
        shrimp.x = random.randint(50, 580)
        shrimp.y = random.randint(50, 350)

    jellyfish.x -= 2
    if jellyfish.x < -50:
        jellyfish.x = 690

    if fish.colliderect(jellyfish):
        game_over = True

    if score >= 20:
        game_over = True

pgzrun.go()
