from CubeModel import CubeModel
from CameraManager import CameraManager

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

def generateDataset(cube, camera, label, flag=''):
    '''
    Inputs:
    - cube: 
        CubeModel object
    
    '''

    cube.printCube()
    if input("Capture image (y/n): ") == "y":
        camera.capture_image(0, label, flag=flag)
        
        
    moves = input("ENTER MOVE(S) OR \'q\' TO QUIT\nMoves: ")

    if(moves == 'q'):
        return
    cube.scramble(moves)
    label = cube.getStateStr()
    
    
    

    generateDataset(cube, camera, label, flag=flag)


camera = CameraManager()
cube = CubeModel(INITIAL_CUBE_STATE)
generateDataset(cube, camera, INITIAL_CUBE_STATE, flag="TEST")
