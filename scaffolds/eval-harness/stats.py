import math
import random
from typing import Sequence


def wilson(successes: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (0.0, 0.0)
    p = successes / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (max(0.0, centre - half), min(1.0, centre + half))


def bootstrap_mean_ci(values: Sequence[float], iters: int = 2000, seed: int = 7) -> tuple[float, float]:
    if not values:
        return (0.0, 0.0)
    rng = random.Random(seed)
    n = len(values)
    means = sorted(sum(rng.choice(values) for _ in range(n)) / n for _ in range(iters))
    return (means[int(0.025 * iters)], means[int(0.975 * iters)])


def paired_delta_ci(a: Sequence[float], b: Sequence[float], iters: int = 2000, seed: int = 7) -> tuple[float, tuple[float, float]]:
    """Delta = mean(b - a) on the same items. Returns (delta, ci95)."""
    assert len(a) == len(b), "paired comparison needs the same items in the same order"
    diffs = [y - x for x, y in zip(a, b)]
    return (sum(diffs) / len(diffs), bootstrap_mean_ci(diffs, iters, seed))
