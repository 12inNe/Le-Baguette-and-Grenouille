transform zoom(z, t = 0):
    subpixel True
    ease t zoom z

transform rotate(r, t = 0):
    subpixel True
    rotate_pad False
    ease t rotate r

transform spin(s):
    subpixel True
    rotate_pad False
    rotate 0
    linear s rotate 360
    repeat

transform additive(a, t = 0):
    ease t additive a