# import pygame
#
# # pygame setup
# pygame.init()
#
# displayList = pygame.display.get_desktop_sizes()
#
# screen = pygame.display.set_mode(displayList[0])
# clock = pygame.time.Clock()
# running = True
# dt = 0
#
# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill("purple")
#     pygame.draw.circle(screen, "red", player_pos, 40)
#
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_ESCAPE]:
#         running = False
#
#     pygame.display.flip()
#
#     dt = clock.tick(60) / 1000
#
# pygame.quit()

class TowerVisualizer:
    def __init__(self):

        pass
    def moveDisk(self):
        pass
    def update(self):
        pass
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
    def append(self, value):
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

    destination.append(source.pop())
    counter.add(1)
    print("Step: ", counter.value)
    print("moving Disk", n, "from", source.name, "to", destination.name)
    for e in StackList:
        print(e.name, ":", e.data)
    print()
    # input()
    TowerOfHanoi(n-1, aux, destination, source, counter)

A = Stack("A")
B = Stack("B")
C = Stack("C")

for i in range(5, 0, -1):
    A.append(i)

print("Initial Condition")
print("A :", A.data)
print("B :", B.data)
print("C :", C.data, "\n")
TowerOfHanoi(5, A, C, B, Counter())

