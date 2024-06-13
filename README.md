# SoCalSolutions

# Predicting Pet Adoption Likelihood
Authors: Sandor Faya, Mohe Dean Hajjar, Ben Denis, Rahim Sarpas

# Introduction
Animal shelters across the globe face a significant challenge in ensuring that the pets they care for find permanent, loving homes. Despite the efforts of shelter staff and volunteers, many pets remain unadopted for extended periods, which can lead to overcrowding and strain on shelter resources. This situation not only affects the well-being of the animals but also the operational efficiency of the shelters. Understanding and predicting the factors that influence pet adoption can greatly enhance the adoption process, ensuring that more pets find their forever homes faster.

The problem we aim to solve is to develop a predictive model that assesses the likelihood of pets getting adopted from shelters. By analyzing various attributes of the pets, such as species, age, sex, color, and health status, we can identify patterns and factors that significantly impact adoption rates. This model will help shelters optimize their resources and strategies by highlighting which pets are less likely to be adopted and may need additional support or visibility. Furthermore, it can assist in tailoring adoption campaigns, improving matchmaking between pets and potential adopters, and ultimately increasing the adoption rates.

# Source Data Set

We will use the "Animal Shelter Intakes and Outcomes" dataset, which comprises detailed records of approximately 27,000 animals that have passed through a shelter system. Each entry in the dataset represents an individual animal, providing comprehensive information about its journey through the shelter. The dataset includes information about each animalʼs species, DOB, sex, color, health status, intake date, and outcome.

# Link to the dataset
https://data.longbeach.gov/explore/dataset/animal-shelter-intakes-and-outcomes/export/?flg=en-us&disjunctive.animal_type&disjunctive.primary_color&disjunctive.sex&disjunctive.intake_cond&disjunctive.intake_type&disjunctive.reason&disjunctive.outcome_type&disjunctive.outcome_subtype&disjunctive.intake_is_dead&disjunctive.outcome_is_dead

# Prediction Goal

We aim to build a system to predict the likelihood of a pet being adopted from the shelter. The target variable will be Outcome Type , where we will focus on outcomes indicating adoption. The predictors we plan to use include species, age, sex, color, health status, and intake conditions.

# Preliminary Work on Data Preparation

Data Preparation The initial steps for data preparation include: 
Loading the dataset Handling missing values Encoding categorical variables creating new features if necessary (e.g., age at intake)

# Data Preparation

The initial steps for data preparation include:

1. Loading the dataset
2. Handling missing values
3. Encoding categorical variables
4. Creating new features if necessary (e.g., age at intake)
   
# Data Exploration and Visualization
Some initial data exploration to understand the dataset better:

(pic)

We will split the data into training and testing sets and build an initial model to predict
the adoption likelihood.

(Pic)

Accuracy: 0.2859221535103674
