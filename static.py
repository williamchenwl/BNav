'''
    This is the place holding the distance information 
    between adjacent landmark and the mapping dictionary
    for the name and the id.
'''

from PIL import Image, ImageDraw

class Points():

    def __init__(self):

        filex = open('sources/xidian.txt', 'r')

        content = filex.readlines()
            
        self.points = []

        for i in range(len(content)):
            
            idx, x, y = content[i].split(' ')

            self.points.append((idx, x, y))
        
        self.bl = []

        fileb = open('sources/blou.txt')

        content = fileb.readlines()

        for i in range(len(content)):

            idx, x, y = content[i].split(' ')

            self.bl.append((idx , x, y))

    def getLat(self, x):

        return self.points[int(x) - 1][1], self.points[int(x) - 1][2]
    
    def findShortest(self, x):

        now_x, now_y = self.getLat(x)

        float_x, float_y = float(now_x), float(now_y)
        
        now_shortest = 999999999
    
        rec = self.bl[0]

        for t in self.bl:

            t_x, t_y = float(t[1]), float(t[2])

            if (t_x - float_x) * (t_x - float_x) + (t_y - float_y) * (t_y - float_y) < now_shortest:

                now_shortest =  (t_x - float_x) * (t_x - float_x) + (t_y - float_y) * (t_y - float_y) 
                
                rec = t

        return rec[0], rec[1], rec[2]

def getLat(x):

    points = Points()

    return points.getLat(x), points.findShortest(x)


image = Image.open('static/map.png')

width, height = image.size

print('image size is', width, height)

class InnerBlock():

    def __init__(self, idx, name, x, y):

        self.x = x

        self.y = y
        
        self.name = name

        self.idx = int(idx)

        if self.idx >= 6 and self.idx <= 12:

            self.stair = True

        else:

            self.stair = False

    def isStair(self):

        return self.stair

    def central(self):

        per_w = width / 23
        
        per_h = height / 20

        xx = width / 23 * (self.x - 1) + per_w / 2

        yy = height / 20 * (self.y - 1) + per_h / 2

        yy = height - yy

        return xx, yy



class BlockList():

    def __init__(self):

        filex = open('static/vertex.txt')
        
        content = filex.readlines()

        self.nameTable = {}

        self.blocks = []

        self.maxID = 0

        for i in range(len(content)):

            idx, name, x, y = content[i].split(' ')

            idx, x, y = int(idx) - 1, int(x), int(y)

            self.nameTable[name] = idx

            self.blocks.append(InnerBlock(idx, name, x, y))

            self.maxID += 1
        
        self.edge = {}

        filee = open('static/edges.txt')

        content = filee.readlines()

        for i in range(len(content)):

            x, y = content[i].split(' ')
            x, y = int(x) - 1, int(y) - 1
            self.edge[(x, y)] = 1
            self.edge[(y, x)] = 1

        filex = open('static/nedges.txt')

        content = filex.readlines()

        for i in range(len(content)):

           x, y = content[i].strip().split(' ')
           print(x, y)
           x, y = self.getIDByName(x), self.getIDByName(y)
           self.edge[(x, y)] = 1
           self.edge[(y, x)] = 1
    
    def idIsStair(self, x):

        return self.blocks[x].isStair()

    def getIDByName(self, name):

        return self.nameTable[name]

    def realBlockList(self, idList):
    
        realList = []

        for x in range(len(idList)):

            realList.append(self.blocks[idList[x]].central())

        return realList

    def getEdge(self, idx, idy):

        if (idx, idy) in self.edge:

            return self.edge[(idx, idy)]

        else:

            return 999999
       
    def pointsNum(self):

        return self.maxID

