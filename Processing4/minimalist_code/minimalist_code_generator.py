w, h = 1000, 1000

class MinimalCodeGenerator():
    i = 0
    code_start = h/20
    code_end = h - h/20
    lines_of_code = 30
    line_sep = (code_end - code_start) / lines_of_code
    tab_sep = 50
    segment_sep = 20
    line_y = code_start
    left_x = 50
    indent = 0
    indent_max = 2

    tab_pct_chance = 0.25

    code_colors = [ "#BB86FC", "#03DAC6", "#CF6679" ]



    state_enum = {
        "function_start" : 0,
        "function_end" : 1,
        "write": 2
                }

    state = state_enum["function_start"]

    def generate(self):
        while self.i < self.lines_of_code:
            self.advance()

    def advance(self):
        if self.state == self.state_enum["write"]:
            self.write_state()
        elif self.state == self.state_enum["function_start"]:
            self.function_start_state()
        elif self.state == self.state_enum["function_end"]:
            self.function_end_state()

    def write_state(self):
        self.line_segments = int(random(2, 8))
        self.write_line()
        
        if ( random(1) < self.tab_pct_chance and self.indent < self.indent_max ):
            self.indent += 1 
        elif ( random(1) < self.tab_pct_chance and self.indent > 0 ):
            self.indent -= 1
        
        if self.indent == 0:
            self.state = self.state_enum["function_end"]

        
    def function_start_state(self):
        self.line_segments = 3
        self.change_color()
        self.write_line()
        self.indent += 1
        self.state = self.state_enum["write"]
        
    def function_end_state(self):
        self.carriage_return()
        self.state = self.state_enum["function_start"]


    def write_line(self):
        self.line_x = self.left_x + (self.tab_sep * self.indent)
        for i in range(self.line_segments):
            self.segment_length = random(10, 80)
            line(self.line_x, self.line_y, self.line_x + self.segment_length, self.line_y)
            self.line_x += self.segment_length + self.segment_sep
        self.carriage_return()

    def change_color(self):
        self.line_color = self.code_colors[ int(random(len(self.code_colors))) ]
        stroke(self.line_color)

    def carriage_return(self):
        self.line_y += self.line_sep
        self.i += 1

def setup():
    size(w, h)
    background("#121212")
    
    strokeWeight(12)
    strokeCap(ROUND)
    
    codeGenerator = MinimalCodeGenerator()
    codeGenerator.generate()
