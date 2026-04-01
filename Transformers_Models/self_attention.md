# Self-Attention

## NLP -> Word sentences -> convert to numbers -> known as vectorization.

## Vectorization is simply define as conversion of word sentences to numbers.

## There are multiple ways of convert word sentences to numbers.

### 1. OHE
### 2. BOW
### Words embedding (TF-IDF), which is most advance. It's also add semantics meaning of words.


## Static embedding where weights are static. Means, you will train embedding on data once, then use them multiple times instead of again train embedding. This is the problem that could 
## lead to bias output.

## Dynamic embedding (contextual embedding know as self attention) are dynamic. Means, some calculations happens in contextual embedding box and then use them for predict task.

## Now, let's talk about calculations happening inside self attention box.

### let's first start with example:
### 1. Money bank grows                           
### 2. River bank flows

### In both sentence, the word bank have difference meanings.

### So, for first sentence, bank can be represent as: 0.3money+0.7bank+0.1grows
### For second sentence, bank can be represent as: 0.5river+0.4bank+0.1grows

### Then, it pass to softmax and then pass to final vector then finally, contextually embeddings of sentence will generated.

### Point to be considered:
### 1. There is no learning parameters involved in this
### 2. The dot product of matrix between softmax and vector is in parallel.

## There are two types of self-attention model
### 1. General self-attention
### 2. Task specific self-attention

### In some case, task specific self-attention perform well as compared to general self-attention

### In general self-attention model, there is no learning parameters, means, general self-attention sometime can predict wrong sentence.
### So, to overcome this issue, task specific self-attention model came. In this, weights and bias will initialize to learn parameters from data,
### which will help to improve better accuracy.

## Also matrix multiplication operations happening between matrix in parallel and called as scaled dot product attention in task specific self-attention