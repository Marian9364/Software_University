result_match_1 = input()
result_match_2 = input()
result_match_3 = input()

team_win = 0
team_lose = 0
team_draw = 0
if result_match_1[0] > result_match_1[2]:
    team_win += 1
elif result_match_2[0] == result_match_2[2]:
    team_draw += 1
else:
    team_lose += 1
if result_match_2[0] > result_match_2[2]:
    team_win += 1
elif result_match_2[0] == result_match_2[2]:
    team_draw += 1
else:
    team_lose += 1
if result_match_3[0] > result_match_3[2]:
    team_win += 1
elif result_match_3[0] == result_match_3[2]:
    team_draw += 1
else:
    team_lose += 1


print(f"Team won {team_win} games.")
print(f"Team lost {team_lose} games.")
print(f"Drawn games: {team_draw}")


