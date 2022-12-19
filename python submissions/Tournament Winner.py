def tournamentWinner(competitions, results):
    best_score = 0
    winner = ""
    score = {}
    for i in range(len(competitions)):  # N times
        homeT = competitions[i][0]
        awayT = competitions[i][1]
        if results[i] == 1:
            if homeT not in score:
                score[homeT] = 0
            score[homeT] += 1
            if score[homeT] > best_score:
                best_score = score[homeT]
                winner = homeT
        else:
            if awayT not in score:
                score[awayT] = 0
            score[awayT] += 1
            if score[awayT] > best_score:
                best_score = score[awayT]
                winner = awayT
    return winner

# O(N) complexity
