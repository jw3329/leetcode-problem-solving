class Solution {
public:
    string countAndSay(int n) {
        if(n == 1) return "1";
        string previous_count = countAndSay(n-1);
        int count = 1;
        string res = "";
        for(int i=0;i<previous_count.size()-1;i++) {
            if(previous_count[i] == previous_count[i+1]) count++;
            else {
                res += to_string(count);
                res += previous_count[i];
                count = 1;
            }
        }
        res += to_string(count);
        res += previous_count[previous_count.size()-1];
        return res;
    }
};
