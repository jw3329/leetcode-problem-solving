class Solution {
public:
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        dfs(board,click[0],click[1]);
        return board;
    }
    
    void dfs(vector<vector<char>> &board, int x, int y) {
        if(board[x][y] == 'M') board[x][y] = 'X';
        if(board[x][y] != 'E') return;
        
        int check[] = {-1,0,1};
        int howMany = 0;
        for(int i=0;i<3;i++) {
            for(int j=0;j<3;j++) {
                int trialX = x + check[i];
                int trialY = y + check[j];
                if(inRange(trialX,trialY,board.size(),board[0].size()) 
                   && board[trialX][trialY] == 'M') howMany++;
            }
        }
        if(howMany) {
            board[x][y] = '0' + howMany;
            return;
        }
        board[x][y] = 'B';
        for(int i=0;i<3;i++) {
            for(int j=0;j<3;j++) {
                int trialX = x + check[i];
                int trialY = y + check[j];
                if(inRange(trialX,trialY,board.size(),board[0].size())) {
                    dfs(board,trialX,trialY);
                }
            }
        }
    }
    
    bool inRange(int x,int y,int n,int m) {
        return x >= 0 && x < n && y >= 0 && y < m;
    }
};