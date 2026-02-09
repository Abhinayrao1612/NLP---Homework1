# nlp-assignment-regex-bpe

NLP assignment covering **regular expressions, Byte Pair Encoding (BPE), Bayes Rule, add-one smoothing, and tokenization**.

---

## Student Information

- **Name:** Abhinay Rao Gandra
- **Student ID:** 700777303

---

## Repository Structure

### `Question Regex`

**Explanation**  
This file contains solutions to all the assigned regular expression problems.  
Each regular expression is clearly written and accompanied by a short explanation describing its purpose and behavior.

---

### `Q2.Manual BPE on a toy corpus `

**Explanation**  
This file walks through the **manual Byte Pair Encoding (BPE)** process using a toy corpus.  
It demonstrates how end-of-word markers are added, how the most frequent character pairs are merged step by step, and how the vocabulary evolves after each merge.

---

### `Q3. Bayes Rule Applied to Text`

**Explanation**  
This file explains **Bayes Rule in the context of text classification**.  
It defines prior, likelihood, and posterior probabilities and explains why the denominator term can be ignored when comparing classes.

---

### `Q4. Add-1 Soothing`

**Explanation**  
This file covers **add-one (Laplace) smoothing** with a worked example.  
It shows how the smoothed denominator is calculated and how probabilities are assigned to words in the negative class, including words that do not appear in training data.

---

### `tokenization.py`

**Explanation**  
This Python file demonstrates different **tokenization techniques** for a short paragraph.  
It compares naïve space-based tokenization, manually corrected tokenization, and tokenization using an NLP tool.

---

### `Q5. Programming Question`

**Explanation**  
This file contains the remaining parts of the tokenization question, including:
- Identification of **Multiword Expressions (MWEs)**
- A short **reflection** on tokenization challenges

---

## How to Run the Code

### tokenization code
```bash
python tokenization.py
