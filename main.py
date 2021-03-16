import random
from time import perf_counter, sleep

wind_forces = [*range(0, 5)]
wind_probabilities = [0.15, 0.15, 0.40, 0.15, 0.15]


def get_gust():
    """return a new random wind gust based on wind_probabilities distribution"""
    return random.choices(wind_forces, wind_probabilities)[0]


def play_chime():
    """play the chime"""
    print(f'{get_gust()}')


def chime_loop(bpm=60):
    """the overall model/metronome loop"""
    delay = d = 60 / bpm
    prev = perf_counter()
    for _ in range(200):
        sleep(d)
        t = perf_counter()
        delta = t - prev - delay
        print(f'tick drift - {delta:+.9f}')
        play_chime()
        d -= delta
        prev = t


if __name__ == '__main__':
    chime_loop(bpm=200)
