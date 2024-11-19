from tkinter import filedialog

from footballer import Footballer
from teams import Teams

players_pool = [
Footballer(name="Philipp", start_rank=3),
Footballer(name="Mormar", start_rank=3),
Footballer(name="Sboben", start_rank=4),
Footballer(name="Mic", start_rank=2),
Footballer(name="Karim", start_rank=3),
Footballer(name="Duccio", start_rank=1),
]


if __name__ == "__main__":

    # Read pool of players from csv
    path = filedialog.askopenfilename(initialdir="~/Desktop/cancella", filetypes=[("footballers", ".csv")])
    f = open(path, 'r')
    f = f.read()

    for pl in players_pool:
        print(f"{pl.name}, {pl.start_rank}, {pl.wins}, {pl.losses}, {pl.draws}, {pl.points}")

    # sort the pool of players (list) by alphabetic order 
    players_pool.sort(key=lambda player: player.name.lower())

    #TODO: read available_players_names from csv
    available_players=[]
    available_players_names = ["Philipp", "Mormar", "Akil"]
    for available_player in available_players_names:
        if available_player in [player.name for player in players_pool]:
            print(f"{available_player} already in pool")
        else:
            print(f"{available_player} NEW PLAYER!")
            players_pool.append(Footballer(available_player, 5))
        
        #TODO: questa condizione non va, trovo sempre duccio
        available_players.append(players_pool[available_players_names in players_pool])
    
    for av in available_players:
        print(f"Availables-> {av.name}\n")

    Teams.create_teams(available_players_names)
    # print("\navailable players:\n\n")


