import pygame

pygame.init()

displayList = pygame.display.get_desktop_sizes()
res = [1366, 728]

screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()
running = True
dt = 0

restart = False
diskCount = 10
delay = 0

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

def initHanoi(count: int):
    A = Stack("A")
    B = Stack("B")
    C = Stack("C")
    for i in range(count, 0, -1):
        A.push(i)
    return [A, B, C]

def TowerOfHanoi(n: int, source: Stack, destination: Stack, aux: Stack, delay: float = 1, counter: Counter = Counter()):
    if n == 0:
        return

    TowerOfHanoi(n-1, source, aux, destination, delay, counter)

    global running
    global restart
    if not running or restart:
        return

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
        y = 100
        width = 20
        height = 600

        rodRect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, "brown", rodRect)

        count = len(destination.data) + len(aux.data) + len(source.data)
        diskHeight = height / count
        diskWidth = 400

        if diskHeight > 50: diskHeight = 50

        yDisk = y + 600 - diskHeight
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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_r]:
        restart = True

    timeCount = 0
    while timeCount < delay:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        timeCount += clock.tick(60) / 1000

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            timeCount = 2
        if keys[pygame.K_ESCAPE]:
            running = False
        if keys[pygame.K_r]:
            restart = True
    # input()
    TowerOfHanoi(n-1, aux, destination, source, delay, counter)

Arr = initHanoi(diskCount)

print("Initial Condition")
print("A :", Arr[0].data)
print("B :", Arr[1].data)
print("C :", Arr[2].data, "\n")

# pygame setup
restart = True

while running:
    if restart:
        diskCount = int(input("Disk Count: "))
        delay = float(input("delay: "))

        Arr = initHanoi(diskCount)
        restart = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        pass
    if keys[pygame.K_ESCAPE]:
        running = False
    TowerOfHanoi(len(Arr[0].data), Arr[0], Arr[2], Arr[1], delay, Counter(),)

pygame.quit()
    

