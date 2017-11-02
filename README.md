

## The Complex Pheno/Geno workflow


##### Dependencies
* Python 3.6
* Plink 1.9
* Entrez Programming Utilities (E-utilities) API


## A. Installing Complex Pheno/Geno

1. Download Complex PhenoGeno from this repository to your computer.

2. Open Terminal, cd to the newly downladed Complex PhenoGeno directory and run:

`pip3 install -r requirements`

This will install all the necessary python modules. It is advised that you create an environment dedicated to Complex Pheno/Geno and you run everything from it.

3. Open the file "Settings.txt" and change the e-mail to the email you used for registering to [E-utilities](https://www.ncbi.nlm.nih.gov/home/develop/api/).

4. Install [plink](https://www.cog-genomics.org/plink2).

## B. Preparing the datasets

*Downloading Complex PhenoGeno comes with some dummy data files to make sure everything works smoothly before you run your own data. These dummy data will be used if there is no "files" folder (see below) and you indicate so during the session (you will be asked). If you choose to use the dummy data, you don't need to do any of the steps described below.*

Complex Pheno/Geno requires your data to be formated in a specific way. These expectations are nothing more than careful data preprocessing, a good practice for any analysis. Please follow the instructions bellow when preparing your data: 

Create a new folder called "files" in the same folder where you dowloaded Complex PhenoGeno. Below are the expected data and their expected formats (you can inspect the dummy data included with the package for an example):

i. **VCFs of the patient genotypes** in gz compressed format. One vcf per chromosome or any type of fragmentation of the data that suits your needs. Multiple files are expected, so please do not include all your genotype data in one VCF file. This is necessary to speed up this pre-processing step by parallelizing the process. Please consult [VCFtools](https://vcftools.github.io/examples.html) on how to manipulate and split these files. The files need to be gz complessed (*i.e.* <name>.vcf.gz).

ii. **CSVs of the clinical results**. The rows are the individual identifiers of the cohort (same as those in the VCF files), and the columns are the different clinical tests performed. Missing values are not allowed. Both continuous and integer values are allowed, categorical values should be represented as dummy variables in their own columns (eg if three individuals, a, b, and c, each belong to categories "A", "B", and "C" respectively, there should be three columns, A, B, C, with values "A":[1,0,0] , "B":[0,1,0] , and "C":[0,0,1]. For more details on dummy variables go [here](https://www.moresteam.com/whitepapers/download/dummy-variables.pdf))

iii. **CSVs of the behavioral data available for the cohort**. Instructions as in (iii).

Only data in the folder "files" will be considered during analysis. 

## C. Running Complex Pheno/Geno

Once everything is set up, got to Terminal, inside the ComplexPhenoGeno folder, and type:

`python3 ComplexPhenoGeno.py`

![Flow diagram](https://github.com/NCBI-Hackathons/Complex_Phenogeno/blob/master/Images/FlowDiagram.jpeg)

This will start a guided interactive session that will take you through the steps of the algorithm. Depending on the size of your files, you should expect a minimum of one hour for the entire workflow (approximately 2,000 individuals in cohort). Below are the steps of the Complex Pheno/Geno pipeline:

1. **rsIDs.py** You are asked to enter an rsID that you know is strongly causally related to the [Complex Disease](https://github.com/NCBI-Hackathons/Complex_Phenogeno/blob/master/ComplexDisease.md) of interest. Using E-utilities and feedback from [PhenVar](https://phenvar.colorado.edu), this first step identifies other rsIDs that are co-cited with your query rsID in the literarure. Make sure the results' visualization offered by PhenVar in a new browser window (optional) make sense. You are offered the ability to filter the rsIDs by the number of publications supporting their co-citation with the query rsID. The folder Outputs is created, and the collected rsIDs are saved in `Outputs/rsids.txt`.

2. **Genotypes.py** The cohort genotypes (in compressed VCF format, as described above) are filtered by the list of rsIDs, created in step 1. This may take a while for large VCF files of big cohorts. You will be given a time estimate. The result of this step is saved as `Outputs/Genotypes.csv`, where each row is an individual, and each column is an rsID from the list determined in the previous step. The minor allele presence for each individual and each locus is encoded: 0 if not present, 1 if present heterozygous, and 2 if present homozygous.

3. **Models.py** Clinical data are modeled as a linear regression (no interactions considered) and with random forests. The user is asked to decide the fraction of the data to be used for training (0.7 or above is recommended, but the size of the dataset should also be taken in consideration). The algorithms are run 50 times and the average and standard deviation of the AUC are returned to the user. A stable model should produce low standard deviations (*i.e.* the model is not significantly affected by the random data subset used). An AUC above 0.5 means prediction better than random, a value closer to 1 is considered best. In the case of the random forest model, a range of [tree depths](https://www.analyticsvidhya.com/blog/2015/06/tuning-random-forest-model/) is tested, and the mean AUC is calculated for each of these values. The depth were the AUCs converge (plateu to a maximum value) is the optimum value for the model. The explanatory variable for these models needs to be a well-understood The estimations for each model are repeated 50 times and the average AUC and 

4.

