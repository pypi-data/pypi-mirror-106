# Metapan

Before opening a new issue here, please check the appropriate already exits issues and commenting on a thread there.

[![pypi version](https://img.shields.io/pypi/v/metapan.svg)](https://pypi.python.org/pypi/metapan)  [![Build Status](https://travis-ci.org/joemccann/metapan.svg?branch=master)](https://travis-ci.org/joemccann/metapan)
## metapan User Manual

metapan help you perform pangenome wise compariosn between two or more group at functional level after the metagenomic dataset have been run through HUMAnN 3.0,  MEGAN6 + Diamond pipleine ,

**If you use metapan in your work, please cite the metapan paper:**

## Contents ##

* [Features](#features)
* [Workflows](#workflows)
    * [Main workflow](#main-workflow)
    * [Workflow by input file type](#workflow-by-input-file-type)
    * [Workflow by bypass mode](#workflow-by-bypass-mode)
    * [Workflow of the resume option](#workflow-of-the-resume-option)
* [Requirements](#requirements)
    * [Software](#software)
    * [Other](#other)
* [Automated Installation](#Automated-installation)

## Requirements ##

### Software ###

1. [cd-hit](https://github.com/weizhongli/cdhit)
Please install the required software in a location in your `$PATH`

## Installation

----
## Automated Installation ## 
```sh
1. Clone metapan git.
      git clone https://github.com/AnupamGautam/metapan.git

2. Move to the metapan directory.
      cd metapan`

3. Create conda enviroment with require dependency. 
      conda env create -n metapan --file metapan_2021.01_py38_conda.yml
      conda activate metapan
```

## Complete Usage ##

```
metapan -h
Usage: metapan [options] infile

Run pangenome and does comparison at Functional level

Options:
  -h, --help            show this help message and exit
  -i inputfiledirectory, --inputfiledirectory=inputfiledirectory
                        Input file directory
  -o output, --output=output
                        output folder path [Default: metapan]
  -m metadatafile, --metadatafile=metadatafile
                        Enter name for input File
  -g columnname, --columnname=columnname
                        Enter columnname name for grouping

  Clustering Parameter:
    -s tool, --tool=tool
                        Enter tool to use for clustering cdhit, usearch etc
                        [Default: cdhit]
    --toolpath=toolpath
                        Enter path to tool to use for clustering cdhit,
                        usearch etc
    -c sequenceidentity, --sequenceidentity=sequenceidentity
                        Enter sequence identity threshold, [Default: 0.9]
    -w wordlength, --wordlength=wordlength
                        Enter word_length, see CD-HIT  user guide for choosing
                        it [Default: 5]
    -a alignmentcoverage, --alignmentcoverage=alignmentcoverage
                        Enter alignment coverage for the longer sequence, if
                        set to 0.9 the alignment must covers 90%% of the
                        sequence [Default: 0.9]

  General Parameter:
    -p prefix, --prefix=prefix
                        Enter prefix
    -t threads, --threads=threads
                        Enter number of threads
    -r ram, --ram=ram   Enter ram in gb you want to use [Default: 2gb]

Anupam_Gautam
```

----



## License

GPL-3.0

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>

