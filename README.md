
## What is complex disease?

Unlike illnesses such as sickle cell anemia or cystic fibrosis, where dys-regulation or mutation of a single gene can completely explain--and is responsible for--disease onset, the causes of [complex diseases](https://report.nih.gov/NIHfactsheets/ViewFactSheet.aspx?csid=42) cannot be easily deciphered using simple mendelian heredity rules. It is actually the majority of non-infectious diseases (and, indeed, the majority of [biological traits](https://www.sciencedaily.com/terms/trait_%28biology%29.htm)) that fall into this category, cancer, cardiovascular conditions, and obesity being all but a few examples.

### Why are complex diseases so hard to understand?

From a biological perspective, complex diseases can be understood as the effect that combinations of mutations have on multiple pathways; different mutations affect different pathways and all together contribute to the onset and severity of the disease. Moreover, certain environmental and behavioral factors (e.g. radiation exposure, smoking, reduced vitamin intake) might further contribute to disrupting these pathways, deteriorating (or enabling) the observed adverse outcomes, even when the mutational burden for the disorder is not too high. Because [multiple pathways are usually involved in complex disease](https://www.genome.gov/10000865/), the symptoms are also, typically, complex, comprising of a collection of distinct phenotypes that are being monitored and used in diagnosis. 

![PseudoFunction](https://github.com/NCBI-Hackathons/Complex_Phenogeno/blob/master/Images/PseudoFunction.jpeg)

<sub>Pathologists are usually relying on a combination of symptoms and diagnostic tests to assess whether a patient suffers from a disease. These symptoms are rarely binary and empirical thresholds have been established to assess pathological status. Moreover, very seldom all symptoms need to be present for a disease diagnosis to be made. This can be explained by the variety of biological pathways that are being affected by the multiple underlying mutations in the patient's genome, as well as the modulatory effect of the environment on them.</sub>

### The promise of personalized medicine and limitations to its broad-scale implementation

With the introduction and readily adoption of high-throughput methods that scan the entire genome for mutations (initially [microarray hybridization](https://www.genome.gov/10000533/dna-microarray-technology/) and lately [genome sequencing](https://www.genome.gov/10001177/dna-sequencing-fact-sheet/)) we now have the means to uncover the various mutations that underlie complex diseases. Genome-wide association studies ([GWAS](https://www.genome.gov/26525384/catalog-of-published-genomewide-association-studies/)) are using the power of statistics (and big patient cohorts) to uncover relationships between mutations and pathologic outcomes. The idea is simple: before we are able to study how different mutations are affecting disease, we need to discover them. This is the first step to [personalized medicine](https://www.nih.gov/about-nih/what-we-do/nih-turning-discovery-into-health/personalized-medicine).

The table below outlines the main limitations for development of personalized medicine for complex diseases.

|                            Biological (genomic)                            |                   Environmental (behavioral)                   |                                        Clinical (diagnostic)                                       |
|:--------------------------------------------------------------------------:|:--------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------:|
| Availability of sufficient number of GWAS studies for a particular disease |            Infinite number of putative  parameters to examine            | Subjectivity of narrowing down to a specific disease due to inconsistent  combination of symptoms  |
|       Discovery of extremely rare alleles depends on GWAS cohort size      |                Difficult to continously monitor                |                            Availability of the appropriate test results                            |
|                        Association is not causation                        |                          Survey design                         |                                Accuracy of different clinical tests                                |
|        Genetic [epistasis](https://en.wikipedia.org/wiki/Epistasis)        | [Respondent bias](https://en.wikipedia.org/wiki/Response_bias) |           Continuous scale of clinical measurements. Semi-arbitrary pathological cutoffs           |
|    The effect of mutations to specific pathways is still largely unknown   |                                                                |                                      Variation between clinics                                     |


## Complex Pheno/Geno

There has now been more than ten years, and throusands of publications, of GWAS (and other) studies that have discovered hundreds of thousands of single nucleotide polymorphisms associated with disease. Taking advantage of this existing (and growing) knowledge generated in the lab, Complex Pheno/Geno restricts the genome space to be examined, potentially lowering the costs of personilized medicine. At the same time it explores models that could offer good explanatory power to the observed pathologic outcomes.

### The Complex Pheno/Geno algorithm

Complex Pheno/Geno is a computational pipeline that allows matching of an assortment of diagnostic traits associated with the disease to the underlying genetic variation and environmental burden for the individual, with the goal to accurately estimate the risk of developing the disease. It leverages experimentally-derived GWAS associations between the disease and the underlying mutations that contribute to it as found in literature. Acknowledging the pleiotropic effects of different mutations, it allows for expanding the range of mutations tested, by utilizing [rsIDs](https://www.ncbi.nlm.nih.gov/books/NBK174586/) ('mutation IDs') that are found linked in the literature.

Usage of the tool requires that the researcher already has a cohort of genotyped individuals (VCF files), alongside measurements for the traits associated with the disease, as well as at least one experimentally determined rsID that contributes to the disease. The pipeline is diagrammatically explained below.


## Further readings
1. [A simple explanation of heredity in complex disease](https://www.med.unc.edu/neurology/files/documents/child-teaching-pdf/Genetics%20Disease.pdf) (UNC Chapel Hill, USA)
2. [Genetic and environmental interactions in complex disease](http://www.genetics.edu.au/publications-and-resources/facts-sheets/fact-sheet-11-environmental-and-genetic-interactions) (New South Wales Health, Australia) 
3. [Wikipedia entry on GWAS](https://en.wikipedia.org/wiki/Genome-wide_association_study)