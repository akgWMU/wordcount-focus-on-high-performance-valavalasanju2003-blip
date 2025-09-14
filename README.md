# WordCount Assignment

This project implements multiple versions of the **WordCount problem**:  
Given *m* ≫ 0 text files, count the frequency of words, print the counts in non-increasing order, and create histograms of the top 50 words.  
One version also assesses the effect of buffering during file reads on performance.

---

## 📌 Versions Implemented

### 1. 🐍 Python (No Buffering)
- Reads the entire file into memory at once.
- Uses `collections.Counter` for counting (C-optimized).
- Fastest pure Python approach (best for small–medium files).

**Run:**
```bash
python python_no_buffering.py
```

---

### 2. 🐍 Python — With Buffering
- Reads files with **explicit buffering** (`buffering=1024*1024`) when opening files.
- Processes the file line by line instead of loading the whole file.
- More efficient for **large files** because it reduces I/O overhead.
- Uses `matplotlib` to generate histogram plots.

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run:**
```bash
python python_buffered.py
```

---

### 3. ⚡ C++ — Multithreaded Version
- Implements **parallel word counting** using C++ threads.
- Each thread processes a chunk of the file independently.
- Local word counts are stored in thread-local maps, then safely merged into a global map using a `mutex`.
- Sorting is done after merging to get the **top 50 most frequent words**.
- Significantly faster than Python versions for **very large datasets** due to compiled performance and concurrency.

**Build:**
```bash
g++ -std=c++17 -pthread -O3 wordcount_multithreaded.cpp -o wordcount_mt
```

**Run:**
```bash
./wordcount_mt <input_file1> <input_file2> ...
```

---

## 📊 Output

- **Word counts** are printed in non-increasing order.
- **Histogram** of the top 50 words is generated (Python versions).

---

## 📝 Notes

- For best performance, use the C++ version on very large datasets.
- Python buffered version is recommended for files that do not fit in memory.
- All scripts assume UTF-8 encoded text files.

---

## 📂 Project Structure

```
.
├── python_no_buffering.py
├── python_buffered.py
├── wordcount_multithreaded.cpp
├── requirements.txt
└── README.md
```

---

## 📦 Requirements

- Python 3.8+
- C++17 compiler (e.g., g++)
- `matplotlib` (for Python histogram plots)

---

## 🚀 Quick Start

1. **Clone the repo:**
    ```bash
    git clone <repo-url>
    cd wordcount-focus-on-high-performance-valavalasanju2003-blip
    ```

2. **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run your desired version as shown above.**

---

Happy Counting!
