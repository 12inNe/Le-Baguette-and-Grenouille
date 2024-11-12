init python:
    class location:
        def __init__(self, name, map, x = 0, y = 0):
            self.name = name
            self.map = map
            self.x = x
            self.y = y
            self.bg = self.map[self.y][self.x][0]
            self.transition  = dissolve
        def move(self, direction):
            if direction == 0:
                self.y -= 1
                # self.transition = pushdown
            elif direction == 1:
                self.x -= 1
                # self.transition = pushright
            elif direction == 2:
                self.y += 1
                # self.transition = pushup
            elif direction == 3:
                self.x += 1
                # self.transition = pushleft

            self.bg = self.map[self.y][self.x][0]
            return 1
    class map_maker_handler:
        def __init__(self, map, wh):
            self.places = [
                "Beast's den",
                "Black stone",
                "Britanistan",
                "Cavemn",
                "Cliff edge city",
                "Clinger town",
                "Dread castle",
                "Electric post",
                "End lands",
                "Fairy cove",
                "Green falls",
                "Junk yard",
                "Oil soak",
                "Polluted side",
                "Pound side",
                "Salt bed boat",
                "Summits",
                "The factory town",
                "The lone cliff",
                "The old mill",
                "The river",
                "The view",
                "Upstream",
                "White castle",
            ]
            self.map = map
            self.wh = wh
        def set_name(self, nn, n, i):
            self.map[nn][n][0] = i

        def change_direction(self, nn, n, direction):
            if self.map[nn][n][2][direction]:
                self.map[nn][n][2][direction] = 0
            else:
                self.map[nn][n][2][direction] = 1
        def add_row(self):
            r = []
            for i in self.map[0]:
                r.append(["", False, [0,0,0,0]])
            self.map.append(r)
        def add_column(self):
            for ii,i in enumerate(self.map):
                self.map[ii].append(["", False, [0,0,0,0]])
        def copy(self):
            t = str(self.map)
            clip_put(t)

default map_create = map_maker_handler(
    [
        [ ["",False, [0,0,0,0]], ["",False, [0,0,0,0]] ],
    ],
    200,
)
screen map_maker(g = map_create):
    modal True
    vbox:
        spacing 0
        for nn,ii in enumerate(g.map):
            hbox:
                spacing 0
                for n,i in enumerate(ii):
                    button:
                        padding 0,0 xsize g.wh ysize g.wh
                        if i[0] == None:
                            background None
                        else:
                            text i[0] at rotate(-45)
                        action Show("map_location_selector", g = g, nn=nn, n=n)
                        button:
                            if not i[2][0]:
                                background None
                            yalign 0.0
                            text "w"
                            action Function(g.change_direction, nn, n, 0)
                        button:
                            if not i[2][1]:
                                background None
                            xalign 0.0
                            text "a"
                            action Function(g.change_direction, nn, n, 1)
                        button:
                            if not i[2][2]:
                                background None
                            yalign 1.0
                            text "s"
                            action Function(g.change_direction, nn, n, 2)
                        button:
                            if not i[2][3]:
                                background None
                            xalign 1.0
                            text "d"
                            action Function(g.change_direction, nn, n, 3)

    button:
        xalign 0.0
        text "Add row"
        action Function(g.add_row)
    button:
        yalign 0.0
        text "Add column"
        action Function(g.add_column)
    button:
        align 0.0,0.0
        text "Copy"
        action Function(g.copy)
        # text g.copy()
transform rotate(r):
    rotate_pad False
    rotate r
screen map_location_selector(g, nn, n):
    modal True
    hbox:
        box_wrap True
        for i in g.places:
            button:
                text i
                action Function(g.set_name, nn, n, i), Hide("map_location_selector")
        button:
            text "None"
            action Function(g.set_name, nn, n, None), Hide("map_location_selector")
            keysym "`"

screen explore(g):
    modal True
    if g.map[g.y][g.x][2][0]:  # Up
        button:
            align (0.5,0.0)
            padding 40, 40
            margin 40, 40
            text "/\\" style "button_text_exploring"
            action Function(g.move, 0)
            keysym "w"
    if g.map[g.y][g.x][2][1]:  # Left
        button:
            align (0.0,0.5)
            padding 40, 40
            margin 40, 40
            text "<<" style "button_text_exploring"
            action Function(g.move, 1)
            keysym "a"
    if g.map[g.y][g.x][2][2]:  # Down
        button:
            align (0.5,1.0)
            padding 40, 40
            margin 40, 40
            text "\/" style "button_text_exploring"
            action Function(g.move, 2)
            keysym "s"
    if g.map[g.y][g.x][2][3]:  # Right
        button:
            align (1.0,0.5)
            padding 40, 40
            margin 40, 40
            text ">>" style "button_text_exploring"
            action Function(g.move, 3)
            keysym "d"

style button_text_exploring:
    size 60
    bold True
    color "#FFFFFF"  # Default (idle) color
    hover_color "#FFCC00"  # Hover color



transform explore_minimap_t(x,y):
    xoffset x yoffset y




default wastelands = location(
    _("Wastelands"),
    [
        [[None, False, [0, 0, 0, 0]], ['bg Fairy cove', False, [0, 0, 1, 1]], ['bg Junk yard', False, [0, 1, 0, 1]], ['bg Oil soak', False, [0, 1, 0, 1]], ['bg Electric post', False, [0, 1, 1, 0]]],
        [['bg Cavemn', False, [0, 0, 0, 1]], ['bg The factory town', False, [1, 1, 1, 0]], [None, False, [0, 0, 0, 0]], [None, False, [0, 0, 0, 0]], ['bg The view', False, [1, 0, 0, 0]]],
        [['bg White castle', False, [0, 0, 0, 1]], ['bg Fairy cove', False, [1, 1, 1, 0]], [None, False, [0, 0, 0, 0]], ['bg Summits', False, [0, 0, 0, 1]], ['bg Upstream', False, [0, 1, 1, 0]]],
        [[None, False, [0, 0, 0, 0]], ['bg Polluted side', False, [1, 0, 0, 1]], ['bg Junk yard', False, [0, 1, 0, 1]], ['bg Oil soak', False, [0, 1, 0, 1]], ['bg The river', False, [1, 1, 0, 0]]],
    ],
    0,1
)
default current_location = wastelands
label explore_example:
    window hide
    #show screen explore(current_location)
    if current_location.map[current_location.y][current_location.x][0] == 'bg The view':
        call screen pnc(p = None, g=room_1, m=current_location)
    elif current_location.map[current_location.y][current_location.x][0] == 'bg Oil soak':
        call screen pnc(p = None, g=room_4, m=current_location)
    elif current_location.map[current_location.y][current_location.x][0] == 'bg Electric post':
        call screen pnc(p = None, g=room_2, m=current_location)
    elif current_location.map[current_location.y][current_location.x][0] == 'bg White castle':
        call screen pnc(p = None, g=room_3, m=current_location)
    elif current_location.map[current_location.y][current_location.x][0] == 'bg Upstream':
        call screen pnc(p = None, g=room_5, m=current_location)
    else:
        call screen pnc(p = None, g=room_6, m=current_location)
    show black
    #with current_location.transition
    show expression current_location.bg.lower()
    
    
    jump explore_example

