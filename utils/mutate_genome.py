import argparse
import screed
import numpy as np

alphabet = ['A', 'C', 'G', 'T']
mutate_dic = {'A':['C', 'G', 'T'], 'C':['G', 'T', 'A'], 'G':['T', 'A', 'C'], 'T':['A', 'C', 'G']}

def create_parser():
    parser = argparse.ArgumentParser(description="This script will mutate a genome using the simple mutation model",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("in_genome", type=str, help="The full path to the FASTA/other genome file")
    parser.add_argument("out_genome", type=str, help="The full path to the output file")
    parser.add_argument("mut_rate", type=float, help="Mutation rate")
    parser.add_argument("--seed", type=int, help="Random seed", default=0)
    args = parser.parse_args()
    return args.in_genome, args.out_genome, args.mut_rate, args.seed

def mutate_string(in_str, mut_rate):
    in_str_split = list(in_str.upper())
    mutate_decisions = np.random.binomial(1, mut_rate, len(in_str))
    for i in range(len(mutate_decisions)):
        if mutate_decisions[i] == 1:
            if in_str_split[i] in alphabet:
                in_str_split[i] = np.random.choice(mutate_dic[ in_str_split[i] ])
    return ''.join(in_str_split)

def mutate_using_SMM(in_genome_fname, out_genome_fname, mut_rate, seed):
    np.random.seed(seed)

    out_file = open(out_genome_fname, 'w')
    with screed.open(in_genome_fname) as f:
        for record in f:
            mut_seq = mutate_string(record.sequence, mut_rate)
            out_file.write('> ' + record.name + '\n')
            out_file.write(mut_seq + '\n')
    out_file.close()

def main():
    in_genome_fname, out_genome_fname, mut_rate, seed = create_parser()
    mutate_using_SMM(in_genome_fname, out_genome_fname, mut_rate, seed)

if __name__ == "__main__":
    main()
