# 1. Title: Detection of housing-health relationship

## 2.  **Abstract**

The aim of this project is to estimate the relation between housing quality and health status of a person. The project is an observational study based on a survey made by Mexican National Institute of Statistics and Geography. The health variables reported for each person will be used to define a single health variable which will be a score for each person's health status. We aim to use machine learning methods to do the classification and we will use regression models to predict this health score from the housing variables. Matching will be used to weed out the possible covariates. The motivation is to estimate the most important parameters of housing quality so that we can propose most cost-effective solutions that would increase the quality of health. The original paper is based on the analysis of influence of concrete floors on health quality, while here we would investigate some other parameters such as material used for building and whether there is a toilet or not in the household.

## 3. **Research Questions**

1. Is there a relation between housing quality and health and how can we measure it?
2. Which housing properties are affecting health the most (if any) ?
3. Is there a certain threshold above which the quality of housing will not affect health anymore?

## 4. **Proposed dataset**

We propose to use datasets from ENH-2017 by Mexican National Institute of Statistics and Geography (INEGI) :

The National Household Survey (ENH) is carried out with the purpose of knowing the characteristics of the housing units; sociodemographic data about the household members, their occupation, education; as well as the availability of information and communication technologies goods and services in households. At the same time, it allows the integration of the satellite accounts of the System of National Accounts of Mexico (SCNM). [National Household Survey (ENH) 2017](https://en.www.inegi.org.mx/programas/enh/2017/)

The dataset consists of 64 000 households with about 208 140 habitants living in those households. The data consist of three different units including households data with 110 variables, house data with 13 variables and person data with 58 variables. Each person is assigned to its corresponding household and house.

- **Sample size:** 64 000 housing units
- **Observation unit:** The household.
- **Sampling unit:** The housing unit.
- **Analysis unit:** The household, the housing unit and the household members.
- **Sampling frame:** For the selection of the sample the Master Sample of the National Housing Framework 2012 of INEGI was used, the latter was made from the cartographic and demographic information that was obtained from the Census of Population and Housing 2010.
- **Sampling scheme:** Probabilistic, at the same time the design is stratified, two-stage and by clusters, where the last selection unit is the housing unit and the observation unit is the household; consequently, the results obtained from the survey are generalized to the entire population.

The data is provided by the one member of the household which provides the data for the rest of the people living in the same household. The sampling is done in a statistical way so that the dataset is a representative sample of both urban and rural areas.

Additionally, if necessary, the datasets from ENH 2014, 2015 and 2016 are available.

## 5. **Methods**

**Data collection and translation:** The proposed datasets are clean and ready to use except by the language (spanish, luckily Erick speaks spanish). In case we decide to add more datasets. They will have to be merged.

**Feature engineering:** We will validate the questions we want to answer and the features we want to use by using regression and machine learning techniques: logistic regression, linear regression, Gradient boosting regressor and KNN. We expect to create a visualization. Finally we will try to create an accurate regressor.

**Data visualization:** We will create different visualizations to show our results and justify the decisions we made.

## 6. **Proposed timeline**

**Week 1:** Download the dataset. Translate the variables descriptions which are written in Spanish. Define if other datasets will be required or could potentially help answer the research questions. Research and test clustering methods.

**Week 2:** Implement and optimize the chosen algorithm and possible application of score matching technique.

**Week 3:** Wrap up the data analysis and work on the data story.

## 7. **Organization within the team**

- Erick will work on the translation and machine learningn methods.
- Antonio will run the regression, using matching scores to weed out possible covariates.
- Mattia will work on creating an ad hoc health variable which will synthesize the group of variables we are trying to predict.

## 8. **Questions for TAs**

- Is it possible to slightly modify the aforementioned methods if necessary in the future, or what we wrote now has to be followed strictly for the realization of P4?
- Is it part of the scope to try and analyze how complex machine learning models work in this task?
