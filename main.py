import sys, locale
import curses

VERTICAL = "║"
HORIZONTAL = "═"
RIGHT_TOP_CORNER = "╗"
RIGHT_BOTTOM_CORNER = "╝"
LEFT_TOP_CORNER = "╔"
LEFT_BOTTOM_CORNER = "╚"
LEFT_CROSS = "╣"
TOP_CROSS = "╩"
BOTTOM_CROSS = "╦"
RIGHT_CROSS = "╠"
CROSS = "╬"


def draw_ui(height, width):
    for i in range(height):
        line = ""
        if i == 0:
            line += LEFT_TOP_CORNER + (HORIZONTAL * width) + RIGHT_TOP_CORNER
        elif i == height - 1:
            line += LEFT_BOTTOM_CORNER + (HORIZONTAL * width) + RIGHT_BOTOM_CORNER
        else:
            line += VERTICAL
            for j in range(width):
                line += " "
            line += VERTICAL
        print(line)


def draw_table(rows, columns, data):
    # Draw the top of the table
    top_line = LEFT_TOP_CORNER
    for i in range(columns):
        top_line += (HORIZONTAL * 10) + BOTTOM_CROSS
    top_line = top_line[:-1] + RIGHT_TOP_CORNER
    print(top_line)

    # Draw the rows of the table
    for i in range(rows):
        row_line = VERTICAL
        for j in range(columns):
            cell_data = data[i][j] if i < len(data) else ""
            row_line += f"{cell_data: <10}" + VERTICAL
        print(row_line)

        if i != rows - 1:
            line_line = RIGHT_CROSS
            for j in range(columns):
                line_line += (HORIZONTAL * 10) + CROSS
            line_line = line_line[:-1] + LEFT_CROSS
            print(line_line)

    # Draw the bottom of the table
    bottom_line = LEFT_BOTTOM_CORNER
    for i in range(columns):
        bottom_line += (HORIZONTAL * 10) + TOP_CROSS
    bottom_line = bottom_line[:-1] + RIGHT_BOTTOM_CORNER
    print(bottom_line)


def draw_rectangle(width, height):
    # Draw the top of the rectangle
    top_line = LEFT_TOP_CORNER
    for i in range(width * 2 - 2):
        top_line += HORIZONTAL
    top_line += RIGHT_TOP_CORNER
    print(top_line)

    # Draw the middle of the rectangle
    for i in range(height - 2):
        middle_line = VERTICAL
        for j in range(width * 2 - 2):
            middle_line += " "
        middle_line += VERTICAL
        print(middle_line)

    # Draw the bottom of the rectangle
    bottom_line = LEFT_BOTTOM_CORNER
    for i in range(width * 2 - 2):
        bottom_line += HORIZONTAL
    bottom_line += RIGHT_BOTTOM_CORNER
    print(bottom_line)


# def draw_window(h: int, w: int, title: str, debug=False):
#     # print title
#     print(LEFT_TOP_CORNER + HORIZONTAL * ((w - 2) * 2 + 2) + RIGHT_TOP_CORNER)
#     print(VERTICAL + title + " " * ((w - 2) * 2 + 2 - len(title)) + VERTICAL)
#     print(RIGHT_CROSS + HORIZONTAL * ((w - 2) * 2 + 2) + LEFT_CROSS)
#     for i in range(h - 4):
#         print(VERTICAL + " " * ((w - 2) * 2 + 2) + VERTICAL, end="")
#         if debug is True:
#             print(i)
#         else:
#             print()
#     print(LEFT_BOTTOM_CORNER + HORIZONTAL * ((w - 2) * 2 + 2) + RIGHT_BOTOM_CORNER)


def draw_window(width, height, title="new window"):
    # Draw the top of the window
    top_line = LEFT_TOP_CORNER
    for i in range(width * 2 - 2):
        top_line += HORIZONTAL
    top_line += RIGHT_TOP_CORNER
    print(top_line)

    # Draw the title
    if len(title) % 2 == 1:
        title_line = (
            VERTICAL
            + " " * ((width * 2 - 2 - len(title)) // 2)
            + title
            + " " * ((width * 2 - 2 - len(title)) // 2 + 1)
            + VERTICAL
        )
    else:
        title_line = (
            VERTICAL
            + " " * ((width * 2 - 2 - len(title)) // 2)
            + title
            + " " * ((width * 2 - 2 - len(title)) // 2)
            + VERTICAL
        )
    print(title_line)

    # Draw the line under the title
    line_under_title = RIGHT_CROSS + HORIZONTAL * (width * 2 - 2) + LEFT_CROSS
    print(line_under_title)

    # Draw the middle of the window
    for i in range(height - 4):
        middle_line = VERTICAL
        for j in range(width * 2 - 2):
            middle_line += " "
        middle_line += VERTICAL
        print(middle_line)

    # Draw the bottom of the window
    bottom_line = LEFT_BOTTOM_CORNER
    for i in range(width * 2 - 2):
        bottom_line += HORIZONTAL
    bottom_line += RIGHT_BOTTOM_CORNER
    print(bottom_line)


class window:
    def __init__(self, pos_x=0, pox_y=0, height=10, wight=10, level=0):
        self.x = x
        self.y = y
        self.height = height
        self.wight = wight
        self.level = level


def pro():
    pass


def main():
    # draw_react(10, 15, debug=True)
    # draw_table(10, 15, "title")

    # main_loop
    # while input() != "q":
    #     print("aaaaaa", end="")
    # curses.initscr()
    # curses.beep()
    # print(curses.getsyx())
    # draw_ui(10, 5)
    data = [["Name", "Age", "Gender"], ["Tom", 25, "Male"], ["Jerry", 30, "Female"]]
    draw_table(3, 3, data)
    draw_rectangle(5, 5)
    draw_window(10, 10, "Hello World")


if __name__ == "__main__":
    main()
