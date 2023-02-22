CNVnator, in the main, relies on the mean-shift method to detect CNVs. First, the software divides the entire genome into equal-length sequences in non-overlapping subsets to then extract an individual read depth from each. For the RD signal, each location can be calculated differently by changing the window size used to count the mapped reads. The number of nucleotides covered by each interval is called the window size, which can be determined from the average coverage of the sequencing data. Estimating the number of CNV changes for each fragment requires a one-sample Student's t-test to obtain p-values (p < 0.05), to test whether the average RD signal in a given window will be close to the genome-wide average.

In addition, CNVnator can identify both deletions and duplications. Furthermore, the programme can be used with low-coverage data and still give accurate results. Based on the above arguments, CNVnator performs exceptionally well for analyses that require the detection and comparison of CNVs, e.g. between different individuals.

Number of deletions for CNVnator before and after filtration

![image](https://user-images.githubusercontent.com/67764136/220764277-2ff0b36d-fd90-45cb-9070-c471a371dbef.png)

Deletion length for CNVnator before and after filtration

![image](https://user-images.githubusercontent.com/67764136/220764351-ec04cb45-b7ee-478c-841b-35af0daeb94e.png)

Number of duplicates for CNVnator before and after filtering

![image](https://user-images.githubusercontent.com/67764136/220764411-ab977170-0fb1-4618-b3a1-d644f2561c6d.png)

Duplication length for CNVnator before and after filtering

![image](https://user-images.githubusercontent.com/67764136/220764481-f168310e-2ea2-469e-ae99-6052e006d27a.png)

