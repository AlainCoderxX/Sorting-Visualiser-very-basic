import pygame
import random
pygame.init()


class App:
    def __init__(self) -> None:
        self.WIDTH, self.HEIGHT = 1200, 600
        self.nums = 120
        self.FPS = self.nums//4
        self.CLOCK = pygame.time.Clock()
        self.values = []
        self.flag = False
        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.i = 0
        self.font_size = 24
        self.font = pygame.font.Font(None, self.font_size)  # Use default font

    def run(self):
        arr = Draw(self.nums, self.WIDTH)
        self.values = randomise(self.nums, self.HEIGHT)
        while True:
            pygame.display.set_caption(
                f"Bubble Sort {int(self.CLOCK.get_fps())}")
            self.WINDOW.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.values = randomise(self.nums, self.HEIGHT)
                    if event.key == pygame.K_RETURN:
                        if self.flag is False:
                            self.flag = True
                        else:
                            self.flag = False
            if self.flag:
                if self.i < len(self.values):
                    self.values,swaparr = bubbleSort(self.values, self.i)
                    self.i += 1
                if self.i>=len(self.values):
                        self.flag=False
                        self.i = 0
            else:
                swaparr=[]
            arr.draw(self.WINDOW, self.HEIGHT, self.values, swaparr)
            pygame.display.flip()
            self.CLOCK.tick(self.FPS)
# Drawing the arrays as rectangles


class Draw:
    def __init__(self, nums, width) -> None:
        self.thickness = width//nums

    def draw(self, surface, height, array, swaparr):
        for i in range(0, len(array)):
            color='red' if i in swaparr else 'green'
            # pygame.draw.line(surface,('green'),[(i,height),(i,height-array[i])],self.thickness)
            rect = pygame.Rect(i * self.thickness, height -
                               array[i], self.thickness, array[i])
            pygame.draw.rect(surface, color , rect)


# Creates an array of random numbers
def randomise(nums, height):
    values = []
    for i in range(nums):
        values.append(random.randint(1, height))
    return values

# Bubble Sort (Only second loop)


def bubbleSort(array, i):
    swaparr=[]
    for j in range(0, len(array)-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
        # swaparr=[i,i+1]
        swaparr=[j+1,j]
    return array,swaparr


if __name__ == "__main__":
    app = App()
    app.run()
