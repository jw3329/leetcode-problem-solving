class Solution {
public:
    int matrixScore(vector<vector<int>>& A) {
        int m = A.size();
        int n = A[0].size();
        int res = (1 << (n-1)) * m;
        for(int j=1;j<n;j++) {
            int cur = 0;
            for(int i=0;i<m;i++) {
                cur += A[i][0] == A[i][j];
            }
            res += max(cur,m-cur) * (1 << (n - j - 1));
        }
        return res;
    }
};
