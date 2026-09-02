# 12-Month Artificial Intelligence Master's Preparation Roadmap

A 12-month roadmap designed to build a strong foundation in **programming, mathematics, machine learning, deep learning, NLP, and modern AI** before starting a Master's Degree in Artificial Intelligence Engineering.

The goal is not to learn everything about AI, but to develop the foundations and practical skills needed to enter the Master's program confidently.

---

# Month 1 — Python & Programming

## Goal

Stop thinking of programming as a barrier and become comfortable writing Python code.

## Topics

* [X] Variables and data types
* [X] `if / elif / else`
* [X] `for` and `while` loops
* [X] Functions
* [X] Lists, sets, tuples, and dictionaries
* [X] List comprehensions
* [X] Classes and objects
* [X] Exception handling
* [X] File reading and writings
* [X] Modules and packages
* [X] Virtual environments
* [X] Git & GitHub
* [X] Jupyter Notebooks

## Practice

Build small programs:

* [ ] Calculator
* [ ] Currency converter
* [ ] Number guessing game
* [ ] CSV file analyzer
* [ ] Simple task management system

Then start working with:

* [ ] NumPy
* [ ] Pandas
* [ ] Matplotlib

## Monthly Goal

Be able to take a dataset and:

**Read → Clean → Analyze → Visualize → Draw Conclusions**

---

# Month 2 — Linear Algebra & Calculus

This is where the mathematics that actually appears in AI starts to become important.

## Linear Algebra

Learn:

* [ ] Vectors
* [ ] Matrices
* [ ] Matrix operations
* [ ] Dot product
* [ ] Norms
* [ ] Transpose
* [ ] Inverse matrices
* [ ] Linear systems
* [ ] Eigenvalues and eigenvectors
* [ ] Linear transformations

You do not initially need to focus on highly abstract mathematical proofs.

The important part is understanding **why these concepts appear in Machine Learning**.

## Calculus

Learn:

* [ ] Functions
* [ ] Derivatives
* [ ] Partial derivatives
* [ ] Gradients
* [ ] Chain rule
* [ ] Minima and maxima
* [ ] Optimization

## Important Exercise

Implement **Gradient Descent using Python/NumPy without using a Machine Learning library**.

Understanding and implementing it is much more valuable than simply reading about it.

---

# Month 3 — Probability, Statistics & NumPy

Build the statistical foundation required for Machine Learning.

## Statistics & Probability

Study:

* [ ] Mean
* [ ] Median
* [ ] Variance
* [ ] Standard deviation
* [ ] Normal distribution
* [ ] Probability
* [ ] Conditional probability
* [ ] Bayes' theorem
* [ ] Random variables
* [ ] Expected value
* [ ] Correlation
* [ ] Covariance
* [ ] Sampling
* [ ] Confidence intervals

## NumPy

Become comfortable with:

* [ ] Arrays
* [ ] Shapes
* [ ] Broadcasting
* [ ] Matrix multiplication
* [ ] Vectorization

## Project

Take a real-world dataset and answer:

> "Which factors appear to be related to the outcome I want to predict?"

Do the entire analysis in Python.

---

# Month 4 — Machine Learning I

Now start getting into Artificial Intelligence properly.

## Supervised Learning

Learn:

* [ ] Linear Regression
* [ ] Logistic Regression
* [ ] K-Nearest Neighbors
* [ ] Decision Trees
* [ ] Random Forest
* [ ] Support Vector Machines (SVM)

## Fundamental Concepts

Understand thoroughly:

* [ ] Features
* [ ] Labels
* [ ] Training set
* [ ] Validation set
* [ ] Test set
* [ ] Loss functions
* [ ] Optimization
* [ ] Overfitting
* [ ] Underfitting
* [ ] Bias and variance

Most importantly, understand:

> **Why can a model with 99% training accuracy still be a bad model?**

---

# Month 5 — Machine Learning II

Start working seriously with **scikit-learn**.

## Machine Learning Workflow

```text
Dataset
   ↓
Exploration
   ↓
Preprocessing
   ↓
Train/Test Split
   ↓
Model
   ↓
Training
   ↓
Evaluation
   ↓
Hyperparameter Tuning
```

## Topics

* [ ] Pipelines
* [ ] Feature scaling
* [ ] Encoding categorical variables
* [ ] Handling missing values
* [ ] Cross-validation
* [ ] Grid Search
* [ ] Random Search

## Evaluation Metrics

### Classification

* [ ] Accuracy
* [ ] Precision
* [ ] Recall
* [ ] F1 Score
* [ ] ROC-AUC
* [ ] Confusion Matrix

### Regression

* [ ] MAE
* [ ] MSE
* [ ] RMSE
* [ ] R²

## Project

Build a complete prediction model.

Possible projects:

* [ ] House price prediction
* [ ] Customer churn prediction
* [ ] Spam email classification

Publish the project on GitHub.

---

# Month 6 — Machine Learning & Statistics in Depth

This month is about consolidation.

Instead of learning 20 more algorithms, start asking:

> **"Why does this model work?"**

## Topics

* [ ] Regularization
* [ ] L1 / L2 Regularization
* [ ] Gradient Descent
* [ ] Loss Functions
* [ ] Feature Engineering
* [ ] Dimensionality Reduction
* [ ] PCA
* [ ] Clustering
* [ ] K-Means
* [ ] Anomaly Detection

Start reading technical papers and tutorials.

## Project

Compare:

**Logistic Regression vs Random Forest vs SVM**

using the same dataset.

Explain:

* [ ] Which model performed best
* [ ] Why it performed best
* [ ] Model limitations
* [ ] Evaluation metrics used
* [ ] Whether overfitting occurred

The goal is to start developing the type of technical reasoning required in a Master's program.

---

# Month 7 — Deep Learning I

Now move into **PyTorch** and neural networks.

## Topics

Learn:

* [ ] Perceptrons
* [ ] Neural networks
* [ ] Layers
* [ ] Activation functions
* [ ] Forward propagation
* [ ] Backpropagation
* [ ] Loss functions
* [ ] Optimizers
* [ ] Epochs
* [ ] Batch size
* [ ] Learning rate

Then study:

* [ ] ReLU
* [ ] Sigmoid
* [ ] Softmax
* [ ] Cross-entropy
* [ ] SGD
* [ ] Adam

## Project

Build a neural network for image classification using **PyTorch**.

### Example

**MNIST**

Start with a simple implementation and then try to improve its performance.

---

# Month 8 — Deep Learning II

Take Deep Learning to the next level.

## Convolutional Neural Networks

Learn:

* [ ] Convolution
* [ ] Filters
* [ ] Pooling
* [ ] Feature maps
* [ ] CNN architectures

## Additional Concepts

* [ ] Dropout
* [ ] Batch normalization
* [ ] Learning rate scheduling
* [ ] Data augmentation
* [ ] Transfer learning

Then learn the concept of:

**Embeddings**

Start understanding how neural networks transform information into meaningful mathematical representations.

## Project

Build an image classifier using:

**PyTorch + CNN + Transfer Learning**

---

# Month 9 — NLP & Transformers

One of the most important months for understanding modern AI.

## Natural Language Processing

Learn:

* [ ] NLP fundamentals
* [ ] Tokenization
* [ ] Vocabulary
* [ ] Embeddings
* [ ] RNNs
* [ ] LSTMs
* [ ] Attention
* [ ] Self-Attention
* [ ] Transformers

## Transformer Architecture

Understand conceptually:

```text
Input
 ↓
Tokens
 ↓
Embeddings
 ↓
Self-Attention
 ↓
Transformer Layers
 ↓
Output
```

Finally, understand:

> **How are Large Language Models (LLMs) related to Transformers?**

You do not need to build ChatGPT.

However, you should understand **how a Transformer works at both a conceptual and mathematical level**.

---

# Month 10 — Applied AI

At this point, start exploring different AI specializations.

It is recommended to experiment with **two or three areas** before deciding which direction interests you most.

## Option A — Computer Vision

* [ ] CNNs
* [ ] Object detection
* [ ] Image segmentation
* [ ] Image classification

## Option B — NLP

* [ ] Embeddings
* [ ] Transformers
* [ ] Text classification
* [ ] Semantic search
* [ ] Retrieval-Augmented Generation (RAG)

## Option C — Reinforcement Learning

* [ ] States
* [ ] Actions
* [ ] Rewards
* [ ] Policies
* [ ] Value functions
* [ ] Q-Learning

## Option D — Generative AI

* [ ] LLMs
* [ ] Embeddings
* [ ] Vector databases
* [ ] RAG
* [ ] Fine-tuning
* [ ] Inference

## Projects

Build **at least one small project in two different areas**.

---

# Month 11 — The Capstone Project

This is probably the most important month.

Choose a real-world problem and build an **end-to-end AI project**.

## Example — AI Research Assistant

```text
PDFs
 ↓
Text Extraction
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector Database
 ↓
Retriever
 ↓
LLM
 ↓
Answer with Sources
```

## Alternative — Computer Vision

Build a system that receives an image and classifies or detects objects.

## Alternative — NLP

Build a system that automatically classifies documents.

## Project Requirements

The project should include:

* [ ] GitHub repository
* [ ] Professional README
* [ ] Clean and organized code
* [ ] Dataset
* [ ] Methodology
* [ ] Results
* [ ] Evaluation metrics
* [ ] Visualizations
* [ ] Limitations
* [ ] Possible improvements

> **Do not build just a 50-line notebook.**

The goal is to enter the Master's program already comfortable with building complete AI systems.

---

# Month 12 — Master's Preparation

This month is different.

Do not try to learn another 50 concepts.

Focus on **consolidating everything you have learned**.

## Python

* [ ] NumPy
* [ ] Pandas
* [ ] Object-Oriented Programming
* [ ] Git

## Mathematics

* [ ] Linear algebra
* [ ] Derivatives
* [ ] Gradients
* [ ] Probability
* [ ] Statistics

## Machine Learning

* [ ] Regression
* [ ] Decision trees
* [ ] SVM
* [ ] Clustering
* [ ] Regularization
* [ ] Model evaluation

## Deep Learning

* [ ] Neural networks
* [ ] Backpropagation
* [ ] CNNs
* [ ] Embeddings
* [ ] Attention
* [ ] Transformers

---

# Final Goal

By the end of these 12 months, the goal is to have a strong foundation across:

```text
                 ARTIFICIAL INTELLIGENCE
                          │
           ┌──────────────┴──────────────┐
           │                             │
     Mathematics                    Programming
           │                             │
     ┌─────┴─────┐                  Python / Git
     │           │
Linear Algebra  Statistics
     │           │
     └─────┬─────┘
           │
     Machine Learning
           │
     ┌─────┴─────┐
     │           │
 Classical   Deep Learning
    ML            │
              ┌───┴────┐
              │        │
             CNN   Transformers
              │        │
        Computer     NLP / LLMs
         Vision
```

More importantly, you should be able to:

> **Take a problem you have never seen before, research what you need, understand the relevant concepts, and build a working solution.**

That skill is more valuable than memorizing algorithms.

---

# Suggested Weekly Schedule

A good target is approximately **10–12 hours per week**.

| Day       | Activity                | Time |
| --------- | ----------------------- | ---: |
| Monday    | Theory                  | 1.5h |
| Tuesday   | Programming             | 1.5h |
| Wednesday | Mathematics             | 1.5h |
| Thursday  | Programming / Exercises | 1.5h |
| Friday    | Rest                    |    — |
| Saturday  | Project                 |   3h |
| Sunday    | Review / Project        |   2h |

**Total: ~11 hours/week**

You can adjust this depending on your schedule.

---

# Recommended Learning Ratio

Aim for:

**30% Theory
70% Practice**

For every concept you learn:

```text
Learn
  ↓
Understand
  ↓
Implement
  ↓
Experiment
  ↓
Make mistakes
  ↓
Fix them
  ↓
Document what you learned
```

For example, when learning Gradient Descent:

**Do not:** Watch three hours of videos about Gradient Descent.

**Do:** Understand the mathematics → implement it with NumPy → experiment with different learning rates → visualize the loss → analyze the results.

---

# Suggested Project Progression

Throughout the 12 months, aim to build approximately:

## Months 1–3

**3–5 small projects**

Focus on Python, data manipulation, mathematics, and visualization.

## Months 4–6

**2 Machine Learning projects**

Focus on classical ML and model evaluation.

## Months 7–8

**1–2 Deep Learning projects**

Focus on PyTorch and neural networks.

## Months 9–10

**1 Transformers / Generative AI project**

Explore modern AI architectures.

## Months 11–12

**1 major capstone project**

Build something substantial, well-documented, and suitable for showcasing your skills.

---

# End Goal

By the time the Master's program starts, you should not simply be able to say:

> *"I studied Artificial Intelligence for a year."*

You should be able to show:

* [ ] Strong Python fundamentals
* [ ] Solid mathematical foundations
* [ ] Machine Learning knowledge
* [ ] Deep Learning experience
* [ ] Understanding of Transformers and modern AI
* [ ] Experience working with real datasets
* [ ] Multiple GitHub projects
* [ ] One substantial end-to-end AI project
* [ ] The ability to learn independently

**The objective is to arrive at the Master's program ready to learn — not starting from zero.**
