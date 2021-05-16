from gametime import game_play,play_again, choice

## Simple python gameplay against an AI opponent, user needs to select r,p,s for
## rock paper or scissors

if __name__ == '__main__':
    while True:
        choice()
        game_play()
        play_again()
