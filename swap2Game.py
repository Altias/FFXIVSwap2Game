#Created by heretic-altias on Tumblr AKA Altais Narluu @ Lich in FFXIV
#Part of the second FFXIV Swap as a gift for brazenelk on Tumblr. The character Brazen Elk is theirs.
#This a fanwork for FFXIV. The only things created by me are this story, the main villians, and most nameless side characters. The setting is entirely in FFXIV's universe.
#I will support this program and fix any bugs found until December 10, 2023 (one week after the end of the swap). After that I will not fix any issues. Sorry lol, I'm a student with lots of things to code.

#This code should be well organized. Mostly. Maybe. We'll see.
#Past me was kind of right. It's organized but only if you read the comments to find out what's where. Good luck.

playerName = "";
path = 0;

#The basic function to manage multiple choice inputs
def getMultChoice(numOptions):
    option = None;
    while option is None:
        try:
            option = int(input("Your choice: "));

            if (option <= 0 or option > numOptions):
                print("Number out of range. Please choose one of the choices given");
                option = None;

            else:
                return(option);

        except ValueError:
            print("Invalid number. Please enter the number of your choice, not the text");

def endGame():
    print();
    print("Consider playing again! This game has multiple endings!");
    print("Press Enter to exit");
    useless = input();
    exit(0);

#Main Game Code

#INTRODUCTION
print("Game created by heretic-altias on Tumblr as part of the second FFXIV Swap.");
print("This is a swap gift for brazenelk on Tumblr, and Brazen Elk is their character");
print("The whole game is a fanwork taking place within the FFXIV universe. The story, the villians, a few side characters, and the game's code are the only things created by me.");
print();
print("To begin please enter your name. You will be addressed by this name through your entire adventure");

playerName = input("Name: ");

print("Thank you " + playerName + "! Now let us begin...");

print();
#Intro Text
print("You stand in Limsa Lominsa, in front of a lift. A letter is clutched in your hand with the Admiral's seal on it.You have been invited to a masquerade party hosted by Merlwyb herself for Maelstorm soliders of notable importance, and whether it was out of genuine interest, a simple craving for the free food, or something else entirely you have chosen to come.");
print();
print("Everyone passing by around you wears a mask. That combined with their dress clothes makes everyone almost impossible to recognize. Rumor has it even the Admiral is mingling with everyone else at the party, hidden behind a mask. Any friends you may know here will be difficult, if not impossible to find. You step onto the lift with the next group and ride up.");
print();
print("The party starts off well enough. You politely mingle with the people around you. But it's quite crowded and noisy, and you find yourself stepping off to the side for a breather. It's then that you hear people speaking in hushed voices.\n\"The Admiral is here. We just have to find her.\"\n\"Good. She'll regret what she's done soon enough.\"");
print();
print("You know something is wrong. Your gut tells you these people are up to no good. Do you:\n1: Move closer\n2: Keep listening");
choice = getMultChoice(2);
clue = choice;
print();

#This choice only impacts information printed, not the path followed.
#Player has chosen to move closer
if (choice == 1):
    print("You move towards the voices, stepping around a corner into a small hallway. Two people are there, a Miqo'te woman and a Hyuran man. Both have masks on, the former wearing a vibrant red one decorated with feathers and the latter wearing a plain black mask. Upon seeing you, they quickly walk away");


#Player has chosen to keep listening where they are
else:
    print("You remain where you are, listening closely. The conversation continues with the first voice, a woman's.\n\"She will. She never should have leashed us in. Pirates as a military force! Ick! We'll be free to sail and pillage as we please soon enough\"\nA man's voice answers her\n\"Any idea where to find her yet?\"\n\"No. But I heard her mask is red. Maelstrom's color of course. I've got the knife on me, we just need to find her and wait for her to move away from prying eyes.\"\nThe converation stops and you hear footsteps moving back into the crowd. You never catch a glimpse of them");


print();
#TODO: Get mask description
print("You can hardly believe it. A plot against the Admiral? Here? There had always been those who didn't like her restrictions on piracy, but you never could have imagined you'd be witnessing an attempt to off her. Desprate, you mingle back into the crowd hoping to find the people again. You're so distracted you end up walking straight into a Roegadyn man. He looks at you in surprise, his face obscured by a white beard and a mask");
print("Do you:\n1: Apologize\n2: Keep walking silently");
print();
choice = getMultChoice(2);
#Another text only choice. Does not effect path
#Player apolgizes
if(choice == 1):
    print("You're quick to apologize. But something in your voice must have given away your worry, because the man speaks to you with a concerned frown.");
    print("\"No worries. You alright though? You look like you've seen a ghost!\"");


#Player tries to walk away
else:
    print("You quickly try to dodge away and continue your search, there's no time to explain yourself to this man. But he must sense something is wrong, because he quickly moves to block your escape with a concerned frown");
    print("\"Hey! You alright? You look like you've seen a ghost!\"");

print();
print("Ah. So you had been that obvious. You silently contemplate how to get out of this situation. You could try and continue away. But this man carries himself like someone experienced, he must either hold or have held a high position in the Maelstrom. Someone with that kind of experience might know what to do. Better than you, bumbling through the crowd hoping for a glimpse of the wannabe killers anyway.");
print("Do you:\n1: Tell him\n2: Ask about his background first");

#Yet another choice with only text lol
choice = getMultChoice(2);

if (choice == 1):
    print("Unable to keep this to yourself any longer, you spill everything you'd just witnessed to this stranger");

else:
    print("You eye him warily. It's hard to trust even the most concerned face after overhearing what you just did. So you ask him who he is. He's quick to answer");
    print("\"Can't say it's traditional to ask at an event like this, but you don't seem like you're just making small talk. Name's Brazen Elk.\"");
    print();
    print("You've heard of this man. While he's retired now, he used to be fairly highly ranked in the Maelstrom. High enough for you to recognize his name anyway. This has to be someone you can trust. The killer wouldn't have given out their real name in conversation anyway.");
    print("You decide to tell him what you've heard, hoping he'll know what to do");

print();
print("The man thinks for a moment, a concerned frown all that you can make out on his obscured face");
print("\"We'd better sort this out then. Wouldn't do to let that happen. So much for a relaxing evening, but I suppose we'll have time to return to that once we catch these fools.\"");
if (choice == 1):
    print("There's a brief pause before he adds on one more detail");
    print("\"Oh yeah, name's Brazen Elk by the way. You'll need to know that in case we lose each other in this crowd\"");
    print();
    print("You recognize his name. He's retired now, but he used to rank quite highly in the Maelstrom. It seems you made the right call telling him.");
    print();
print();
print("You're surprised he believed you so quickly.");

#Text choice againnnn
print("Do you:\n1: Ask him why he believes you\n2: Don't question it, you don't have time");
choice = getMultChoice(2);
print();

if (choice == 1):
    print("His answer has no hesitation behind it");
    print("\"I've seen enough troublemakers in my day to know the difference between someone stirring up trouble and someone in genuine distress. Your story was real.\"");
    print();

print("You tell him your name, you know his now after all");
print("\"" + playerName + ". I'll be sure to remember. We'd better get to work\"");
print();
print("Well it seems you're not doing this alone anymore, thank the gods. Your new companion is quick to put his experience to use in thinking of a plan");
print("\"Way I see it, we have two options. Security won't listen to us without proof, there's always someone stirring up trouble at these sorts of things. Being retired, I don't have rank to pull over them anymore. We'll need to either find the culprits before they find the Admiral, or beat them to her and try to warn her ourselves. You're the one who overheard them, what do you think we can do faster?\"");
print();
print("Make your choice:\n1: Pursue the killers you overheard\n2: Find the Admiral\n3: Ask Brazen Elk which you should do");
path = getMultChoice(3);
if (path == 1):
    print();
    print("You decide to pursue the killer. If you can stop them before anything can happen, the Admiral will be saved.");

elif (path == 2):
    print();
    print("You decide to search for the Admiral. Surely if you find her she'll have the resources to stop the killer.");

elif (path == 3):
    #Don't ask why none of these numbers are in order I just put the wrong ones and didn't feel like moving entire code lines.
    print();
    print("Uncertain, you hope your new friend's experience can direct you. Brazen Elk thinks for a moment before answering you");
    if (clue == 2):
        print("\"Well we've got more information on the Admiral herself. Seems faster to make use of that\""); 
        path = 2;

    else:
        print("\"Well since you caught a glimpse of these killers, it might be easier to find them again\"");
        path = 1;
    print("You have your answer. Surely an experienced soldier's advice can't steer you wrong.");
        
    
print();

#END OF INTRODUCTION

#And now we've hit a point of no return. These choices are entire game paths. Would this be neater if I used seperate files for them? Maybe, but I'm lazy and this is free lol.

#PATH 1 - FIND CRIMINALS
#Clue 1 is relevant
if (path == 1):

    if (clue == 1):
        print("You look around the party, hoping for a glimpse of one of the masks you'd seen. Both black and red are quite common being the Maelstrom's colors of choice. Feathers, however, are a little less common. Around you, a few people wear feathered masks. Each is a different color");

    else:
        print("You don't have much to go on, so you take Brazen Elk back to the area you'd overheard the conversation. As the two of you are looking around a man sneezes nearby.");
        print("\"Bloody hells! Who wears feathers on a mask?\"");
        print("His anger draws your attention. Not a lot of people came through this corner. Brazen Elk catches onto this too and talks to the man");
        print("\"You alright sir?\"");
        print("The stranger takes on a formal tone as he realizes he has company");
        print("\"Ah, yes. Aplogies for the swearing. I have a pretty terrible feather allergy, and I wasn't expecting to run into any here. Seems someone wearing some was here recently, one probably fell off the mask and is setting off my sneezing now.\"");
        print("You and Brazen Elk both apologize for how much that must stink, and the moment the man turns a corner out of sight you look at each other. Chances are, your murderer was the one wearing feathers after all!");
        print();
        print("You return to the main party and start looking around. Who's wearing feathers here? There are a few you can see with feathered masks, each wearing different colors");

    print();

    end = False;
    spoken1 = False;
    spoken2 = False;
    spoken3 = False;
    
    while (end == False):
        print("Who do you want to talk to?");
        print("1: A Hyuran man with a mask decorated with raven black feathers");
        print("2: A Miqo'te woman with a mask covered in scarlet feathers");
        print("3: An Auri woman who's mask is covered in pure white feathers that match her scales");

        choice = getMultChoice(3);
        print();
        if (choice == 1 and spoken1 == False):
            spoken1 = True;
            print("You and Brazen Elk approach the Hyuran man");
            print();
            print("\"Evening!\" Brazen Elk greets the man with a smile");
            print("The man raises a glass of wine in toast as he greets the two of you");
            print("\"Evening friends! Care to share a drink? I have the whole bottle right here!\"");
            print("Accept a drink?");
            print("1: Yes\n2: Politely decline");
            choice = getMultChoice(2);
            if (choice == 1):
                print("You accept the glass and take a sip. It's clearly an expensive wine, better than any on offer tonight. The man grins at your surprised expression");
                print("\"Admiral never offers the good stuff at these events. Snuck it in myself, and that was no small feat let me tell you! Though I bet the guards would be having a much better night if I'd been caught! Don't tell them by the way. Wouldn't want them taking it after everyone's already been enjoying it!\"");

            else:
                print("You politely decline. The man shrugs.");
                print("\"Fair enough. Not everyone wants to taste a drink brought in from the outside at these things. Never know what kind of shady business could be going on. I promise you I only brought in the best wine though, so I'd appriciate you not telling. They never offer the good stuff at these things\"");

            print();
            print("Do you want to keep speaking to this man or have you heard enough?");
            print("1: Yes, he seems like a suspect\n2: No, he seems innocent");
            choice = getMultChoice(2);
            print();
            print("You look around once more, your eyes finding all the same people as before.");
            print();

            if (choice == 1):
                print("A glance to Brazen Elk tells him you find this man suspicous. He gives you the slightest nod and shifts the conversation");
                print("\"And what if the Admiral sees your secret wine? They say she's at this party tonight\"");
                print("The man pauses for a moment surpised before answering");
                print("\"Honestly, didn't think of that. But if she does maybe I can buy her silence with a glass. Surely even the Admiral appriciates a good drink sometimes!\"");
                print("Brazen Elk shakes his head and you have a feeling the Admiral would not be bought by a simple glass of wine");
                print();
                print("Do you want to accuse this man?");
                print("1: Yes\n2: No");
                choice = getMultChoice(2);

                
                #Ending 1
                if (choice == 1):
                    print();
                    print("You loudly accuse this man of plotting to kill the Admiral, drawing the attention of everyone arouind you. The guards are quick to approach and ask what's going on. When you relay everything you know the guards nod. Perhaps this man would have had a better chance at pleading his case if he wasn't carrying a bottle of wine from outside the event. The man is arrested. For a few hours, you're quite happy believing you solved the case. Youa and Brazen Elk spend the evening together laughing and enjoying the party. But your victory didn't last, as only a few hours later, someone falls over dead with a knife between the ribs. It was the Admiral. You had 'caught' the wrong guy, and in doing so allowed the real culprit to get away with it. The party is ended abruptly, everyone is thrown out and you lose Brazen Elk in the chaos. Whether Limsa Lominsa can handle the death of their leader is something you'll see in time");
                    print();
                    print("THE END");
                    endGame();

                else:
                    print();
                    print("You decide this man seems innocent. You move on and locate the other two people you'd been eyeing in the room");
                    print();
            else:
                print();
                print("You decide this man seems innocent. You move on and locate the other two people you'd been eyeing in the room");
                print();
        

        elif (choice == 2 and spoken2 == False):
            spoken2 = True;
            print("You and Brazen Elk approach the Miqo'te woman");
            print();
            print("Even Limsa Lominsa has its share of wealthy people, and this woman is obviously one of them. She stands among a small group waving a fan that matches her mask. Brazen Elk picks up on this as he greets her");
            print("Good evening, madam! Enjoying the party so far?");
            print("The woman sighs before replying");
            print("\"These events are always so dull. You would think the Admiral would know how to throw a party at least, that was something those pirate types always got right\"");
            print("Brazen Elk laughed at this remark");
            print("Still always an honor to be invited. Reminds me my time with the Maelstrom was worth something to them, even after all this time");
            print("The woman smiles slightly at his remark");
            print("\"Suppose so. But I'll be much happier when it's all over\"");
            print();

            print("Do you want to keep talking to this woman?");
            print("1: Yes, she seems suspicous\n2: No, she seems innocent");
            choice = getMultChoice(2);

            if (choice == 1):
                print();
                print("You glance at Brazen Elk to tell him you suspect this woman. He gives you a slight nod and shifts the conversation to something relevant.")
                print("\"Heard the Admiral herself is among the crowd tonight. Have you run into her?\"");
                print("The woman responds excitedly");
                print("\"Not yet. But I've been hoping to. Now there would be someone worth talking to! I have quite a bit I'd like to discuss with her. If you do spot her would you mind telling me? The rest of these people are just common soldiers and pirates. Nowhere near as influential.\"");
                print("Brazen Elk frowns. He clearly did not appriciate that last remark. The cluster of people around the woman find it hysterical though and burst out laughing.");

                print("Do you want to accuse this woman?");
                print("1: Yes\n2: No");
                choice = getMultChoice(2);

                #Ending 2
                if (choice == 1):
                    print();
                    print("You loudly accuse this woman of plotting the Admiral's murder. She looks shocked, and the commotion attracts the guards. When you and Brazen Elk explain to them what's going on, they decide to check the woman for weapons. She resists, but in the struggle a knife clatters to the floor. And it's no kitchen knife, this is clearly a weapon. Exposed she starts screeching at you and Brazen Elk. How you ruined everything. How her pirates couldn't make any more money with the Admiral's new laws. She effectively confesses in front of everyone that her wealth came from piracy and she wanted the Admiral dead to continue making it. She is escorted out, and the Admiral ends up finding you and Brazen Elk later on as you're enjoying the party to person thank the two of you. You end up spending the evening with your new friend and the Admiral herself until the party ends. It's certainly an event you'll never forget. For years you'll hear retellings of how you and Brazen Elk saved the Admiral. Limsa Lominsa's leader is saved, and the city can continue into the new era she had been building.");
                    print();
                    print("THE END");
                    endGame();
                    
                else:
                    print();
                    print("You decide this woman seems innocent. You move on and locate the other two people you'd been eyeing in the room");
                    print();
                
            else:
                print();
                print("You decide this woman seems innocent. You move on and locate the other two people you'd been eyeing in the room");
                print();
                
        elif (choice == 3 and spoken3 == False):
            spoken3 = True;
            print("You and Brazen Elk approach the Auri woman");
            print();
            print("This woman is dancing elegantly. When you meet her eyes she extends a hand, inviting you to dance with her");
            print("Do you:\n1: Accept her hand and dance\n2: Hold up your hands and shake your head in a polite denial");
            choice = getMultChoice(2);

            if (choice == 1):

                print("You accept and twirl around dancing with the woman for a few minutes. She's clearly a talented dancer. You end up complimenting her on it to start a conversation when the song ends and she smiles");
                print("\"I'm glad you noticed! I learned from these Thavnarians that were in the city. They can use dancing as a form of combat if what they told me is true. I would love to learn such a skill, I bet I would rise through the Maelstrom in the most elegant way possible if I could do that\"");
                

                
            else:

                print("The woman shrugs.");
                print("\"Not much of a dancer? I suppose not many people here are. At least not in this style. I learned from some Thavnarians that were visiting the city. I would love to learn how they use it as a method of fighting. Imagine rising in the Maelstrom's ranks while being so elegant!\"");

            print("Brazen Elk smiles upon hearing this");
            print("\"Can't say I've seen any dancing soldiers. It would certainly be a surprise to anyone expecting pirates. You're currently serving then?\"");
            print("The woman smiles back.");
            print("\"I am! Though certainly not at the rank of most of the people in this room. I'm still only a private, my commander got me into this. I saved some fellow soliders in the last battle and she insisted I deserved the invitation for my actions. I'm not so sure, but I'm enjoying myself! At least no one here can tell I'm the rookie with all the masks. Though I did just out myself to you!\"");
            print("Brazen Elk nods in understanding");
            print("\"It can be daunting to be the lowest ranked in the room. But if you're here you've earned it. I won't tell\"");

            print("Do you want to keep talking to this woman?");
            print("1: Yes, she seems suspicous\n2: No, she seems innocent");
            choice = getMultChoice(2);

            if (choice == 1):
                print();
                print("You meet Brazen Elk's eyes to tell him you suspect this woman. He gets the message and shifts the conversation in the right direction");
                print("\"Met the Admiral yet? If you haven't I heard she's here\"");

                print("The woman's eyes widen.");
                print("\"Oh gods, is she? If I did meet her I had no idea. I hope I haven't! I've done so many embarassing things in front of people!\"");

                print("Do you want to accuse this woman?");
                print("1: Yes\n2: No");
                choice = getMultChoice(2);

                #Ending 3
                if (choice == 1):
                    print();
                    print("You loudly accuse this woman of plotting the Admiral's murder. Brazen Elk shakes his head, he clearly didn't think it was her at all. But the guards have noticed the commotion so you explain yourself and everything you've found so far. The Auri woman's commander recognizes her and marches over in a rage. How dare you accuse her soldier? The Auri woman is crying, you have ruined her evening. Ultimately, you look like the bad guy here. The guards throw you and Brazen Elk out for causing trouble. He's not terribly happy with you for accusing this one. You're alone in a bar later when you get the news - the Admiral has been murdered. Your failure led to the real culprit pulling it off. And for it, Limsa Lominsa is forever changed");
                    print();
                    print("THE END");
                    endGame();

                else:
                    print();
                    print("You decide this woman seems innocent. You move on and locate the other two people you'd been eyeing in the room");
                    print();
                

            else:
                print();
                print("You decide this woman seems innocent. You move on and locate the other two people you'd been eyeing in the room");
                print();
            
                

        else:
            print("Brazen Elk quietly reminds you you've already talked to that person. Perhaps another would be a better choice.");
            print();

        if (spoken1 == True and spoken2 == True and spoken3 == True):
            end = True;

        #Loop over
            
    #Ending 4
    print("You spoke to all three suspects you saw, yet couldn't find one worth accusing. You try to find them again, but they had been steadily moving farther apart and now can't see any of the three. You continue searching through the evening and talking to other people, but you find no more leads. Your panic kept rising as time went on making it harder to think clearly. Brazen Elk took over most of the talking, but even with his level head you don't find anything. The Admiral eventually is killed with a knife between the ribs and the guilt you feel is immeasurable. Perhaps if you had been more certain you could have pervented this. The party is ended abruptly and you lose Brazen Elk in the chaos as everyone is herded out by the guards. Limsa Lominsa will just have to learn to live with another leader. And you and the new friend you never saw again will both have to learn to live with the guilt of failure.");
    print();
    print("THE END");
    endGame();



#PATH 2 - FIND ADMIRAL
#Clue 2 is relevant
if (path == 2):
    if (clue == 2):
        print("You consider what you heard before - you know the color of the Admiral's mask. But the Maelstrom's colors are probably the most popular colors here, and most of the crowd is decorated in red and black.");

    else:
        print("You wonder what the Admiral could be wearing. You know to look for a Roegadyn woman, but there's plenty of them in Limsa Lomsina. You ask Brazen Elk if he has any idea. Luckily he does.");
        print("\"The Admiral probably wouldn't be trying to stick out if she wants to blend with the party. Still, she'd probably sport the Maelstrom's colors. It may not narrow things too much, but I'd look for someone in reletively plain red and black\"");

    print("You look around and manage to spot a few Roegadyn women in black and red outfits");
    print();

    end = False;
    spoken1 = False;
    spoken2 = False;
    spoken3 = False;

    while (end == False):
        print("Who would you like to talk to?");
        print("1: The woman wearing entirely blood red from head to toe");
        print("2: The woman in a striped black and red mask");
        print("3: The woman wearing all black except for her mask, which is a dark red");
        choice = getMultChoice(3);
        print();

        if (choice == 1 and spoken1 == False):
            spoken1 = True;
            print("You and Brazen Elk approach the red clad woman");
            print();
            print("This woman stands alone off to the side, her arms crossed. She's clearly unhappy. Brazen Elk attempts to talk to her.");
            print("\"Everything alright?\"");
            print("The woman huffs in annoyance before responding");
            print("\"This whole event is ridiculous! Most of us were pirates at one point, who does a masquerade with pirates?\"");

            print("Do you: ");
            print("1: Agree that it's a dumb party\n2: Think it's actually a nice idea to do something different");
            choice = getMultChoice(2);

            if (choice == 1):
                print("\"A kindred spirit! Thank the Navigator! Perhaps if there are more of us we can do something normal next time!\"");

            else:
                print("\"You think so? Suppose I'll at least try and give it a chance. Everyone else has said the same thing so far\"");

            print();
            print("Do you think this could be the Admiral?");
            print("1: Yes, it's possible");
            print("2: No, this definitely isn't her");
            choice = getMultChoice(2);
            print();

            if (choice == 1):
                print("You nod slightly to Brazen Elk. He shifts the conversation in the right direction");
                print("\"Heard the Admiral is here tonight in the crowd. Have you run into her?\"");
                print("The woman responds quickly");
                print("\"I hope not! Imagine if I complained to the Admiral herself! I'd better keep my mouth shut the rest of the night if that's true!\"");

                print("Your decision: ");
                print("1: This is the Admiral, tell her everything\n2: This isn't her. Keep looking");
                choice = getMultChoice(2);
                print();

                #Ending 5
                if (choice == 1):
                    print("You tell her you know she's the Admiral and warn her of the plot against her. However, this woman is not the Admiral. She panics hearing this story and goes straight to the guards, who are quick to kick you out for causing a panic. You and Brazen Elk try insisting to the guard at the lift that while you found the wrong person, the plot is very real and they need to tell the real Admiral. Unfortunately, the guards don't listen. Not until the Admiral is killed mid party. They apologize to you both, but that can't undo what has been done. Limsa Lominsa will have to move on without their Admiral.");
                    print();
                    print("THE END");
                    endGame();

                else:
                    print("You glance at Brazen Elk and shake your head. He nods in agreement. The Admiral wouldn't complain about her own party. The two of you leave this woman alone and look for the other two you'd seen.");
                    print();
            else:
                print("You glance at Brazen Elk and shake your head. He nods in agreement. The Admiral wouldn't complain about her own party. The two of you leave this woman alone and look for the other two you'd seen.");
                print();

        elif (choice == 2 and spoken2 == False):
            spoken2 = True;
            print("You and Brazen Elk approach the woman with the striped mask.");
            print();
            print("She's standing with a small group of people, a bottle of ale in her hand as she tells a story. You recognize it as one of the many stories often told about the Admiral herself.");
            print("\"And that's how it happened! Leviathan is not to be messed with, let me tell you!\"");
            print("Brazen Elk is quick to question this");
            print("\"How do you know that's how it went? Last I checked, only the Admiral knows the details of that one. Most of the tales passed around are speculation, nothing more\"");
            print("The men around the women laugh. They insist she knows because she is the Admiral of course! Brazen Elk looks skeptical.");

            print("Do you: ");
            print("1: Believe these men and tell the woman everything");
            print("2: Ask Brazen Elk what's bugging him");
            choice = getMultChoice(2);
            print();
            
            #Ending 6
            if (choice == 1):
                print("You decide Brazen Elk must just be worried. These people have been talking to this woman for awhile, if they believe she's the Admiral she must be! You pull her away from the group and tell her everything. She grows angry. She yells that you don't have to come along and mess with her, if you knew she was pretending just leave her to her fun! This woman was never the Admiral, she had simply gained a group of followers for the evening that thought she was and was basking in the attention. You apologize and move to keep looking, but she punches you across the face and continues hitting. You fall to the ground, and though Brazen Elk is quick to pull her off of you, you're injured quite badly. The woman is kicked out, and you're taken out of the party to the healers. While you recover, Limsa Lominsa never will. Brazen Elk did his best without you, but you knew more evidence than he did. You have no idea if he ever found the Admiral, but later that night you get the news that she had been killed and the party ended early. You will recover from your wounds, but the city may never recover from this loss");
                print();
                print("THE END");
                endGame();
                
            else:
                print("You pull Brazen Elk aside and ask what's bothering him about this woman. He seems relieved you asked as he answers.");
                print("\"There's no way that's the Admiral. I know enough of that tale to know some of what she told was lies, common ones used to embelish the story. It's the version passed around by common folk, but not the one the Admiral would tell herself.\"");
                print("You nod and decide to trust his judgement - he knows more about the Admiral than you do. You leave this woman be and go look for the others you'd seen");
                print();

        elif (choice == 3 and spoken3 == False):
            spoken3 = True;
            print("You and Brazen Elk approach the red masked woman");
            print();

            print("She stands near a large crowd that's taking turns telling war stories. Listening and laughing along with them. Brazen Elk greets the woman.");
            print("\"Good story?\"");
            print("The woman smiles and nods.");
            print("\"He says he killed a hundred Sahagin. The numbers are always exaggerated, but these soldiers can always tell a good tale\"");

            print("Do you: ");
            print("1: Keep listening to the story alongside her\n2: Ask her if she has any good ones of her own");
            choice = getMultChoice(2);
            print();

            if (choice == 1):
                print("The story is exciting, but even someone with no soldiering experience could tell it's quite exaggerated. This man probably never killed a hundred Sahagin and he certainly doesn't look like someone who 'punched Leviathan right in his slimy face'. It's quite entertaining to listen too though, and it's almost dissapointing when the crowd disperses");
                print("The woman beside you seems happy.");
                print("\"I'll never tire of hearing them spin tales like that\"");

            else:
                print("She answers with a laugh");
                print("\"None worth telling like this one, I'm afraid\"");
                print("She does not elaborate on this, but you wait until the current story is over and the crowd is dispersed before continuing to speak to her. She was clearly invested in it.");

            print("Brazen Elk offers his own comment.");
            print("\"They can certainly tell stories. If you want truth you've got to pick it out of the embelishment, but they certainly tell exciting tales\"");

            print("Do you think she could be the Admiral?");
            print("1: Yes, it's possible");
            print("2: No, definitely not");
            choice = getMultChoice(2);
            print();

            if (choice == 1):
                print("You nod at Brazen Elk to continue, you think this woman could be the Admiral. He keeps talking to her");
                print("\"Heard the Admiral is out in this crowd somewhere. Bet she'd have quite the stories to tell\"");

                print("The woman looks unfazed.");
                print("\"Perhaps she is. There's that woman over there who seems insistent it's her. But the version she's telling is a common one full of lies. I doubt the Admiral is out there advertising herself like that.");

                if (spoken2 == True):
                    print("Brazen Elk laughs and shares how you ran into that woman earlier.");

                else:
                    print("Brazen Elk laughs");
                    print("\"Someone's always pretending to be more important than they are at these things\"");

                print("You decision: ");
                print("1: This is the Admiral, tell her everything");
                print("2: This isn't her, continue your search");
                choice = getMultChoice(2);

                #Ending 7
                if (choice == 1):
                    print("You call this woman's bluff. She's clearly the Admiral. She laughs, realizing her low profile wasn't as good as she'd hoped. You tell her everything, and with Brazen Elk backing you up she takes you seriously. She moves to the guards and removes her mask, explaining the situation and giving them orders. She puts the mask back on and moves back through the crowd towards you, now on high alert. So when the Miqo'te woman moves in with a quickly drawn knife, both the Admiral and the guards are prepared. The woman is arrested, and dragged out screeching about how the Admiral ruined everything by ending piracy. Her mask falls off and people recognize her as a wealthy woman who earned her wealth from piracy. The Admiral is grateful to you and Brazen Elk for your efforts and raises a toast in your names. You spend the rest of the evening with her and Brazen Elk, having a great time. People never recognize you in the streets after since they never saw your face, but you often hear tales about how you and Brazen Elk saved the Admiral. It will be remembered for a long time, and Limsa Lominsa can continue into its bright future.");
                    print();
                    print("THE END");
                    endGame();
                          
                else:
                    print("You glance at Brazen Elk and shake your head. This doesn't seem like the Admiral. The two of you regroup to look for the other people you saw.");
                    print();

            else:
                print("You glance at Brazen Elk and shake your head. This doesn't seem like the Admiral. The two of you regroup to look for the other people you saw.");
                print();        

        else:
            print("Brazen Elk quietly reminds you you've already talked to that person. Perhaps another would be a better choice.");
            print();

        if (spoken1 == True and spoken2 == True and spoken3 == True):
            end = True;

    #Ending 8
    print("You spoke to all three women and were fairly certain none of them were the Admiral. They've been lost to the crowd, and though you try speaking to others you still can't find anything. You panic as more and more time passes, you don't know when the killer will strike but you know you must be running out of time. Brazen Elk is calmer than you are and takes control of the search, but even that isn't enough. Eventually, someone falls over dead with a knife between the ribs causing the party to freeze. You heart drops as you realize it was someone you had already spoken to. You hadn't been able to recognize the Admiral and now she was dead. The guests are quickly herded out by the guards, and though you try to stay together you end up losing Brazen Elk in the chaos. Limsa Lomsinsa is forever changed, and you have to live the guilt that you couldn't prevent it.");
    print();
    print("THE END");
    endGame();
