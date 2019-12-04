def speaking_grandma(phrase):
    if phrase != phrase.upper():
        print("HUH?! SPEAK UP, SONNY!")
    elif phrase == "I LOVE YOU GRANDMA!":
        print("I LOVE YOU TOO PUMPKIN!")
    elif phrase == phrase.upper():
        print("NO, NOT SINCE 1938!.")


speaking_grandma("I LOVE YOU GRANDMA!")
speaking_grandma("blah")
speaking_grandma("BLAH")
