import random

# Base de données des régions et leurs chefs-lieux
regions = {
    "Abidjan": "Abidjan",
    "Bas-Sassandra": "San-Pédro",
    "Comoé": "Abengourou",
    "Denguélé": "Odienné",
    "Gôh-Djiboua": "Gagnoa",
    "Lacs": "Yamoussoukro",
    "Lagunes": "Dabou",
    "Montagnes": "Man",
    "Savanes": "Korhogo",
    "Vallée du Bandama": "Bouaké",
    "Woroba": "Séguéla",
    "Zanzan": "Bondoukou",
}

# Tableau des meilleurs scores
meilleurs_scores = [0, 0, 0, 0, 0]

def afficher_meilleurs_scores():
    print("\n=== Meilleurs scores ===")
    for i, score in enumerate(sorted(meilleurs_scores, reverse=True), 1):
        print(f"{i}. {score} points")

def poser_question(region, chef_lieu):
    print(f"Quel est le chef-lieu de la région {region} ?")
    reponse = input("Votre réponse : ").strip()
    if reponse.lower() == chef_lieu.lower():
        print("Bonne réponse !")
        return True
    else:
        print(f"Mauvaise réponse. La bonne réponse est : {chef_lieu}")
        return False

def jeu():
    global meilleurs_scores

    # Mélanger les régions pour poser des questions aléatoires
    questions = list(regions.items())
    random.shuffle(questions)

    # Limiter à 10 questions
    questions = questions[:10]

    score = 0
    for region, chef_lieu in questions:
        if poser_question(region, chef_lieu):
            score += 1

    print(f"\nVotre score final : {score} / 10")

    # Mise à jour des meilleurs scores
    meilleurs_scores.append(score)
    meilleurs_scores = sorted(meilleurs_scores, reverse=True)[:5]

def main():
    print("Bienvenue dans le jeu sur les régions de Côte d'Ivoire !")

    while True:
        afficher_meilleurs_scores()
        print("\nNouvelle partie de jeu !")
        jeu()

        rejouer = input("Voulez-vous rejouer ? (oui/non) : ").strip().lower()
        if rejouer != "oui":
            print("Merci d'avoir joué. À bientôt !")
            break

if __name__ == "__main__":
    main()
