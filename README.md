# Complex Pheno/Geno

![#c5f015](https://placehold.it/15/c5f015/000000?text=+) **Age-related macular degeneration example**

## Background
Unlike illnesses such as sickle cell anemia or cystic fibrosis, where dys-regulation of a single gene can completely explain--and is responsible for--disease onset, the causes of [**complex diseases**](http://www.genetics.edu.au/publications-and-resources/facts-sheets/fact-sheet-11-environmental-and-genetic-interactions), cannot be easily deciphered using simple mendelian heredity rules. Obesity, cancer, and cardiovascular conditions, among others, fall under this category. The reason for our current inability to completely understand the pattern of disease onset in these cases is that complex diseases are **multifactorial**, *i.e.* they are influenced by the interaction of multiple genes, environmental factors, as well as the person's behavior. We know for example that increased caloric intake can lead to obesity, but a person's height and overall metabolism (among other genetic factors), as well sedentary lifestyle and other behaviors are also important contributors to a person's [BMI](https://en.wikipedia.org/wiki/Body_mass_index). Without therefore knowing how different factors might affect different individuals, medical and legislative interventions can only offer partial solutions to theses **diseases of civilization**, whose prevalence is correlated with a country’s GDP. 

From a biological perspective, complex diseases can be understood as the effect that combinations of mutations have on multiple pathways; different mutations affect different pathways and all together contribute to the onset and severity of the disease. Moreover, certain environmental and behavioral factors (*e.g.* reduced vitamin intake or smoking) might further contribute to disrupting these pathways, deteriorating (or enabling) the observed adverse outcomes, even when the mutational burden for the disorder is not too high. Because multiple pathways are usually involved in complex disease, the symptoms are also usually complex, comprising of a [collection of distinct phenotypes](https://www.genome.gov/10000865/) that are being monitored and used in diagnosis. 

## Outline
Complex Pheno/Geno is a computational pipeline that allows matching of an assortment of diagnostic traits associated with the disease (as *e.g.* those found in Electronic Health Records, EHR) to the underlying genetic variation of the individual, with the goal to estimate the risk of developing the disease. It leverages experimentally-derived associations between the disease and the underlying mutations that contribute to it as found in literature. Acknowledging the pleiotropic effects of different mutations, it allows for expanding the range of mutations tested, by utilizing [rsIDs](https://www.ncbi.nlm.nih.gov/books/NBK174586/) ('mutation IDs') that are found linked in the literature.

Usage of the tool requires that the researcher already has a cohort of genotyped individuals (VCF files), alongside measurements for the traits associated with the disease, as well as at least one experimentally determined rsID that contributes to the disease. The pipeline is diagrammatically explained below.
![FlowDiagram](https://github.com/NCBI-Hackathons/Complex_Phenogeno/blob/master/Images/FlowDiagram.jpeg)

## Tools
1. [PhenVar](https://phenvar.colorado.edu/results/?rsids=800292&visualization=png-wordcloud&visualization=js-graph&normalization_type=default) [(Git)](https://github.com/NCBI-Hackathons/PhenVar/tree/python3)
2. [GenomicRobots (Git)](https://github.com/NCBI-Hackathons/GenomicRobots)
3. [Super Concise Single Cell Snp Caller, SC3](https://github.com/NCBI-Hackathons/SC3)
4. [Polygenic SNP Search Tool, PSST](https://github.com/NCBI-Hackathons/PSST)
5. [MultiPhen : Joint model of multiple phenotypes can increase discovery in GWAS](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0034861) [(CRAN)](https://CRAN.R-project.org/package=MultiPhen)
6. [SNP Feasible Solutions Algorithm, SNP FSA (Git)](https://github.com/NCBI-Hackathons/Network_Stats_Acc_Interop)

## References
1. [The genetics of age-related macular degeneration](http://www.macularisk.com/amd-prognosis/genetics-of-amd.html)
2. [National Eye Institute (NEI) Age-Related Eye Disease Study (AREDS)](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000001.v3.p1)
3. [Diet, exercise, smoking habits, and genes interact to affect AMD risk (2015)](https://nei.nih.gov/news/pressreleases/habits_genes_affect_AMD)
