import subprocess
import numpy as np
import argparse
from utils.mutate_genome import mutate_using_SMM
from utils.ani_by_sourmash import compute_ani_by_sourmash
from utils.helper import read_sourmash_sketch, containment_to_mutation_rate

def parse_args():
    parser = argparse.ArgumentParser(description="This script will mutate a given genome, and determine the ANI using sourmash",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("genome", type=str, help="The full path to the genome")
    parser.add_argument("--ksize", type=int, help="k size", default=21)
    parser.add_argument("--pstart", type=float, help="Starting value of mutation rate", default=0.0)
    parser.add_argument("--pend", type=float, help="Ending value of mutation rate", default=1.0)
    parser.add_argument("--stepsize", type=float, help="Step size of the mutation rate", default=0.01)
    parser.add_argument("--seed", type=int, help="Random seed", default=0)
    parser.add_argument("--scalef", type=float, help="Scale factor, in [0,1]", default=0.001)
    args = parser.parse_args()
    return args.genome, args.ksize, args.pstart, args.pend, args.stepsize, args.seed, args.scalef

if __name__ == "__main__":
    genome_fname, ksize, pstart, pend, stepsize, seed, scalef = parse_args()
    scaled = int(1.0/scalef)
    mutated_genome_fname = 'mutated/' + genome_fname.split('/')[-1]
    print(mutated_genome_fname)
    for mut_rate in np.arange(pstart, pend+0.001, stepsize):
        mutate_using_SMM(genome_fname, mutated_genome_fname, mut_rate, seed)
        ani_estimates_sourmash = compute_ani_by_sourmash(genome_fname, mutated_genome_fname, seed, ksize, scaled)
        print(ani_estimates_sourmash)
        fmh_sketch1 = read_sourmash_sketch('sketch1', scalef)
        fmh_sketch2 = read_sourmash_sketch('sketch2', scalef)
        ani_1 = 1.0 - containment_to_mutation_rate( fmh_sketch1.get_containment(fmh_sketch2), ksize )
        ani_2 = 1.0 - containment_to_mutation_rate( fmh_sketch2.get_containment(fmh_sketch1), ksize )
        print(ani_1, ani_2)
