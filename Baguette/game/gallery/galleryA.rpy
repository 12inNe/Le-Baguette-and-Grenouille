init python:
    g = Gallery()

    g.button("pg1_1")
    g.condition("persistent.cg1")
    g.image(im.Scale("CGs/cg1.png",1920,1080))

    g.button("pg1_2")
    g.condition("persistent.cg2")
    g.image(im.Scale("CGs/cg2.png",1920,1080))

    g.button("pg1_3")
    g.condition("persistent.cg3")
    g.image(im.Scale("CGs/cg3.png",1920,1080))




screen galleryA:
    tag menu
    add "gui/gallery.png"
    hbox:
        yalign 0.5
        xalign 0.5

        use gallery_navigation

        grid 3 1:
            spacing 25

            ## Row 1
            add g.make_button("pg1_1",(im.Scale("CGs/cg1.png",280,158)), locked = "CGs/preview/locked.png")
            add g.make_button("pg1_2",(im.Scale("CGs/cg2.png",280,158)), locked = "CGs/preview/locked.png")
            add g.make_button("pg1_3",(im.Scale("CGs/cg3.png",280,158)), locked = "CGs/preview/locked.png")
