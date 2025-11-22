

# 📄 Evaluation & Design Summary

This document explains the design decisions behind the **Trigram Language Model** implementation and the steps required to test and validate it.

## 1. Problem Understanding

The assignment requires building a **Trigram Language Model** that:

* Learns word sequences from raw text
* Computes next-word probabilities using (w1, w2) → w3 mappings
* Generates text using learned distributions
* Passes a unit test suite
* Is clean, modular, and easy to understand

## 2. Key Design Decisions

### 2.1 Data Structures

| Structure                                  | Purpose                            |
| ------------------------------------------ | ---------------------------------- |
| `trigram_counts = {(w1, w2): {w3: count}}` | Stores trigram frequencies         |
| `bigram_counts = {(w1, w2): total_count}`  | Used for probability normalization |
| `vocab = set()`                            | Tracks unique words                |

---

### 2.2 Text Preprocessing

* Lowercasing
* Removing punctuation
* Splitting into tokens
* Padding text using:

  ```
  <s>, <s>, ..., </s>
  ```

This ensures a valid trigram context even for the first two words.

---

### 2.3 Probability Sampling

Used:

```python
random.choices(words, probs)
```

Reason:

* Built-in weighted sampling
* Simple, clean, maintainable
* Avoids manually implementing cumulative probability logic

---

### 2.4 Edge Case Handling

The model must return an empty string if trained on empty text.
To satisfy the test suite:

#### In `fit()`:

```python
if not text.strip():
    self.trigram_counts = {}
    self.bigram_counts = {}
    self.vocab = set()
    return
```

#### In `generate()`:

```python
if len(self.trigram_counts) == 0:
    return ""
```

This ensures the model does not produce meaningless `<s>` tokens.

---

### 2.5 Modularity

* `ngram_model.py` → all model logic
* `generate.py` → script to train & generate
* `tests/test_ngram.py` → independent test suite
* Added `__init__.py` & `conftest.py` for reliable imports

The code is structured for clarity and simplicity.

---

## 3. Testing Steps

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest -q tests/test_ngram.py
```

Run generator:

```bash
python src/generate.py
```

All tests pass (`3 passed`).


