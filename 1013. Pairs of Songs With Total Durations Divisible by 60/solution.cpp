class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        int c[60] = {};
        int res = 0;
        for(auto &t : time) {
            res += c[(60 - t % 60) % 60];
            c[t%60] += 1;
        }
        return res;
    }
};
