# Sentence-Selection-For-Question-Answering
NLP&amp;SSL Project

## Introduction
Sentence selection is an important subtask of the QA (question answering) problem.  
The objective of this project is to identify the sentence from a large text or paragraphs,
that __*contains*__ the correct answer for a given question.


## Steps to follow
1. Clone or download the project;
2. Create the folder `./data/squad/`;
3. Copy the [train and dev set of SQuAD][1] in `./data/squad/`;
4. Run the kernel `./src/data_preprocessing.ipynb`.  
   After this step, in `./data/squad/` will be created the following files:
    * __*train-v1.1-preprocessed.json*__
    * __*dev-v1.1-preprocessed.json*__


## Datasets
I use the [SQuAD (Stanford Question Answering Dataset)][1] - a reading comprehension dataset.  
An eda of the SQuAD can be found here `./eda/squad_dataset_v_1_1.ipynb`.  




[1]: https://rajpurkar.github.io/SQuAD-explorer/

