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
---
### 2. 🐍 Python — With Buffering  

- Reads files with **explicit buffering** (`buffering=1024*1024`) when opening files.  
- Processes the file line by line instead of loading the whole file.  
- More efficient for **large files** because it reduces I/O overhead.  
- Uses `matplotlib` to generate histogram plots.  

**Install dependencies:**  
```bash
pip install -r requirements.txt

---

### 3. ⚡ C++ — Multithreaded Version  

- Implements **parallel word counting** using C++ threads.  
- Each thread processes a chunk of the file independently.  
- Local word counts are stored in thread-local maps, then safely merged into a global map using a `mutex`.  
- Sorting is done after merging to get the **top 50 most frequent words**.  
- Significantly faster than Python versions for **very large datasets** due to compiled performance and concurrency.  

**Compile & Run:**  
```bash
g++ -O2 -std=c++17 -pthread cpp_wordcount.cpp -o cpp_wordcount
./cpp_wordcount file1.txt file2.txt file3.txt
