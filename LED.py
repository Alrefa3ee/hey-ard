from pyfirmata import Arduino, util


def turn_LED():
    board = Arduino('PORT')
    board.digital[13].write(1)
