---
This project implements a **Trigram Language Model** as part of the AI/ML Intern assignment. 
The objective is to build a clean, modular, and testable system using core Python skills.

---

# Installation 

## **1) Create a virtual environment**

```bash
python -m venv venv
```

---

## **2) Activate it**

### **→ Windows PowerShell**

```bash
.\venv\Scripts\Activate.ps1
```

### **→ CMD**

```bash
.\venv\Scripts\activate.bat
```

---

## **3) Install dependencies**

```bash
pip install -r requirements.txt
```

---

# Running the Trigram Model 

### Train the model + generate text:

```bash
python src/generate.py
```

### This will:

1. Load `data/example_corpus.txt`
2. Train the trigram model
3. Generate text based on learned probabilities

---

# Running Tests 

### Unit tests are located in:

```
ml-assignment/tests/test_ngram.py
```

### Run all tests with:

```bash
pytest -q tests/test_ngram.py
```

### Expected output:

```
3 passed
```

---

# About the Model 

This implementation includes:

1. Text preprocessing
2. Tokenization
3. Start/end padding
4. Trigram counting
5. Probability calculation
6. Weighted random sampling (`random.choices`)
7. Clean generation stopping logic
8. Edge-case handling (especially empty text)

---
