# Define some point and click objects
default classroom_badge = pnco(
    "Badge",
    "hidden object/classroom/badge.png",
    (81, 1010),
    items = ["Badge"]
    )
default classroom_book = pnco(
    "Book",
    "hidden object/classroom/book.png",
    (799, 806),
    items = ["Book"]
    )
default classroom_diary = pnco(
    "Diary",
    "hidden object/classroom/diary.png",
    (1788, 1003),
    items = ["Diary"]
    )
default classroom_letter = pnco(
    "Letter",
    "hidden object/classroom/letter.png",
    (1323, 875),
    items = ["Letter"]
    )
default classroom_outfit = pnco(
    "Outfit",
    "hidden object/classroom/outfit.png",
    (300, 520),
    items = ["Outfit"]
    )
default classroom_potion = pnco(
    "Potion",
    "hidden object/classroom/potions.png",
    (1700, 622),
    items = ["Potion"]
    )
default classroom_scyth = pnco(
    "Scyth",
    "hidden object/classroom/scyth.png",
    (739, 458),
    items = ["Scyth"]
    )
default classroom_door = pnco(
    "Door",
    "hidden object/classroom/door.png",
    (885, 380),
    items = ["Door"]
    )
default classroom_shelf = pnco(
    "Shelf",
    "hidden object/classroom/shelf.png",
    (111, 1050),
    items = ["Shelf"]
    )

# Define a point and click location
default room_1 = pncs(
    "Classroom",
    [
        classroom_door,
        
    ],
    
)

default room_2 = pncs(
    "Classroom",
    [
        classroom_badge,
        classroom_letter,
        classroom_outfit,
        
    ],
    darkness = "darkness"
    
)

default room_3 = pncs(
    "Classroom",
    [
       
        classroom_potion,
        classroom_book,

    ],
    
)

default room_4 = pncs(
    "Classroom",
    [
  
        classroom_diary,
        classroom_shelf
 
    ],
    darkness = "darkness"
    
)

default room_5 = pncs(
    "Classroom",
    [

        classroom_scyth,
        
    ],
    
)

default room_6 = pncs(
    "Classroom",
    [

      
    ],
    
)







label hidden_object_example:
    show bg classroom
    call screen pnc(p = None, g=hidden_object)
    if _return:
        "Great you've got everything."
    else:
        "Looks like something is missing."
        "Are you sure you have everything?"