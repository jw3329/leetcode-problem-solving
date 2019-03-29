class Solution {
public:
    bool isMatch(string s, string p) {
        // set dp as 2d pointer
        bool **dp = new bool*[s.size() + 1];
        for(int i=0;i<=s.size();i++) {
            bool *sub = new bool[p.size()+1];
            dp[i] = sub;
        }
        // set dp value as all false
        for(int i=0;i<=s.size();i++) {
            for(int j=0;j<=p.size();j++) {
                dp[i][j] = false;
            }
        }
        // in case both text and pattern empty is true 
        dp[s.size()][p.size()] = true;
        for(int i=s.size();i>=0;i--) {
            for(int j=p.size()-1;j>=0;j--) {
                bool first_match = i < s.size() && (p[j] == s[i] || p[j] == '.');
                if(j + 1 < p.size() && p[j+1] == '*') {
                    dp[i][j] = dp[i][j+2] || (first_match && dp[i+1][j]);
                } else {
                    dp[i][j] = first_match && dp[i+1][j+1];
                }
            }
        }
        bool res = dp[0][0];
        // delete heap memory
        for(int i=0;i<=s.size();i++) {
            delete[] dp[i];
        }
        delete[] dp;
        return res;
    }
};
