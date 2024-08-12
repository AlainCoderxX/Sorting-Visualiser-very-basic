import pygame
import random
pygame.init()


class App:
    def __init__(self) -> None:
        self.WIDTH, self.HEIGHT = 1200, 600
        self.nums = 600
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
        sorting_generator = None
        while True:
            pygame.display.set_caption(
                f"Merge Sort {int(self.CLOCK.get_fps())}")
            self.WINDOW.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.flag = False
                        self.values = randomise(self.nums, self.HEIGHT)
                    if event.key == pygame.K_RETURN:
                        if self.flag is False:
                            self.flag = True
                            sorting_generator = mergeSort(
                                self.values, 0, len(self.values) - 1)
                        else:
                            self.flag = False
            if self.flag and sorting_generator:
                   try:
                        swaparr = next(sorting_generator)
                   except StopIteration:
                        self.flag = False
                        swaparr = []
            else:
                   swaparr = []
            arr.draw(self.WINDOW, self.HEIGHT, self.values, swaparr)
            if self.values==sorted(self.values):
                arr.finish_draw(self.WINDOW,self.HEIGHT,self.values)
            pygame.display.flip()
            self.CLOCK.tick(self.FPS)
# Drawing the arrays as rectangles


class Draw:
    def __init__(self, nums, width) -> None:
        self.thickness = width//nums
        self.color='white'

    def draw(self, surface, height, array, swaparr):
        for i in range(0, len(array)):
            self.color = 'red' if i in swaparr else 'white'
            # pygame.draw.line(surface,('green'),[(i,height),(i,height-array[i])],self.thickness)
            rect = pygame.Rect(i * self.thickness, height -
                               array[i], self.thickness, array[i])
            pygame.draw.rect(surface, self.color, rect)
    def finish_draw(self,surface,height,array):
        for i in range(0, len(array)):
            self.color = 'orange'
            # pygame.draw.line(surface,('green'),[(i,height),(i,height-array[i])],self.thickness)
            rect = pygame.Rect(i * self.thickness, height -
                               array[i], self.thickness, array[i])
            pygame.draw.rect(surface, self.color, rect)
# Creates an array of random numbers
def randomise(nums, height):
    arr=[]
    while len(arr)!=nums:
        x=random.choice(range(height))
        if x not in arr:
            arr.append(x)
    return arr



def mergeSort(array, left, right):
    if left < right:
        mid = (left + right) // 2
        yield from mergeSort(array, left, mid)
        yield from mergeSort(array, mid + 1, right)
        yield from merge(array, left, mid, right)


def merge(array, left, mid, right):
    left_half = array[left:mid + 1]
    right_half = array[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            array[k] = left_half[i]
            i += 1
        else:
            array[k] = right_half[j]
            j += 1
        yield [k]  # Highlight the current index being updated
        k += 1

    while i < len(left_half):
        array[k] = left_half[i]
        i += 1
        yield [k]
        k += 1

    while j < len(right_half):
        array[k] = right_half[j]
        j += 1
        yield [k]
        k += 1


if __name__ == "__main__":
    app = App()
    app.run()
