This project implements a Trigram Language Model as part of the AI/ML Intern assignment.
The objective is to build a clean, modular, and testable system using core Python skills.


# Installation

## 1) Create a virtual environment
python -m venv venv

## 2) Activate it
## -> Windows PowerShell
.\venv\Scripts\Activate.ps1
## -> CMD
.\venv\Scripts\activate.bat

## 3) Install dependencies
pip install -r requirements.txt

# Running the Trigram Model
## Train model + generate text
python src/generate.py

# This will:
## -> Load data/example_corpus.txt
## -> Train the trigram model
## -> Generate text based on learned probabilities

# Running Tests
## Unit tests are located in:
ml-assignment/tests/test_ngram.py

## Run all tests with:
pytest -q tests/test_ngram.py

## You should see:
3 passed

# About the Model
## This implementation includes:

## -> Text preprocessing
## -> Tokenization
## -> Start/end padding
## -> Trigram counting
## -> Probability calculation
## -> Weighted random sampling (random.choices)
## -> Clean stopping logic
## -> Edge-case handling (empty text)