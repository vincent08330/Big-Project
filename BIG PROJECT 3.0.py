from tkinter import *                                                # apport tk

bleu_nuit = (125, 125, 125)
vert      = ( 30, 200,  82)                                             # set up var couleurs
rouge     = (255,   0,   0)
bleu      = ( 48, 159, 236)
violet     = (125,   0,  50)


menu = Tk()                                                             # taille fenetre

menu.geometry("200x100")

menu["bg"] = "light blue"


Titre = Label(menu, text="Select your game mode:")                      # titre / couleur
Titre["fg"] = "black"
Titre["bg"] = "light blue"
Titre.pack()

var_jeu1 = IntVar()
jeu1 = Checkbutton (menu, text="Mode 1v1", variable = var_jeu1)         # case 1 à cocher
jeu1.pack()

var_jeu2 = IntVar()
jeu2 = Checkbutton(menu, text="Tower defense", variable = var_jeu2)     # case 2 à cocher
jeu2.pack()

bouton_quitter = Button(menu, text="Valider", command=menu.quit)
bouton_quitter.pack()

menu.mainloop()
menu.destroy()



if (var_jeu2.get() == 1):                                                    # si case 2 cochée

    import pygame
    from pygame.locals import *                                             # pygame import

    pygame.init()
    taille_fenetre = (750,775)                                             # gestion fenetre
    fenetre_rect = pygame.Rect((0, 0), taille_fenetre)
    screen_surface = pygame.display.set_mode(taille_fenetre)

    timer = pygame.time.Clock()

    p1 = pygame.Surface((25, 25))                                            # p1 = player 1   #taille
    p1.fill(rouge)

    x, y = 500, 500                                                         #position + vitesse
    vx, vy = 0, 0

    p2 = pygame.Surface((25, 25))                                            # p2 = player 2   # taille
    p2.fill(bleu)

    x2, y2 = 250, 500                                                         #position + vitesse
    vx2, vy2 = 0, 0

    pistol1 = pygame.Surface((5,15))
    pistol1.fill(violet)

    direction_x1 = x+10
    direction_y1 = y-10


    pistol2 = pygame.Surface((5,15))
    pistol2.fill(violet)

    direction_x2 = x2+10
    direction_y2 = y2-10



    mur = pygame.Surface((25, 25))                                           #taille blocks
    mur.fill(vert)

    niveau = [
      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],             # visuel niveau
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
      ]

    def dessiner_niveau(surface, niveau):                                                               #cases

      for j, ligne in enumerate(niveau):
           for i, case in enumerate(ligne):                                            # gestion apparitions blocks
             if case == 1:
                 surface.blit(mur, (i*25, j*25))                                     # taille block



    continuer = True

    while continuer == True :
        for event in pygame.event.get():
            if event.type == QUIT :
                continuer = False

        timer.tick(60)                                                                      #clock
        keys_pressed = pygame.key.get_pressed()
        vx = (keys_pressed[K_RIGHT] - keys_pressed[K_LEFT]) * 3                          #keys moves
        vy = (keys_pressed[K_DOWN] - keys_pressed[K_UP]) * 3
        x += vx
        y += vy                                                                             #vitesse
        y  = min(725,  y)
        y  = max(  0,  y)
        x  = max(  x,   0)                                                                  #maxs et mins
        x  = min(  x, 725)


        if vx > 1:
            pistol1 = pygame.Surface((15,5))
            pistol1.fill(violet)
            direction_x1 = x+20
            direction_y1 = y+10

        elif vx < 0:
            pistol1 = pygame.Surface((15,5))
            pistol1.fill(violet)
            direction_x1 = x-10
            direction_y1 = y+10


        if vy > 1:
            pistol1 = pygame.Surface((5,15))
            pistol1.fill(violet)
            direction_x1 = x+10
            direction_y1 = y+20

        elif vy < 0:
            pistol1 = pygame.Surface((5,15))
            pistol1.fill(violet)
            direction_x1 = x+10
            direction_y1 = y-10

        xpistol1, ypistol1 = direction_x1, direction_y1







        vx2 = (keys_pressed[K_d] - keys_pressed[K_a]) * 3                                    #keys moves
        vy2 = (keys_pressed[K_s] - keys_pressed[K_w]) * 3
        x2 += vx2
        y2 += vy2                                                                             #vitesse
        y2  = min(725,  y2)
        y2  = max(  0,  y2)
        x2  = max(  x2,   0)                                                                  #maxs et mins
        x2  = min(  x2, 725)


        if vx2 > 1:
            pistol2 = pygame.Surface((15,5))
            pistol2.fill(violet)
            direction_x2 = x2+20
            direction_y2 = y2+10

        elif vx2 < 0:
            pistol2 = pygame.Surface((15,5))
            pistol2.fill(violet)
            direction_x2 = x2-10
            direction_y2 = y2+10


        if vy2 > 1:
            pistol2 = pygame.Surface((5,15))
            pistol2.fill(violet)
            direction_x2 = x2+10
            direction_y2 = y2+20

        elif vy2 < 0:
            pistol2 = pygame.Surface((5,15))
            pistol2.fill(violet)
            direction_x2 = x2+10
            direction_y2 = y2-10

        xpistol2, ypistol2 = direction_x2, direction_y2




        screen_surface.fill(bleu_nuit)                                                   # couleur fenetre
        dessiner_niveau(screen_surface, niveau)
        screen_surface.blit(p1, (x, y))                                                  # affichage p1
        screen_surface.blit(p2, (x2, y2))
        screen_surface.blit(pistol1, (xpistol1, ypistol1))
        screen_surface.blit(pistol2, (xpistol2, ypistol2))                                                # affichage p2
        pygame.display.flip()

        if keys_pressed[K_e] > 0:
            print("okkk")

        if keys_pressed[K_SPACE] > 0:
            print("pew pew")


    pygame.quit()




if (var_jeu1.get() == 1):

    print("youpiiiiiiiiii")



