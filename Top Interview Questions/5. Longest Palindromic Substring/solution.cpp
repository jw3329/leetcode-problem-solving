class Solution {
private:
    int low = 0;
    int max_length = 0;
public:
    string longestPalindrome(string s) {
        if(s.size() < 2) return s;
        for(int i=0;i<s.size()-1;i++) {
            // odd case
            checkPalindrome(s,i,i);
            // even case
            checkPalindrome(s,i,i+1);
        }
        return s.substr(low,max_length);
    }
    
    void checkPalindrome(string s, int i, int j) {
        while(i>=0 && j < s.size() && s[i] == s[j]) {
            i--;
            j++;
        }
        if(max_length < j - i - 1) {
            low = i+1;
            max_length = j - i - 1;
        }
    }
};
