# LLM Reasonanig | Murray Campbell, IBM T. J. Watson Research Center
What is reasoning
* use known facts
* employ reasoning
* derive new facts

Types of reasoning
* inductive
* deductive
* abductive (my car didn't star, brainstorm why)

Why is reasoning important
1. search
* go through a step of possible options and pick the best
* LLMs can do well if they have seen the problem before or if the number of steps is small (3)
2. data efficient learning
* learn grammar
    * aa
    * aabb
    * aaaabbbb
    * a^n b^n
* learn a shift cipher
    * move a by x positions. Find what x is 
* learn a rule
    * 1, 2, 4, 8, 16 ... 32
3. abstraction
4. explainable decision
5. verifiable decision
6. knowledge integration

How to test if LLMs can reason:
* Train on a task, give it a different/similar task
* Train on a task, randomize the steps of the same task and test
* give LLMs problems it can solve but give it different names/words

Do LLMs need to reason?
* in memorization, pattern matching or shortcuts can substitute for reasoning

How to improve reasoning of LLMs:
1. scale
 * improves empirical performance on reasoning tasks but not unlikely to generalize
2. prompting
 * chain of thoughts
3. multi-agent based system
 * specilized agents for each task

How can we measure progress in reasoning
* testing tasks must not be in the training data

# Enhancing Semantic Search: A Case Study on Fine-tuning with Noisy Data | Barbora Rišová, Seznam.cz
Traditional approach - term search
New approach - vector search
Often there are no clear clusters
We can deal with it usiing contrastive learning


# Supercharging Recommendation Systems with Large Language Models | Amey Dharwadker, Meta


# Practical LLM Fine-Tuning For Semantic Search
nixiesearch https://github.com/nixiesearch/nixiesearch


document > embedding > similarity (cosine)




# Translating Mobile Network Signals to Roads with Transformers
gps data > cell towers
gps data is translated into road segments (90k)


90k segments > decoder > decoder