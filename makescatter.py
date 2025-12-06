import matplotlib.pyplot as plt
import math

def s10(m: int) -> int:
    """Return the sum of decimal digits of m."""
    return sum(int(d) for d in str(m))

# Range of n
ns = list(range(0, 101))

# Compute s10(2^n)
vals = [s10(2**n) for n in ns]

# Conjectured linear approximation L(n) = 4.5 * (log10(2) * n + 0.5)
L = [4.5 * (math.log10(2) * n) for n in ns]
# L0 = [4.5 * math.log10(2) * n for n in ns]


plt.figure(figsize=(8, 5))

# Scatter of s10(2^n)
plt.scatter(ns, vals, label=r"$s_{10}(2^n)$", s=20)

# Line plot of the conjectured approximation
plt.plot(ns, L, 'r', label=r"$4.5n\,\log_{10} 2$")
# plt.plot(ns, L0, label=r"$4.5n \,\log_{10} 2$")

plt.xlabel("n")
# plt.ylabel(r"$s_{10}(2^n)$")
# plt.title(r"Scatterplot of $s_{10}(2^n)$ with Conjectured Approximation")
plt.legend()
plt.tight_layout()
plt.savefig('s10_scatter.png')
plt.show()
