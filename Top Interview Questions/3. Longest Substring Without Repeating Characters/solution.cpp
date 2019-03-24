class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.empty()) return 0;
        unordered_map<char,int> char_map;
        int max_len = 0;
        for(int i=0, j=0;i<s.size();i++) {
            if(char_map.find(s[i]) != char_map.end()) {
                j = max(j,char_map[s[i]] + 1);
            }
            char_map[s[i]] = i;
            max_len = max(max_len,i-j+1);
        }
        return max_len;
    }

};
