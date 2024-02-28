import curses
import time
import random

#   curses setting 
stdscr = curses.initscr()
curses.start_color()
curses.cbreak()
curses.curs_set(False)
stdscr.keypad(True)



#   add color
curses.init_pair(1, curses.COLOR_GREEN  , curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_BLUE , curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_YELLOW , curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_RED , curses.COLOR_BLACK)
green = curses.color_pair(1)
blue = curses.color_pair(2)
yellow = curses.color_pair(3)
red = curses.color_pair(4)



def check_terminal_size():
    global maxl , maxc
    maxl = curses.LINES - 1
    maxc = curses.COLS - 1

    if maxl < 20 or maxc < 50 :
        stdscr.addstr(0, 0 , 'Error: The terminal window is small' , red)
        stdscr.refresh()
        return False
    else:
        return True










if check_terminal_size():
    pass

stdscr.getkey()