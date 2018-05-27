'''
    This is the place holding the distance information 
    between adjacent landmark and the mapping dictionary
    for the name and the id.
'''

class Points():

    def __init__(self):

        filex = open('sources/xidian.txt', 'r')

        content = filex.readlines()
            
        self.points = []

        for i in range(len(content)):
            
            idx, x, y = content[i].split(' ')

            self.points.append((idx, x, y))


    def getLat(self, x):

        return self.points[int(x) - 1][1], self.points[int(x) - 1][2]


def getLat(x):

    points = Points()

    return points.getLat(x)

    
