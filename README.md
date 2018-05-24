# Sentence-Selection-For-Question-Answering
NLP&amp;SSL Project

## Introduction
Sentence selection is an important subtask of the QA (question answering) problem.  
The objective of this project is to identify the sentence from a large text or paragraphs,
that contains the correct answer for a given question.


## Steps to follow
1. Clone or download the project;
2. Create the folder `./data/squad/`;
3. Copy the [train and dev set of SQuAD][1] in `./data/squad/`;
4. Run the kernel `./src/data_preprocessing.ipynb`;  
   After this step, in `./data/squad/` will be created the following files:
    * _train-v1.1-preprocessed.json_;
    * _dev-v1.1-preprocessed.json_;  
5. Run the kernel `./src/baseline.ipynb`.  
   Here are the first results using simple approaches.
6. Create the folder `./word_embeddings/`;  
   Download and copy in this folder pretrained word embeddings: https://code.google.com/archive/p/word2vec/
   Run the kernel `./src/classification.ipynb`.  
   Here are the results using LogisticRegression for pretrained word embeddings.
6. Run the kernel `./src/bm25.ipynb`.  
   Here are the results using bm25 ranking function.
8. Run the kernel `./src/combined_methods.ipynb`.  
   Here are the last results using a combination of previous methods.


## Datasets
I use the [SQuAD (Stanford Question Answering Dataset)][1] - a reading comprehension dataset.  
An eda of the SQuAD can be found here `./eda/squad_dataset_v_1_1.ipynb`.  




[1]: https://rajpurkar.github.io/SQuAD-explorer/

