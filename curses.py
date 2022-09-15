import curses


w_int = []


def show_interface(stdscr, current_index):
    h, w = stdscr.getmaxyx()
    stdscr.clear()
    stdscr.addstr(h//2 - 5, w//2 - len('Choose an inteface')//2,
                  'Choose an interface', curses.color_pair(1))
    for i, row in enumerate(w_int, 0):
        if i == current_index:
            stdscr.addstr(
                h//2 + i, w//2-5,
                row, curses.color_pair(2))
        else:
            stdscr.addstr(h//2 + i, w//2-5, row)
    stdscr.refresh()


def get_interface() -> list:
    w_int = list(filter(lambda x: x[0:2] ==
                        'wl', list(zip(*socket.if_nameindex()))[1]))
    return w_int


def curses_main(stdscr):
    current_index = 0
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
    show_interface(stdscr, current_index)
    while(1):
        key = stdscr.getch()
        if key == curses.KEY_UP and current_index > 0:
            current_index -= 1
        elif key == curses.KEY_DOWN and current_index < len(w_int)-1:
            current_index += 1
        elif key == 10:
            if w_int[current_index] == 'exit':
                exit(0)
            else:
                return w_int[current_index]
        show_interface(stdscr, current_index)


