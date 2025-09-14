from collections import Counter
import matplotlib.pyplot as plt
import time

def word_count_fast(file_list, top_n=50):
    counts = Counter()
    start = time.time()

    for filename in file_list:
        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read().lower()
            clean_text = "".join(ch if ch.isalnum() else " " for ch in text)
            counts.update(clean_text.split())

    end = time.time()
    print(f"Processed {len(file_list)} file(s) in {end - start:.4f} sec")

    # Sort: frequency desc, then alphabetically
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_counts[:top_n]

def plot_histogram(word_counts, title="Top 50 Words Frequency"):
    """Plot histogram of top word counts."""
    words, freqs = zip(*word_counts)
    plt.figure(figsize=(12, 6))
    plt.bar(words, freqs)
    plt.xticks(rotation=45)
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title(title)
    plt.show()
if __name__ == "__main__":
    files = ["Copy of Nishafin.csv"]

    top_words = word_count_fast(files, top_n=50)

    for word, count in top_words:
        print(f"{word} : {count}")

    plot_histogram(top_words, title="Fast WordCount (No Buffering)")
