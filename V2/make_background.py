from random import choice

all_colors = ['white', 'yellow', 'red','green','purple','orange', 'blue']
used_colors=[]
size = 50

def chose_color():
    global all_colors,used_colors
    avalable = list(set(all_colors)-set(used_colors))
    color = choice(avalable)
    used_colors.append(color)
    if used_colors.lenght== all_colors.length : 
        used_colors = []
    return color


    


def make_line(case,background,direction, x_start,y_start,number):
    if direction=='h':
        for x in range(x_start, x_start+size*number):
            case.append( background.create_rectangle(x, y_start, x+50, y_start+50, fill = chose_color) )         # 0
    else :
        for y in range(y_start, y_start+size*number):
            case.append( background.create_rectangle(x, y_start, x+50, y_start+50, fill = chose_color) )         # 0

def make_square(case,background,x_center,y_center):
    for x in range(x_center-size,x_center+size):
        for y in range(y_center-size,y_center+size):
            if (x,y != x_center,y_center):
               case.append( background.create_rectangle(x, y, x+size, y+size, fill = chose_color) )         # 0
  
            
def makebackground(background):

    case = [ ]
    case.append( background.create_rectangle(30, 750, 100, 800, fill = 'white') )         # 0

    case.append( background.create_rectangle(40, 700, 90, 750, fill = 'yellow') )
    case.append( background.create_rectangle(40, 650, 90, 700, fill = 'red') )
    case.append( background.create_rectangle(40, 600, 90, 650, fill = 'green') )
    case.append( background.create_rectangle(40, 550, 90, 600, fill = 'purple') )
    case.append( background.create_rectangle(40, 500, 90, 550, fill = 'orange') )         # 5
    case.append( background.create_rectangle(40, 450, 90, 500, fill = 'red') )
    case.append( background.create_rectangle(40, 400, 90, 450, fill = 'blue') )
    case.append( background.create_rectangle(40, 350, 90, 400, fill = 'green') )
    case.append( background.create_rectangle(40, 300, 90, 350, fill = 'yellow') )
    case.append( background.create_rectangle(40, 250, 90, 300, fill = 'orange') )         # 10
    case.append( background.create_rectangle(40, 200, 90, 250, fill = 'purple') )
    case.append( background.create_rectangle(40, 150, 90, 200, fill = 'black') )
    case.append( background.create_rectangle(40, 100, 90, 150, fill = 'yellow') )
    case.append( background.create_rectangle(40, 50, 90, 100, fill = 'red') )
    case.append( background.create_rectangle(40, 0, 90, 50, fill = 'blue') )              # 15
    case.append( background.create_rectangle(90, 0, 140, 50, fill = 'yellow') )
    case.append( background.create_rectangle(140, 0, 190, 50, fill = 'black') )
    case.append( background.create_rectangle(190, 0, 240, 50, fill = 'green') )
    case.append( background.create_rectangle(240, 0, 290, 50, fill = 'purple') )
    case.append( background.create_rectangle(290, 0, 340, 50, fill = 'orange') )          # 20
    case.append( background.create_rectangle(290, 50, 340, 100, fill = 'red') )
    case.append( background.create_rectangle(290, 100, 340, 150, fill = 'black') )
    case.append( background.create_rectangle(290, 150, 340, 200, fill = 'green') )
    case.append( background.create_rectangle(290, 200, 340, 250, fill = 'blue') )
    case.append( background.create_rectangle(240, 200, 290, 250, fill = 'red') )          # 25
    case.append( background.create_rectangle(190, 200, 240, 250, fill = 'yellow') )
    case.append( background.create_rectangle(140, 200, 190, 250, fill = 'white') )
    case.append( background.create_rectangle(140, 250, 190, 300, fill = 'purple') )
    case.append( background.create_rectangle(140, 300, 190, 350, fill = 'black') )
    case.append( background.create_rectangle(140, 350, 190, 400, fill = 'orange') )       # 30
    case.append( background.create_rectangle(140, 400, 190, 450, fill = 'green') )
    case.append( background.create_rectangle(190, 400, 240, 450, fill = 'black') )
    case.append( background.create_rectangle(240, 400, 290, 450, fill = 'blue') )
    case.append( background.create_rectangle(290, 400, 340, 450, fill = 'red') )
    case.append( background.create_rectangle(290, 450, 340, 500, fill = 'yellow') )       # 35
    case.append( background.create_rectangle(290, 500, 340, 550, fill = 'purple') )
    case.append( background.create_rectangle(290, 550, 340, 600, fill = 'green') )
    case.append( background.create_rectangle(290, 600, 340, 650, fill = 'orange') )
    case.append( background.create_rectangle(240, 600, 290, 650, fill = 'red') )
    case.append( background.create_rectangle(190, 600, 240, 650, fill = 'blue') )         # 40
    case.append( background.create_rectangle(140, 600, 190, 650, fill = 'black') )
    case.append( background.create_rectangle(140, 650, 190, 700, fill = 'yellow') )
    case.append( background.create_rectangle(140, 700, 190, 750, fill = 'red') )
    case.append( background.create_rectangle(140, 750, 190, 800, fill = 'orange') )
    case.append( background.create_rectangle(190, 750, 240, 800, fill = 'purple') )       # 45
    case.append( background.create_rectangle(240, 750, 290, 800, fill = 'green') )
    case.append( background.create_rectangle(290, 750, 340, 800, fill = 'red') )
    case.append( background.create_rectangle(340, 750, 390, 800, fill = 'blue') )
    case.append( background.create_rectangle(390, 750, 440, 800, fill = 'yellow') )
    case.append( background.create_rectangle(440, 750, 490, 800, fill = 'orange') )        #50
    case.append( background.create_rectangle(490, 750, 540, 800, fill = 'purple') )
    case.append( background.create_rectangle(490, 700, 540, 750, fill = 'red') )
    case.append( background.create_rectangle(490, 650, 540, 700, fill = 'black') )
    case.append( background.create_rectangle(490, 600, 540, 650, fill = 'blue') )
    case.append( background.create_rectangle(490, 550, 540, 600, fill = 'green') )        # 55
    case.append( background.create_rectangle(490, 500, 540, 550, fill = 'purple') )
    case.append( background.create_rectangle(490, 450, 540, 500, fill = 'black') )        # debut de la boucle
    case.append( background.create_rectangle(440, 450, 490, 500, fill = 'blue') )
    case.append( background.create_rectangle(390, 450, 440, 500, fill = 'white') )
    case.append( background.create_rectangle(390, 400, 440, 450, fill = 'yellow') )       # 60
    case.append( background.create_rectangle(390, 350, 440, 400, fill = 'red') )
    case.append( background.create_rectangle(390, 300, 440, 350, fill = 'orange') )
    case.append( background.create_rectangle(390, 250, 440, 300, fill = 'black') )
    case.append( background.create_rectangle(390, 200, 440, 250, fill = 'green') )
    case.append( background.create_rectangle(440, 200, 490, 250, fill = 'red') )          # 65
    case.append( background.create_rectangle(490, 200, 540, 250, fill = 'yellow') )
    case.append( background.create_rectangle(540, 200, 590, 250, fill = 'blue') )
    case.append( background.create_rectangle(590, 200, 640, 250, fill = 'yellow') )
    case.append( background.create_rectangle(640, 200, 690, 250, fill = 'purple') )
    case.append( background.create_rectangle(640, 250, 690, 300, fill = 'red') )          # 70
    case.append( background.create_rectangle(640, 300, 690, 350, fill = 'orange') )
    case.append( background.create_rectangle(640, 350, 690, 400, fill = 'green') )
    case.append( background.create_rectangle(640, 400, 690, 450, fill = 'black') )
    case.append( background.create_rectangle(640, 450, 690, 500, fill = 'yellow') )
    case.append( background.create_rectangle(590, 450, 640, 500, fill = 'blue') )         # 75
    case.append( background.create_rectangle(540, 450, 590, 500, fill = 'purple') )       # fin de la boucle
    case.append( background.create_rectangle(540, 150, 590, 200, fill = 'black') )
    case.append( background.create_rectangle(540, 100, 590, 150, fill = 'green') )
    case.append( background.create_rectangle(540, 50, 590, 100, fill = 'orange') )
    case.append( background.create_rectangle(540, 0, 590, 50, fill = 'red') )             # 80
    case.append( background.create_rectangle(590, 0, 640, 50, fill = 'purple') )
    case.append( background.create_rectangle(640, 0, 690, 50, fill = 'yellow') )
    case.append( background.create_rectangle(690, 0, 740, 50, fill = 'red') )
    case.append( background.create_rectangle(740, 0, 790, 50, fill = 'orange') )
    case.append( background.create_rectangle(790, 0, 840, 50, fill = 'black') )           # 85
    case.append( background.create_rectangle(840, 0, 890, 50, fill = 'red') )
    case.append( background.create_rectangle(840, 50, 890, 100, fill = 'purple') )
    case.append( background.create_rectangle(840, 100, 890, 150, fill = 'blue') )         # debut de la boucle
    case.append( background.create_rectangle(790, 100, 840, 150, fill = 'yellow') )
    case.append( background.create_rectangle(740, 100, 790, 150, fill = 'purple') )       # 90
    case.append( background.create_rectangle(740, 150, 790, 200, fill = 'red') )
    case.append( background.create_rectangle(740, 200, 790, 250, fill = 'orange') )
    case.append( background.create_rectangle(740, 250, 790, 300, fill = 'green') )
    case.append( background.create_rectangle(790, 250, 840, 300, fill = 'blue') )
    case.append( background.create_rectangle(840, 250, 890, 300, fill = 'yellow') )       # 95
    case.append( background.create_rectangle(890, 250, 940, 300, fill = 'blue') )
    case.append( background.create_rectangle(940, 250, 990, 300, fill = 'purple') )
    case.append( background.create_rectangle(940, 200, 990, 250, fill = 'black') )
    case.append( background.create_rectangle(940, 150, 990, 200, fill = 'green') )
    case.append( background.create_rectangle(940, 100, 990, 150, fill = 'orange') )       # 100
    case.append( background.create_rectangle(890, 100, 940, 150, fill = 'red') )          # fin de boucle
    case.append( background.create_rectangle(840, 300, 890, 350, fill = 'white') )
    case.append( background.create_rectangle(840, 350, 890, 400, fill = 'blue') )
    case.append( background.create_rectangle(840, 400, 890, 450, fill = 'red') )
    case.append( background.create_rectangle(840, 450, 890, 500, fill = 'blue') )         # 105
    case.append( background.create_rectangle(840, 500, 890, 550, fill = 'yellow') )
    case.append( background.create_rectangle(840, 550, 890, 600, fill = 'purple') )
    case.append( background.create_rectangle(840, 600, 890, 650, fill = 'red') )
    case.append( background.create_rectangle(840, 650, 890, 700, fill = 'orange') )
    case.append( background.create_rectangle(840, 700, 890, 750, fill = 'green') )        # 110
    case.append( background.create_rectangle(840, 750, 890, 800, fill = 'blue') )
    case.append( background.create_rectangle(890, 750, 940, 800, fill = 'yellow') )
    case.append( background.create_rectangle(940, 750, 990, 800, fill = 'black') )
    case.append( background.create_rectangle(990, 750, 1040, 800, fill = 'purple') )
    case.append( background.create_rectangle(1040, 750, 1090, 800, fill = 'blue') )       # 115
    case.append( background.create_rectangle(1090, 750, 1140, 800, fill = 'green') )
    case.append( background.create_rectangle(1140, 750, 1190, 800, fill = 'orange') )
    case.append( background.create_rectangle(1140, 700, 1190, 750, fill = 'white') )
    #   cases par matière
    case.append( background.create_rectangle(1040, 550, 1190, 700, fill = 'orangered') )
    case.append( background.create_rectangle(1040, 400, 1190, 550, fill = 'deepskyblue') )# 120
    case.append( background.create_rectangle(1040, 250, 1190, 400, fill = 'chocolate') )
    case.append( background.create_rectangle(1040, 100, 1190, 250, fill = 'gold') )
    #   prison
    case.append( background.create_rectangle(650, 570, 750, 770, fill = 'navy') )
    #   cases légendes
    case.append( background.create_rectangle(1200, 400, 1250, 450, fill = 'red'))
    case.append( background.create_rectangle(1200, 450, 1250, 500, fill = 'purple'))
    case.append( background.create_rectangle(1200, 500, 1250, 550, fill = 'blue'))
    case.append( background.create_rectangle(1200, 550, 1250, 600, fill = 'yellow'))
    case.append( background.create_rectangle(1200, 600, 1250, 650, fill = 'green'))
    case.append( background.create_rectangle(1200, 650, 1250, 700, fill = 'black'))
    case.append( background.create_rectangle(1200, 700, 1250, 750, fill = 'orange'))

    #   legendes des couleurs
    texteRouge = background.create_text(1285, 420,font = 250, text="Maths")
    texteViolet = background.create_text(1295, 470,font = 250, text="CultureG")
    texteBleu = background.create_text(1315, 520,font = 250, text="Philo/Français")
    texteJaune = background.create_text(1325, 570,font = 250, text="Physique/Chimie")
    texteVert = background.create_text(1305, 620,font = 250, text="SVT/Anglais")
    texteNoire = background.create_text(1315, 670,font = 250, text="Manga/Anime")
    texteOrange = background.create_text(1310, 720,font = 250, text="Histoire/Géo")

    #   ligne de separation
    background.create_line(1195, 0, 1195, 800)

    #   texte dans les cases particulieres
    texteBac = background.create_text(1110, 175,font = 250, text="Le Bac")
    texteS = background.create_text(1110, 620,font = 250, text="S")
    texteL = background.create_text(1110, 480,font = 250, text="L",)
    texteES = background.create_text(1110, 325,font = 250, text="ES")
    textePrison = background.create_text(700, 680, font = 250, fill = "red", text="PRISON")

    return case
