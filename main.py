"""c'est une fonction palindrome"""
#### Fonction secondaire


def ispalindrome(p):
    """fonction vérifie si palindrome"""
    accents = "éàèùâêîôûäëïöüç.;,-_:?!'"
    pas_accents = "eaeuaeiouaeiouc         "
    p = p.lower()
    p = p.translate(str.maketrans(accents, pas_accents)).replace(" ", "")
    return p == p[::-1]

#### Fonction principale

def main():
    """test de la fonctionne ispalindrome"""
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
