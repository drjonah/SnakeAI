from game import Game

class agent:
    pass

def train():
    game = Game()

    while True:
        game.update()

        game_over, score = game.play()
        if game_over:
            game.game_over()
            game.reset()

if __name__ == '__main__':
    train()