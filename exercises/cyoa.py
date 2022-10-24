"""An adventure game."""

__author__: str = "731615250"

player: str = ""
points: int = 0
WIN_EMOJI: str = "\U0001F389"
LOSE_EMOJI: str = "\U0001F4AA"
CLIFF_EMOJI: str = "\U0001F3D4"
HOME_EMOJI: str = "\U0001F3E0"
ENEMY_EMOJI: str = "\U0001F54B"
CAVE_EMOJI: str = "\U0001FAA8"


def main() -> None:
    """The body of the game."""
    global points
    greet()
    print(f"{player}, you get a sword and a sheild from your father. You earn 20 adventure points automatically.")
    points += 20
    normal_turns: int = 0
    boss_turns: int = 0
    treasure_turns: int = 0
    while points >= 0:
        print(f"You are now in the forest, facing three pathways. Choose one of them.\n1)A path to the cliff. {CLIFF_EMOJI} \n2)The way to home. {HOME_EMOJI} \n3)A path to the middle of nowhere. {ENEMY_EMOJI} \n4)A path to a cave. {CAVE_EMOJI}")
        way_chosen: str = input("Enter order of the way you choose: ")
        if int(way_chosen) == 1:
            boss_dragon(normal_turns, points)
            normal_turns += 1
            print(f"{points} point(s) left.")
        elif int(way_chosen) == 3:
            normal_enemy(boss_turns, points)
            boss_turns += 1
            print(f"{points} point(s) left.")
        elif int(way_chosen) == 4:
            treasure(treasure_turns, points)
            treasure_turns += 1
            print(f"{points} point(s) left.")
        else:
            print("You are on the way back home. Your accumulated adventure points is {points}. Goodbye!")
            quit()
    if points <= 0:
        print("Game over! You have lost all of your adventure points. Try again later!")
        print(LOSE_EMOJI)
        quit()
    
    
def greet() -> None:
    """Greet to the player and introduce the rules of the game."""
    global player
    print("Welcome to the advanture! You are a knight and you are on the journey to find the devil dragon and defeat it! During the journey, you might encounter a bunch of hostile creatures or you might find secret treasure. Be brave and GOOD LUCK!")
    player = input("Enter your name: ")


def attack(attack_time: int) -> int:
    """The function for the action attack."""
    attack_value: int = int(input("The enemy is coming. Enter the value you choose to attack your enemy: "))
    return attack_value


def normal_enemy(turns: int, points: int) -> int:
    """The battle with normal enemies."""
    print("You encounter some hostile creatures during the journey. It's not very hard to defeat them! The life of these enemies is an integer between 1 and 120. You have 4 chances to beat your enemy!")
    if points >= 0:
        if turns <= 7:
            from random import randint
            enemy_life: int = randint(1, 120)
            attack_time: int = 0
            while attack_time <= 4:
                print(f"--- Round {attack_time}/4 ---")
                attack_value: int = attack(attack_time)
                if attack_value == enemy_life:
                    print("Your attack is successful! The enemy is defeated. You get 10 adventure points. ")
                    print(WIN_EMOJI)
                    return points + 10
                else:
                    print("Your guess is not correct!")
                    if attack_value < enemy_life:
                        print("Your guess is too low! The enemy is getting more powerful now. You lose 1 adventure points.")
                    else: 
                        print("Your guess is too high! The enemy is getting more powerful now. You lose 1 adventure points.")
                    points -= 1
                    attack_time += 1
            print("Sorry, you are defeated. You lose 5 adventure points. Come back home and do some pratice. Try again later!")
            print(LOSE_EMOJI)
            return points - 5
        else:
            print("You can't see any enemies. Go back and choose your path again!")
            return points
    else:
        print("You don't have enough adventure points. Go back and try another path!")
        return points
        

def boss_dragon(turns: int, points: int) -> int:
    """The battle with the boss, the dragon."""
    print("You meet the dragon! The life of the value is an integer between 1 and 500. You have 8 chances to beat your enemy!")
    if points <= 20:
        if turns <= 2:
            from random import randint
            boss_life: int = randint(1, 500)
            attack_time: int = 0
            while attack_time <= 8:
                print(f"--- Round {attack_time}/8 ---")
                attack_value: int = attack(attack_time)
                if attack_value == boss_life:
                    print("Your attack is successful! ")
                    print(WIN_EMOJI)
                    return points + 50
                else:
                    print("Your guess is not correct!")
                    if attack_value < boss_life:
                        print("Your guess is too low! The enemy is getting more powerful now. You lose 5 adventure points.")
                    else: 
                        print("Your guess is too high! The enemy is getting more powerful now. You lose 5 adventure points.")
                    points -= 5
                    attack_time += 1
            print("Sorry, you are defeated. You lose 5 adventure points. Come back home and do some pratice. Try again later!")
            print(LOSE_EMOJI)      
            return points - 20
        else:
            print("You can't see any enemies. Go back and choose your path again!")
            return points
    else:
        print("You don't have enough adventure points. Go back and try another path!")
        return points


def treasure(treasure_turns: int, points: int) -> int:
    """Treasure helps add adventure points."""
    if treasure_turns <= 2:
        return points
    else:
        return points


if __name__ == "__main__":
    main()