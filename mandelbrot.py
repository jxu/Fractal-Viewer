from tkinter import *
# import colorsys colorspace conversion

# PARAMETERS
ITERATIONS = 50
WIDTH, HEIGHT = 600, 600
# Mandel zoom 03
CENTER = (-.5, 0)
DIAMETER = 3.0

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
    colors = ("#EEEEEE", "#CCCCCC", "#AAAAAA", "#999999", "#777777", 
              "#555555", "#000000")
    if i == ITERATIONS:
        return colors[-1]
    else:
        return colors[(i//2) % len(colors)]


def draw(image):
    """Puts all pixels, from top to bottom."""
    full = ""
    
    D_HEIGHT = DIAMETER / HEIGHT
    D_WIDTH = DIAMETER / WIDTH
    
    real = CENTER[0] - DIAMETER/2
    imag = CENTER[1] + DIAMETER/2
    real_copy = real
    #print(real, imag)
    
    for y in range(HEIGHT):
        horizontal_line = []
        
        for x in range(WIDTH):         
            i = mandel(complex(real, imag))
            horizontal_line.append(color(i))
            
            real += D_WIDTH

        imag -= D_HEIGHT
        real = real_copy
         
        line_str = '{' + " ".join(horizontal_line) + '}'
        full += line_str + ' '
        
    image.put(full)
        
        
photo = PhotoImage(width=WIDTH, height=HEIGHT)
draw(photo)

label = Label(root, image=photo)
label.grid()
root.mainloop()

