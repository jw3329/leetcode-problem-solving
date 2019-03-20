class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& M) {
        vector<vector<int>> res;
        int m = M.size();
        int n = M[0].size();
        
        for(int i=0;i<m;i++) {
            vector<int> row_vec;
            for(int j=0;j<n;j++) {
                row_vec.push_back(searchAround(M,i,j));
            }
            res.push_back(row_vec);
        }
        return res;
    }
    
    int searchAround(vector<vector<int>> &M, int i, int j) {
        int check[] = {-1,0,1};
        int sum = 0;
        int floor = 0;
        for(int x=0;x<3;x++) {
            for(int y=0;y<3;y++) {
                int x_try = i + check[x];
                int y_try = j + check[y];
                if(inConstraint(M,x_try,y_try)) {
                    floor++;
                    sum += M[x_try][y_try];
                }
            }
        }
        return sum / floor;
    }
    
    bool inConstraint(vector<vector<int>> &M, int x, int y) {
        return x >= 0 && x < M.size() && y >= 0 && y < M[0].size();
    }
};
