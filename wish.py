# This program was crated to simulate wishing in a game "Genshin Impact"
# I assume that you know how this mechanic works and I'll be using terminology specific to the game

import random as r

# This function solely purpose is to decide whenever you won 50/50 or not
# Works both for the 4-stars and 5-stars

def characterRoll(banner, standard, fifty_fifty):
    if fifty_fifty == True:
        return banner + 1, standard, False
    else:
        if r.randint(0,1) == 1:
            return banner + 1, standard, False
        else:
            return banner, standard + 1, True

# This function has all the logic responsible for choosing the outcome of users wish

def roll(wish, banner5, standard5, banner4, standard4, fifty_fifty5, fifty_fifty4, garbage, soft_pity, pity):
    if wish <= 6 + soft_pity:
        banner5, standard5, fifty_fifty5 = characterRoll(banner5, standard5, fifty_fifty5)
        pity = 0
    elif wish <= 51 + soft_pity and wish > 6 + soft_pity:
        banner4, standard4, fifty_fifty4 = characterRoll(banner4, standard4, fifty_fifty4)
    else:
        garbage += 1
    return banner5, standard5, banner4, standard4, fifty_fifty5, fifty_fifty4, garbage, pity


def main():
    num_of_wishes = int(input("How many wishes do you want to simulate? "))


    five_star_fifty_fifty = False
    four_star_fifty_fifty = False
    pity = 1
    soft_pity = 0
    # Soft pity is a theory popular among Genshin players. It postulate that if you reach 75 pity, chances to drop 5-star (slightly) increase.
    # Most of 5-star pulls occur between 75 to 85 wishes, so it seems like a reasonable theory, but it was never confirmed by the devs.
    banner_five_star_count = 0
    standard_five_star_count = 0
    banner_four_star_count = 0
    standard_four_star_count = 0
    garbage_count = 0

    for wishes in range(num_of_wishes):
        if pity % 90 == 0 and pity != 0:
            banner_five_star_count, standard_five_star_count, five_star_fifty_fifty = characterRoll(banner_five_star_count, standard_five_star_count, five_star_fifty_fifty)
            pity = 0
        elif pity % 10 == 0 and pity != 0:
            banner_four_star_count, standard_four_star_count, four_star_fifty_fifty = characterRoll(banner_four_star_count, standard_four_star_count, four_star_fifty_fifty)
        else:
            if pity > 75:
                soft_pity = 3 # If you don't want soft pity you can simply put 0 here
            else:
                soft_pity = 0
            wish = r.randint(1,1000)
            banner_five_star_count, standard_five_star_count, banner_four_star_count, standard_four_star_count, five_star_fifty_fifty, four_star_fifty_fifty, garbage_count, pity = roll(wish, banner_five_star_count, standard_five_star_count, banner_four_star_count, standard_four_star_count, five_star_fifty_fifty, four_star_fifty_fifty, garbage_count, soft_pity, pity)
        pity += 1

    print(f"You rolled {num_of_wishes} wishes and got:\n{banner_five_star_count} banner 5-stars\n{standard_five_star_count} standard 5-stars\n{banner_four_star_count} banner 4-stars\n{standard_four_star_count} standard 4-stars\n{garbage_count} garbage\n\n")
    print(f"That means you've got 5-star character once per {round(num_of_wishes / (banner_five_star_count + standard_five_star_count))} wishes") 
    print(f"{round((banner_five_star_count / (banner_five_star_count + standard_five_star_count)*100),3)}% of them were from the banner")

if __name__ == "__main__":
    main()