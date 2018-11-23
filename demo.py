import tkinter as tk
import math
import tkinter.font as tkfont

class DemoFrame(tk.Frame):
  @staticmethod
  def colornames():
    names = []
    with open('colornames.txt') as f:
      for line in f:
        line = line.strip()
        if '#' in line:
          continue
        if len(line)>0:
          names.append(line)
    return names

  def showColors(self, colors:list, numPerRow:int):
    """rowCount：how many items in a row"""
    total = len(colors)
    rowCount = math.ceil( total/numPerRow)
    labelfont = tkfont.Font(size=8)
    for rowNo in range(rowCount):
      for columnNo in range(numPerRow):
        i = numPerRow * rowNo + columnNo
        if i>=total:
          break
        color = colors[i]
        print("adding {i}/{total} {color}".format(i=i,total=total,color=color))

        label = tk.Label(self, text=str(i)+color,font=labelfont, background=color)
        label.grid(row=rowNo,column=columnNo,sticky=tk.NSEW)



if __name__ == '__main__':
  root = tk.Tk()
  root.title('tkColorDemo')
  f = DemoFrame(root)
  f.pack()
  numPerRow=15
  f.showColors(DemoFrame.colornames(),numPerRow)
  root.mainloop()
