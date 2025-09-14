#include <bits/stdc++.h>
#include <thread>
#include <mutex>
using namespace std;

unordered_map<string, int> global_counts;
mutex mtx;

void process_chunk(const string& text) {
    unordered_map<string, int> local_counts;
    string word;
    for (char c : text) {
        if (isalnum(c)) word += tolower(c);
        else if (!word.empty()) {
            local_counts[word]++;
            word.clear();
        }
    }
    lock_guard<mutex> lock(mtx);
    for (auto& [w, c] : local_counts) global_counts[w] += c;
}

int main() {
    ifstream file("file1.txt");
    stringstream buffer;
    buffer << file.rdbuf();
    string text = buffer.str();

    int n = thread::hardware_concurrency();
    vector<thread> threads;
    size_t chunk_size = text.size() / n;

    for (int i = 0; i < n; i++) {
        string chunk = text.substr(i * chunk_size, chunk_size);
        threads.emplace_back(process_chunk, chunk);
    }
    for (auto& t : threads) t.join();

    vector<pair<string, int>> result(global_counts.begin(), global_counts.end());
    sort(result.begin(), result.end(), [](auto& a, auto& b) {
        if (a.second == b.second) return a.first < b.first;
        return a.second > b.second;
    });

    for (int i = 0; i < 50 && i < result.size(); i++)
        cout << result[i].first << " : " << result[i].second << endl;
}
