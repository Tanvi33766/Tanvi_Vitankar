def climbing_leaderboard(leaderboard, player_scores):
  

  player_ranks = []
  for score in player_scores:
    rank = len(leaderboard) + 1 
    for i, leaderboard_score in enumerate(leaderboard):
      if score > leaderboard_score:
        rank = i + 1
        break 

    player_ranks.append(rank)

  return player_ranks


leaderboard = [100, 90, 90, 80]
player_scores = [70, 80, 105]

player_ranks = climbing_leaderboard(leaderboard, player_scores)

print(player_ranks)  
