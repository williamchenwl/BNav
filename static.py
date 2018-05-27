'''
    This is the place holding the distance information 
    between adjacent landmark and the mapping dictionary
    for the name and the id.
'''


class ShortestPath():

    def __init__():
        
        self.inf = 999999

        self.landmark_n = 100

        self.landmark = u'' * self.landmark_n

        self.distance = [[inf] * self.landmark_n for _ in range(self.landmark_n)]
        
    def add_edge(x, y, z):

        distance[x][y] = z

    def calc():
    
        for k in range(self.landmark_n):
            for i in range(self.landmark_n):
                for j in range(self.landmark_n):

                    distance[i][j] = min(distance[i][k] + distance[k][j], distance[i][j]) 






