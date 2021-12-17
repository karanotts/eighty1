"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, math, simulation"""


import datetime
import random

INTRO = """Birthday Paradox, by Al Sweigart al@inventwithpython.com
The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.
(It's not actually a paradox, it's just a surprising result.)
"""

MONTHS = (
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
)


def get_birthdays(number_of_birthdays):
    """Returns a list of randomly generated objects for birthdays."""
    birthdays = []

    for _ in range(number_of_birthdays):
        start_of_year = datetime.date(2000, 1, 1)

        random_number_of_days = datetime.timedelta(
            random.randint(0, 365)  # 2000 was a leap year!
        )
        birthday = start_of_year + random_number_of_days

        birthdays.append(birthday)

    return birthdays


def get_match(birthdays):
    """Returns the date object of a birthday that occurs more than once in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None

    matches = []
    for a, birthday_a in enumerate(birthdays):
        for _, birthday_b in enumerate(birthdays[a + 1 :]):
            if birthday_a == birthday_b:
                matches.append(birthday_a)

    return matches


print(INTRO)


def main():
    """Birthdays paradox."""
    while True:
        print("How many birthdays shall I generate? (Max 100)")
        response = input("> ")
        if response.isdecimal() and (0 < int(response) <= 100):
            response_birthdays = int(response)

        print(f"\nHere are {response_birthdays} birthdays:")
        birthdays = get_birthdays(response_birthdays)
        for _, birthday in enumerate(birthdays):
            month_name = MONTHS[birthday.month - 1]
            date_text = f"{month_name} {birthday.day}"
            print(date_text, end="; ")

        matches = get_match(birthdays)

        if matches is not None:
            print("\n\nIn this simulation multiple people have birthdays on:")
            for match in matches:
                month_name = MONTHS[match.month - 1]
                date_text = f"{month_name} {match.day}"
                print(f"* {date_text}")
        else:
            print("\n\nNo matches found.")

        break


if __name__ == "__main__":
    main()
