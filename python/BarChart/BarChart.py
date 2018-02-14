
from tkinter import *
from tkinter import messagebox
import math

def drawDelim(i, lowerBorder, graphStep, lineHeight):
    x = i - lowerBorder + 1
    canvas.create_line(graphStep * x, lineHeight - 5 , graphStep * x, lineHeight + 5)
    canvas.create_text(graphStep * x, lineHeight + 12, text = str(i), font = ("Monotype Corsiva", 15, "italic"))

def drawColumn(points, maxValue, isOdd, lineHeight, maxColumnHeight, graphStep, lowerBorder,
               darkColumnFill, lightColumnFill):
    currentColumnHeight = lineHeight - (lineHeight - maxColumnHeight) * points[2] / maxValue
    canvas.create_rectangle(graphStep * (points[0] - lowerBorder + 1), currentColumnHeight, 
                            graphStep * (points[1] - lowerBorder + 1), lineHeight, 
                            fill = darkColumnFill if isOdd else lightColumnFill)
    #canvas.create_line(-5, currentColumnHeight , graphStep * (points[0] - lowerBorder + 1), currentColumnHeight)

def drawBarChart(points, values):
    
    lowerBorder   = points[0] - 1
    higherBorder  = points[len(points) - 1] + 1
    margin        = 1/15
    
    darkColumnFill = "#90C3D4"
    lightColumnFill = "#CBE9F2"

    nrange     = higherBorder - lowerBorder
    graphRange = nrange + 2
    lineHeight = graphHeight * (1 - margin)
    maxColumnHeight = graphHeight * margin
    graphStep  = graphWidth / graphRange

    canvas.delete("all")
    canvas.create_line(0, lineHeight, graphWidth, lineHeight)

    for i in points:
        drawDelim(i, lowerBorder, graphStep, lineHeight)

    odd = True
    ints = makeIntervals(points, values)
    for i in ints:
        drawColumn(i, max(values), odd, lineHeight, maxColumnHeight, graphStep, lowerBorder,
                   darkColumnFill, lightColumnFill)
        odd = not(odd)
    """currentColumnHeight = lineHeight - (lineHeight - maxColumnHeight) * points[2] / max(values)
    canvas.create_rectangle(graphStep * (ints[len(ints)-1][0] - lowerBorder + 1), maxColumnHeight, 
                            9999, lineHeight, 
                            fill = darkColumnFill)"""

def makeIntervals(points, values):
    intervals = []
    for i in range(0,len(points)-1):
        intervals.append([])
        intervals[i].append(points[i])
        intervals[i].append(points[i+1])
        intervals[i].append(values[i])
    return intervals

def makePoints(start, step, range):
    return list(i * step + start for i in range(0,count))

def changeValuesCallback():
    points = list(int(s) for s in pointsString.get().split())
    values = list(int(s) for s in valuesString.get().split())
    if(len(points) == 0) or (len(values) == 0):
        messagebox.showerror("Ошибка", "Введены неправильные данные")
    elif(len(points) - len(values) != 1):
        messagebox.showerror("Ошибка", "Количество значений интервалов должно быть\nна единицу меньше количества концов интервалов")
    else:
        drawBarChart(points, values)

def validateIntegersString(var):
    var.set(re.sub(r'[^(\d | ' ')]+|(?<= ) +|(?<=^) +','',var.get()))
    #var.set(''.join(re.findall(r'(\-?\d+\ ?)+',var.get())))

def fillStringVarFromArray(var, array):
    var.set(' '.join(str(i) for i in array))

def distributionFunction(values):
    dist = []
    for i in range(0,len(values)):
        dist.append(sum(values[:(i+1)]))
    return dist

graphWidth    = 500
graphHeight   = 500
backgroundFill = "#FCFAE3"

root = Tk()
root.title("Гистограмма")
root.resizable(height = False, width = False)
root.wm_iconbitmap("favicon.ico")
root.geometry(str(graphWidth) + 'x' + str(graphHeight+60))

canvas = Canvas(root, width = graphWidth, height = graphHeight, bg = backgroundFill)

points = [ 6, 10, 14, 18, 22, 26, 30, 34, 38, 42 ]
values = [ 15, 26, 25, 30, 26, 21, 24, 20, 13 ]

drawBarChart(points, distributionFunction(values))

pointsLabel = Label(root, text="Концы интервалов: ")
pointsString = StringVar()
pointsString.trace('w', lambda nm, idx, mode, var=pointsString: validateIntegersString(var))
pointsField = Entry(root, textvariable = pointsString, width = 28)
fillStringVarFromArray(pointsString, points)

valuesLabel = Label(root, text="Значения интервалов: ")
valuesString = StringVar()
valuesString.trace('w', lambda nm, idx, mode, var=pointsString: validateIntegersString(var))
valuesField = Entry(root, textvariable = valuesString, width = 28)
fillStringVarFromArray(valuesString, values)

pointsButton = Button(root, text="Сделать гистограмму", command = changeValuesCallback)

canvas.place(bordermode = OUTSIDE)
pointsLabel.place(bordermode = OUTSIDE, y = graphHeight + 5)
pointsField.place(bordermode = OUTSIDE, y = graphHeight + 5, x = 150)
valuesLabel.place(bordermode = OUTSIDE, y = graphHeight + 30)
valuesField.place(bordermode = OUTSIDE, y = graphHeight + 30, x = 150)
pointsButton.place(bordermode = OUTSIDE, y = graphHeight + 15, x = 350)
root.mainloop()