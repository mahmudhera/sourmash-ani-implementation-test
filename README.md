# sourmash-ani-implementation-test

Tests if sourmash implementation matches our implementation.

## Short description
We take a mutation rate, then mutate the given genome by simulating simple mutation model.
Then, we use sourmash to compute the ANI using containment, and we also compute the ANI
using the containment index manually. Then, these two values are matched for discrepancies.

## Directory organization
1. utils: all helper codes

## Steps implemented in `main.py`:
1. Take a fixed mutation rate, then simulate mutation using SMM (simple mutation model)
1. Take the mutated genome and the original genome, then determine the ANI estimate using sourmash compare
1. Take the mutated genome and the original genome, then determine the ANI estimate using our implementation independently
1. Check if there is any discrepancy between the previous two estimates
1. Repeat for multiple mutation rates

## How to run
`python main.py -h`

## Results
The results are in the file `ani_comparison_results`.
There is a faithful agreement between the two methods for ANI >= 66%.
For ANI <= 65%, we notice some discrepancies.
