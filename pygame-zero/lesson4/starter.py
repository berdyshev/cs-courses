import pgzrun

WIDTH = 640
HEIGHT = 480

speed = 5

fish = Actor('sea3')
fish.pos = (320, 200)

def draw():
    screen.fill("steelblue")
    screen.draw.filled_rect(Rect((0, 400), (640, 80)), "tan")
    fish.draw()

def update():
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

    if fish.x < 50:   fish.x = 50
    if fish.x > 600: fish.x = 600
    if fish.y < 50:   fish.y = 50
    if fish.y > 360: fish.y = 360

pgzrun.go()