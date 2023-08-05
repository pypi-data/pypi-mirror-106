# pyCRAC

## Contents

- [Overview](#overview)
- [Repo Contents](#repo-contents)
- [System Requirements](#system-requirements)
- [Installation Guide](#installation-guide)
- [Results](#results)
- [License](./LICENSE)
- [Citation](#citation)

## Overview
This package contains a number of software tools for processing CRAC/CLIP/PAR-CLIP type data. 
Included in this package is a detailed manual with examples on how to run the code and with detailed explanation of the format of the resulting output files.

## Repo Contents

- [pyCRAC](./pyCRAC): pyCRAC Python code
- [The pyCRAC Manual](./The_pyCRAC_Manual.pdf): Package documentation, and usage examples.
- [tests](./tests): folder with test data and test code

## System Requirements

### Hardware Requirements

RAM: 16+ GB  
CPU: At least four cores are recommended.

The runtimes vary considerably, depending on how large the sequencing data files are.
But a typical run generally takes several hours to complete.

### Software Requirements

#### OS Requirements

The installer has been tested on Mac OSX 10.8 and up, Debian Wheezy/Sid, Linux Mint 16, Ubuntu 13.04 and Fedora 20.
May work for other distros as well but you might find yourself having to install many dependencies manually.

Other dependencies:

Python 2.7 and Python 3.6 or higher
Note that support for Python 2 will be removed in the near future.

## Installation Guide

All the necessary dependencies will be installed when running the installer script.
To install enter the folder using the terminal and type the following:

```
sudo python setup.py install
```

Enter your password and hit return key.

The installer will ask you where you want to have your data files installed.
Default is your home directory.

PySam installation has been causing problems for some users because some dependencies were missing (zlib compression libraries mostly).

If you discover a bug, leave a note in the issue tracker. Please include as much information about the problem as you possibly can, including all error messages.

Note that some of the pyCRAC tools have undergone a number of changes since version 1.2. 
All of these changes have been highlighted in the updated manual. 
The changes do NOT affect compatibility with previous versions.

pyCRAC version 1.4.0 is compatible with both python 2.x and 3.x.
This beta version is still being heavily tested so please send me an e-mail if you spot a bug.

NOTE!! pyCRAC can now also be installed using Pip!

```
sudo pip install pyCRAC
```

### Development Version

#### Package dependencies

All the dependencies will be installed automatically when running the installation script.

## Citation

Please cite the following paper when discussing pyCRAC tools in your manuscript:

Webb, S., Hector, R. D., Kudla, G. & Granneman, S. 
PAR-CLIP data indicate that Nrd1-Nab3-dependent transcription termination regulates expression of hundreds of protein coding genes in yeast. 
Genome Biol. 15, R8 (2014).

All the best,

Sander Granneman

Sander.Granneman@ed.ac.uk

Granneman Lab
University of Edinburgh, UK
Department of Synthetic and Systems Biology (SynthSys)
