import static 
import heapq
from PIL import Image, ImageDraw

class ShortestPath():
    
    def __init__(self):
        
        self.inf = 999999
        self.pointsNum = len(static.points)
        self.points = static.points
        self.distance = [self.inf] * self.pointsNum
        self.pre = [-1] * self.pointsNum
        self.visited = [False] * self.pointsNum

    def relax(self, s_id, now_id):
        
        if self.distance[s_id] + static.getEdge(s_id, now_id) < self.distance[now_id]:
        self.distance[now_id] = self.distance[s_id] + static.getEdge(s_id, now_id)
        self.pre[now_id] = s_id

    def printPath(self, current, source):
        
        if current == source:

            return [source]

        return [current] + printPath(self.pre[current], source)
        
        
    def find_shortest(self, s_id, d_id):
        
        self.distance[s_id] = 0 

        for times in range(pointsNum - 1):

            k_node = 0

            minmum = self.inf

            for k in range(self.pointsNum):

                if not self.visited[k] and self.distance[s_id] < minmum:

                    minmum = self.distance[s_id]
                    
                    k_node = k
            
            self.visited[k_node] = True
        
            for des_node in range(self.pointsNum):
    
                if static.exist(k_node, des_node):
    
                    relax(k_node, des_node)
            
            return self.printPath(d_id, s_id)

def mark_on_graph(path, filename):

    image = Image.open(filename)

    draw = ImageDraw.Draw(image)

    for i in range(len(path) - 1):

        source = path[i]

        dest = path[i + 1]

        s_pix = source.getPixel(source)

        d_pix = source.getPixel(dest)

        draw.line((s_pix.x, s_pix.y, y_pix.x, y_pix.y), fill = (0, 0, 255))

    image.save(filename.replace('ori', 'tmp'))
        

import os

def query(location, destination):

    source = static.mapNameToID(location)

    destination = static.mapNameToID(destination)

    SP = ShortestPath()
    
    tmp_image_path = 'tmp/ori.img'

    mark_on_graph(SP.find_shortest(source, destination), tmp_image_path)
