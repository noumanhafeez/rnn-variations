# 🔄 Recurrent Neural Networks (RNN) - Easy Explanation

---

## 🔹 What is RNN?

A **Recurrent Neural Network (RNN)** is a type of neural network designed for **sequential data** like:

- Text  
- Time series  
- Speech  
- Videos  

### Key Idea:
RNNs **remember previous information** using a **hidden state** while processing a sequence.

---

## 🔹 Why do we need RNNs?

Normal neural networks (like CNNs or Feedforward) **cannot remember past inputs**.  

- Example: Predicting next word in a sentence  
  - Input: "I am going to the"  
  - Output: "market"  
  - **Feedforward NN** has no memory → cannot know the previous words  
  - **RNN** remembers previous words → can predict correctly ✅  

---

## 🔹 Types of RNN Architectures

### 1️⃣ One-to-One

- Input: Single value  
- Output: Single value  
- **Same as a normal neural network**  

**Example:** Predict house price from features

---

### 2️⃣ One-to-Many

- Input: Single value  
- Output: Sequence of values  

**Example:** Generate a **sequence of notes** from a single chord

---

### 3️⃣ Many-to-One

- Input: Sequence of values  
- Output: Single value  

**Example:** Sentiment analysis (sequence of words → positive/negative)  

---

### 4️⃣ Many-to-Many

- Input: Sequence  
- Output: Sequence  

**Example:**  
- Machine Translation: English sentence → French sentence  
- Video classification: sequence of frames → sequence of labels  

---

## 🔹 Feedforward in RNN (Forward Pass)

### Step by Step:

1. Input at time t → combined with **previous hidden state**  
2. Compute new hidden state:  h_t = activation(W * x_t + U * h_{t-1} + b)
3. Output at time t (if needed) →  y_t = activation(V * h_t + c)


### Analogy:

- Think of writing a story  
- Each word depends on **previous words**  

---

## 🔹 Backpropagation in RNN (Backward Pass)

- Called **Backpropagation Through Time (BPTT)**  
- Gradients are computed **for each timestep**  
- Weights are updated using an optimizer (SGD, Adam, etc.)  

### Analogy:

- Teacher corrects your story **word by word**, considering the previous context  
- Model adjusts to reduce mistakes over time  

---

## 🔹 Problems with Vanilla RNNs

1. **Vanishing Gradients**  
   - Gradients become very small → network forgets long-term dependencies  
2. **Exploding Gradients**  
   - Gradients become too large → unstable learning  

---

## 🔹 LSTM (Long Short-Term Memory)

### Why LSTM?

- Solves **vanishing gradient problem**  
- Can **remember long-term dependencies**  

### Structure:

- **Cell State (C_t):** long-term memory  
- **Gates:** control flow of information  
  - Forget Gate → decide what to forget  
  - Input Gate → decide what new info to add  
  - Output Gate → decide what to output  

### Analogy:

- LSTM = smart student  
  - Remembers important things  
  - Forgets unimportant things  

**Example:** Predict next word in a long paragraph  

---

## 🔹 GRU (Gated Recurrent Unit)

### Why GRU?

- Simplified version of LSTM  
- Combines forget + input gate into **update gate**  
- Faster to train, fewer parameters  

**Example:** Similar tasks as LSTM, but when you need **speed over complexity**  

---

## 🔹 Key Differences: RNN vs LSTM vs GRU

| Model | Can remember long-term? | Complexity | Speed | Use case |
|-------|------------------------|------------|-------|----------|
| Vanilla RNN | ❌ Short-term | Low | Fast | Simple sequences |
| LSTM | ✅ Long-term | High | Medium | Text, Speech, Time series |
| GRU | ✅ Long-term | Medium | Fast | Similar to LSTM, smaller datasets |

---

## 🔹 Advantages of RNNs / LSTMs / GRUs

- Handle **sequential data** naturally  
- Can capture **context & temporal dependencies**  
- LSTM/GRU solve vanishing gradient problem  

---

## 🔹 Disadvantages

- Vanilla RNN → vanishing/exploding gradients  
- LSTM/GRU → computationally heavy  
- Hard to parallelize (sequential processing)  

---

## 🔹 Summary / Cheat Sheet

1. RNN → remembers short-term context  
2. LSTM → remembers long-term context using gates  
3. GRU → simpler & faster version of LSTM  
4. Architectures:  
   - One-to-One → single input/output  
   - One-to-Many → single input, sequence output  
   - Many-to-One → sequence input, single output  
   - Many-to-Many → sequence input, sequence output  
