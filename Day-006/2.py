"""
7 runs of program, each run crashes wuth a probability of 0.3.what is the
cchaance of exactly 3 crashes.
"""

from scipy.stats import binom


def main():
    k = 3
    n = 7
    p = 0.3

    res = binom.pmf(k, n, p)
    print(f"probability of exactly %d crashes is %.2f" % (k, res * 100))


if __name__ == "__main__":
    main()
