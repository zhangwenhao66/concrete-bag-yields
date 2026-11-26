#!/usr/bin/env python3
"""Concrete volume and bag count for a rectangular slab.

Usage: python3 concrete.py LENGTH_FT WIDTH_FT THICKNESS_IN [WASTE_PCT]
Example: python3 concrete.py 10 10 4 10
"""
import json, math, sys
from pathlib import Path

def slab_cubic_feet(length_ft: float, width_ft: float, thickness_in: float) -> float:
    return length_ft * width_ft * (thickness_in / 12)

def bags_needed(cubic_feet: float, yield_ft3: float) -> int:
    # Round up: you cannot buy part of a bag.
    return math.ceil(round(cubic_feet / yield_ft3, 6))

def main():
    if len(sys.argv) not in (4, 5):
        raise SystemExit(__doc__)
    l, w, t = map(float, sys.argv[1:4])
    waste = float(sys.argv[4]) if len(sys.argv) == 5 else 0.0
    ft3 = slab_cubic_feet(l, w, t) * (1 + waste / 100)
    print(f"{l:g} ft x {w:g} ft x {t:g} in, +{waste:g}% waste: {ft3:.2f} ft3 = {ft3/27:.2f} yd3")
    seen = set()
    for p in json.load(open(Path(__file__).parent / "yields.json"))["products"]:
        key = (p["bag_lb"], p["yield_ft3"])
        if key in seen:
            continue
        seen.add(key)
        print(f"  {p['bag_lb']} lb bags at {p['yield_ft3']} ft3 each: {bags_needed(ft3, p['yield_ft3'])}")

if __name__ == "__main__":
    main()
