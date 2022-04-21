symbols = ['\u250c', '\u2500', '\u2510',
               '\u2502', ' TEXT ', '\u2502',
               '\u2514', '\u2500', '\u2518']
def box_func(length, width):
    ul_corner = '\u250c'
    ur_corner = '\u2510'
    bl_corner = '\u2514'
    br_corner = '\u2518'
    vertical_pipe = '\u2502'
    horizontal_pipe = '\u2500'
    
    print(ul_corner, end='')
    print(horizontal_pipe * length)
    print(ur_corner)
    print(f'{vertical_pipe}')
    
