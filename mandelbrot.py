from tkinter import *
# import colorsys colorspace conversion

# Parameters 
ITERATIONS = 40
WIDTH, HEIGHT = 600, 600 # Mandel zoom 03
CENTER = (-.5, 0.9)
DIAMETER = 1.0

PALATE = "GRAY1"
COLOR_SMOOTHING = False


# Color palates 
GRAY1   = ("#EEEEEE", "#CCCCCC", "#AAAAAA", "#999999", "#777777", 
           "#555555", "#000000")
BW      = ("#FFFFFF", "#000000")

def mandel(c):
    z = 0
    for i in range(ITERATIONS):
        z = z*z + c
        if abs(z) > 2:
            return i     
    return ITERATIONS



def color(i, colors):
    return colors[round(i/ITERATIONS * (len(colors)-1))]


def draw(image):
    """Puts all pixels, from top to bottom."""
    print("Starting...")
    full = ""
    
    D_HEIGHT = DIAMETER / HEIGHT
    D_WIDTH = DIAMETER / WIDTH
    
    real = CENTER[0] - DIAMETER/2
    imag = CENTER[1] + DIAMETER/2
    real_copy = real
    #print(real, imag)
    
    colors = eval(PALATE) # Pre-load color table
    
    for y in range(HEIGHT):
        horizontal_line = []
        
        for x in range(WIDTH):         
            i = mandel(complex(real, imag))
            horizontal_line.append(color(i, colors))
            
            real += D_WIDTH

        imag -= D_HEIGHT
        real = real_copy
         
        line_str = '{' + " ".join(horizontal_line) + '}'
        image.put(line_str)
        full += line_str + ' '
        
    image.put(full)
    
def main():   
    root = Tk()
    photo = PhotoImage(width=WIDTH, height=HEIGHT)
    draw(photo)
    
    label = Label(root, image=photo)
    label.grid()
    root.mainloop()
    
main()