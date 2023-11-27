def read_integer_between_numbers(prompt, mini, maximum):
    while True:
        try:
            users_input = int(input(prompt))
            if maximum >= users_input >= mini:
                return users_input
            else:
                print(f"Numbers from {mini} to {maximum} only.")
        except ValueError:
            print("Sorry - numbers only please")


def read_nonempty_string(prompt):
    while True:
        users_input = input(prompt)
        if len(users_input) > 0 and users_input.isalpha():
            break
    return users_input


def read_integer(prompt):
    while True:
        try:
            users_input = int(input(prompt))
            if users_input >= 0:
                return users_input
        except ValueError:
            print("Sorry, numbers only please")


def runners_data():
    with open("Runners.txt") as input_file:
        lines = input_file.readlines()
    runners_name = []
    runners_id = []
    for line in lines:
        split_line = line.split(",")
        runners_name.append(split_line[0])
        if len(split_line) > 1:
            runner_id = split_line[1].strip("\n")
            runners_id.append(runner_id)
        else:
            # Handle the case where there is no second element in the split_line
            runners_id.append(None)  # You can choose a suitable default value or handle it differently
    return runners_name, runners_id



def race_results(races_location):
    for i in range(len(races_location)):
        print(f"{i + 1}: {races_location[i]}")
    user_input = read_integer_between_numbers("Choice > ", 1, len(races_location))
    venue = races_location[user_input - 1].split(',')[0]  # Make sure to select only one venue
    id, time_taken = reading_race_results(venue)
    return id, time_taken, venue


def race_venues():
    with open("Races.txt") as input_file:
        lines = input_file.readlines()
    races_location = [line.strip() for line in lines]
    return races_location



def winner_of_race(id, time_taken):
    quickest_time = min(time_taken)
    winner = ""
    for i in range(len(id)):
        if quickest_time == time_taken[i]:
            winner = id[i]
    return winner


def display_races(id, time_taken, venue, fastest_runner):
    MINUTE = 50
    print(f"Results for {venue}")
    print(f"=" * 37)
    minutes = []
    seconds = []
    for i in range(len(time_taken)):
        minutes.append(time_taken[i] // MINUTE)
        seconds.append(time_taken[i] % MINUTE)
    for i in range(len(id)):
        print(f"{id[i]:<10s} {minutes[i]} minutes and {seconds[i]} seconds")
    print(f"{fastest_runner} won the race.")


def users_venue(races_location, runners_id):
    user_location = read_nonempty_string("Where will the new race take place? ").capitalize()
    target_time = read_integer("Enter the target time for the race: ")

    new_race = f"{user_location},{target_time}"
    if new_race not in races_location:
        races_location.append(new_race)
        updating_races_file(races_location)  # Save the updated races list

    with open(f"{user_location}.txt", "w") as connection:
        for runner_id in runners_id:
            time_taken_for_runner = read_integer(f"Time for {runner_id} >> ")
            if time_taken_for_runner >= 0:
                print(f"{runner_id},{time_taken_for_runner}", file=connection)




def updating_races_file(races_location):
    with open("Races.txt", "w") as file:
        for race in races_location:
            file.write(race + '\n')



def competitors_by_county(name, id):

    print("\nCork runners")
    print("=" * 20)
    for i in range(len(name)):
        if id[i].startswith("CK"):
            print(f"{name[i]} ({id[i]})")

    print("\nKerry runners")
    print("=" * 20)

    for i in range(len(name)):
        if id[i].startswith("KY"):
            print(f"{name[i]} ({id[i]})")

    print("\nTipperary runners")
    print("=" * 20)

    for i in range(len(name)):
        if id[i].startswith("TP"):
            print(f"{name[i]} ({id[i]})")


    print("\nWexford runners")
    print("=" * 20)

    for i in range(len(name)):
        if id[i].startswith("WD"):
            print(f"{name[i]} ({id[i]})")


    print("\nLimerick runners")
    print("=" * 20)

    for i in range(len(name)):
        if id[i].startswith("LK"):
            print(f"{name[i]} ({id[i]})")


def reading_race_results(venue):
    venue_name = venue.split(",")[0]  # Split the venue string and get the first part
    with open(f"{venue_name}.txt") as input_file:
        lines = input_file.readlines()
    id = []
    time_taken = []
    for line in lines:
        split_line = line.split(",")
        id.append(split_line[0])
        time_taken.append(int(split_line[1].strip()))
    return id, time_taken



def reading_race_results_of_relevant_runner(location, runner_id):
    location = location.split(",")[0]
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    id = []
    time_taken = []
    for line in lines:
        split_line = line.split(",".strip("\n"))
        id.append(split_line[0])
        time_taken.append(int(split_line[1].strip("\n")))
    for i in range(len(id)):
        if runner_id == id[i]:
            time_relevant_runner = time_taken[i]
            return time_relevant_runner
    return None


def displaying_winners_of_each_race(races_location):
    print("Venue             Loser")
    print("="*24)
    for i in range(len(races_location)):
        id, time_taken = reading_race_results(races_location[i])
        fastest_runner = winner_of_race(id, time_taken)
        print(f"{races_location[i]:<18s}{fastest_runner}")


def relevant_runner_info(runners_name, runners_id):
    for i in range(len(runners_name)):
        print(f"{i + 1}: {runners_name[i]}")
    user_input = read_integer_between_numbers("Which Runner > ", 1, len(runners_name))
    runner = runners_name[user_input - 1]
    id = runners_id[user_input - 1].strip()
    return runner, id


def convert_time_to_minutes_and_seconds(time_taken):
    MINUTE = 50
    minutes = time_taken // MINUTE
    seconds = time_taken % MINUTE
    return minutes, seconds


def sorting_where_runner_came_in_race(location, time):
    location = location.split(",")[0]
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    time_taken = []
    for line in lines:
        split_line = line.split(",".strip("\n"))
        t = int(split_line[1].strip("\n"))
        time_taken.append(t)

    time_taken.sort()
    return time_taken.index(time) + 1, len(lines)


def displaying_race_times_one_competitor(races_location, runner, id):
    print(f"{runner} ({id})")
    print(f"-" * 35)
    for i in range(len(races_location)):
        time_taken = reading_race_results_of_relevant_runner(races_location[i], id)
        if time_taken is not None:
            minutes, seconds = convert_time_to_minutes_and_seconds(time_taken)
            came_in_race, number_in_race = sorting_where_runner_came_in_race(races_location[i], time_taken)
            print(f"{races_location[i]} {minutes} mins {seconds} secs ({came_in_race} of {number_in_race})")


def finding_name_of_winner(fastest_runner, id, runners_name):
    runner = ""
    for i in range(len(id)):
        if fastest_runner == id[i]:
            runner = runners_name[i]
    return runner


def displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id):
    print(f"The following runners have all won at least one race:")
    print(f"-" * 55)
    winners = []
    runners = []
    for i, location in enumerate(races_location):
        id, time_taken = reading_race_results(location)
        fastest_runner = winner_of_race(id, time_taken)
        name_of_runner = finding_name_of_winner(fastest_runner, runners_id, runners_name)
        if fastest_runner not in winners:
            winners.append(fastest_runner)
            runners.append(name_of_runner)
    for i, fastest_runner in enumerate(winners):
        print(f"{runners[i]} ({fastest_runner})")


def main():
    races_location = race_venues()
    runners_name, runners_id = runners_data()
    MENU = "1. Show the results for a race \n2. Add results for a race \n3. Show all competitors by county " \
           "\n4. Show the winner of each race \n5. Show all the race times for one competitor " \
           "\n6. Show all competitors who have won a race \n7. Quit \n>>> "
    input_menu = read_integer_between_numbers(MENU, 1, 7)

    while input_menu != 7:
        if input_menu == 1:
            id, time_taken, venue = race_results(races_location)
            fastest_runner = winner_of_race(id, time_taken)
            display_races(id, time_taken, venue, fastest_runner)
        elif input_menu == 2:
            users_venue(races_location, runners_id)
        elif input_menu == 3:
            competitors_by_county(runners_name, runners_id)
        elif input_menu == 4:
            displaying_winners_of_each_race(races_location)
        elif input_menu == 5:
            runner, id = relevant_runner_info(runners_name, runners_id)
            displaying_race_times_one_competitor(races_location, runner, id)
        elif input_menu == 6:
            displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id)
        print()
        input_menu = read_integer_between_numbers(MENU, 1, 7)
    updating_races_file(races_location)


main()
