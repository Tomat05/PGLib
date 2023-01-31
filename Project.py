from PgLib import *

WIDTH, HEIGHT = 1920, 1080
GRAVITY = 450

playerPos = vector((WIDTH / 2) - 100, HEIGHT - 60)

ballPos = vector(WIDTH / 2, 50)
ballVel = vector(random(-250, 250), 1)

# Called once at the start
def setup():
    createWindow(WIDTH, HEIGHT)

def updatePlayer():
    global playerPos
    if getKey("A") and playerPos.x > 0:
        playerPos.set(playerPos.x - 500 * deltaTime(), playerPos.y)
    elif getKey("D") and playerPos.x < WIDTH - 200:
        playerPos.set(playerPos.x + 500 * deltaTime(), playerPos.y)

def updateBall():
    global ballPos, ballVel

    ballVel.set(ballVel.x, ballVel.y + GRAVITY * deltaTime())
    ballPos.set(ballPos.x + ballVel.x * deltaTime(), ballPos.y + ballVel.y * deltaTime())

    if ballPos.x >= WIDTH:
        ballPos.set(WIDTH, ballPos.y)
        ballVel.set(-ballVel.x, ballVel.y)
    elif ballPos.x <= 0:
        ballPos.set(0, ballPos.y)
        ballVel.set(-ballVel.x, ballVel.y)

    if ballPos.x >= playerPos.x and ballPos.x <= playerPos.x + 200 and ballPos.y >= playerPos.y:
        ballPos.set(ballPos.x, playerPos.y)
        ballVel.set(ballVel.x + random(-125, 125), -ballVel.y)

    if ballPos.y >= HEIGHT:
        quit()


# Called every frame
def update():
    background(0, 0, 0)

    updatePlayer()
    updateBall()

    circle(ballPos.x, ballPos.y, 20, colour(0, 0, 255))

    rect(playerPos.x, playerPos.y, 200, 30, colour(255, 255, 255))