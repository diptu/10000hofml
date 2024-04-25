"""
Warriors are going to play the Bucks in a best of 7 series during the 2022 NBA 
finals.What is the probability that the warriors win the series? Each game is
independent. Each game, the warriors have a 0.55 probability of winning.win
series if you win atleast 4 games.
"""

from scipy.stats import binom


def main():
    k = 4  # P(X>=4) = P(X=4) +  P(X=5) + P(X=6) + P(X=7)
    n = 7
    p = 0.55

    res = 0
    for i in range(k, 8):
        res += binom.pmf(i, n, p)
    # res = (
    #     binom.pmf(k, n, p)  # P(X=4)
    #     + binom.pmf(k + 1, n, p)  # P(X=5)
    #     + binom.pmf(k + 2, n, p)  # P(X=6)
    #     + binom.pmf(k + 3, n, p)  # P(X=7)
    # )
    print(f"probability of  atleast %d win is %.2f" % (k, res * 100))


if __name__ == "__main__":
    main()
