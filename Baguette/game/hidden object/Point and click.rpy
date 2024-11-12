init python:

    def item_collection_dialogue(item_name):
        renpy.say(None, "You've found {}.".format(item_name))

    class pnco:
        def __init__(self, name, img, pos,
            act = None, enabled = True, items = []
        ):
            self.name = name
            self.img = img
            self.pos = pos
            self.act = act
            self.enabled = enabled
            self.items = items

    class pncs:
        def __init__(self, name, clicks = [], darkness = None):
            self.name = name
            self.clicks = clicks
            self.darkness = darkness
        def clicked(self, o, p):
            if o.items:
                # Trigger a dialogue for the first item in `o.items`
                item_name = o.items.pop(0)  # Removes the item from list
                self.clicks.remove(o) if not o.items else None
                item_collection_dialogue(item_name)
        def add(self, click):
            if not click in self.clicks:
                self.clicks.append(click)
                msg.msg("New location: {}".format(click.name))
        def rem(self, click):
            if click in self.clicks:
                self.clicks.remove(click)
        def items_left(self):
            for i in self.clicks:
                if len(i.items):
                    return True
            else:
                return False

screen pnc(m,p , g, isMap = False):
    modal True
    for i in g.clicks:
        if isinstance(i, basestring):
            add i
        else:
            button:
                background None padding 0,0
                pos i.pos
                add i.img
                focus_mask True
                if isMap:
                    anchor .9,1.0
                    at btn
                else:
                    anchor 0.0,0.0
                    at map_btn
                if i.enabled:
                    if i.act:
                        action Function(g.clicked, i, p), i.act
                    else:
                        action Function(g.clicked, i, p)

    #text "[persistent.clue]"                     

    if m.map[m.y][m.x][2][0]:  # Up
        button:
            align (0.5,0.0)
            padding 40, 40
            margin 40, 40
            text "/\\" style "button_text_exploring"
            action Function(m.move, 0)
            keysym "w"
    if m.map[m.y][m.x][2][1]:  # Left
        button:
            align (0.0,0.5)
            padding 40, 40
            margin 40, 40
            text "<<" style "button_text_exploring"
            action Function(m.move, 1)
            keysym "a"
    if m.map[m.y][m.x][2][2]:  # Down
        button:
            align (0.5,1.0)
            padding 40, 40
            margin 40, 40
            text "\/" style "button_text_exploring"
            action Function(m.move, 2)
            keysym "s"
    if m.map[m.y][m.x][2][3]:  # Right
        button:
            align (1.0,0.5)
            padding 40, 40
            margin 40, 40
            text ">>" style "button_text_exploring"
            action Function(m.move, 3)
            keysym "d"

    default mouse = (0,0)
    if g.darkness:
        timer 0.02 repeat True action SetScreenVariable("mouse", renpy.get_mouse_pos())
        add g.darkness pos mouse align .5,.5 at additive(.02)
init python:
    def return_mouse_pos():
        return renpy.get_mouse_pos()
    def item_collection_dialogue(item_name):
        renpy.call("item_found_dialogue", item_name=item_name)

label item_found_dialogue(item_name):
    play sound "clk.mp3"
    if item_name == "Badge":
        MC "Are those... Guild... Badges?"
        MC "Did she just... KILL all of them!? But... Why do they all look so clean?"
        MC "That's weird. There should be no reason for her to wash the blood on these badges when no one is supposed to see this. What could be the reason for that?"
        scene black
        centered "{=centered_text}--Clue has been found--{/centered_text}"
        hide black
        $ persistent.clue += 1

    elif item_name == "Outfit":
        MC "Maid outfit? with BLOOD???"
        MC "Purple blood? Looks like it didn’t come from humans."
        MC "And that part was ripped? Looks like it came from something sharp."
        scene black
        centered "{=centered_text}--Clue has been found--{/centered_text}"
        hide black
        $ persistent.clue += 1

    elif item_name == "Letter":
        MC "What are these… letters? Sealed with wax and addressed to… humans? They’re unopened."

        MC "There’s one for a ‘Commander of the Order of the Sun.’ Did she try to reach out to the human military?"

        "“Esteemed Commander, I seek only peace between our realms. This ongoing hostility harms us all. Perhaps we can meet and discuss a way to end the cycle of bloodshed. Yours, Azumi.”"

        MC "So she was reaching out, trying to negotiate peace? And they didn’t even bother to open them."

        scene black
        centered "{=centered_text}--Clue has been found--{/centered_text}"
        hide black
        $ persistent.clue += 1
    elif item_name == "Potion":  
        MC "Potion bottles? These seem… strange to keep in a kitchen."

        MC "They’re labeled… but with odd symbols. Some are marked with a symbol for ‘health’ and others for ‘protection.’ Why would a demon stock health potions in her kitchen?"

        MC "One bottle says, ‘Healing for injured travelers - effects on humans only.’ Was she… preparing these for human use?"

        MC "Why would a supposed enemy have such items ready, and in the kitchen of all places?"

        scene black
        centered "{=centered_text}--Clue has been found--{/centered_text}"
        hide black
        $ persistent.clue += 1
    elif item_name == "Scyth":
        MC "Scythe? I don’t remember there being this weapon in town. Maybe it belongs to the demon queen?"

        MC "The thickness of the blade is about…. 1.8 to 2 centimeters."

        MC "Thinking about being the one who was killed with this. *Gross*"

        MC "Ow!!"

        "You jerked your head back, And seeing blood on your finger"
        MC "How is it this sharp? Did she have time to repair it?"

        scene black
        centered "{=centered_text}--Clue has been found--{/centered_text}"
        hide black
        $ persistent.clue += 1
    elif item_name == "Book":
        MC "A recipe book? That’s unexpected… I wouldn’t imagine her spending time on something as mundane as cooking."

        MC "And she’s not just following the recipes… She’s making adjustments. There are notes in the margins… all about ways to improve flavor, even adding specific spices for certain seasons. Seems like she’s really put thought into this."

        MC "Wait… Some of these notes are specifically about dishes humans might like. She’s… practicing dishes that human visitors would enjoy?"

        MC "Why go to all that effort? And who would even come here to eat? Did she really… want guests?"
        scene black
        centered "{=centered_text}--Clue has been found--{/centered_text}"
        hide black
        $ persistent.clue += 1
    elif item_name == "Shelf":
        MC "What are these… stories about demons? They speak of the 'Kind Demon,' one who protects the innocent and seeks peace with humanity."

        MC "These notes… they’re written by Tsukino. It says: 'Perhaps there is truth in this legend.'"

        MC "Is she actually trying to embody this myth? Does she believe she can change how humans see demons?"

        MC "Why would she think kindness could overcome hatred? How naive can one be? All this time, and they still think peace is an option."

        MC "They're myths for a reason—fantasies that humans created to cope with their fears. She’s chasing shadows."
        
        scene black
        centered "{=centered_text}--Clue has been found--{/centered_text}"
        hide black
        $ persistent.clue += 1
                 
    elif item_name == "Diary":
        MC "A Diary? It’s written in pretty handwriting about her usual life. But there are marks on some pages"

        nvl clear
        Narr "(Day 285)"
        Narr "It’s been a while since we have any contact with humans, and today there is a knight who had come to my castle, strange.What's even stranger is that for some unknown reason the knight tried to kill me without saying any single word. But Why? What did I do wrong?" 
        nvl clear
        Narr "(Day 380)"
        Narr "This is the 13th time that a deaf knight has come with a purpose of killing me again, this situation is getting weird. Why does every human who gets into my castle want to kill me?"
        nvl clear
        Narr "(Day 441)"
        Narr "His citizens are slain by me??? What are those knights even talking about? All they do is talking nonsense about my murderous intent to humans but I didn’t didn’t remember doing such a thing at all"
        "After checking a lot of marked pages, it’s full of the Demon questioning herself about humans who have come to kill her, but there seems to be no page which implies about the curse yet."
        "Continue reading the diary."
        nvl clear
        Narr "(Day 633)" 
        Narr "I can’t hold it anymore, I’ve been giving myself a false hope again and again that there will be a single human who I can reason with, but no.. none of them tried to reason with me. Hell, not even say a single word before they strike. What is wrong with these people.. or is it me who is on the wrong side? But what did I even do to them?" 
        Narr "Maybe this is the last chance I’m gonna hold back. I have to do something."
        nvl clear
        Narr "(Day 651)" 
        Narr "I have to do it… I really have to, I try my hardest not to cause any harm to them but of course none of them listen. I have to use it, I cursed all those foolish humans. It was just self-protection, it’s not my entire fault, those knights make me have to do such a thing. Yes I must do it for myself . . . and for Tsukino."
        nvl clear
        Narr "(Day 654)" 
        Narr "It’s been half a week since the last time I encountered those knights. It's good news so far, I hope I didn’t go too far with it."
        nvl clear
        Narr "      "
        "Flip to the next page, but there are blanks."
        MC "She seems to be traumatized? But what about my citizens? Is it really necessary to curse all of the citizens? Maybe she lied and tried to make herself feel like being on the right side? It’s her own diary after all"

        scene black
        centered "{=centered_text}--Clue has been found--{/centered_text}"
        hide black
        $ persistent.clue += 1 
    
    
    elif item_name == "Door":
        jump chapter6



transform map_btn:
    on idle:
        easein .2 additive 0
    on hover:
        easein .2 additive .3

    on insensitive:
        easein .2 additive 0


