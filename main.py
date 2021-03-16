import random
from time import perf_counter, sleep

wind_forces = [*range(0, 5)]
wind_probabilities = [0.15, 0.15, 0.40, 0.15, 0.15]


def get_gust():
    """
    Returns a new random wind gust based on wind_probabilities distribution.

    NOTE: this should be swappable so that we can have a more accurate wind
          model
    """
    return random.choices(wind_forces, wind_probabilities)[0]


def play_chimes():
    """
    Plays the chimes a single time.
    """
    print(f'{get_gust()}')


def chime_loop(bpm=60, count=20, verbose=False):
    """
    The overall model/metronome loop. Manages tick drift and calls play_chime().
    """
    delay = d = 60 / bpm
    prev = perf_counter()
    for _ in range(count):
        sleep(d)
        t = perf_counter()
        delta = t - prev - delay
        d -= delta
        prev = t

        if verbose:
            print(f'tick drift - {delta:+.9f}')
        play_chimes()


if __name__ == '__main__':
    chime_loop(bpm=20, count=100, verbose=True)
