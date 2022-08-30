import random
import matplotlib.pyplot as plt


class Noise:
    def __init__(self):
        self.noise = []

    def __generate(self, X, Y, noise):
        for i in range(Y):
            self.noise.append([random.randint(0, 1) for x in range(X)])
        plt.contourf(
            list(range(0, X)),
            list(range(0, Y)),
            noise,
            # order goes from 1st color which is assigned to the lowest value
            # to the latest color placed for the highest value integer/float
            colors=[
                'k',  # Black
                'k',  # Black
                'k',  # Black
                'gray',
                'darkgrey',
                'silver',
                'w'  # White
            ]
        )
        plt.show()

    def create_noise(self, height, width):
        self.__generate(width, height, self.noise)


if __name__ == '__main__':
    game = Noise()
    game.create_noise(100, 100)
