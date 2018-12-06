

f = open("in.txt")
coords = [[int(l) for l in line.strip().split(", ")] for line in f]
print(coords)
sbX = sorted(coords, key=lambda x: x[0])
sbY = sorted(coords, key=lambda x: x[1])
print(sbX)
print(sbY)
minX = sbX[0][0]
maxX = sbX[-1][0]
minY = sbY[0][1]
maxY = sbY[-1][1]
node = "N"
area = "A"

#Try a router-style shortest path algo

def get_squares(posn, d):
    n = posn[1] - d
    s = posn[1] + d
    e = posn[0] - d
    w = posn[0] + d
    spaces = set()
    for y in range(n, s + 1):
        spaces.add((e, y))
        spaces.add((w, y))
    for x in range(e, w + 1):
        spaces.add((x, n))
        spaces.add((w, s))
    return spaces

class PuzzleGrid:
    def __init__(self, aX, zX, aY, zY):
        self.posns = dict()
        self.counter = 1
        self.aX = aX
        self.zX = zX
        self.w = zX - aX
        self.aY = aY
        self.zY = zY
        self.h = aY - zY
        self.grid = [[None for x in range(0, self.w)] for y in range(0, self.h)]
        print("made grid: ax=%d zx=%d ay=%d zy=%d w=%d h=%d aw=%d ah=%d" % (aX, zX, aY, zY, self.w, self.h, len(self.grid[0]), len(self.grid)))

    def adjust(self, coord):
        return coord[0] - self.aX, coord[1] - self.aY

    def add_and_spread(self, coord):
        adjusted = self.adjust(coord)
        self.grid[adjusted[1]][adjusted[0]] = (node, self.counter)
        self.posns[self.counter] = adjusted
        self.counter += 1
        self.spread(adjusted)

    def spread(self, p):
        distance = 1
        done = False
        while not done:
            spaces = get_squares(p, distance)
            any_good = False
            for space in spaces:




pg = PuzzleGrid(minX, maxX, minY, maxY)
for coord in coords:
    pg.add_and_adjust(coord)


