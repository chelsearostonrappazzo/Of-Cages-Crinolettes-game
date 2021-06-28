# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define nb = Character("Lady Natalena")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg darktown
    with fade

    play music "audio/vocalise.mp3"

    narrator """

    Beneath the city of Lucca, speakeasies, theaters and gambling dens appeared.

    The locals called it 'Darktown' in the most reverent of whispers.

    The denizens of the world above did not even notice its existence.

    It was a place where one escaped the after effects of the Wars.

    Where a girl like me escaped the confines of the Duke's Palace with the sorriest excuse of an enchantment to darken my hair.

    A place where ladies shed their corsets to don spangled dresses that dusted their calves.

    For just a few hours, I could just breathe...

    Free from the Cloud District and the Duke's Palace.

    Down here, no one knew me as the Brunelli Bastard or sneered and called me an island rat from Rasenna.

    It was nice to just forget amongst acquaintances who knew nothing of the life I lived during the day.

    """

    
    show natalena darktown
    with fade



    return
