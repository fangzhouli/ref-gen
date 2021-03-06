# Ref-gen: A pipeline for retrieving reference genome data

## Description

Reference genome is important in omics research, but it is difficult to pick a right reference genome for an organism when there are too many options. This pipeline prepares and downloads the best reference genome candidate for users.

## Algorithm

Ref-gen goes over different metadata of available reference genome to prioritize the ones that are in the best quality. It ranks the reference genome according to the following standard:

- RefSeq category       : Representative genome > Reference genome
- Assembly level        : Complete genome > Chromosome > Scaffold > Contig
- Release               : Major > Minor > Patch
- Genome representation : Full > Partial

## Usage

### Command-line Interface

```console
usage: ref-gen [-h] [--update] [--output OUTPUT] term [term ...]

positional arguments:
  term             organism name needed for reference genome

optional arguments:
  -h, --help       show this help message and exit
  --update         re-download summary file if included
  --output OUTPUT  path to store gff file
```

#### Example

This will allow ref-gen to download salmonella reference genome in the current directory.

```console
ref-gen 'salmonella' --output './output.txt'

2 reference genome detected.
Id Assembly             Name                                                                                                
1  GCF_000006945.2      Salmonella enterica subsp. enterica serovar Typhimurium str. LT2                                    
2  GCF_000195995.1      Salmonella enterica subsp. enterica serovar Typhi str. CT18                                         
Choose an id: 1
Downloading...
Finished!
```

### API

```python
Extractor(update_summary = False)
"""extractor class for reference genome

    parameters
    ==========
    update_summary  : (bool, default = False) if True, it will redownload
        summary file from NCBI server which takes longer time. However, it will
        download a summary regardless for the first run of meta-omics

    attributes
    ==========
    prep            : (object) preprocessor

    methods
    ==========
    find_refgen     : loos for the best reference genome
        input:
            term            : (str) str
        output:
            (list of tuple) : (assembly, name, ftp_url)

    extract         : find the best reference genome of the term from the NCBI server and download the binary file to the specified local path
        input:
            ftp_url     : (str)
            output      : (str, default PATH = omics/refgen/data/gff) """
```

#### Example

```python
>>> from refgen import Extractor
>>> extr = Extractor()
>>> candidates = extr.find_refgen('salmonella')
>>>
>>> candidates
[('GCF_000006945.2', 'Salmonella enterica subsp. enterica serovar Typhimurium str. LT2', 'ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/006/945/GCF_000006945.2_ASM694v2'), ('GCF_000195995.1', 'Salmonella enterica subsp. enterica serovar Typhi str. CT18', 'ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/195/995/GCF_000195995.1_ASM19599v1')]
>>>
>>> extr.extract(candidates[0][2]) # downloading the first candidate by using its ftp_path
```