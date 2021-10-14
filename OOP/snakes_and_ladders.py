class SnakesLadders():
    SNAKES_LADDERS = {
            2:38, 7:14, 8:31, 15:26, 28:84, 21:42, 36:44, 51:67, 78:98, 71:91, 87:94,
            16:6, 46:25, 49:11, 62:19, 64:60, 74:53, 89:68, 92:88, 95:75, 99:80
        }
    def __init__(self):
        self.player_positions = {
            "1":0,
            "2":0
        }
        self.who_play = "1"
        self.game_in_progress = True

    def play(self, die1, die2):
        isDouble = True if die1 == die2 else False                                    # check if player rolled a double
        if self.game_in_progress:                                                     # check if game is not over
            player_init_position = self.player_positions[self.who_play]               # get player init position
            player_position = player_init_position + die1 + die2                      # move to the rolls
            if player_position == 100:                                                # check if not 100
                result = f"Player {self.who_play} Wins!"
                self.game_in_progress = False
            else:
                if player_position >= 100:                                            # check if > 100 and do action if
                    player_position = 100 - abs(100 - player_position)
                if player_position in self.SNAKES_LADDERS:                            # check if snake or ladder
                    player_position = self.SNAKES_LADDERS[player_position]
                self.player_positions[self.who_play]=player_position                  # update player position
                result = f"Player {self.who_play} is on square {player_position}"
                if isDouble:                                                          # get who goes next
                    self.who_play = "1" if self.who_play == "1" else "2"
                else:
                    self.who_play = "1" if self.who_play == "2" else "2"
        else:
            result = "Game over!"
        return result

game = SnakesLadders()
print(game.play(1, 1))
print(game.play(1, 5))
print(game.play(6, 2))
print(game.play(1, 1))