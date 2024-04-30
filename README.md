Notes from ML Prague conference 22 to 24.4.2024.


Summary of topics:

### Can LLM reason?
 * Deductive/Inductive/Abductive
 * Reasoning requires some abstraction


Deductive prompt
```
Complete this argument:

French cars have faulty engines. 
I own a french car
Therefore, my car has <complete>
```

Inductive prompt 
```
Complete the argument:

90% of cyclists who complete training program ABC go to ride Tour de France.
Piere completed training program ABC.
Therefore, Piere will  <complete>
```

Abductive reasoning
```
My egine didnt start in the morning, list reasons why
```


#### Abstraction
Prompt
```
Complete the next step in this sequence:

ab
aabb
aaaabbbb
```

Answer
```
Certainly! Let’s analyze the given sequence:

ab: This sequence consists of alternating letters ‘a’ and ‘b’. To continue the pattern, we add another ‘a’ and ‘b’, resulting in ‘aaabbb’.
aabb: Here, we have two 'a’s followed by two 'b’s. To extend the sequence, we add another pair of 'a’s and 'b’s, giving us ‘aaaabbbb’.
aaaabbbb: Continuing the trend, we add one more ‘a’ and ‘b’ to get ‘aaaaabbbbb’.
So, the next term in the sequence is ‘aaaaabbbbb’. If you have any more sequences or questions, feel free to ask! 😊
```


Example of LLM reasoning Ceasar Cipher https://en.wikipedia.org/wiki/Caesar_cipher. LLM can decipher known ciphers (like the one from Wiki) but unable to generalize. It can complete single steps if prompted. 

Prompt:

```
Knowing this information:

In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code, or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.[1]

The encryption step performed by a Caesar cipher is often incorporated as part of more complex schemes, such as the Vigenère cipher, and still has modern application in the ROT13 system. As with all single-alphabet substitution ciphers, the Caesar cipher is easily broken and in modern practice offers essentially no communications security.

Decipher this cipher:
QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD
```


Prompt:
```
Knowing this information:

In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code, or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.[1]

The encryption step performed by a Caesar cipher is often incorporated as part of more complex schemes, such as the Vigenère cipher, and still has modern application in the ROT13 system. As with all single-alphabet substitution ciphers, the Caesar cipher is easily broken and in modern practice offers essentially no communications security.

'Qlaxv fp Qrbpaxv'
```

Prompt:
```
Write a python code that will cipher text using this method
```

Prompt:
```
Write a python code that will be able to decipher using this cipher method. The function should detect any shift.

Knowing this information:

In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code, or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.[1]

The encryption step performed by a Caesar cipher is often incorporated as part of more complex schemes, such as the Vigenère cipher, and still has modern application in the ROT13 system. As with all single-alphabet substitution ciphers, the Caesar cipher is easily broken and in modern practice offers essentially no communications security.
```


This is where an agent based system like langchain might be useful https://www.langchain.com/. This is a tool that combines some set steps and uses LLMs to perform specific operatons within these steps. <show langchain app>

Use analysis from https://www.kaggle.com/code/priy998/imdb-sqlite/notebook and compere to LLM:
prompts: 
`Check how many movies are present in iMDB`
`Find all directors with name starting with Steven`


### Finding new planets 
Methods:
* 30 pixes pro star https://www.google.com/search?sca_esv=a44e7edcd40cf9fd&sxsrf=ACQVn09TTF7sraAl23gp9zhKWDUp0iQVKg:1714457386103&q=kepler+telescope+image+of+a+star&tbm=isch&source=lnms&prmd=ivnbz&sa=X&ved=2ahUKEwiRm-y7o-mFAxWn7LsIHU3yAqYQ0pQJegQICBAB&biw=1344&bih=942&dpr=1&safe=active&ssui=on#imgrc=X169fF9wZ1TbBM 
* measure changes in brightness of a star
* birghness is folded based on periodicity of the brighness changes https://www.nasa.gov/missions/kepler/new-deep-learning-method-adds-301-planets-to-keplers-total-count/ 

Take data labeled by statistical method and train a ML model. 


### Map cell tower data to road segments
Use info about cell tower connections to gps to road segments. Using labeled data from a fleet of vehicles with GPS signal. 

Example: https://dataclair.ai/case-study/optimization-for-outdoor-campaigns 
