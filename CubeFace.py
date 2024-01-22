import numpy as np

class CubeFace():
    def __init__(self, faceMatrix):
        self.matrix = faceMatrix
        self.Left = None
        self.Up = None
        self.Right = None
        self.Down = None

    def setNeighbors(self, neighbors):
        self.Left, self.Up, self.Right, self.Down = neighbors
    
    def rotateFace(self, clockwise):
        '''
        Inputs:
        - clockwise: True if rotation is clockwise, false otherwise (false for U', D', ...)

        Actions:
        - updates the face and neighbor matrices based on clockwise or counterclockwise rotation
        '''
        upBuffer = np.copy(self.getNeighborValues(self.Up))
        if clockwise:
            self.setMatrix(np.rot90(self.getMatrix(), 3))
            self.updateNeighbor(self.Up['face'], self.Up['range'], self.getNeighborValues(self.Left))
            self.updateNeighbor(self.Left['face'], self.Left['range'], self.getNeighborValues(self.Down))
            self.updateNeighbor(self.Down['face'], self.Down['range'], self.getNeighborValues(self.Right))
            self.updateNeighbor(self.Right['face'], self.Right['range'], upBuffer)
        else:
            self.setMatrix(np.rot90(self.getMatrix(), 1))
            self.updateNeighbor(self.Up['face'], self.Up['range'], self.getNeighborValues(self.Right))
            self.updateNeighbor(self.Right['face'], self.Right['range'], self.getNeighborValues(self.Down))
            self.updateNeighbor(self.Down['face'], self.Down['range'], self.getNeighborValues(self.Left))
            self.updateNeighbor(self.Left['face'], self.Left['range'], upBuffer)

    def updateNeighbor(self, curFace, curRange, newValues):
        '''
        Inputs:
        - curFace: current values of a neighbor
            np array of shape (3, 3)
        - curRange: location of values in the neighbor matrix
            np slice
        - newValues: values sliced from the clockwise or counterclockwise face (relative to curFace)
            np array of shape (3, )
        '''

        temp = curFace.getMatrix()
        temp[curRange] = newValues
        curFace.setMatrix(temp)

    def getNeighborValues(self, neighbor):
        '''
        Inputs:
        - neighbor: matrix and slice index for neighboring face
            dict {'face': ___ , 'range': np.s_[___]}

        Returns:
        - neighborValues: values sliced from the clockwise or counterclockwise face (relative to curFace)
            np array of shape (3, )
        '''
        return neighbor['face'].matrix[neighbor['range']]

    def getMatrix(self):
        return self.matrix
    
    def setMatrix(self, newMatrix):
        self.matrix = newMatrix