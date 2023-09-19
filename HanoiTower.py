import pygame
import sys

pygame.init()

displayList = pygame.display.get_desktop_sizes()

screen = pygame.display.set_mode(displayList[0])
clock = pygame.time.Clock()
running = True
dt = 0

pygame.display.flip()
class Counter:
    def __init__(self):
        self.value = 0
    def add(self, value):
        self.value += value
    def reset(self):
        self.value = 0

class Stack:
    def __init__(self, name = "Stack Default"):
        self.data = []
        self.name = name
    def push(self, value):
        self.data.append(value)
    def pop(self):
        return self.data.pop()

def KeyByName(stack: Stack):
    value = 0
    multiplier = 10**len(stack.name)
    for e in stack.name:
        value += ord(e) * multiplier
        multiplier /= 10
    return value

def TowerOfHanoi(n: int, source: Stack, destination: Stack, aux: Stack, counter: Counter):
    if n == 0:
        return

    TowerOfHanoi(n-1, source, aux, destination, counter)

    StackList = [source, destination, aux]
    StackList.sort(key=KeyByName)

    destination.push(source.pop())
    counter.add(1)
    print("Step:", counter.value)
    print("moving Disk", n, "from", source.name, "to", destination.name)

    for e in StackList:
        print(e.name, ":", e.data)
    print()

    clock.tick(60)

    screen.fill("white")

    pos = 350
    for i in range(3):
        x = pos - 50
        y = 200
        width = 20
        height = 600

        rodRect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, "brown", rodRect)

        count = len(destination.data) + len(aux.data) + len(source.data)
        diskHeight = height / count
        diskWidth = 400

        yDisk = 800 - diskHeight
        xDisk = x

        color = ["red", "green", "blue"]

        for e in StackList[i].data:
            scaled = e / count * diskWidth + 40
            diskRect = pygame.Rect(pygame.Rect(xDisk, yDisk, scaled, diskHeight))
            diskRect.center = rodRect.center
            diskRect.y = yDisk
            pygame.draw.rect(screen, color[e % 3], diskRect)
            yDisk -= diskHeight
        pos += 400
    pygame.display.flip()
    timeCount = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    while timeCount < 0.3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        timeCount += clock.tick(60) / 1000

        if keys[pygame.K_SPACE]:
            timeCount = 2
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
    # input()
    TowerOfHanoi(n-1, aux, destination, source, counter)

A = Stack("A")
B = Stack("B")
C = Stack("C")

for i in range(10, 0, -1):
    A.push(i)

print("Initial Condition")
print("A :", A.data)
print("B :", B.data)
print("C :", C.data, "\n")

# pygame setup

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    TowerOfHanoi(len(A.data), A, C, B, Counter())

pygame.quit()

