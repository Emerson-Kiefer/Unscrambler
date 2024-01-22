import numpy as np
import re
from CubeFace import CubeFace

'''
                |************|
                |*U1**U2**U3*|
                |************|
                |*U4**U5**U6*|
                |************|
                |*U7**U8**U9*|
                |************|
    ************|************|************|************
    *L1**L2**L3*|*F1**F2**F3*|*R1**R2**R3*|*B1**B2**B3*
    ************|************|************|************
    *L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6*
    ************|************|************|************
    *L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9*
    ************|************|************|************
                |************|
                |*D1**D2**D3*|
                |************|
                |*D4**D5**D6*|
                |************|
                |*D7**D8**D9*|
                |************|

    CUBE STATE:
        U1-U9, R1-R9, F1-F9, D1-D9, L1-L9, B1-B9
    INITIAL CUBE STATE: 
        U = (W)hite,    R = (R)ed,  F = (G)reen,    D = (Y)ellow,   L = (O)range,   B = (B)lue
        0               1           2               3               4               5
'''
CUBE_STATE = 'WGBBWGOWO YOWWRYWOB BRBGGBGBG YYROYYYYR GOWROWRWO RROGBBYRG'
INITIAL_CUBE_STATE = "WWWWWWWWW RRRRRRRRR GGGGGGGGG YYYYYYYYY OOOOOOOOO BBBBBBBBB"

class CubeModel():
    def __init__(self, stateStr):
        self.U, self.R, self.F, self.D, self.L, self.B = self.initializeFaces(stateStr)
        self.faces = [self.U, self.R, self.F, self.D, self.L, self.B]
    
    def faceToString(self, mat):
        '''
        Inputs:
        - mat: matrix from a CubeFace
            np array of shape (3, 3)

        Returns:
        - faceStr: matrix converted to a string mapped from ints to chars
            String of length 9
        '''

        toStr = {'0':'W', '1':'R', '2':'G', '3':'Y', '4':'O', '5':'B'}
        faceStr = ''.join(map(str, mat.flatten()))
        faceStr = ''.join(toStr[char] for char in faceStr)
        return faceStr 
    
    def getStateStr(self):
        '''
        Returns:
        - stateStr: values from faces converted to a single, space-separated (for each face) string
            String
        '''

        stateStr = ""
        for face in self.faces:
            stateStr += self.faceToString(face.getMatrix().flatten()) + " "
        stateStr = stateStr[:-1]
        return stateStr

    def initializeFace(self, str):
        '''
        Inputs:
        - str: Colors on a face identified by 'W', 'R', 'G', 'Y', 'O', 'B'
            String of length 9
        Returns:
        - faceMatrix: Colors on face identified by ints
            String str mapped to: W -> 0, R -> 1, G -> 2, Y -> 3, O -> 4, B -> 5
            np array of shape (3, 3)
        '''
        toInt = {'W': 0, 'R': 1, 'G':2, 'Y':3, 'O':4, 'B':5}
        faceMatrix = np.array([[toInt[char] for char in str[i:i+3]] for i in range(0, 9, 3)])
        return CubeFace(faceMatrix)


    def initializeFaces(self, stateStr):
        '''
        Inputs:
        - stateStr: space-separated (for each face) string
            ex: "WWWWWWWWW RRRRRRRRR GGGGGGGGG YYYYYYYYY OOOOOOOOO BBBBBBBBB"
            String
        
        Returns: 
        - U, R, F, D, L, B: neighbor dictionaries with keys:
            - face: neighboring face
                CubeFace object
            - range: location of neighboring values in face
                tuple defined by np.s_

        '''
        faceStrs = re.split('[^a-zA-Z]', stateStr)
        U, R, F, D, L, B = [self.initializeFace(faceStr) for faceStr in faceStrs]
        #setNeighbors: [Left, Right, Up, Dow] in relation to the current face
        U.setNeighbors([{'face': L, 'range': np.s_[0, ::-1]}, 
                        {'face': B, 'range': np.s_[0, ::-1]}, 
                        {'face': R, 'range': np.s_[0, ::-1]}, 
                        {'face': F, 'range': np.s_[0, ::-1]}])
        
        R.setNeighbors([{'face': F, 'range': np.s_[::-1, 2]},
                        {'face': U, 'range': np.s_[::-1, 2]},
                        {'face': B, 'range': np.s_[:, 0]},
                        {'face': D, 'range': np.s_[::-1, 2]}])
        
        F.setNeighbors([{'face': L, 'range': np.s_[::-1, 2]},
                        {'face': U, 'range': np.s_[2, :]},
                        {'face': R, 'range': np.s_[:, 0]},
                        {'face': D, 'range': np.s_[0, ::-1]}])
        
        
        D.setNeighbors([{'face': L, 'range': np.s_[2, :]},
                        {'face': F, 'range': np.s_[2, :]},
                        {'face': R, 'range': np.s_[2, :]},
                        {'face': B, 'range': np.s_[2, :]}])

        L.setNeighbors([{'face': B, 'range': np.s_[::-1, 2]},
                        {'face': U, 'range': np.s_[:, 0]},
                        {'face': F, 'range': np.s_[:, 0]},
                        {'face': D, 'range': np.s_[:, 0]}])

        B.setNeighbors([{'face': R, 'range': np.s_[::-1, 2]},
                        {'face': U, 'range': np.s_[0, ::-1]},
                        {'face': L, 'range': np.s_[:, 0]},
                        {'face': D, 'range': np.s_[2, :]}])
        
        return U, R, F, D, L, B

    def rotateCube(self, move):
        '''
        Inputs: 
        - move: face and rotation direction information
            String (examples: "R", "U'", or "D2")

        Actions:
        - Update CubeFace matrices to reflect the "move"
        '''

        clockwiseBool = True
        iterations = 1    
        if len(move) > 1:
            if move[1] == "\'":
                clockwiseBool = False
            elif move[1] == "2":
                iterations = 2
            else:
                raise ValueError("Invalid move")
            
        for i in range(iterations):
            if move[0] == "U":
                self.U.rotateFace(clockwiseBool)
            elif move[0] == "R":
                self.R.rotateFace(clockwiseBool)
            elif move[0] == "F":
                self.F.rotateFace(clockwiseBool) 
            elif move[0] == "D":
                self.D.rotateFace(clockwiseBool)
            elif move[0] == "L":
                self.L.rotateFace(clockwiseBool)
            elif move[0] == "B":
                self.B.rotateFace(clockwiseBool)
                

    def scramble(self, scrambleStr):
        '''
        Inputs:
        - scrambleStr: face and rotation information for a series of moves
            String
            ex: "F L D L\' D2 R\' B2 F L2 B2 F\' R\' L D\' R L\' D\' L\' U R L2 B F2 D2 B\'"

        Actions:
        - moves faces based on scrambleStr
        '''

        scrambleMoves = re.split('[\s]', scrambleStr)
        for move in scrambleMoves:
            self.rotateCube(move)
        

    def printFaces(self, matrices, whitespace):
        for matrix in matrices:
            print(" " * whitespace + "|=============", end='')
        print("|")
        for i in range(0, 3):
            for matrix in matrices:
                row = matrix[i]
                print(" " * whitespace + f"|* {row[0]:^2}* {row[1]:^2}* {row[2]:^2}*", end="")
            print("|")
            for matrix in matrices:
                print(" " * whitespace + "|=============", end="")
            print("|")
    
    def printCube(self):
        self.printFaces([self.U.getMatrix()], 14)
        self.printFaces([self.L.getMatrix(), self.F.getMatrix(), self.R.getMatrix(), self.B.getMatrix()], 0)
        self.printFaces([self.D.getMatrix()], 14)



    