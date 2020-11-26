Tiles = []
size = 8

def Tile(x,y,z):
    return(str(x) + ", " + str(y) + ", " + str(z))


EvenStartY = 0
EvenStartZ = 0
OddStartZ = 0
OddStartY = -1
for count in range (1, size // 2 + 1):
    y = EvenStartY
    z = EvenStartZ
    for x in range (0, size - 1, 2):
        TempTile = Tile(x, y, z)
        Tiles.append(TempTile)
        y -= 1
        z -= 1
    EvenStartZ += 1
    EvenStartY -= 1
    y = OddStartY
    z = OddStartZ
    for x in range (1, size, 2):
        TempTile = Tile(x, y, z)
        Tiles.append(TempTile)
        y -= 1
        z -= 1
    OddStartZ += 1
    OddStartY -= 1

print(Tiles)
