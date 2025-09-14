from collections import Counter
import matplotlib.pyplot as plt
import time

def word_count_optimized(file_list, buffer_size=1024*1024, top_n=50):
    counts = Counter()
    start = time.time()
    for filename in file_list:
        try:
            with open(filename, "r", encoding="utf-8", errors="ignore", buffering=buffer_size) as f:
                for line in f:
                    line = line.lower()
                    clean_line = "".join(ch if ch.isalnum() else " " for ch in line)
                    counts.update(clean_line.split())
        except Exception as e:
            print(f"Error processing {filename}: {e}")
    end = time.time()
    print(f"Processed {len(file_list)} file(s) with buffer={buffer_size} in {end - start:.4f} sec")
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_counts[:top_n]
def plot_histogram(word_counts, title="Top 50 Words Frequency"):
    words, freqs = zip(*word_counts)
    plt.figure(figsize=(12, 6))
    plt.bar(words, freqs)
    plt.xticks(rotation=45)
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title(title)
    plt.show()
if __name__ == "__main__":
    files = ["/content/Copy of Nishafin.csv"]  # Works for txt and csv
    top_words = word_count_optimized(files, buffer_size=1024*1024, top_n=50)
    for word, count in top_words:
        print(f"{word} : {count}")
    plot_histogram(top_words, title="Buffered WordCount (Top 50)")
