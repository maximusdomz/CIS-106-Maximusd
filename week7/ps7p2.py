def calc_batting_average(number_of_hits, number_of_at_bats):
    if number_of_at_bats == 0:
        return 0.0
    else:
        batting_average = number_of_hits / number_of_at_bats
        return round(batting_average, 3)

def main():
    number_of_players = 0

    while True:
        player_last_name = input("Please enter your last name: ")
        try:
            number_of_hits = int(input("Please enter your number of hits: "))
            number_of_at_bats = int(input("Please enter your number of at-bats: "))
        except ValueError:
            print("Please enter a number.")
            continue

        batting_average = calc_batting_average(number_of_hits, number_of_at_bats)

        print(f"Player: {player_last_name}, Batting Average: {batting_average:.3f}")
        number_of_players += 1

        another = input("Do you want to enter another player? (Yes/No): ").lower()
        if another != "yes":
            break

    print(f"\nTotal number of players entered: {number_of_players}")

if __name__ == "__main__":
    main()