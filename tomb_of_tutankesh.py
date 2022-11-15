name=input("Welcome to The Tomb of Tutan'kesh brave adventurer What is your name?\n")
print("With the help of an ancient map, you have found your way into the lost buriel chamber of Tutan'kesh deep within his tomb. You packed away a good amount of the priceless treasures you found in the burial chamber, but when you opened the sarcophagus of the pharaoh you must have triggered a trap! The way back has collapsed and the only way out you can see is through a narrow passageway ahead! The ceiling is trembling and large rocks are falling all around you!\n")
choice1=input('Will you head through the (N)arrow passage or try to dig your way (B)ack to where you came from?\n').lower().strip()
if choice1 == 'n':
    print('You rush forward, squeezing yourself through the tight passageway and into whatever lays beyond.\n')
    print('From what your torch can iluminate, the passageway widens into a long hallway. You cannot see the end, but the rumbling from behind you grows louder. You must hurry!\n')
    print('As you hurry forward, you hear a click from a tile beneath you and hear the whoosh of something rushing towards you from above. What do you do?\n')
    choice2=input('You can (D)uck, (J)ump, or (S)print forward.\n').lower().strip()
    if choice2 == 'd':
        print('You duck just in time as a large axe swings down from above right where you were standing! That was close!\n')
        print("You're very shaken from the close call and make your way forward a bit more slowly now.\n")
        print("The hallway splits into two paths. The left one seems to have partly collapsed long ago, rocks are scattered across the floor. The right one seems to have a strange mist rising from the ground.\n")
        choice3=input('Will you go (L)eft or (R)ight?\n').lower().strip()
        if choice3 == 'l':
            print("You head down the left passageway cautiously, careful not to trigger any more traps. It's not long before you get to a cave in. Searching around with your torch, you are able to find an opening in at top of the cave in just large enough to crawl through.\n")
            choice4=input('Are you brave enough to (C)rawl through the tight opening or will you turn (B)ack to go the other way?\n')
            if choice4 == 'c':
                print('You steel yourself before shimmying into the tight opening. There is hardly room to hold your torch before you. \n It seems to take an eternity, but you finally make it to a room on the other side.\n')
            elif choice4 == 'b':
                print("That opening is way too small. There's no you'd go through that. Instead you head back to the other hallway. It's not long before you hear a shuffling noise coming from nearby. Stopping, you listen. What is that?\n")
                choice6=input('Do you (I)nvestigate the shuffling noise or (C)ontinue to the other hallway?\n').lower().strip()
                if choice6 == 'i':
                    print("You look around warily. The shuffling sounds seems closer now. Peering around the corner of the way back to the main chamber you spy the mummified corpse of Tutan'kesh shuffling its way towards you.\n")
                    choice9=input("Will you (R)un from the corpse or attempt to (A)ttack it head on?\n")
                    if choice9 == 'r':
                        print('Hell no! You scram like your life depends on it (because it does) and rush headlong into the misty hallway\n')
                    elif choice9 == 'a':
                        print("You're not afraid of a scrawny mummy! With your torch held high in front of you, you approach the mummy.\n")
                        choice10=input('How will you attack the mummy? Will you attack it with your (T)orch or will you go at it with your (F)ists only?\n')
                        if choice10 == 't':
                            print()
                        elif choice10 == 'f':
                            print()
                        elif choice10 == 'dance':
                            print("You challenge the mummy to a dance off. He trips on his bandages and falls face-first on the ground, collapsing into a pile of dust. Congrats! You beat The Tomb of Tutan'kesh!")
                        else:
                            print('You walk forward confidently before tripping on your shoe laces and landing right at the feet of the mummy. Uh oh. You perish.')
                    else:
                        print("You are frozen in fear and watch in horror as you mummy shuffles slowly closer before finally reaching you and ripping your still beating heart out before your eyes. You perish.")
                elif choice6 == 'c':
                    print()
                else:
                    print("You sit there listening to the noise for what seems like an eternity before it stops. Then you hear it again, but this time right behind you! You turn around and there stands the mummified corpse of Tutan'kesh, reaching for you. Your heart stops out of fear. You perish.\n")
        elif choice3 == 'r':
            print('You carefully head down the misty hallway. The mist is icy and you shiver involuntarily. The further you go, the colder and thicker the mist becomes.\n')
            choice5=input('Do you wish to (C)ontinue into the mist? Or will you head (B)ack to the other hallway?\n')
    elif choice2 == 'j':
        print('You jump into the air, right into the oncoming blade of a large axe. You perish.')
    elif choice2 == 's':
        print('You sprint forward, almost dodging whatever it was that came at you, but it snags your pack and a few of your priceless treasures fall out as your backpack rips. Too bad.\n')
        print("Your adrenaline is running high from the close call and you keep at a run down the hallway!\n")
        print('At the end of the hallway you come to a fork. The (L)eft fork seems to have rubble scattered on the floor, while the (R)ight has a strange mist rising from the floor.\n')
        choice7=input('Which will you take? (L)eft or (R)ight?\n').lower().strip()
        if choice7 == 'l':
            print('You rush down the left passageway, perhaps you should have been a bit more cautious because only a few meters in you trip on a rock and fall. Your torch is extinguished...\n')
            print('You can see nothing. You can hear nothing. This is now your tomb. You perish.')
        elif choice7 == 'r':
            print('You run down the right passageway. The mist grows colder and thicker and fully covers you now. You shiver involuntarily; not only from the cold but from the growing fear you feel.\n')
            choice8=input('Will you let your fear get the better of you and head (B)ack or will you (C)ontinue running through the mist?\n').lower().strip()
            if choice8 == 'b':
                print("There's no way you're going through that mist. You begin back down the hallway before stopping dead in your tracks. There's a shadowy figure right in front of you, obscured by the mist. You reach your torch out further and reveal the mummified corpse of Tutan'kesh. You perish.")
            elif choice8 == 'c':
                print("You continue through the mist at a run. You need to get out of here and soon!\n")
                print("All of a sudden the mist gives way and a gaping chasm looms just in front of you. You don't have time to stop, but you can see a small ledge on the left side.\n")
                choice11=input('Will you try to jump onto the (L)edge, will you try to jump (A)cross the chasm, or will you just (D)own into the chasm?\n')
                if choice11 == 'l':
                    print('You see the ledge just in time and jump for it. You land on it, but your momentum carries you into the pit and you fall, breaking your legs and extinguishing your torch. This is the end for you. You perish.')
                elif choice11 == 'a':
                    print('You can just barely see the other side of the chasm and you take a massive leap towards it. Thank goodness you were running, you just barely make it over to the other side.\n')
                elif choice11 == 'd':
                    print('You take a leap of faith into the unknown. It appears luck is with you today as you fall only a few meters before landing on a large growth of moth, breaking your fall.\n')
                    print()
                else:
                    print('In surprise you fall down into the chasm, hitting the ground head-first. You perish.')
            else:
                print('You take too long deciding what to do. The mist is so cold now you cannot feel any of your limbs. You cannot walk, you cannot move, you will perish...')
elif choice1 == 'b':
    print('You scramble back to the now collapsed entrance and dig frantically at the fallen debris. You think you can see a hole through the top, perhaps just big enough to squeeze through before a large piece of the ceiling gives way and knocks you unconscious. You perish.')
 
else: 
    print('You wait too long deciding what to do and the room collapses around you, burying you with the pharaoh... You perish.')
   