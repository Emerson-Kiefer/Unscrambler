import kociemba
# from pyfirmata import ArduinoMega, util
import time
import serial

cubeString = ""
scrambleStringColor = 'WGBBWGOWO YOWWRYWOB BRBGGBGBG YYROYYYYR GOWROWRWO RROGBBYRG'
## U = (W)hite, F = (G)reen, R = (R)ed, B = (B)lue, L = (O)range, D = (Y)ellow


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


cubeString = convertColorToCubeString(scrambleStringColor)
# print(cubeString)
        
# print(kociemba.solve(cubeString))

print(kociemba.solve('UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'))

# board = ArduinoMega('/dev/cu.usbmodem142401')
# iterator = util.Iterator(board)
# iterator.start()
# # Tv1 = board.get_pin('a:3:o')
# # board.digital[3].write(1)
# # time.sleep(10)
# # board.digital[3].write(0)

# dirPin = board.digital[2]
# stepPin = board.digital[3]
# stepsPerRev = 200

# testPin = board.digital[4]

# # while(1):
# #     testPin.write(1)
# #     time.sleep(1/10)
# #     testPin.write(0)
# #     time.sleep(1)

# while(1):
#     dirPin.write(1)
#     numSteps = 50

#     for x in range (0, numSteps*4):
#         stepPin.write(1)
#         time.sleep(500/1000000.0)
#         stepPin.write(0)
#         time.sleep(500/1000000.0)
#     time.sleep(1/2.0)

#     time.sleep(1)
#     break
