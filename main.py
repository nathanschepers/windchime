import random
from time import perf_counter, sleep


class SystemEnergy:
    def __init__(self, wind_forces=None, wind_probabilities=None, decay=0.5):
        if wind_forces is None:
            wind_forces = [*range(0, 5)]
        if wind_probabilities is None:
            wind_probabilities = [0.15, 0.15, 0.40, 0.15, 0.15]

        self.wind_forces = wind_forces
        self.wind_probabilities = wind_probabilities
        self.decay = decay
        self.previous_energy = 0

    def get_energy(self):
        gust = random.choices(self.wind_forces, self.wind_probabilities)[0]
        current_energy = self.decay * (self.previous_energy + gust)
        self.previous_energy = current_energy
        return current_energy


def play_chimes(system_energy: SystemEnergy):
    """
    Plays the chimes a single time.
    """
    print(f'{system_energy.get_energy()}')


def chime_loop(system_energy: SystemEnergy, bpm=60, count=20, verbose=False):
    """
    The overall model/metronome loop. Manages tick drift and calls play_chime().
    https://stackoverflow.com/questions/51389691/how-can-i-do-a-precise-metronome
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
        play_chimes(system_energy=system_energy)


if __name__ == '__main__':
    energy = SystemEnergy()
    chime_loop(system_energy=energy, bpm=100, count=100, verbose=False)
