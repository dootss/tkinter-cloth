from tkinter import *
from simulation import Cloth

def button_pressed(event):
    global drag, drag_pos
    drag = True
    drag_pos = (event.x, event.y)
    cloth.start_drag(drag_pos)

def button_released(event):
    global drag
    drag = False
    cloth.end_drag()

def reset_cloth(event):
    global cloth
    cloth = Cloth(offset=(500,0), screen_size=(1400,1000))

def draw_links():
    for link in cloth.links:
        canvas.create_line(link.p1.x, link.p1.y, link.p2.x, link.p2.y)

def update_cloth():
    global drag, cloth
    root.update()

    if drag == True:
        mouse_pos = (root.winfo_pointerx() - root.winfo_rootx(), root.winfo_pointery() -root.winfo_rooty())
        cloth.drag(mouse_pos[0]-drag_pos[0],mouse_pos[1]-drag_pos[1])

    cloth.update()
    canvas.delete(ALL)
    draw_links()

    root.after(0, update_cloth)

root = Tk()
root.geometry("1400x1000")
root.title("Physics Simulation")

canvas = Canvas(root, width=1400, height=1000)
canvas.pack()

cloth = Cloth(offset=(500, 0), screen_size=(1400, 995))

drag = False
drag_pos = None

canvas.bind("<ButtonPress-1>", button_pressed)
canvas.bind("<ButtonRelease-1>", button_released)
root.bind("<KeyPress-r>", reset_cloth)

root.after(0, update_cloth)
root.mainloop()
