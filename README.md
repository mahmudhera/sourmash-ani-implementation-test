# sourmash-ani-implementation-test

Tests if sourmash implementation matches our implementation.

Steps:
1. Take a fixed mutation rate, then simulate mutation using SMM (simple mutation model)
1. Take the mutated genome and the original genome, then determine the ANI estimate using sourmash compare
1. Take the mutated genome and the original genome, then determine the ANI estimate using our implementation independently
1. Check if there is any discrepancy between the previous two estimates
1. Repeat for multiple mutation rates

## How to run
