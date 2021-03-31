# Pattern Extraction

**Objective**
In this project, we show an application of the data mining process to a  dataset from the Mexican government’s purchases named ‘ExpedientesPublicados’. The objective consists of extracting patterns, analyzing them, and presenting them with the use of data visualization and with an attempt to obtain and show insights.

**Dataset**
The dataset is obtained from the electronic system of government public information and consists of service hiring contracts.

**Methods**
In this project, we make use of the PBC4cip algorithm to obtain contrast patterns from the CompraNet's database. 

The PBC4cip [2] classifier is a contrast pattern-based classifier. In the data mining phase, the PBC4cip algorithm computes the contrast patterns for each of the classes analyzed and its weights. Following, in the classification phase, the algorithm delivers the sum of supports in each class for all the patterns found. The sum is then multiplied by the weight of each class respectively. The algorithm obtains the contrast patterns in the dataset by extracting characteristics from the decision nodes that go from the root node to the leaves inside a decision tree,  and this is done for multiple decision trees. The constraints considered for pattern extraction are the ones outlined in Table 2. 


![alt text](https://github.com/ML-Group-Col/Exped_Visualizations/blob/master/table2.png)

**Conclusions**

Before the extraction of the patterns and the analysis of the data, and as part of our feature engineering process we created a few attributes using natural language processing. Specifically, these attributes describe if one of the three most common words are present in the text objects ‘Descripción del Anuncio’ and ‘Nombre de la UC’. To obtain these words a natural language processing library was used. To normalize and count the most common words, the attributes were then tokenized and words were stemmed into their basic forms.

Next, the PBC4cip algorithm was used to extract the patterns from the transformed and selected attributes. Following, within the visualization design process we created multiple variations to observe patterns with one, two, and three univariate items.  We found the bar graph subplot matrix to be a good tool to represent this, as one can observe from afar how the support for each class varies with different attribute value combinations and just filter certain combinations to see how the pattern has found a situation with clear grater support for the target variable. We also observed that the ‘seaborn’ and ‘plotly express’  libraries were of great use for this graph implementation.

**References**
[1]  Han, J., Pei, J., & Kamber, M. (2011). Data mining: concepts and techniques. Elsevier.
[2] L. Cañete-Sifuentes, R. Monroy, M. A. Medina-Pérez, O. Loyola-González and F. Vera Voronisky, "Classification Based on Multivariate Contrast Patterns," in IEEE Access, vol. 7, pp. 55744-55762, 2019. doi: 10.1109/ACCESS.2019.2913649
