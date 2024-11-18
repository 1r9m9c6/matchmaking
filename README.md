"Ok guys let's play _fobal_, who does the teams?"

...

"I don't", "Me neither", "No he sucks", "...", "Last time you messed it up", "Never again"

Theese are just some of the complications you face when you plan a match with your friens, and no one want to make the teams.

This simple python makes the teams for you! It is best suited for weekly matches, since it adapts the matchmaking based on all previous match results. Therefore, the result will match-by-match improve!

---

The algorithm is very complicated:
- each player is characterized by its ```name``` and ```overall_rank```
- the ```overall_rank``` is a sum of player's ```start_rank``` (decided by you at the beginning of the championship) and the player's ```points```.
- the players gain one point when they win a match and lose one point when they lose one.
- teams are defined almost randomly: the only constraint is that the ```overall_team_rank``` (i.e., the sum of the players' ```overall_rank``` of a team) must be similar between both the teams.
    
