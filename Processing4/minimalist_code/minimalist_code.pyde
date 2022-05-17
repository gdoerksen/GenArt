w, h = 1000, 1000

code_start = h/20
code_end = h - h/20
lines_of_code = 30
line_sep = (code_end - code_start) / lines_of_code
tab_sep = 50
segment_sep = 20

tab_pct_chance = 0.25

code_colors = [ "#BB86FC", "#03DAC6", "#CF6679" ]

def setup():
    size(w, h)
    background("#121212")
    
    strokeWeight(12)
    strokeCap(ROUND)

    
    line_y = code_start
    left_x = 50
    indent = 0
    indent_max = 2
    state = state_enum["function_start"]
    
    for i in range(lines_of_code):
        
        #advance(state)
        
        if ( indent == 0 ):
            line_segments = 3
            line_color = code_colors[ int(random(len(code_colors))) ]
            stroke(line_color)
        else:
            line_segments = int(random(2, 8))
            
        line_x = left_x + (tab_sep * indent)
        
        for j in range(line_segments):
            segment_length = random(10, 80)
            line(line_x, line_y, line_x + segment_length , line_y)
            
            line_x += segment_length + segment_sep

        #carriage_return()
        line_y += line_sep
        if( indent == 0 ):
            indent += 1
        elif ( random(1) < tab_pct_chance and indent < indent_max ):
            indent += 1 
        elif ( random(1) < tab_pct_chance and indent > 0 ):
            indent -= 1

def advance(state):
    if state == state_enum["write"]:
        write_state()
    elif state == state_enum["function_start"]:
        function_start_state()
    elif state == state_enum["function_end"]:
        function_end_state()

def write_state():
    pass
    
def function_start_state():
    line_segments = 3
    change_color()
    write_line()
    
def function_end_state():
    pass

def write_line():
    pass

def change_color():
    line_color = code_colors[ int(random(len(code_colors))) ]
    stroke(line_color)

def carriage_return():
    line_y += line_sep


# TODO could totally make a state machine to output real code like lines 

state_enum = {
    "function_start" : 0,
    "function_end" : 1,
    "write": 2
            }
