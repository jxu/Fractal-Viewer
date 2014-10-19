from tkinter import *
# import colorsys colorspace conversion


# PARAMETERS
ITERATIONS = 10
WIDTH, HEIGHT = 600, 600
# Mandel zoom 03
CENTER = (-.5, 0)
DIAMETER = 2.5

def mandel(c):
    z = 0
    for i in range(ITERATIONS):
        z = z*z + c
        if abs(z) > 2:
            return i     
    return ITERATIONS

print("Starting...")
root = Tk()


def color(i):
    colors = ("#DDDDDD", "#AAAAAA", "#666666", "#000000")
    if i == ITERATIONS:
        return colors[-1]
    else:
        choice = (i) % len(colors)
    return colors[choice] 

def draw(image):
    full = ""
    
    D_HEIGHT = DIAMETER / HEIGHT
    D_WIDTH = DIAMETER / WIDTH
    
    real = CENTER[0] - DIAMETER/2
    imag = CENTER[1] + DIAMETER/2
    
     
    print(real, imag)
    
    for y in range(HEIGHT):
        horizontal_line = []
        
        
        for x in range(WIDTH):         
            i = mandel(complex(real, imag))
            horizontal_line.append(color(i))
            
            real += D_WIDTH

        imag -= D_HEIGHT
        real = CENTER[0] - DIAMETER//2
         
        horizontal_line = '{' + " ".join(horizontal_line) + '}'
        full += horizontal_line + ' '
        
    image.put(full)
        
    print(real, imag)
        
photo = PhotoImage(width=WIDTH, height=HEIGHT)
draw(photo)

label = Label(root, image=photo)
label.grid()
root.mainloop()


