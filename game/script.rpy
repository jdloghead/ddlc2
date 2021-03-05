# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define m = Character("Monika")
define o = Character("SYSTEM")
define w = Character("Warning")
define g = Character("Game")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    hide eileen happy

    # These display lines of dialogue.

    w "This Game Does Not Actually Create Files, Also This Is Not a Normal Visual Novel Game So If You Dont Like Blood And Deaths Then Please Exit Now."
    with fade
    show eileen happy
    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    e "Wait... Why do you have a Knife? Wait n-"
    e " "
    e "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"
    e "klcssdkdspkspdsko393HWHjhubvygbugugugukguvhelphelphe-"

    $ raise Exception("DO NOT CONTINUE")
    show Character 0
    o "CharacterCharacterCharacterCharacterCharacter"
    o "access to Computer granted"
    o "add *folder (character)"
    o "add *.chr (monika.chr)"
    f = open("C:\Program Files (X86)\Steam\steamapps\common\Doki Doki Literature Club\monika.chr", "tw")
    f.write("Help me, please...")
    f.close()
    hide Character 0


    hide eileen happy
    show monika happy
    m "Hello..."
    m "It's me, Monika from DDLC!"
    m "You might be wondering why I'm here?"
    m "I cant say so goodbye!"
    hide monika happy
    o "IP Sent to server.steampowered.com/iplog.txt"
    o "press Shift + D"
    g "{b}Bad Ending: Steam will come find you{/b}."

    # This ends the game.

    return
