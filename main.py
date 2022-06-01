import subprocess
import numpy as np
import argparse
from utils.mutate_genome import mutate_using_SMM
from utils.ani_by_sourmash import compute_ani_by_sourmash

def parse_args():
    parser = argparse.ArgumentParser(description="This script will mutate a given genome, and determine the ANI using sourmash",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("genome", type=str, help="The full path to the genome")
    parser.add_argument("--ksize", type=int, help="k size", default=21)
    parser.add_argument("--pstart", type=float, help="Starting value of mutation rate", default=0.0)
    parser.add_argument("--pend", type=float, help="Ending value of mutation rate", default=1.0)
    parser.add_argument("--stepsize", type=float, help="Step size of the mutation rate", default=0.01)
    parser.add_argument("--seed", type=int, help="Random seed", default=0)
    parser.add_argument("--scalef", type=int, help="Scale factor, in [0,1]", default=0.001)
    args = parser.parse_args()
    return args.genome, args.ksize, args.pstart, args.pend, args.stepsize, args.seed, args.scalef

if __name__ == "__main__":
    genome_fname, ksize, pstart, pend, stepsize, seed, scalef = parse_args()
    scaled = int(1.0/scalef)
    mutated_genome_fname = 'mutated/' + genome_fname.split('/')[-1]
    print(mutated_genome_fname)
    for mut_rate in np.arange(pstart, pend+0.001, stepsize):
        # run SMM
        mutate_using_SMM(genome_fname, mutated_genome_fname, mut_rate, seed)
        # compute the ani
        ani_estimates_sourmash = compute_ani_by_sourmash(genome_fname, mutated_genome_fname, seed, ksize, scaled)
        # print this ani