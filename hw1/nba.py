import random
import numpy as np

# The number of times the experiment is repeated
N = 10**7
Na = 0
Nba = 0

# Let event A be the event that MIA is up 3-0 after 3 games agaubst BOS
# Let event B be the event that MIA wins the series 4-3 against BOS
# Then, A and B is the event that MIA is up 3-0 in the first 3 games and wins the series 4-3 against BOS
# It is given that games 1,2 and 3, were played in BOS, BOS, MIA, respectively
# and games 4,5,6 and 7 is played in MIA, BOS, MIA, BOS, respectively
# And we assume the outcome of each game is independent. (We can simulate bernoulli trial for each game)
# Home team has a 0.75 chance of winning and away team has a 0.25 chance of winning
# And we are verifying P(A)~=Na/N and P(B|A)~=Nba/Na

for i in range(N):
    # Initialize the number of wins for MIA and BOS
    mia = 0
    bos = 0
    # Initialize the number of games played
    games = 0
    over = False
    # Play the first 3 games
    for j in range(3):
        # If the game is played in BOS, BOS can win with a probability of 0.75 and MIA can win with a probability of 0.25
        if j in [0, 1]:
            r = np.random.binomial(1, 0.75)
            if r > 0:
                bos += 1
            else:
                mia += 1
        # If the game is played in MIA, MIA can win with a probability of 0.75 and BOS can win with a probability of 0.25
        else:
            r = np.random.binomial(1, 0.75)
            if r > 0:
                mia += 1
            else:
                bos += 1
        # Increment the number of games played
        games += 1
    if mia == 3:
        # Increment the number of times MIA is up 3-0
        Na += 1
        # Play the remaining 4 games
        for j in range(4):
            if not over:
                # Generate a random number between 0 and 1
                # If the game is played in MIA, MIA can win with a probability of 0.75 and BOS can win with a probability of 0.25
                if j in [0, 2]:
                    r = np.random.binomial(1, 0.75)
                    if r > 0:
                        mia += 1
                    else:
                        bos += 1
                # If the game is played in BOS, BOS can win with a probability of 0.75 and MIA can win with a probability of 0.25
                elif j in [1, 3]:
                    r = np.random.binomial(1, 0.75)
                    if r > 0:
                        bos += 1
                    else:
                        mia += 1

                # If MIA or BOS wins 4 games, the series is over
                if mia == 4 or bos == 4:
                    over = True

                # Increment the number of games played
                games += 1

        if mia == 4 and bos == 3:
            # Increment the number of times MIA is up 3-0 and wins the series 4-3
            Nba += 1

if Na == 0 or Nba == 0:
    print("Na or Nba is 0, so P(A) or P(B|A) is undefined.")
else:
    print("For N = ", N, ", the simulated value for part (e) is:")
    print("\t P(A) ~= ", Na / N, " and P(B|A) ~= ", Nba / Na, sep="")
