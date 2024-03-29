import time
import serial
import kociemba
from SerialCommunicator import write_read
from CubeModel import CubeModel

ARDUINO = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=2.0)
INITIAL_CUBE_STATE = "WWWWWWWWW RRRRRRRRR GGGGGGGGG YYYYYYYYY OOOOOOOOO BBBBBBBBB"

	
# def userCreateStateStr():
	# print("SOLVED STATE: " + INITIAL_CUBE_STATE)
	# W = input("Input WHITE face state: ")
	# R = input("Input RED face state: ")
	# G = input("Input GREEN face state: ")
	# Y = input("Input YELLOW face state: ")
	# O = input("Input ORANGE face state: ")
	# B = input("Input BLUE face state: ")
	
	# return W + ' ' + R + ' ' + G + ' ' + Y + ' ' + O + ' ' + B
	
 
def userCreateStateStr():
	print("SOLVED STATE: " + INITIAL_CUBE_STATE)
#	value = input("Enter CURRENT state: ")
	value = "GBYRWGRGW OROWROGYY WOBGGRGYR ROWOYGBBG OYBWOWRWY BRWBBBOYY"
	return value
	
def convertColorToCubeString(colorScramble):
    newScramble = ""
    switcher = {
        "W": 'U',
        "G": 'F',
        "R": 'R',
        "B": 'B',
        "O": 'L',
        "Y": 'D',
        " ": ''
    }
    for i in range(0, len(colorScramble)):
        newScramble += switcher[colorScramble[i]]
    if(len(newScramble) != 54):
        print("Invalid string size")
        return -1
    return newScramble


	


def solve_cube():
	input("Begin?")
	stateStr = userCreateStateStr()
	cube = CubeModel(stateStr)
	cubeString = convertColorToCubeString(stateStr)
	solution = kociemba.solve(cubeString)
	#remove spaces to reduce the data size sent via serial
	solution.replace(" ", "")
	print(cubeString)
	print(solution)
	write_read(solution, ARDUINO)

def singleMoves(cube):
	move = input("Move ('q' to quit): ")
	if move == "q":
		return
	cube.scramble(move)
	move.replace(" ", "")
	value = write_read(move, ARDUINO)
	print(cube.getStateStr())
	singleMoves(cube)
	
# def multipleMoves(moves):
	# move_arr = moves.split(" ")
	# print(move_arr)
	
	
solve_cube()
#singleMoves(CubeModel(userCreateStateStr()))
