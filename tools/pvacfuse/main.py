import argparse
import sys
import os
import pkg_resources
from tools.pvacfuse import *

def define_parser():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    subparsers = parser.add_subparsers()

    #add subcommands
    run_main_program_parser = subparsers.add_parser(
        "run",
        help="Run the pVACfuse pipeline",
        add_help=False
    )
    run_main_program_parser.set_defaults(func=run)

    binding_filter_parser = subparsers.add_parser(
        "binding_filter",
        help="Filter variants processed by IEDB by binding score",
        add_help=False
    )
    binding_filter_parser.set_defaults(func=binding_filter)

    top_score_filter_parser = subparsers.add_parser(
        "top_score_filter",
        help="Pick the best neoepitope for each variant",
        add_help=False,
    )
    top_score_filter_parser.set_defaults(func=top_score_filter)

    generate_protein_fasta_parser = subparsers.add_parser(
        "generate_protein_fasta",
        help="Generate an annotated fasta file from Integrate-Neo or AGFusion output",
        add_help=False,
    )
    generate_protein_fasta_parser.set_defaults(func=generate_protein_fasta)

    generate_aggregated_report_parser = subparsers.add_parser(
        "generate_aggregated_report",
        help="Generate an aggregated report from a pVACfuse .all_epitopes.tsv report file.",
        add_help=False
    )
    generate_aggregated_report_parser.set_defaults(func=generate_aggregated_report)

    valid_alleles_parser = subparsers.add_parser(
        "valid_alleles",
        help="Show a list of valid allele names",
        add_help=False
    )
    valid_alleles_parser.set_defaults(func=valid_alleles)

    allele_specific_cutoffs_parser = subparsers.add_parser(
        "allele_specific_cutoffs",
        help="Show the allele specific cutoffs",
        add_help=False,
    )
    allele_specific_cutoffs_parser.set_defaults(func=allele_specific_cutoffs)

    download_example_data_parser = subparsers.add_parser(
        "download_example_data",
        help="Download example input and output files",
        add_help=False
    )
    download_example_data_parser.set_defaults(func=download_example_data)
    return parser

def main():
    parser = define_parser()
    args = parser.parse_known_args()
    try:
        args[0].func.main(args[1])
    except AttributeError as e:
        parser.print_help()
        print("Error: No command specified")
        sys.exit(-1)

if __name__ == '__main__':
    main()
