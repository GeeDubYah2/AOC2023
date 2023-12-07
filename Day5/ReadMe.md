# Performance issue with Day5_2:

Instead of creating a list of all possible seed values.
Keep the seeds as a list of ranges.
Perform mappings by splitting ranges based on next level mappings. Convert start and end values based on mapOp. Merge overlapping & contiguous ranges. Repeat with next map.

```
seed-to-foo map:    0..50(0); 50..250(+50); 251..500(-150)

seeds:              0..100;           101..200;  201..300
split ranges:       0..50;  51..100;  101..200;  201..250;  251..300   # split seed ranges to match mappings
apply mapOp:        0..50; 101..150;  151..251;  251..300;  101..150   # apply the mapOp based on the corresponding mapping
sort:               0..50; 101..150;  101..150;  151..251;  251..300   # sort based on start values.
merge:              0..50; 101..300                                    # merge contiguous and overlapping ranges.
```

repeat with remaining mappings

once we have location ranges. sort and find start of first range.

functions:
  - read seed ranges
  - split and apply mapOp on ranges.
  - sort and merge ranges
