"""
1000 add served, each served clicked wiyh p = 0.01, otherwise ignored. What is 
the probability of of 10 clicks?
"""

from scipy.stats import binom


def main():
    k = 10
    n = 1000
    p = 0.01

    res = binom.pmf(k, n, p)
    print(f"probability of %d clicks is %.2f" % (k, res * 100))


if __name__ == "__main__":
    main()
