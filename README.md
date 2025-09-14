# WordCount Assignment

This project implements multiple versions of the **WordCount problem** (given m >> 0 text files, count the frequency of words, print the counts in non-increasing order, and create histograms of the top 50 words).  
One version also assesses the effect of buffering during file reads on performance.  

---

## 📌 Versions Implemented

### 1. Python (No Buffering)
- Reads entire file into memory at once.
- Uses `collections.Counter` for counting (C-optimized).
- Fastest pure Python approach (best for small–medium files).

Run:
```bash
python python_no_buffering.py
