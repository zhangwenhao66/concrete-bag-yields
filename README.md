# Concrete bag yields, with sources

How much mixed concrete one bag of premix actually makes, taken from the manufacturers' own data sheets, plus a tiny script that turns slab dimensions into cubic yards and bag counts.

Most "how many bags" answers online quote a bags-per-yard number without saying where it came from. The manufacturers publish the yield per bag instead, so this repo keeps that number and the link to the sheet it came from.

## Yield per bag

| Brand | Product | Bag | Yield (ft³) | Source |
| --- | --- | --- | --- | --- |
| QUIKRETE | Concrete Mix No. 1101 | 40 lb | 0.30 | [data sheet, rev. Oct 2022](https://www.quikrete.com/pdfs/data_sheet-concrete%20mix%201101.pdf) |
| QUIKRETE | Concrete Mix No. 1101 | 50 lb | 0.375 | same |
| QUIKRETE | Concrete Mix No. 1101 | 60 lb | 0.45 | same |
| QUIKRETE | Concrete Mix No. 1101 | 80 lb | 0.60 | same |
| QUIKRETE | Concrete Mix No. 1101 (regional) | 90 lb | 0.675 | same |
| QUIKRETE | Fast-Setting Concrete Mix No. 1004 | 50 lb | 0.375 | [data sheet, rev. Nov 2025](https://www.quikrete.com/pdfs/data_sheet-fast%20setting%20concrete%20mix%201004-50.pdf) |
| Sakrete | High-Strength Concrete Mix | 40 lb | 0.30 | [TDS](https://www.sakrete.com/wp-content/uploads/2024/01/Sakrete-High-Strength-Concrete-Mix-TDS.pdf) |
| Sakrete | High-Strength Concrete Mix | 60 lb | 0.45 | same |
| Sakrete | High-Strength Concrete Mix | 80 lb | 0.60 | same |
| Sakrete | High-Strength Concrete Mix | 90 lb | 0.66 | same |

Machine-readable copy: [`yields.json`](yields.json). Sheets retrieved 2026-11-20; check the manufacturer's site for the current revision.

## The math

```
cubic feet = length_ft × width_ft × (thickness_in ÷ 12)
cubic yards = cubic feet ÷ 27
bags = ceil(cubic feet ÷ yield per bag)
```

A 10 × 10 ft slab, 4 in thick, is 33.33 ft³ (1.23 yd³): 56 bags of 80 lb, or 112 bags of 40 lb, before any allowance for waste or an uneven base.

```
$ python3 concrete.py 10 10 4 10
10 ft x 10 ft x 4 in, +10% waste: 36.67 ft3 = 1.36 yd3
  40 lb bags at 0.3 ft3 each: 123
  50 lb bags at 0.375 ft3 each: 98
  60 lb bags at 0.45 ft3 each: 82
  80 lb bags at 0.6 ft3 each: 62
  ...
```

## Limits

- Yields are the manufacturers' "approximately" figures for properly mixed concrete. Real jobs lose material to spillage, form bulge and low spots in the base, so add an allowance.
- This is a quantity estimate, not a structural design. Thickness, reinforcement and base requirements come from your plans and local code.

For other shapes (footings, columns, steps) and a bag-versus-ready-mix cost comparison, the browser calculator at https://diyconcretecalc.com/ uses the same yields.

License: MIT for the code and README. Yield figures belong to their publishers and are quoted with links.
