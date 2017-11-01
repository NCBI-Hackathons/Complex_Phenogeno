

## The Complex Pheno/Geno algorithm

Run Complex Pheno/Geno from the Terminal calling :

`python3 ComplexPhenoGeno.py`

##### Dependencies
* Python 3.6
* Plink 1.9
* Entrez Programming Utilities (E-utilities) API

![Flow diagram](https://github.com/NCBI-Hackathons/Complex_Phenogeno/blob/master/Images/FlowDiagram.jpeg)

## A. Installing the sofware

1. Download Complex PhenoGeno from this repository to your computer.

2. Open Terminal, cd to the newly downladed Complex PhenoGeno directory and run:

`pip3 install -r requirements`

This will install all the necessary python modules. It is advised that you create an environment dedicated to Complex Pheno/Geno.

3. Open the file "Settings.txt" and change the e-mail to the email you used for registering to [E-utilities](https://www.ncbi.nlm.nih.gov/home/develop/api/).

4. Install [plink](https://www.cog-genomics.org/plink2).


## B. Preparing the datasets

Downloading Complex PhenoGeno comes with some dummy data files to make sure everything runs smoothly before you run your data. These data will be used if you indicate so during the session, or will be skipped if you have created a "files" folder with your own data. If you choose to use the dummy data, you don't need to do anything of the things described below. 

Complex Pheno/Geno requires your data to be formated in a specific way. These expectations are nothing more than careful data preprocessing, a good practice for any analysis. Please follow the instructions bellow when preparing your data: 

1. Create a new folder called "files" in the same folder where you dowloaded Complex PhenoGeno. Below are the expected data and their expected formats (you can inspect the dummy data included with the package for an example):

	a. **VCFs of the patient genotypes** in gz compressed format. One vcf per chromosome or any type of fragmentation of the data that suits your needs. Multiple files are expected, so please do not include all your genotype data in one VCF file. This is necessary to speed up this pre-processing step by parallelizing the process. Please consult [VCFtools](https://vcftools.github.io/examples.html) on how to manipulate and split these files. The files need to be gz complessed (*e.g.* <name>.vcf.gz).

	b. **CSVs of the clinical results**. The rows are the individual identifiers of the cohort (same as those in the VCF files), and the columns are the different clinical tests performed. Missing values are not allowed. Both continuous and integer values are allowed, categorical values should be represented as dummy variables in their own columns (eg if three individuals, a, b, and c, each belong to categories "A", "B", and "C" respectively, there should be three columns, A, B, C, with values "A":[1,0,0] , "B":[0,1,0] , and "C":[0,0,1]. For more details on dummy variables go [here](https://www.moresteam.com/whitepapers/download/dummy-variables.pdf))

2. When prompted to answer 

3. Only data in the folder "files" will be considered during analysis.

