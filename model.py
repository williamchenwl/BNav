import static 
import heapq
from PIL import Image, ImageDraw
from static import Points, BlockList

class ShortestPath():
    
    def __init__(self):
        
        self.inf = 999999
        self.points = BlockList()
        self.pointsNum = self.points.pointsNum()
        self.distance = [999999] * self.pointsNum
        self.pre = [-1] * self.pointsNum
        self.visited = [False] * self.pointsNum

    def relax(self, s_id, now_id):
        
        if self.distance[s_id] + self.points.getEdge(s_id, now_id) < self.distance[now_id]:
            self.distance[now_id] = self.distance[s_id] + self.points.getEdge(s_id, now_id)
            self.pre[now_id] = s_id

    def printPath(self, current, source):
        
        if current == source:

            return [source]

        return [current] + self.printPath(self.pre[current], source)
        
        
    def findShortest(self, s_id, d_id):
    

        self.distance[s_id] = 0 

        for times in range(self.pointsNum - 1):

            k_node = 0

            minmum = self.inf

            for k in range(self.pointsNum):

                if not self.visited[k] and self.distance[k] < minmum:
                    
                    minmum = self.distance[k]
                    
                    k_node = k
            
            self.visited[k_node] = True
        
            for des_node in range(self.pointsNum):
    
                if self.points.getEdge(k_node, des_node) <= 1:
   
                    self.relax(k_node, des_node)
    
        print(self.distance[d_id])

        return self.printPath(d_id, s_id)

            
    def findDraw(self, in_name, out_name):

        s_id = self.points.getIDByName(in_name)

        d_id = self.points.getIDByName(out_name)

    
        print(s_id, d_id)

        idList = self.findShortest(s_id, d_id)

        path = self.points.realBlockList(idList)

        image = Image.open('static/map.png')

        draw = ImageDraw.Draw(image)
        
        s_x, s_y = path[0]

        draw.ellipse([s_x - 5, s_y - 5, s_x + 5, s_y + 5],  fill = 'yellow')

        d_x, d_y = path[-1] 

        draw.ellipse([d_x - 5, d_y - 5, d_x + 5, d_y + 5],  fill = 'green')

        i = 0

        while i < (len(path) - 1):

            pre = i

            mid = i + 1

            nxt = mid

            print('list is', idList[pre], idList[mid], idList[nxt])
            
            print('coor is', path[pre], path[mid], path[nxt])
            if i < len(path) - 2:

                nxt = mid + 1
            

            if self.points.idIsStair(idList[mid]):

                

                pre_x, pre_y  = path[pre]

                mid1_x, mid1_y = path[mid]

                mid1_y = pre_y

                mid2_x, mid2_y = mid1_x, mid1_y

                nxt_x, nxt_y = path[nxt]

                mid2_y = nxt_y
 
                draw.line((pre_x, pre_y, mid1_x, mid1_y), fill = 'red')
                draw.line((mid1_x, mid1_y, mid2_x, mid2_y), fill = 'red')
                draw.line((nxt_x, nxt_y, mid2_x, mid2_y), fill = 'red')

            else:

                pre_x, pre_y = path[pre]

                mid_x, mid_y = path[mid]

                nxt_x, nxt_y = path[nxt]

                if not self.points.idIsStair(idList[pre]):

                    draw.line((pre_x, pre_y, mid_x, mid_y), 'red')

                if not self.points.idIsStair(idList[nxt]):
    
                    draw.line((mid_x, mid_y, nxt_x, nxt_y), 'red')
            
            i += 1

        image.save('tmp/{}{}.png'.format(in_name, out_name))

        return image
            

def query(location, destination):

    sp = ShortestPath()

    sp.findDraw(location, destination)


if __name__ == '__main__':

    query('201', '511')
