from itertools import cycle
from tkinter import *
 
root = Tk()
root.title("DayNight")
root.geometry('800x800')


canv = Canvas(root,bg='orange')
canv.pack(fill=BOTH,expand=1)
canv.create_text(770, 400, 
              text="MAKSIMKA",
              justify=CENTER, font="Verdana 14")
def clear(event):
    canv.delete(ALL)
    canv.create_rectangle(0,0,1600,1600, fill='black', outline='black')
    canv.create_oval(50,50,180,180,fill='grey', outline="grey")
    canv.create_polygon([800,50],[780,80],[820,80],fill="yellow", outline="yellow")
    canv.create_polygon([780,60],[800,90],[820,60],fill="yellow", outline="yellow")
    
    canv.create_polygon([1200,80],[1180,110],[1220,110],fill="yellow", outline="yellow")
    canv.create_polygon([1180,90],[1200,120],[1220,90],fill="yellow", outline="yellow")
    
    canv.create_polygon([400,400],[380,430],[420,430],fill="yellow", outline="yellow")
    canv.create_polygon([380,410],[400,440],[420,410],fill="yellow", outline="yellow")
    
    canv.create_polygon([1000,400],[980,430],[1020,430],fill="yellow", outline="yellow")
    canv.create_polygon([980,410],[1000,440],[1020,410],fill="yellow", outline="yellow")
def paint(event):
    canv.create_rectangle(0,0,1600,1600, fill='white', outline='white')
    canv.create_oval(50,50,180,180,fill='yellow', outline="yellow")
    
    canv.create_oval(200, 100, 330, 190,fill='blue', outline="blue")
    canv.create_oval(200, 100, 430, 190,fill='blue', outline="blue")
    
    canv.create_oval([400,250],[600,350],fill="blue", outline="blue")
    canv.create_oval([350,300],[500,350],fill="blue", outline="blue")
    
  
btn1 = Button(text = "Day", width = 10, bd = 10)  
btn1.pack()
btn2 = Button(text = "Night", width = 10, bd = 10)  
btn2.pack()
btn1.bind("<Button-1>", paint)
btn2.bind('<Button-1>', clear)
mainloop()
