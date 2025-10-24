import random
import colorama

def initialisation(): # Initialisation du plateau 
    color=["bleue","rouge","jaune","violet","rose","blanc"]
    guess = association_secrete(color)
    print("============================================ MASTER MIND ============================================ \n")
    return color, guess
    


def association_secrete (color) : #Combinaison secrète
    return random.sample(color, 4)

def ask_username() :
    user=input("Veuillez saisir votre username pour continuer la partie : ") 
    return user


def association_user(color,guess,user) : # On initialise le joueur et sa combinaison

    ok=False 
    over=0

    while not ok and over<=10:
        print("\nTentative : "+str(over)+"/10")
        over+=1
        association=input(user+" Veuillez saisir votre combinaision : \n\n"
                          +"- 0 pour "+colorama.Fore.BLUE+"Bleue\n"+colorama.Style.RESET_ALL
                          +"- 1 pour "+colorama.Fore.RED+"Rouge\n"+colorama.Style.RESET_ALL
                          +"- 2 pour "+colorama.Fore.YELLOW+"Jaune \n"+colorama.Style.RESET_ALL
                          +"- 3 pour "+colorama.Fore.MAGENTA+"Violet \n"+colorama.Style.RESET_ALL
                          +"- 4 pour "+colorama.Fore.LIGHTRED_EX+"Rose \n"+colorama.Style.RESET_ALL
                          +"- 5 pour "+colorama.Fore.WHITE+"Blanc \n\n"
                          +colorama.Style.RESET_ALL).strip().split()

        if len(association) != 4 :
            print("Veuillez saisir exactement 4 nombres !")
            continue
        if all(element.isdigit() and 0 <= int(element) <=5 for element in association) :
            color_user=convert_in_color(association,color)
            print("Saisi de l'utilisateur "+user+ ": "+str(color_user))
            ok=True

            validate=guess_color(color_user,guess)

            if not validate_color(validate) :
                yes=element_yes(validate)
                no=element_no(validate)
                ok=False

                print(f"Vous avez {yes} bonne{'s' if yes > 1 else ''} réponse{'s' if yes > 1 else ''} et "f"{no} mauvaise{'s' if no > 1 else ''} réponse{'s' if no > 1 else ''} : {validate}")
            else :
                ok=True
                print("__________________________________ Vous avez gagné ! __________________________________")
    if not ok : 
        print("Fin de partie ! \nLa combinaison était : ",guess)

    return ok
            

    

def convert_in_color(association, color) : # ici l'utilisateur va deviner la combinaison
    return [color[int(element)] for element in association]


def guess_color(user,color) : # On indique le nombre de couleurs corrects à la bonne position avec un symbole '*' sinon '-'
    validate=[]
    for color_element in range(len(user)) :
        if user[color_element]==color[color_element] :
            validate.append("*")
        elif user[color_element] in color :
           validate.append("-")
        else :
            validate.append("-")
    return validate

def validate_color(user_validate) :
    return all(element=="*" for element in user_validate)

def element_yes(user_validate) :
    return  sum(element_yes=="*" for element_yes in user_validate)

def element_no(user_validate) :
    return  sum(element_yes=="-" for element_yes in user_validate)

def game() :
    over=0
    color, guess=initialisation()
    user=ask_username()
    win=association_user(color,guess,user)
 

if __name__ == "__main__":
    game()