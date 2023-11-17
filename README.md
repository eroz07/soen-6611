# METRICSTICS

## Team H - Members

- Naman Kumar
- Yvonne Chooi Mei Lee
- Yang Liu
- Jothi Basu Lkv
- Nasrin Maarefi

## Introduction

METRICSTICS (a portmanteau of METRICS and STATISTICS), is a system for finding m, M, o, d, μ, MAD, and σ. The system takes a random number of data values as inputand output its descriptive statistics. The random data could be real, obtained from an authoritative source, or could be artificial, generated using a random data generator.

The purpose of the project is to create a set of interrelated artifacts for conducting certain measurements related to METRICSTICS.

In the rest of the document, ‘METRICSTICS’ stands for the name of both the project and the product, unless otherwise stated. The work on METRICSTICS has been divided into a collection of related problems. These problems have been annotated with notes, as necessary.

A system to analyse sales performance data has been developed by implementing METRICSTICS and it's required functions. This allows for the statistical analysis of sales data such that the users of the system are able to make informed decisions based on the insights gained.

### Use case diagram

![Alt text](D1/H-D1_LatexFiles/images/use_case_diagram.jpeg)

## Project directory structure

```
.
├── D1          # Delivery 1 deliverables
└── D2          # Delivery 2 deliverables
    ├── code    # Source code for the implementation of METRICSTICS
    ├── demo    # Steps taken from running the project to generating the output
    ├── docs    # Documents, reports, etc.
    ├── input   # Input test files
    └── output  # Output to tests ran

```

## Test files

### Input files

- Input files with the prefix `input{x}_{xxx},csv` were used to test the csv upload function (labelled as the `Upload data` button)
- Input files with the prefix `random{x}.csv` were values generated from the button labelled as `Generate data`. These values were copied into a csv file for tracing and verification purposes for the input and their corresponding outputs produced.

### Output files

- Output files are prefixed with the input file name and the functions they have performed so that they can be easily identified and verified.
- For example, the `Mininum` screenshot for `random1.csv` is named as `random1_min.png`, the `Standard Deviation` for `input1_sequential.csv` is named as `input1_standarddeviation.png`, etc
