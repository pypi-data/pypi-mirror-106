# Genbank Parser

## Contents

- [Overview](#overview)
- [Repo Contents](#repo-contents)
- [System Requirements](#system-requirements)
- [Installation Guide](#installation-guide)
- [License](./LICENSE)

## Overview

This is a simple class for processing Genbank files.

## Repo Contents

- [GenbankParser Classes](./GenbankParser/Classes) Directory with the ParseGenbank Class for processing genbank files

## System Requirements

Should work on Linux and OSX

### Hardware Requirements

RAM: 4+ GB  
CPU: multicore CPU

The runtimes vary considerably, depending on how large the sequencing data files are.
But a typical run generally takes several hours to complete.

### Software requirements

 - Python 3.6+ or higher

## Installation Guide

Go to the directory containing the setup file and run:

```
sudo python setup.py install
```

This should run the installation script, making it possible to access the class from Python.

## Results

To run the code on the test data, please have a look at the jupyter notebook in the test_code directory.
The results of these test runs can be found in the test_code directory.
=======

## Overview

This is a simple class for processing Genbank files.

## Repo Contents

- [GenbankParser Classes](./GenbankParser/Classes) Contains the ParseGenbank Class for processing Genbank files
- [test code](./test_code) Contains a jupyter notebook with code showing how to run the class

## System Requirements

### Hardware Requirements

RAM: 4+ GB  
CPU: multi-core CPU


### Software requirements

 - Linux and OSX operating systems
 - Python 3.6+ or higher 

## Installation Guide

All you need to do is to make sure that the scripts in the scripts_folder are added to PATH in linux
For this you would need to add the path of this directory to the .bash_profile or .bashrc file.

## Results

To run the code on the test data, please have a look at the jupyter notebook in the test_code directory.
The results of these test runds can be found in the test_code directory.