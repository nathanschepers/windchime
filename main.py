import random
from collections import Counter

wind_forces = [*range(0, 5)]
wind_probabilities = [0.15, 0.15, 0.40, 0.15, 0.15]


def output_stuff():
    print(f'forces - {wind_forces}, probabilities - {wind_probabilities}')
    gusts = []
    for _ in range(1000):
        gusts.extend(random.choices(wind_forces, wind_probabilities))

    print(f'all gusts - {gusts}')
    print(f'all gusts (counted) - {Counter(gusts)}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    output_stuff()
