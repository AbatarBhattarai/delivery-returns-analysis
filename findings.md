# Findings — Delivery & Returns Analysis (synthetic practice data)

Dataset: 900 orders after cleaning 908 raw rows (removed 8 duplicates, filled 18 missing regions).

## Headline
- Return rate: 11.6%
- Returned orders: 104 of 900
- Average delivery time, returned orders: 4.1 days vs kept orders: 3.6 days
- Orders taking 6+ days: 15.7%

## Return rate by category
category
Clothing       16.746411
Electronics    10.970464
Sports          9.523810
Home            9.417040

## Return rate by shipping
shipping
Express      7.741935
Standard    13.559322

## Return rate by region
region
Unknown    22.222222
South      14.553991
West       11.790393
East       10.280374
North       8.849558

## Takeaways
1. Clothing has the highest return rate (16.7%) — check sizing / product descriptions first.
2. Slow delivery is linked to returns — returned orders took 4.1 days on average vs 3.6 for kept orders.
3. Express shipping has a lower return rate — test free express over a value threshold.
