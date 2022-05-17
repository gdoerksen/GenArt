
def setup():
    size(1000,1000)
    background(255, 255, 255)
    
    circle_radius = 150
    shadow_offset_pct = 0.1
    
    colors1 = ["#264653","#2a9d8f","#e9c46a","#f4a261","#e76f51"]
    colors2 = ["#8ecae6","#219ebc","#023047","#ffb703","#fb8500"]
    colors3 = ["#5f0f40","#9a031e","#fb8b24","#e36414","#0f4c5c"]
    color_palettes = [colors1, colors2, colors3]
    
    color_palette = color_palettes[ int(random(len(color_palettes))) ]

    noStroke()
    for c in range(30):
        center_x = random(200, 800)
        center_y = random(200, 800)
        
        fill(15, 15, 15, 5)
        for i in range(30):
            shadow_x = center_x + circle_radius*shadow_offset_pct
            shadow_y = center_y + circle_radius*shadow_offset_pct
            circle(shadow_x, shadow_y, circle_radius - i*5)
    
        noStroke()
        color_choice = color_palette[ c % len(color_palette) ]
        fill(color_choice)
        circle(center_x, center_y, circle_radius)
