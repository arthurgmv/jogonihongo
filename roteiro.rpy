# Declare characters used by this game
define tabata = Character("Tabata")
define yusuke = Character ("Yusuke")
define sensei = Character ("Sensei")


# The game starts here
label start:
    scene bg sala de aula   
    show tabata
    tabata "Hoje tem aula de japonês, e eu amor ter aulas de japonês!"
    tabata "Mas não pensem que é porque eu sou estudiosa, mas sim porque..."
    tabata "O Yusuke vai estar lá, nossa ele é tão lindo!!! Tenho de impressioná-lo hoje!"
    tabata "andei estudando bastante em casa, ele vai ficar muito interessado em mim!"

    # This ends the game.
    return