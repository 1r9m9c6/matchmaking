from footballer import footballer

players = [
footballer(name="Philipp", start_rank=3),
footballer(name="Mormar", start_rank=3),
footballer(name="Sboben", start_rank=4),
footballer(name="Mic", start_rank=2),
footballer(name="Karim", start_rank=3),
footballer(name="Duccio", start_rank=1),
footballer(name="Akil", start_rank=3),
]

if __name__ == "__main__":
    for player in players:
        print(f"name: {player.name}\n\toverall_rank {player.overall_rank}\n\tvictory rate {player.victory_rate}")
    # players.name.sort()
    print(players.name)
