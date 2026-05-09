import pgzrun
import random

WIDTH = 640
HEIGHT = 480

score = 0

fish = Actor('sea3')
fish.pos = (320, 200)

shrimp = Actor('sea9')
shrimp.scale = 0.5
shrimp.pos = (400, 150)

def draw():
    screen.fill("steelblue")
    screen.draw.filled_rect(Rect((0, 400), (640, 80)), "tan")
    fish.draw()
    shrimp.draw()
    screen.draw.text("⭐: " + str(score), (10, 10), fontsize=30)
    if score >= 20:
        screen.draw.text("ПЕРЕМОГА!", (160, 200), fontsize=60, color="yellow")

def update():
    global score
    if keyboard.right:
        fish.x += 5
        fish.flip_x = True
    if keyboard.left:
        fish.x -= 5
        fish.flip_x = False
    if keyboard.up:
        fish.y -= 5
    if keyboard.down:
        fish.y += 5
    if fish.x < 50:  fish.x = 50
    if fish.x > 600: fish.x = 600
    if fish.y < 50:  fish.y = 50
    if fish.y > 360: fish.y = 360
    if fish.colliderect(shrimp):
        score += 1
        shrimp.x = random.randint(50, 580)
        shrimp.y = random.randint(50, 350)

pgzrun.go()
