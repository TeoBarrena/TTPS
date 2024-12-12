
"""
Input
The input will consist on an arbitrary number of city sequence pairs. The end of input occurs when the
first sequence starts with an ‘#’ character (without the quotes). Your program should not process this
case. Each travel sequence will be on a line alone and will be formed by legal characters (as defined
above). All travel sequences will appear in a single line and will have at most 100 cities.

Output
For each sequence pair, you must print the following message in a line alone:
Case #d: you can visit at most K cities.
Where d stands for the test case number (starting from 1) and K is the maximum number of cities
you can visit such that you’ll satisfy both you father’s suggestion and you mother’s suggestion.

Sample Input
abcd
acdb
abcd
dacb
#

Sample Output
Case #1: you can visit at most 3 cities.
Case #2: you can visit at most 2 cities."""

#include <iostream>
#include <vector>
#include <string>
using namespace std;

int get_lcs(const string& string_1, const string& string_2, int idx) {
    int n = string_1.size() + 1;  // filas
    int m = string_2.size() + 1;  // columnas

    // init en 0 la matriz dp
    vector<vector<int>> dp(n, vector<int>(m, 0));

    for (int i = 1; i < n; i++) {
        for (int j = 1; j < m; j++) {
            if (string_1[i - 1] == string_2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]); //agarras el max entre el que esta a su izq, y el que esta arriba 
            }
        }
    }

    
    cout << "Case #" << idx << ": you can visit at most " << dp[n - 1][m - 1] << " cities." << endl;

    return dp[n - 1][m - 1];
}

int main() {
    vector<string> list_seqs;
    string line;

    
    while (getline(cin, line)) {
        if (line == "#") {
            break;
        }
        list_seqs.push_back(line);
    }

    
    int idx = 1;
    for (size_t i = 0; i < list_seqs.size(); i += 2) {
        
        string seq1 = list_seqs[i];
        string seq2 = list_seqs[i + 1];
        get_lcs(seq1, seq2, idx);
        idx++;
        
    }

    return 0;
}
