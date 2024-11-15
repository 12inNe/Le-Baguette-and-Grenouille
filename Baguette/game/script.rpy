﻿
init python:
    import random
    import time
    random.seed(time.time())

init python:
    def eyewarp(x):
        return x**1.33
    eye_open = ImageDissolve("Transitions/eye.png", .5, ramplen=128, reverse=False, time_warp=eyewarp)
    eye_shut = ImageDissolve("Transitions/eye.png", .5, ramplen=128, reverse=True, time_warp=eyewarp)

transform camera_identity(t = 0):
    ease t xpos 0 ypos 0 zpos 0 rotate 0 blur 0
transform camera_step(advance = 0, up = 0, lean = 5):
    parallel:
        ease 1 zpos -advance ypos -up
    parallel:
        ease .3 rotate lean
        ease .3 rotate -lean
        ease .4 rotate 0 
transform camera_drunk(t = 3, x = 10, y = 10, z = 50, r = 3, b = 3):
    parallel:
        ease t+t*random.random() blur b
        ease t+t*random.random() blur b*2
        repeat
    parallel:
        ease t+t*random.random() xpos x
        ease t+t*random.random() xpos -x 
        repeat
    parallel:
        ease t+t*random.random() ypos y
        ease t+t*random.random() ypos -y
        repeat
    parallel:
        ease t+t*random.random() zpos z
        ease t+t*random.random() zpos -z
        repeat
    parallel:
        ease t+t*random.random() rotate r
        ease t+t*random.random() rotate -r
        repeat
transform camera_quake(t = .1, x = 2, y = 10, z = 10):
    parallel:
        ease t xpos x
        ease t xpos -x 
        repeat
    parallel:
        ease t ypos -y
        ease t ypos y
        repeat
    parallel:
        ease t zpos z
        ease t zpos -z
        repeat
transform camera_y_quake(t = .1, x = 2, y = 10, z = 50, sway = 5):
    parallel:
        ease sway+t xpos x
        ease sway+t xpos -x 
        repeat
    parallel:
        ease t ypos -y
        ease t ypos y
        repeat
    parallel:
        ease sway+t+random.random() zpos z
        ease sway+t+random.random() zpos -z
        repeat
transform camera_x_quake(t = .1, x = 10, y = 2, z = 50, sway = 5):
    parallel:
        ease t xpos x
        ease t xpos -x 
        repeat
    parallel:
        ease sway+t ypos -y
        ease sway+t ypos y
        repeat
    parallel:
        ease sway+random.random() zpos z
        ease sway+random.random() zpos -z
        repeat
transform camera_shaky_cam(t = .05, x = 18, y = 18, z = 18, r = 5):
    matrixtransform RotateMatrix(0,0,0)
    parallel:
        ease t + (t * random.random()) xpos x
        ease t + (t * random.random()) xpos -x 
        repeat
    parallel:
        ease t + (t * random.random()) ypos -y
        ease t + (t * random.random()) ypos y
        repeat
    parallel:
        ease t + (t * random.random()) zpos z
        ease t + (t * random.random()) zpos -z
        repeat
    parallel:
        # ease t matrixtransform RotateMatrix(r * random.random(), r * random.random(), r * random.random())
        # ease t matrixtransform RotateMatrix(r * random.random(), r * random.random(), r * random.random())
        # ease t matrixtransform RotateMatrix(r * random.random(), r * random.random(), r * random.random())
        # ease t matrixtransform RotateMatrix(r * random.random(), r * random.random(), r * random.random())
        ease t + (t * random.random()) rotate r * random.random()
        ease t rotate -r * random.random()
        ease t + (t * random.random()) rotate r * random.random()
        ease t rotate -r * random.random()
        ease t + (t * random.random()) rotate r * random.random()
        ease t rotate -r * random.random()
        ease t + (t * random.random()) rotate r * random.random()
        ease t rotate -r * random.random()
        repeat
transform camera_heart_beat(t = .15, w = 3, z = 5):
    parallel:
        pause w
        ease t zpos -z
        ease t zpos z
        # pause t
        ease t zpos -z*4
        ease t zpos z*4
        repeat
transform camera_lean(t = 1, x = 0, y = 0, z = 0):
    matrixtransform RotateMatrix(0,0,0)
    ease t matrixtransform RotateMatrix(x, y, z)
transform camera_lean_2(t = 1, x = 0, y = 0, z = 0):
    ease t matrixtransform RotateMatrix(x, y, z)
transform test_3d_animation():
    perspective True
    rotate_pad False
    matrixtransform RotateMatrix(20,0,0)
    on idle:
        linear 3 matrixtransform RotateMatrix(20,360,0) additive 0
        repeat
    on hover:
        linear 1 matrixtransform RotateMatrix(40,0,0) additive .4

define transition_1 = ImageDissolve("images/Transitions/090.png", 2.0, time_warp=_warper.easeout)
define transition_2 = ImageDissolve("images/Transitions/073.png", 1.5, time_warp=_warper.easeout)
define transition_3 = ImageDissolve("images/Transitions/087.jpg", 1.0, time_warp=_warper.easeout)

define DQ = Character("Demon Queen", color="#D2691E")
define unknow = Character("???", color="#ffffff")
define OG = Character("OG", color="#8B0000")
define King = Character("King", color="#4682B4")
define MC = Character("[pov]", color="#2E8B57")
define BBQ = Character("Baguette God", color="#fad883")
define Azumi = Character("Azumi", color="#D2691E")
define Narr = nvl_narrator
define Tsukino = Character("Tsukino", color="#BA55D3")
define Dragon =  Character("Dragon", color="#e34949")
define Snake =  Character("Snake", color="#79ef84")
define Villager = Character("Villager", color="#fff")
define OlderVillager =Character("Older Villager", color="#fff")
image cg1 = im.Scale("images/CGs/cg1.png", 1920,1080)
image cg2 = im.Scale("images/CGs/cg2.png", 1920,1080)
image cg3 = im.Scale("images/CGs/cg3.png", 1920,1080)
image black:
    Solid("#000")
image white:
    Solid("#FFF")
image purple:
    Solid("#ca18be")
image blue:
    Solid("#211de5")
image red:
    Solid("#f83434")

image king normal = "images/king_normal.png"
image king sad = "images/king_sad.png"
image king smile = "images/king_smile.png"
image king talk = "images/king_talk.png"
image king tired = "images/king_tired.png"
image king tired_talk = "images/king_tired_talk.png"

image mc bag_die = "images/mc_bag_die.png"
image mc bag_normal = "images/mc_bag_normal.png"
image mc bag_scare = "images/mc_bag_scare.png"
image mc bag_smile = "images/mc_bag_smile.png"
image mc bag_talk = "images/mc_bag_talk.png"
image mc normal = "images/mc_normal.png"
image mc riz = "images/mc_riz.png"
image mc scare = "images/mc_scare.png"
image mc smile = "images/mc_smile.png"
image mc talk = "images/mc_talk.png"

image queen blush = "images/queen_blush.png"
image queen cast = "images/queen_cast.png"
image queen close = "images/queen_close.png"
image queen happy = "images/queen_happy.png"
image queen normal = "images/queen_normal.png"
image queen smile = "images/queen_smile.png"
image queen talk = "images/queen_talk.png"

image maid blush = "images/maid_blush.png"
image maid happy = "images/maid_happy.png"
image maid normal = "images/maid_normal.png"
image maid shi = "images/maid_shi.png"
image maid sleep = "images/maid_sleep.png"
image maid smile = "images/maid_smile.png"
image maid talk = "images/maid_talk.png"
image maid unhappy = "images/maid_unhappy.png"

style centered_text:
    color "#b5b5e9"  # Blue text color
transform middlepostsuru():
    align (0.5, 1.0)
    zoom 0.5
transform leftpostsuru():
    align (0.22, 1.0)
    zoom 0.5
transform rightpostsuru():
    align (0.75, 1.0)
    zoom 0.5
transform tsuru_close():
    align (0.5, 0.2)
    zoom 0.7

transform middleposdel():
    align (0.35, 1.0)
    zoom 0.5
transform leftposdel():
    zoom 0.6
    ypos 315
    xpos 200
transform rightpostdel():
    align (0.95, 1.0)
    zoom 0.5

transform middleposmild():
    align (0.5, 0.1)
    zoom 0.5
transform leftposmild():
    align (0.21, 0.1)
    zoom 0.38
transform rightposmild():
    align (1.0, 0.1)
    zoom 0.5
transform mild_close():
    align (0.5, 0.155)
    zoom 0.7

transform mildhood():
    align (0.75, 0.4)
    zoom 0.4
transform mildunhood():
    align (0.5, 0.4)
    zoom 0.4
transform mildunhood_close():
    align (0.5, 0.3)
    zoom 0.8
transform mildchibi():
    zoom 0.18
    ypos 620
    xpos 980
# The game starts here.

label start:
    $ persistent.maid_route = False
    $ persistent.clue = 0
    stop sound
    stop music
    scene throne with fade
    show queen_talk at middlepostsuru()
    camera:
        perspective True
    DQ "Halt!! Can't you just listen and think about this first!"
    camera at camera_identity(.2)
    OG "Enough Rambling, Monster. Your word doesn’t matter. And today, one of us will fall, and it's either YOU or ME!"
    $ renpy.music.play("the-law-of-the-samurai.mp3", loop=True)
    pause 1.0
    camera at camera_lean(2, 2, 2, 2)
    pause 1.0
    scene sw1
    play sound "sword.mp3"
    "{w=1}{nw}"
    camera at camera_step(0, 100)
    pause 1.0
    play sound "sword.mp3"
    "{w=1}{nw}"
    scene sw2
    play sound "clash.mp3"
    "{w=1}{nw}"
    camera at camera_lean_2(2, 5)
    pause 1.0
    scene sw3
    play sound "echo.mp3"
    "{w=1}{nw}"
    camera at camera_step(-2, 0, 2)
    pause 1.0
    camera at camera_lean_2(2, -2, -5)
    pause 1.0
    scene sw1
    scene sw2
    play sound "echo.mp3"
    scene sw3
    "{w=1}{nw}"
    camera at camera_heart_beat(.15, 3)
    pause 1.0
    "{w=1}{nw}"
    camera at camera_lean_2(2, 5)
    pause 1.0
    scene sw1
    play sound "sword.mp3"
    "{w=1}{nw}"
    camera at camera_lean(0,0,0,0)
    pause 1.0
    camera at camera_identity(0)
    scene throne 
    show queen_normal at middlepostsuru()
    OG "Stop moving around and just let’s end this here now, Monster!!!"
    DQ "*sigh* Another deaf knight with musclebrain again huh? Alright, if you want it that way.. Fine, I'm tired of this meaningless battle now."
    scene black with dissolve
    show queen_talk at middlepostsuru()
    DQ "Hope we’ll never meet again.. forever"
    stop music
    # DQ cast a giant magic.
    show queen_cast at middlepostsuru()
    OG "!!! What are you-"
    with dissolve 
    # Cut and transition into the next scene
    play sound "cast.mp3"
    scene blue with transition_2
    centered "{=centered_text}The Demon Queen raises her hands, the air around her beginning to hum with a strange energy.{/centered_text}" 
    play sound "circle.mp3"
    scene purple with transition_3
    centered "{=centered_text}A dark, swirling aura forms around her, growing thicker with every second.{/centered_text}" 
    play sound "cast.mp3"
    scene blue with transition_1
    centered "{=centered_text}Sparks of arcane energy flicker at her fingertips, illuminating the room in ominous flashes of purple and blue.{/centered_text}"
    play sound "circle.mp3"
    scene purple with transition_2
    centered "{=centered_text}A wave of dark magic surges outward from her, rippling through the castle and beyond, engulfing everything in its path.{/centered_text}"
    play sound "wave.mp3"
    scene white with eye_open
    centered "{=centered_text}A blinding flash fills the throne room, and when it fades...{/centered_text}"
    scene black with eye_shut
    centered "{=centered_text}..Everthing have changed..{/centered_text}"
    centered "{=centered_text}..What next?..{/centered_text}"
    centered "{=centered_text}..It just the start of the story..{/centered_text}"
    centered "{=centered_text}..And the end, Is yours..{/centered_text}"
    $ pov = renpy.input("What's your name for the journey:")

label chapter1:
    $ renpy.music.play("kingsong.mp3", loop=True)
    scene king room with fade
    show king_normal at rightpostsuru()
    show mc_normal at leftpostsuru()
    King "After the defeat of our hero, by the hatred of the Six-horn demon toward us, our kingdom has been put under the demon’s curse, which is why all our citizens have ended up like this..."
    show king_talk at rightpostsuru()

    King "Thus, that’s why we sought any brave soul who could free us from this curse once and for all. Especially for you, as your grandfather was a great adventurer back in time."

    menu:
        "So how exactly do I fix this":
            show mc_talk at leftpostsuru()
            MC "So how exactly do I fix this?"
            show king_tired_talk at rightpostsuru()
            King "There’s still a way, but..."
            hide mc_talk
            show mc_normal
            MC "What happened? You seem scared..."
            show king_tired at rightpostsuru()
            King "Since the last confrontation of our hero and the Six-horn demon, all the parties we sent to investigate have never been seen or heard from again."

            menu:
                "Then, I’ll do what needs to be done":
                    show mc_talk at leftpostsuru()
                    MC "Then, I’ll do what needs to be done."
                    hide king_tired
                    hide king_normal
                    show king_tired_talk at rightpostsuru()
                    King "A... Are you sure you can handle this on your own???"
                    hide mc_talk
                    show mc_riz at leftpostsuru()
                    MC "Nah, I’d win."
                    show king_smile at rightpostsuru()
                    King "Hohoho, that’s the spirit!"

                    King "Very well, Since you seem to be ready for this, here’s some money for your adventure and the map to show you the path to the castle of the Six-horn demon. I wish you luck on your journey, Hero."

                    "You received a bag of money and a map to the castle"

                    MC "So…."
                    show mc_talk at leftpostsuru()
                    MC "That means I can get access to the carriage or those horses for the mission for free, right?"
                    stop music
                    show king_sad at rightpostsuru()
                    King ". . ."
                    show mc_scare at leftpostsuru()
                    MC "... right?"

                    jump chapter2

                "I’m scared... I want to go home":
                    show mc_scare at leftpostsuru()
                    with dissolve
                    MC "I’m scared... I want to go home."
                    # Jump to bad joke end
                    jump bad_joke_end

        "That’s it, I’m going home":
            scene king room 
            show mc_scare at middlepostsuru()
            with dissolve
            MC "That’s it, I’m going home."
            # Jump to bad joke end
            jump bad_joke_end

label bad_joke_end:
    stop music
    window hide
    # Play the bad end video
    play movie "bad_end.webm"
    # Wait until the video finishes
    $ renpy.pause(5)  # Adjust the duration to match the video length if needed
    scene black
    # Jump back to the previous choice
    centered "{=centered_text}I will send you back to start again, OK?{/centered_text}"
    jump chapter1 # Or specify the exact menu label you want to return to

label chapter2:
    scene forest1
    $ renpy.music.play("walkingwood.mp3", loop=True)
    show map
    MC "Look like if I pass through this forest there’ll be a big demon castle eh? …Um, but how to use this map by the way."
    "You go into the forest with the map in his hand but somehow he is also a meat brain even with a map he has in his hand."
    scene dragon01 
    pause 1.0
    scene dragon02 with dissolve
    MC "With my adventurer sense I’m sure this is the right way-"
    scene dragon03 with dissolve
    Dragon ". . ."
    MC "Oh hello there big guy… wait…"
    MC "Ok Adventurer Rule number 34, If you encounter something too powerful, always use this spell…"
    scene forest1 with dissolve
    MC "RUN AWAY FOR YOUR LIFEEEEE"
    $ renpy.music.play("runwood.mp3", loop=True)
    show dsprite at middleposmild
    Dragon "hey I just want to talk... "
    #2nd cut
    scene snake
    $ renpy.music.play("walkingwood.mp3", loop=True)
    MC "pant pant Welp, as the wise one said, failure is success in progress. This time I’m going in the right direction for sure"
    show ssp1 at middleposmild
    stop music
    MC "why do I feel like I’m stepping onto something-"
    window hide
    play sound "snake.mp3"
    pause 2.0
    show ssp2 at middleposmild
    MC "My lord save me"
    #3rd cut
    scene forest2
    $ renpy.music.play("walkingwood.mp3", loop=True)
    MC "There goes my antidote, and now there are only 2 ways left to go, and to guess it right the chance of success will be 50 \% I can’t be that unlucky right?"
    scene forest4 with fade
    "Sky is getting Nearly dark, at least [pov] is going in the right way now"
    MC "And I have learnt the hard way about how unlucky I am… Time sure flies… guess I need to learn how to read maps next time. *Yawn* But first, I need to find and set up a place to sleep for now."
    MC "Hm? A random baguette in a deep dark forest? Strange. But at least I’m sure it’s much better than using these rocks as a pillow."
    "Wiping the dust of the weird baguette to make it a pillow"
    $ renpy.music.play("Ambient 1.wav", loop=True)
    show god_yawn at middlepostsuru
    with dissolve
    BBQ " *Yawn* Did you just summon me for what?"
    MC "Huhhh? Who are you?"
    BBQ " *Tsk* Another weird frogman who just summoned me by accident again huh? . . . HUH!? Are you just a speakable frogman or did the curse just not be removed?"
    MC "Curse ...removed? That aside, who are you?"
    hide god_yawn
    show god_normal at middlepostsuru
    with dissolve
    BBQ "Ahem, I’m Baguettia, the goddess of all baguettes, I have the power to do baguette things that can be used by the baguette for people who love baguettes."
    MC "Um cool whatever… First, I’m sorry for waking you up from your rest."
    MC "I’m [pov] and I’m not the frogman, to started of I’m a normal human being until last year after the clash between the hero and the demon."
    MC "All people in the kingdom were turned into frogs by the curse of the Six-horn demon, that's the story I was told by the king."
    hide god_normal
    show god_bored at middlepostsuru
    with dissolve
    BBQ "*Hmm* So, that thing can be used, huh? I guess."
    MC "Did you say something?"
    hide god_bored
    show god_talk at middlepostsuru
    with dissolve
    BBQ "Don’t mind it, just know that once I heard a story like this before and at that time I helped that frogman or… I mean a man that turned into a frog named \"Pepe\"."
    hide god_talk
    show god_normal at middlepostsuru
    with dissolve
    BBQ "but at that time I didn’t have that much power, so I wasn’t sure if my power could do much."
    MC "At that time? But since I was borned I haven’t heard about this story all my life."
    hide god_normal
    show god_bored at middlepostsuru
    with dissolve
    BBQ "Maybe, it's a little bit old story like 100-150 years ago already I think. Or maybe older, I don't remember the time."
    MC "Whoaa, so how’s the result, Ms.Baguettia"
    hide god_bored
    show god_talk at middlepostsuru
    with dissolve
    BBQ "Umm, I’m not sure about that too but I think he’s alright and everything is turning good, because there are no more requests from that time."
    MC "Request?"
    hide god_talk
    show god_smile at middlepostsuru
    with dissolve
    BBQ "You don’t know? This place was once a shrine but now I’m too old to help people so I’m just enjoying my life now." 
    BBQ "But if it’s just the same power that I just gave him last time I think I can help you with that, I mean if you want it you can just take this and continue your journey and I might just continue to take some rest."
    "Baguettia give you a baguette"
    MC "Umm, what can I do with this baguette?" 
    hide god_smile
    show god_normal at middlepostsuru
    with dissolve
    BBQ "I mean just use it as you pleased I gave it to you already by the way but remember this, a baguette is just a tool not a weapon."
    MC "Thanks, Ms.Baguettia. I’m glad about this but you give me this so easily without any condition wouldn’t that be bad?"
    hide god_normal
    show god_smile at middlepostsuru
    with dissolve
    BBQ "*Glances back and giggles* Kiddo, I am old but I know that you are kind and not a bad person, and somehow it reminds me of him a little bit somehow. Whatever, just keep going [pov], I trusted you."
    hide god_smile
    show god_yawn at middlepostsuru
    with dissolve
    pause 0.5
    hide god_yawn at middlepostsuru
    with fade
    "She walks back into the empty void and disappear as same as when she approach"
    MC "She trusted me huh. Guess I couldn’t make this chance a mistake."
    MC "By the way, 100-150 years ago huh and Pepe that’s the same name as my grandfather and he’s once an adventure… doesn’t thissss."
    MC "Nah, I might be too curious. I sure need to sleep too as she did. Tomorrow’s goal is still waiting, I better take some rest."
    scene black with eye_shut
    pause 1.5
    # The next day
    scene forest3 with eye_open
    MC "*Streching* Ughh, a nice long sleep and this weather, bright but not too sunny, what a great day for adventur-"
    play sound "scream.mp3"
    unknow "Whaa!!"
    menu:
        "Go to the sound":
            $ persistent.maid_route = True
            "You followed the sound by rushing through the forest, then he met a woman who’s picking up her fallen stuff back into her shopping bag."
            show maid_unhappy at middlepostsuru
            with dissolve
            MC "Need a hand?"
            show maid_smile at middlepostsuru
            with dissolve
            unknow "Thank you kind one, I appreciated your help."
            unknow "May I know your name, kind one?"
            show maid_happy at middlepostsuru
            with dissolve
            MC "Oh, it’s [pov]. how did you even end up here?"
            Tsukino "I’m Tsukino. I lived around here so I just went for a little shopping in town a bit, and then while I was going back to my home a little boar just ran past me then the story ended up as what you’ve just seen."
            show maid_talk at middlepostsuru
            with dissolve
            MC "Oh! so you live nearby, so… I know it’s a little funny that 1 minute before I just help you …but can you lead me the way to get out of this forest, I’m kinda dumb with reading the maps."
            hide maid_talk
            hide maid_happy
            hide maid_unhappy
            show maid_smile at middlepostsuru
            with dissolve
            Tsukino "*Giggles* You are kind and brave but you look so goofy now, [pov]. For someone who just rushed through the forest to help the girl and now you are lost. *hehe* Of course, this time let me help you. Follow me, Mr.Hero."
            MC "Thanks, Tsukino."

            "After a while, They walked together and shared good moments until they got out of the black forest and now it’s time to say goodbye."
            hide maid_smile
            show maid_blush at middlepostsuru
            with dissolve
            Tsukino "So, I have to go that way, thanks for today [pov], you are very kind to me. Please take this as our relationship sign. See ya."
            hide maid_blush 
            with easeoutleft
            MC "Such a nice and energetic girl, time to finish my mission too."

        "Don't go ":
            MC "Whoa, that scream surprised me in the morning as a start of the day huh. That doesn’t look like a good sign. Guess today I might start by going that way first."
            "You don’t want to be involved in the situation at first thing in the morning, so he tries to go the other way and spends the whole day trying to figure out the way to the demon castle"
            
label chapter4:
    scene castle_far with dissolve
    pause 1.5
    scene castle_door with fade
    MC "Ahhhh, finally arrived."
    MC "Such a big and beautiful castle like the king has told, but somehow looks harmless, at least it looks better than I thought."
    MC "Soooo, should I just go in with a knock?"

    # Show choice options to the player
    menu:
        "Go in":
            # This path triggers the "bad end" if not on the maid route
            MC "Why should it even take me so much time to think, let’s just get in straight."
            "With a single knock on the entrance, not even twice, [pov] feels like something heavy just hit on the back of his head, and things start to blur and get dizzy."
            if persistent.maid_route == True:
                camera at camera_drunk(4,5,4,1,10,2)
                show maid_shi at middlepostsuru
                MC "That skirt, that hair, and that sound... don’t tell me..."
                show maid_unhappy at middlepostsuru
                with dissolve
                Tsukino "*Mumble* I’m glad to see you again, but I just hope it’s not here… not like this."
                MC "Tsukino..."
                camera at camera_identity(0)
                scene black with eye_shut
        
                jump chapter5

            else:
                scene black with eye_shut               
                centered "{=centered_text}..And that all..{/centered_text}"
                centered "{=centered_text}..The end of unknown story..{/centered_text}"
                centered "{=centered_text}..BAD END : Unknown ..{/centered_text}"
                $ MainMenu(confirm=False)()  

        "Stealth and find another path":
            MC "Maybe not from the front door, I guess. Let’s check if there’s another way."
            scene entry with fade
            $ renpy.music.play("Dark Ambient 3.wav", loop=True)
            MC "Somehow, I just got in through an open backdoor. I wonder where this path will lead me to."
            $ persistent.clue = 0
            jump explore_example

label chapter5:
    scene castle_jail
    with fade
    show maid_shi at middlepostsuru
    with moveinright
    MC "So… this is how it ends? After all the trouble I went through, just to end up here?"
    MC "Caught by the same woman I helped just a few days ago."
    MC "I didn’t think you’d turn on me so quickly."
    Tsukino "It’s nothing personal. You’re a kind one, but you’re also an intruder in my master's castle."
    MC "Fair point, but don’t you think this is a little extreme?"
    MC "Maybe you’ve just forgotten who helped you when you were in trouble?"
    hide maid_shi
    show maid_unhappy at middlepostsuru
    with dissolve
    Tsukino "I remember… but the orders are clear. I have to protect my master at all costs."
    MC "And what about what’s right? You’ve seen the way things are."
    MC "You know deep down this isn’t just about loyalty; it’s about what’s fair."
    hide maid_unhappy
    show maid_sleep at middlepostsuru
    with dissolve 
    Tsukino "It’s not that simple. There are consequences to defying her."
    MC "I get that. But what if there’s a chance to change things? What if you could help her see a different way?"
    # Tsukino bites her lip, torn between her duty and her growing feelings for the MC.
    hide maid_sleep
    show maid_smile at middlepostsuru
    with dissolve 
    Tsukino "You’re really willing to risk everything for this?"
    MC "Absolutely. I believe in you, Tsukino."
    # Tsukino’s eyes soften, a flicker of hope sparking within her.
    hide maid_smile
    show maid_happy at middlepostsuru
    with dissolve 
    Tsukino "But how can I trust you? You’re just a human, after all."
    MC "I’ve proven myself before, haven’t I? I helped you when you were in danger."
    MC "I’m not like the others. I want to understand and help."
    # Tsukino looks into the MC's eyes, searching for sincerity.
    hide maid_happy
    show maid_sleep at middlepostsuru
    with dissolve 
    Tsukino "Alright, I’ll listen. But you need to promise me something."
    MC "Anything."
    hide maid_sleep 
    show maid_normal at middlepostsuru
    with dissolve 
    Tsukino "Promise me you won’t let anger cloud your judgment. My master has her reasons."
    MC "I promise. I’ll approach this with an open mind."
    # There’s a moment of silence as they share a meaningful look. Tsukino steps closer, lowering her voice.
    Tsukino "I’ve seen how my master has suffered. She’s not the monster everyone believes. There’s so much more to her story."
    MC " I want to know. Tell me everything."
    MC "I’m here to learn the truth, whatever it is."
    # Tsukino takes a deep breath, her resolve strengthening.
    hide maid_normal 
    show maid_shi at middlepostsuru
    with dissolve 
    Tsukino "There have been misunderstandings, and she’s been forced into this role. I’ve seen her kindness, her efforts to reach out to humans."
    MC "Reach out? How?"
    MC "Does she really want peace?"
    hide maid_shi
    show maid_unhappy at middlepostsuru
    with dissolve
    Tsukino "Yes. She’s sent letters, trying to negotiate with the human military. But they never respond. It’s like they’re just waiting for a reason to attack."
    # The MC’s expression shifts from confusion to curiosity, understanding the depth of the situation.
    MC "What happened to those letters?"
    Tsukino "They were never opened. Just tossed aside."
    # MC clenches their fists in frustration.
    hide maid_unhappy
    show maid_sleep at middlepostsuru
    with dissolve 
    MC "That’s so unfair! She’s trying, and they won’t even give her a chance."
    # Tsukino nods, a touch of admiration in her eyes for the MC's passion.
    hide maid_sleep
    show maid_smile at middlepostsuru
    with dissolve 
    Tsukino "Exactly. It’s heartbreaking. I wish I could show you how kind she really is."
    MC "You can! If you help me meet her, maybe we can change her mind about humans."
    # Tsukino pauses, contemplating the idea. A glimmer of hope crosses her face.
    hide maid_smile
    show maid_happy at middlepostsuru
    with dissolve 
    Tsukino "If I can convince her to meet you, it might be the chance we need. But you have to promise to be respectful."
    MC "I promise. I’ll be honest and open."
    # They share a moment of silence, the tension in the air shifting as their bond deepens.
    hide maid_happy
    show maid_sleep at middlepostsuru
    with dissolve
    Tsukino "Okay. But you’ll need to prepare. My master is fierce, and she won’t tolerate any disrespect."
    MC "I’ll be ready. I won’t let you down."
    hide maid_sleep
    show maid_smile at middlepostsuru
    with dissolve 
    Tsukino "I believe in you."
    "Tsukino turns to leave but glances back one last time, her expression softening further."
    Tsukino "Thank you for seeing me for who I really am. I’ll do my best to help you."
    # With that, she disappears down the corridor, leaving MC with a mix of hope and determination

    scene throne with moveinright
    # SCENE 5-2: BG [Demon Castle] (maid)
    # [The scene shifts to a more ornate part of the castle, with rich decorations and an imposing throne at the far end. The atmosphere is thick with anticipation as MC prepares to meet Azumi. The tension is palpable as Tsukino leads the way, glancing back to check on MC.]
    show maid_smile at leftpostsuru
    with moveinleft
    Tsukino "We’re almost there. Just remember to stay calm. She’s not like anyone you’ve ever faced."
    MC "I’m ready. I can do this. I believe in what we can accomplish together."
    "We approach the throne, where Azumi awaits, her expression unreadable and regal."
    show queen_normal at rightpostdel
    with moveinright
    Azumi "So, you’ve come to plead your case. What makes you think you can change anything here?"
    MC "I believe we can find common ground. I’ve heard about your efforts, and I want to help."
    hide queen_normal
    show queen_talk at rightpostdel
    with dissolve
    Azumi "Help? Or is this just a ploy to further your kind’s agenda? I’ve seen enough deceit from humans to last a lifetime."
    MC "It’s neither! I want to understand your perspective. You’ve suffered, and I want to help alleviate that pain."
    hide maid_smile
    show maid_unhappy at leftpostsuru
    with dissolve
    Tsukino "Mistress, please. He’s shown nothing but kindness to me, and I trust him. You can’t dismiss this opportunity."
    hide queen_talk
    show queen_normal at rightpostdel
    with dissolve
    Azumi "You’ve chosen a human over your loyalty to me? Have you forgotten who raised you?"
    hide maid_unhappy
    show maid_talk at leftpostsuru
    with dissolve
    Tsukino "No, it’s not like that! I’m not choosing sides, I just want us to be understood. Please listen."
    hide queen_normal
    show queen_talk at rightpostdel
    with dissolve
    Azumi "And why should I trust a human? What guarantee do I have that you won’t betray us?"
    MC "Because I’m here willingly, without weapons or threats. I came to offer a hand, not a sword."
    hide queen_talk
    show queen_normal at rightpostdel
    with dissolve
    Azumi "Very well. Speak, human. But know this I will not tolerate disrespect or lies."
    MC "I understand. I’ll be as respectful as possible, and I won’t hide the truth."
    hide maid_talk
    show maid_happy at leftpostsuru
    with dissolve
    Tsukino "Thank you, Mistress. This could be the start of something different."
    MC "I believe it is. Together, we can change everything for the better."
    hide queen_normal
    show queen_smile at rightpostdel
    with dissolve
    Azumi "Then tell me, what do you propose? What makes you think you can be different?"
    MC "I propose dialogue, a chance for us to share our perspectives. The world is not black and white, we all have our stories."
    hide queen_smile
    show queen_talk at rightpostdel
    with dissolve
    Azumi "What stories can you tell that would make me trust your kind? All I’ve known is war and betrayal."
    MC "Stories of hope, of cooperation. There are humans who wish to see peace, who believe in the possibility of understanding."
    hide maid_happy
    show maid_smile at leftpostsuru
    with dissolve
    MC "I’ve seen how fear drives us apart, and I want to be part of a new narrative."
    hide maid_smile
    show maid_normal at leftpostsuru
    with dissolve
    Tsukino "Mistress, we can make this work. If we share our stories, we might discover we’re not so different after all."
    hide queen_talk
    show queen_normal at rightpostdel
    with dissolve
    Azumi "And what of my people? They have suffered greatly. What do you expect me to do?"
    MC "I expect you to allow dialogue, to let your story be heard just as you would hear ours. It’s not easy, but it’s a start."
    hide queen_normal
    show queen_talk at rightpostdel
    with dissolve
    Azumi "I could allow a meeting… but it would be on my terms. I will not put my people at risk."
    MC "Of course! I wouldn’t ask you to do that. Let’s find a way to make it safe for everyone involved."
    hide queen_talk
    show queen_normal at rightpostdel
    with dissolve
    Azumi "If I agree to this, it will not be an easy path. You will have to prove your intentions time and again."
    MC "I will do whatever it takes. I’m willing to earn your trust."
    Tsukino "And I’ll stand by you, Mistress. I want what’s best for all of us."
    hide queen_normal
    show queen_smile at rightpostdel
    with dissolve
    Azumi "Very well. Let us see if your words hold true. Don't betray the trust, the consequences will be dire."
    MC "I understand, and I won’t take this opportunity lightly. I promise."
    hide maid_normal
    show maid_happy at leftpostsuru
    with dissolve
    Tsukino "Thank you, Mistress. This could change everything."
    MC "I believe it can. Together, we can forge a new path."

    scene garden with fade
    $ renpy.music.play("Light Ambience 4.wav", loop=True)
    # SCENE 5-3: BG [Demon Castle – Garden]
    # [The scene opens in a beautiful garden outside the demon castle, filled with vibrant flowers and an air of tranquility, a stark contrast to the tensions of earlier. The sun sets in the distance, casting a warm glow over the surroundings. The MC and Tsukino walk side by side, the weight of their earlier discussions still hanging in the air.]
    MC "I can’t believe she agreed to meet. It feels like a step in the right direction."
    show maid_blush at middlepostsuru
    with dissolve
    Tsukino "Yes, but it’s only the beginning. We need to be careful how we approach this. She’s still very much on edge."
    MC "I get that. But there’s a spark of hope now, isn’t there? We just need to keep nurturing it."
    hide maid_blush
    show maid_smile at middlepostsuru
    with dissolve
    Tsukino "You really believe we can change things? It’s a lot to ask of both sides."
    MC "Absolutely. If we show them that we’re not their enemies, they might start to see us differently."
    MC "And if Azumi sees how much I care about you, maybe she’ll understand that humans can be trusted."
    hide maid_smile
    show maid_sleep at middlepostsuru
    with dissolve
    Tsukino "It’s not just about you, you know. It’s about all of us—demons and humans. I’ve seen how fear has divided us."
    MC "And fear can be overcome with understanding. That’s why I want to fight for this, for you."
    hide maid_sleep
    show maid_blush at middlepostsuru
    with dissolve
    # [Tsukino’s cheeks flush slightly, her heart racing at the admission. She looks up, meeting the MC’s gaze with determination.]
    Tsukino "I want to fight too. But we need a plan. If we’re going to change hearts, we have to be smart about it."
    MC "Right. We need to gather support from both sides. Maybe some humans who believe in peace can help."
    hide maid_blush
    show maid_smile at middlepostsuru
    with dissolve
    # [Tsukino nods, her confidence growing as they brainstorm together.]
    Tsukino "And I can talk to some of the other demons who trust me. If they see that we’re serious about this, they might be willing to help."
    MC "Exactly! We need to create a coalition of sorts—people who want to see this through."
    "We pause, looking around the garden, taking in the beauty that surrounds us. It’s a brief moment of peace amidst the chaos of our mission."
    MC "You know, I’ve never really appreciated nature like this before. It’s peaceful here."
    Tsukino "It is. I often come here when I need to think. The garden has a calming effect."
    # [The mood shifts as Tsukino steps closer, her voice dropping to a whisper.]
    hide maid_smile
    show maid_blush at middlepostsuru
    with dissolve
    Tsukino "You know, it’s strange… I never expected to feel this way about a human. You make me feel… understood."
    MC "I feel the same way. You’ve shown me so much about your world, and I want to protect it."
    # [They share a moment of silence, their eyes locking, an unspoken connection growing stronger between them.]
    Tsukino "If we’re going to do this, we need to be open with each other. No secrets, okay?"
    MC "I agree. Transparency is key. We can’t afford to let misunderstandings derail our mission."
    # [Tsukino hesitates, then takes a deep breath.]
    Tsukino "I’ve never told anyone this, but… I often dream of a world where humans and demons can coexist peacefully. It feels so distant, but you make it feel possible."
    scene cg2
    MC "It’s a beautiful dream, and I believe we can turn it into reality. Together."
    Tsukino "Together. I like the sound of that."
    MC "So, what’s our first step?"
    Tsukino "First, let’s start spreading the word. I’ll gather some of my friends in the castle and introduce them to your idea of a meeting. We can create a safe space to talk."
    MC "And I’ll reach out to some humans who might be sympathetic to our cause. Maybe even some leaders who can influence others."
    # [As they strategize, the tension in the air begins to lift, replaced by a growing sense of purpose.]
    MC "This feels right. I can see a future where we stand side by side."
    Tsukino "Me too. And I’ll do everything I can to make sure it happens."
    "WE share a confident smile, our partnership solidifying as we walk further into the garden, filled with determination to forge a new path."
    MC "One step at a time, right?"
    Tsukino "Right. Together, we can make this happen."
    scene black with eye_shut
    centered "{=centered_text}As the scene fades out, the sun sets behind them, symbolizing the end of one chapter and the hopeful beginning of another{/centered_text}"
    $ persistent.cg2 = True
    $ quick_menu = False
    call credits from _call_credits
    $ quick_menu = True
    $ MainMenu(confirm=False)()
    
label chapter6:
    "After stealth through many rooms there is only the last room which is at the end of the hallway that is led by the big red carpet and that room has an elegant double door."
    show mc_bag_normal at leftpostsuru
    MC "That way leads to the other side of the entrance door from before and then that way led by a big red carpet with a very enormous and elegant door, so guess my detour in this place ends here."
    MC "*Huhh* Let’s just finish this and return home, I kinda miss my cozy bed and blanket now."
    scene throne with fade
    show mc_bag_normal at leftpostsuru
    with easeinleft
    # // Creaking sound of closing the big door
    $ renpy.music.play("teller-of-the-tales-by-kevin-macleod-from-filmmusic-io.mp3", loop=True)
    "The throne is actually empty with dim lights in a room but in this room there is only 1 place that is brighter than the other. It is a writing desk at one corner of the room with someone working on something."
    MC "Was tha…"
    show queen_smile at rightpostsuru
    with moveinright
    DQ "Heyyy Tsukino, wasn’t I told you I will have a diet today so I will not have my snack brea…"
    hide queen_smile
    hide mc_bag_normal
    show mc_bag_die at leftpostsuru
    show queen_talk at rightpostsuru
    with dissolve
    "The silence has been going on for a few seconds."
    show queen_talk at rightpostdel
    with moveoutright
    "Demon queen reacted a lot faster than [pov] and jumped back into fighting position and brought her death scythe out."
    DQ "*Stare* Who are you? And how do you even get in here?"
    MC "Wha… Wait for a sec!!! I’m not a bad guy."
    show queen_normal at rightpostdel
    with dissolve
    DQ "Hmmm, explain yourselves now. I won’t wait too long."
    menu:
        "Make conversation and wait for a chance":
            scene throne
            show queen_close at rightpostdel
            show mc_bag_smile at leftpostsuru
            with dissolve
            jump chapter6_option2
            

        "Explain yourselves" if persistent.clue > 4:
            scene throne
            show queen_close at rightpostdel
            show mc_bag_normal at leftpostsuru
            with dissolve
            if persistent.clue == 8:
                jump chapter6_option3
            else:
                jump chapter6_option1

label chapter6_option1:
    MC "She doesn’t look like she’s fully on guard… Maybe I can reason with her."
    show mc_bag_normal at leftpostsuru
    MC "Listen, I’m just a normal villager. Or… at least, I was, before all this happened. I didn’t come here to fight you. I came to find out why you did this to us—to everyone."
    show queen_talk at rightpostdel
    DQ "Did what to you?"
    show mc_bag_talk at leftpostsuru
    MC "The curse! You’ve turned everyone into… frogs! Humanoids, yes, but not themselves. I need to understand why, and I need to know if you’ll reverse it."
    "The Demon Queen’s expression flickers with a mixture of surprise and something else, perhaps regret, but it quickly hardens."
    hide mc_bag_talk 
    show queen_normal at rightpostdel
    with dissolve
    DQ "Do you think I cast that curse without reason? Do you think I enjoyed it?"
    show mc_bag_talk at leftpostsuru 
    with dissolve
    MC "Then why? What drove you to do this? I can’t go back empty-handed; people are suffering."
    "The Demon Queen falters, her grip on the scythe loosening slightly."
    hide queen_normal
    with dissolve
    DQ "You wouldn’t understand… Humans have always looked at us as monsters, as threats to be eradicated. Every attempt at peace has been thrown back in my face."
    hide mc_bag_talk
    MC "But this—this curse isn’t the answer! It only fuels that hatred, makes them fear you even more. Isn’t there a better way?"
    show queen_talk at rightpostdel
    with dissolve
    DQ "You think I haven’t tried? You think I haven’t hoped that things could change?"
    "The room falls silent as they stare each other down, the weight of her words settling over to you"
    MC "Then why not try again? If you’re willing, I’ll do everything I can to help. There are people out there who don’t want war—who want peace, just like you."
    hide queen_talk 
    with dissolve
    DQ "What makes you think you’re different? I’ve seen countless humans, all with their promises, and yet they all crumble when it comes to coexistence."
    hide mc_bag_normal
    show mc_bag_smile at leftpostsuru 
    with dissolve
    MC "Because I’m standing here, aren’t I? I came all this way, unarmed, just to speak with you. Doesn’t that prove something?"
    "The Demon Queen’s expression softens slightly, her scythe lowering."
    DQ "…Perhaps."
    hide queen_normal
    show queen_talk at rightpostdel
    with dissolve
    DQ "There was a time when I believed in peace, you know. When I thought humans and demons could coexist. But that dream has only brought pain."
    show mc_bag_talk at leftpostsuru
    with dissolve
    MC "What happened? What made you give up on it?"
    show queen_normal at rightpostdel
    with dissolve
    DQ "Years ago, I reached out to your leaders, trying to bridge the gap between our worlds. I sent letters, each one more heartfelt than the last. I asked for parley, for understanding. And you know what they did?"
    hide mc_bag_talk
    hide mc_bag_smile
    show mc_bag_normal at leftpostsuru
    with dissolve
    MC "They ignored you?"
    DQ "Worse. They burned them. Every last one, without even reading my words. They sent my couriers back, beaten, humiliated. After that… I hardened. I vowed that if they saw me as a monster, then a monster I would be."
    "Your heart aches for her, seeing the pain she’s held for so long."
    MC "I’m sorry. I didn’t know. But maybe… it’s time to let go of that hatred. Not everyone’s the same. I believe people can change, but they need someone strong enough to show them the way."
    hide queen_normal
    hide queen_talk
    show queen_smile at rightpostdel
    with dissolve
    "She looks at you, her gaze piercing but softened with a flicker of hope."
    DQ "And you think you can do that? That you, a mere villager, can convince me to risk everything I’ve fought for?"
    show queen_talk at rightpostdel
    with dissolve
    MC "Maybe. But I can promise I’ll stand by you and help however I can. It might not be easy, but it’s a chance."
    "The Demon Queen stands, moving toward the window, looking out over her lands, lost in thought. A quiet resolve fills her face as she finally turns back to the you"
    DQ "If I reverse the curse, it will take every ounce of my magic. I’ll be vulnerable, weakened. My enemies—your leaders—will see it as an opening."
    hide queen_smile
    show mc_bag_smile at leftpostsuru
    with dissolve
    MC "You don’t have to face them alone. There are those among my people who will understand, who’ll defend you."
    DQ "You’re willing to risk your life… for a demon?"
    MC "I’m willing to risk my life for what’s right. I believe in second chances, and I believe you deserve one, too."
    hide queen_talk
    hide queen_close
    show queen_happy at rightpostsuru
    with dissolve
    "A silence falls between them, filled with an unspoken understanding. She nods slowly, walking back toward her throne. The faint glow of her magic begins to fill the room as she closes her eyes, focusing her energy."
    show queen_close at rightpostsuru
    DQ "Then I shall grant your wish. But remember, this curse was not just a spell. It’s bound by the pain and fury that fueled it. Reversing it will take time… and it will hurt."
    show mc_bag_normal at leftpostsuru
    MC "Do whatever it takes. I’ll be here."
    scene black with eye_shut
    centered "{=centered_text}With a solemn nod, she raises her hands, chanting words of power as a swirl of dark energy begins to envelop her. The air grows thick, crackling with energy, as the spell weaves itself back. Light begins to emanate from her hands, expanding out in waves across the land.{/centered_text}"
    scene blue with transition_2
    centered "{=centered_text}As she chants, her form flickers, visibly weakening. The MC moves closer, reaching out to steady her, his presence a quiet support.{/centered_text}"
    centered "{=centered_text}…Thank you… for believing in me. For giving me a reason to hope again.{/centered_text}"
    scene white with transition_3
    "The spell completes in a burst of light. The transformation is complete, everyone has been returned to normal. The Demon Queen stumbles, nearly collapsing, and you catches her."
    scene cg1
    MC "You did it. You saved them."
    DQ "Perhaps… but saving them doesn’t mean they’ll forgive me."
    MC "Maybe not at first. But we’ll prove to them that you’re not what they think. That you’re capable of more than they ever imagined."
    "He helps her to her throne, and she manages a faint smile, looking at him with newfound warmth."
    DQ "Then let this be our new beginning, human. Together, we’ll rebuild what was lost."
    $ persistent.cg1 = True
    $ quick_menu = False
    call credits from _call_credits_1
    $ quick_menu = True
    $ MainMenu(confirm=False)()
    
label chapter6_option2:
    # Option 2: Attempt to Engage in Combat (Leads to Bad Ending)
    $ renpy.music.play("Action 3.wav", loop=True)
    MC "If I can just get close enough… She doesn’t look completely guarded. Maybe I can catch her off guard, force her hand, and end this quickly."
    show mc_bag_smile at middleposdel
    with moveinright
    "You take a cautious step forward, trying to mask their intentions with calm conversation."
    MC "Look, I get it. You’ve got your reasons for doing this, but don’t you think this is going too far?"
    hide queen_close
    show queen_normal at rightpostdel
    with dissolve
    DQ "Oh, I’m going too far?"
    show queen_talk at rightpostdel
    with dissolve
    DQ "You barged into my castle, violated my defenses, and you think you’re in any position to lecture me?"
    MC "I just need to keep her talking… get a bit closer…"
    show mc_bag_smile at middleposmild
    with moveinright
    hide queen_close
    MC "You have a point. But wouldn’t it be better if we could just resolve this without anyone getting hurt?"
    "The Demon Queen’s expression shifts, suspicion clouding her eyes as she notices the MC’s steady, subtle advance. Her fingers tighten around her scythe, muscles tensing."
    hide queen_talk
    show queen_cast at rightpostdel
    with dissolve
    DQ "Strange. For someone claiming peace, you’re getting awfully close. You’re not planning anything foolish, are you?"
    MC "Of course not! I’m just…"
    hide queen_normal with dissolve
    show queen_cast at rightposmild
    with moveoutright
    show mc_bag_scare at middleposmild
    "Suddenly, the Demon Queen’s eyes flash with sharp awareness. She steps back, twirling her scythe in an arc to create distance. Her voice turns cold, unyielding."
    hide mc_bag_smile
    show mc_bag_scare at leftpostsuru
    with moveinright
    DQ "You really think you’re the first to try this?"
    MC "What do you mean?"
    show mc_bag_die at leftpostsuru
    with dissolve
    DQ "Humans. Always claiming peace, claiming diplomacy. And then the moment I show trust, the moment I dare to believe in you, you strike. Just like they all did."
    DQ "I gave you a chance to explain yourself. But it seems words aren’t enough for someone like you."
    MC "Wait, please! I didn’t—"
    scene red with transition_2
    "But there’s no time to explain as the Demon Queen strikes, her scythe is a blur of motion. The MC tries to dodge, but the blow lands, the power behind it forcing them back, vision blurring as they realize the mistake was fatal."
    DQ "A shame. But I won’t fall for the same trick twice."
    scene black with eye_shut
    centered "{=centered_text}..And that it..{/centered_text}"
    centered "{=centered_text}..Your story come to an end..{/centered_text}"
    centered "{=centered_text}..Maybe you can try to fight her..{/centered_text}"
    centered "{=centered_text}..But I'm sure nothing will change..{/centered_text}"
    centered "{=centered_text}..BAD END : Wasted..{/centered_text}"
    $ MainMenu(confirm=False)()
    
label chapter6_option3:
    # Option 3: Calm Explanation (Alternate Success)
    MC "I get it. You probably don’t trust humans—why would you? But I’m not here to fight or trick you. I’m here to understand."
    show mc_bag_normal at leftpostsuru
    DQ "To understand? Humans understanding demons? I’ve heard that one before."
    show mc_bag_talk at leftpostsuru
    MC "I know it sounds unlikely. But I’m willing to risk everything, even my life, to prove that I mean what I say."
    show queen_talk at rightpostdel
    "The Demon Queen stares at you, her grip on the scythe loosening slightly, though her gaze remains guarded."
    DQ "Risk everything… for what? For your people who fear and despise us? For the villagers who treat us like monsters lurking in the shadows?"
    MC "For the people who are scared, yes. But also for the ones who have lost their loved ones, their homes… because of misunderstandings, because of this curse."
    hide mc_bag_talk 
    show queen_normal at rightpostdel
    with dissolve
    $ renpy.music.play("Ambient 10.wav", loop=True)
    "The Demon Queen’s gaze falters for a moment, her shoulders tense but conflicted."
    DQ "You speak of misunderstandings as if they’re so easy to overcome. As if a few words could erase centuries of bloodshed."
    MC "Maybe not erase it. But it’s a start, isn’t it? All I’m asking for is a chance."
    show mc_bag_talk at leftpostsuru 
    with dissolve
    hide queen_normal
    with dissolve
    DQ "And if I say no? If I refuse to listen to another word from you?"
    MC "Then I’ll keep trying, in any way I can. Because the people I care about deserve a second chance. And maybe… so do you."
    hide queen_talk
    show queen_smile at rightpostdel
    with dissolve
    DQ "You’re strange for a human. They never speak this way. Never… look at me this way."
    MC "I’m here, aren’t I? I could have come with an army, with a weapon, but I came alone, unarmed, willing to listen."
    show queen_blush at rightpostdel
    with dissolve
    DQ "Perhaps I’ve misjudged you."
    DQ "But my people have been hurt too. My attempts at peace have only led to betrayal. What assurance can you give me that you’re any different?"
    hide mc_bag_talk
    show mc_bag_normal at leftpostsuru 
    with dissolve
    MC "I can’t speak for everyone. But I can speak for myself."
    "The Demon Queen’s gaze remains locked with his tension hanging heavy in the air as she deliberates. Finally, she releases a weary sigh, some of the hardness in her eyes melting away."
    hide mc_bag_normal
    show mc_bag_smile at leftpostsuru
    with dissolve
    DQ "…Fine. If you’re truly sincere, I’ll give you a chance. I’ll hear what you have to say. But I warn you, one hint of betrayal, and I won’t hesitate."
    hide queen_blush
    hide queen_smile 
    show queen_happy at rightpostdel
    with dissolve
    MC "I know humans have hurt you. I know our history is filled with reasons to be bitter. But I’m here now because I believe we can change that. This curse… it doesn’t have to be the end of the story."
    hide mc_bag_smile 
    show mc_bag_talk at middleposdel
    with dissolve
    DQ "After everything that’s happened, you’re asking me to take a leap of faith? You, a single human, are asking me to believe in something I’ve never been given?"
    MC "I am. And I can’t promise it will be easy. But I can promise that I’ll stand by you to show both humans and demons that we can be more than our past mistakes."
    hide queen_happy
    show queen_smile at rightpostdel
    with dissolve
    DQ "Alright. I’ll give you this chance. But undoing the curse will take every ounce of strength I have. You must be prepared to help me, to carry whatever weight I cannot bear alone."
    MC "You have my word. Let’s do this together."
    hide mc_bag_talk
    show mc_bag_smile at middleposdel
    with dissolve
    "The Demon Queen positions herself in the center of the throne room, closing her eyes as she begins to draw the dark magic of the curse back into herself. A storm of energy swirls around her, thick and pulsing with raw power. You steadies her, reaching out to share the burden of the curse."
    scene black with eye_shut
    DQ "This magic… it’s rooted in years of pain and betrayal. To break it, I must face it all again, every wound… every betrayal. It will try to overwhelm us. Are you ready for that?"
    scene white with dissolve
    MC "I’m here. Whatever you need, I’ll be by your side."
    centered "{=centered_text}As the Demon Queen channels her energy, her memories and the pain they carry manifest around them—visions of burning villages, humans wielding swords against demons, cries of anguish and loss echoing throughout the hall. The weight of centuries presses down on them, almost too heavy to bear.{/centered_text}"
    scene blue with transition_3
    MC "This… this is what you’ve been carrying all along?"
    DQ "Yes. This is the burden my people and I have suffered in silence. And it’s what drove me to cast the curse. But I will not let it consume me any longer."
    scene purple with transition_2
    centered "{=centered_text}With a fierce determination,you reaches out, sharing her pain and letting her feel his support. Gradually, the dark energy begins to weaken, light breaking through the shadows. The magic disperses in waves, spreading across the land, and people begin transforming back to their human forms, freed from the curse{/centered_text}"
    scene white with transition_1
    centered "{=centered_text}In villages across the kingdom, cheers erupt as people recognize each other once more, their hearts filled with relief and gratitude. Meanwhile, in the throne room, the Demon Queen collapses to her knees, exhausted but relieved, the curse finally broken.{/centered_text}"

    centered "{=centered_text}A day later at the village{/centered_text}"
    scene cg3
    MC "Please, listen. The curse is gone. She’s shown mercy to everyone. She isn’t the monster you believed her to be. She’s as much a victim of this pain as any of us."
    Villager "But… she’s the Demon Queen. How can we know this isn’t a trick?"
    MC "Because she didn’t have to do any of this. She could have kept us cursed, but instead, she risked everything to make things right. We have a chance now—to heal, to move forward without fear."
    DQ "I know my actions have hurt many of you. But if you are willing, I will work to earn your trust. I have no desire to harm you—only to protect my people, as you would protect yours."
    OlderVillager "I… I lost my family because of the curse. But if you’re sincere… maybe we can start again. With caution, but with hope."
    DQ "Thank you. This is all I ask."
    MC "That was brave of you."
    DQ "No braver than you coming here alone, hoping to reason with me. I owe you thanks… for showing me that trust is possible again."
    MC "We still have a long way to go. But we’ve taken the first step. And if we keep trying, I believe we can truly bring peace."
    DQ "Perhaps you’re right. For the first time in a long time… I believe it too."
    scene black with eye_open
    centered "{=centered_text}They share a brief look of understanding, the animosity of the past finally put to rest. Together, they walk out of the throne room, each feeling a newfound hope that one day, humans and demons will truly see each other as allies rather than enemies. The scene fades as they step into the dawn of a new era, a world filled with possibilities for peace.{/centered_text}"
    $ persistent.cg3 = True
    $ quick_menu = False
    call credits from _call_credits_2
    $ quick_menu = True
    $ MainMenu(confirm=False)()