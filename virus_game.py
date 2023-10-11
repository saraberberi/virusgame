import random
import pygame

class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.infected = False
        self.eliminated = False

    def get_role(self):
        return self.role

    def is_infected(self):
        return self.infected

    def is_eliminated(self):
        return self.eliminated

class Game:
    def __init__(self, num_players):
        self.players = []
        for i in range(num_players):
            role = random.choice(["Terrorist", "Researcher", "Police Officer", "Fanatic", "Reporter", "Civilian"])
            self.players.append(Player(i, role))

        # Create a list to store the AI-generated players
        self.ai_players = []
        for i in range(num_players - len(self.players)):
            self.ai_players.append(Player(i + len(self.players), "AI"))

        # Initialize the graphical interface
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.SysFont("Arial", 20)

    def start(self):
        # Assign roles to players
        for player in self.players:
            player.role = random.choice(["Terrorist", "Researcher", "Police Officer", "Fanatic", "Reporter", "Civilian"])

        # Start the game loop
        while True:
            # Get the current player
            current_player = self.players[0]

            # Take the current player's turn
            self.current_player_turn(current_player)

            # Check if the game is over
            if self.game_over():
                break

            # Go to the next player
            self.players.rotate(1)

    def current_player_turn(self, current_player):
        # Display the game state to the current player
        self.display_game_state(current_player)

        # Get the current player's choice
        choice = self.get_current_player_choice(current_player)

        # Take the current player's action
        self.take_current_player_action(current_player, choice)

    def display_game_state(self, current_player):
        # Display the list of players
        for player in self.players:
            self.display_player(player)

        # Display the current player's role and infected status
        self.display_current_player_info(current_player)

    def get_current_player_choice(self, current_player):
        # Display the current player's options
        options = ["Accuse another player of being a Terrorist", "Try to heal another player who is infected with the virus", "Investigate another player to try to learn their role", "Vote to eliminate a player"]
        for i in range(len(options)):
            self.display_text(f"{i + 1}. {options[i]}", 10, 100 + i * 20)

        # Get the current player's choice
        choice = int(input("Enter your choice: "))

        # Validate the current player's choice
        while choice < 1 or choice > len(options):
            choice = int(input("Invalid choice. Enter your choice again: "))

        return choice

    def take_current_player_action(self, current_player, choice):
        # Take the current player's action based on their choice
        if choice == 1:
            # Accuse another player of being a Terrorist
            accused_player = self.get_player_by_name(input("Enter the player you want to accuse: "))
            if accused_player.role == "Terrorist":
                accused_player.eliminated = True
            else:
                current_player.eliminated = True
        elif choice == 2:
            # Try to heal another player who is infected with the virus
            healed_player = self.get_player_by_name(input("Enter the player you want to heal: "))
            if healed_player.infected:
                healed_player.infected = False
        elif choice == 3:
            # Investigate
