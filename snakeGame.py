import curses
import time
import random

#   curses setting 
stdscr = curses.initscr()
curses.start_color()
curses.use_default_colors()
curses.cbreak()
curses.curs_set(False)
stdscr.keypad(True)



#   add color
curses.init_pair(1, curses.COLOR_GREEN  , curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_BLUE , curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_YELLOW , curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_RED , curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_CYAN , curses.COLOR_BLACK)
curses.init_pair(6, 8 , -1)
green = curses.color_pair(1)
blue = curses.color_pair(2)
yellow = curses.color_pair(3)
red = curses.color_pair(4)
cyan = curses.color_pair(5)
gray = curses.color_pair(6)



def check_terminal_size():
    global maxl , maxc
    maxl = curses.LINES - 1
    maxc = curses.COLS - 1

    if maxl < 20 or maxc < 50 :
        stdscr.addstr(0, 0 , 'Error: The terminal window is small' , red)
        stdscr.refresh()
        return False
    else:
        maxl = 30 if maxl > 30 else maxl
        maxc = 100 if maxc > 100 else maxc
        return True




def menu():
    snakepic = '''Snake Game        __
      _______    /*_>-<
  ___/ _____ \__/ /
 <____/     \____/'''
    
    stdscr.addstr(0,0 , snakepic , green)
    stdscr.addstr(4,0 , 'https://github.com/mamrez2002' , cyan)
    for i , j in enumerate(['exit', 'classic' , 'level', 'setting']):
        stdscr.addstr(i + 7 , 1 , '[' , yellow)
        stdscr.addstr(i + 7 , 2 , str(i) )
        stdscr.addstr(i + 7 , 3 , ']', yellow)
        stdscr.addstr(i + 7 , 5 , j, gray)

    stdscr.addch(12, 1 , '>', yellow)
    curses.curs_set(True)
    n = stdscr.getstr(12 , 3, 1)
    curses.curs_set(False)
    stdscr.refresh()




if check_terminal_size():
    menu()

stdscr.getkey()
stdscr.clear()
stdscr.refresh()