
from tkinter import *



def drawCell(canvas, x, y, size, text):
    canvas.create_rectangle(x, y, x + size, y + size)
    canvas.create_text(x + size / 2, y + size / 2 - 1, text = str(text))   

def drawCellLine(canvas, x, y, cellSize, elements, xBitCount):
    for column in range(0, 1 << xBitCount):
        drawCell(canvas, x + column * cellSize, y, cellSize, elements[column])

def drawTable(canvas, x, y, cellSize, table, xBitCount, yBitCount):
    for row in range(0, 1 << yBitCount):
        drawCellLine(canvas, x, y + row * cellSize, cellSize, table[row], xBitCount)

def generateGrayCode(bitCount):
    if(bitCount == 1):
        return ["0", "1"]
    else:
        prevGrayCode = generateGrayCode(bitCount - 1)
        first = list(("0" + x) for x in prevGrayCode)
        prevGrayCode.reverse()
        second = list(("1" + x) for x in prevGrayCode)
        return (first + second)

def drawGrayCodeHorizontal(canvas, x, y, cellSize, xBitCount):
    grayCode = generateGrayCode(xBitCount)
    for column in range(0, len(grayCode)):
        canvas.create_text(x + column * cellSize + cellSize / 2, y, text = grayCode[column])

def drawGrayCodeVertical(canvas, x, y, cellSize, yBitCount):
    grayCode = generateGrayCode(yBitCount)
    for row in range(0, len(grayCode)):
        canvas.create_text(x, y + row * cellSize + cellSize / 2, text = grayCode[row])

def drawTableWithGrayCode(canvas, x, y, cellSize, table, xBitCount, yBitCount):
    drawTable(canvas, x + 30, y + 16, cellSize, table, xBitCount, yBitCount)
    drawGrayCodeHorizontal(canvas, x + 30, y + 10, cellSize, xBitCount)
    drawGrayCodeVertical(canvas, x + 16, y + 15, cellSize, yBitCount)

class KarnaughMap:
    def __init__(self, xBitCount = 3, yBitCount = 3, x = 0, y = 0, cellSize = 40):
        self.xBitCount = xBitCount
        self.yBitCount = yBitCount
        self.elements = [[0] * (1 << xBitCount)] * (1 << yBitCount)
        self.x = x
        self.y = y
        self.cellSize = cellSize

    def draw(self, canvas, cellSize = 40):
        drawTableWithGrayCode(canvas, self.x, self.y, cellSize, self.elements, self.xBitCount, self.yBitCount)

    def handleClick(self, event):
        column = int((event.x - (self.x + 30)) / self.cellSize)
        row = int((event.y - (self.y + 16)) / self.cellSize)
        self.elements[row][column] = 1

def click(event):
    map.handleClick(event)

graphWidth    = 400
graphHeight   = 400
backgroundFill = "#FFFFFF"

root = Tk()
root.title("Karnaugh map drawer")
root.resizable(height = False, width = False)
#root.wm_iconbitmap("favicon.ico")
root.geometry(str(graphWidth) + 'x' + str(graphHeight+60))
canvas = Canvas(root, width = graphWidth, height = graphHeight, bg = backgroundFill)
canvas.bind("<Button-1>", click)

map = KarnaughMap()
map.draw(canvas)

#print(elements)

#drawTableWithGrayCode(canvas, 20, 20, 40, elements, xBitCount, yBitCount)

canvas.place(bordermode = OUTSIDE)
root.mainloop()