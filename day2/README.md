# Detecting planets with ML
Methods:
* 30 pixes pro star
* measure changes in brightness of a star
* birghness is folded based on periodicity of the brighness changes


create a method that will take the input brighness and 
preprocessing - specific normalization
use cnn to extract features 

## Confirmation
Domain experts look at more images from different telescopes

## Validation
A statistical test used to validate if this is a planet or not


# Online learning

## Pricing
started with static fules
started with offline training
 > take a data with prices and conversion rate

Problems:
1. Drift
 * suden
 * gradual
 * reoccuring
 * inrecemental
> do model retraining offline
2. Requires exsiting data of good quality
 * thge training data might not contain enough variability 
3. Adapting to new tasks (new products) is expensive

Online (Incremental training)
1. Train a model offline (quick, small data)
2. Collect the data online (did the customer buy or not)
3. Update the parameter

Solution:
1. Training (adaptive learning)
* detect data drift, changes, active learing
2. Evaluation
* adaptive validation (validation on adaptive sliding window)
3. Approximation algorithms
* move from: precise + slow answers > approximate + fast answers

When to consider online learning
1. data drifts
2. No need to retain past data
* privacy policy
3. Real time / event based
* fraud detection, recommendation system, ranking of search results, spam 


Drawbacks
* not every algoritm offers this option
* catastrophic forgetting 
* cold start
Clustering
1. Input data
2. Phase1 
* Micro clusters with summary statistics (mean, centroid position)
3. Phase2
* Offline macro clustering

Implementation
* River https://riverml.xyz/latest/ 
* Scikit-multiflow https://scikit-multiflow.github.io/ 

Seasonality problem
* encode features for seasonality
* balance quickly - perform simulations offline


# Prevent churn
Always down-sample data (remove irrelevant cases), dimension reduction
Bayesian network reasoning


# Phishing emails
Take a sample of data from prod, run the model with different thresholds and observe how many cases are labled as phisting (anomaly)
Use bayesian logistic regression > Use LLM to categorize and take care of non-linear bahaviour  



# RAG
Take a whole docuemnt > split to chunks (pages) > embbed 

## Hyperparameters:
1. Weight cut-off
* when to cut-off similarity in the vector space
2. Max docs
* what is the maximum amounts of chungs we can use

## 3 Common problems
1. Data imbalance
* a lot of text on one topic, almost nothing for another topic
What is the differnece in singing style of Beyonce and Bill Gates? 
    * it will have no information about BIll Gates singing style
    1. Can use: Langchain MultiQuery Retrieval which will split the question into multiple small questions
    2. Can use: Maximal Marginal Relevance
2. Meta questions
3. Too much data
* Cluster the RAG data (Voronoi clustering)
> find some segments of the data > ask only cluster centroids if they are close to the question > only search all documents in top X clusters



# LLM in HR
Few shot learnings - give a number of example > output as a prompt to the LLM and then give the actual task
Use few-shot learning to generate synthetic data
For evaluation it uses a specificly trained LLM (Cross-encoder) that checks if the question and answer talk about the same
