# Active learning

Repo: https://github.com/fkabs/mlprague_2024

An iterative process that takes some samples of the predicted data (based on sampling strategy) and asks a human to review the data. The human provides an answer and the decision boundary can be adjusted.

When to use:
* when you have only a small number of sampled data. 
* can be on command line during training


Example:
1. Unlabeled data > random sample > label > train a model
2. Find cases close to decision boundary > label > retrain


# ------------------------------------------------------------------------
Process:
1. Train on small subset of labeled data
2. Predict on unseen/unlabeled data > take X of least certain data 
3. Add to labeled data > retrain
4. Evaluate the model
5. Continue to 1. if needed

Sampling:
https://robertmunro.com/Uncertainty_Sampling_Cheatsheet.pdf
1. Uncertainty sampling
* we pick data where the model is most uncertain about and use human
* approaches:
    1. least confidence sampling - select most uncertain cases
    2. margin of confidence - take the smallest difference between the top two highest probabilities for each label
    3. ratio of confidence - take the smallest ratio between the top two highest probabilities for each label
    4. entropy - take the smallest entropy  

2. Diversity sampling
* pick a cluster and select data that are not part of any cluster
* approaches:
    1. model based - sample data outside of the model (like an item with a lowest activation function value)
    2. cluster based
        - take a random sample from each cluster and label
        - take a centroid of the cluster and label
        - take an outlier (part of a cluster but furthest from a cluster) and label
    3. representative sampling - find a sample of unlabeled items, compare to target domain
    4. sampling for real-world diversity - 

## New methods

### Semi-supervise learning
1. Select small amount of labeled data
2. Train a model
3. Take a lot of unlabeled data
4. Make prediction > take the most confident data
5. Add to labels
6. go back to 2.

### Effcient supervised learning
One-shot learning
* 
Few-shot learning
Zero-shot learning
* 


Ideas: 
* Could start with a dummy model prediction one category and update continuously. 
* Take some reasonable/good quality samples (even if smaller) and build a model 