class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        bool row[9] = {false}, col[9] = {false}, box[9] = {false};
        for(int i=0;i<9;i++) {
            for(int j=0;j<9;j++) {
                if(board[i][j] != '.') {
                    if(!checkRow(board,i,j,row) 
                       || !checkCol(board,i,j,col) || !checkBox(board,i,j,box)) return false;
                }
            }
        }
        return true;
    }
    
    int getBox(int row, int col) {
        return row / 3 + 3*(col / 3);
    }
    
    bool checkRow(vector<vector<char>> &board, int row, int col, bool searched[]) {
        if(searched[col]) return true;
        searched[col] = true;
        unordered_set<char> num_set;
        for(int i=0;i<9;i++) {
            if(num_set.find(board[i][col]) != num_set.end()) return false;
            if(board[i][col] != '.') num_set.insert(board[i][col]);
        }
        return true;
    }
    
    bool checkCol(vector<vector<char>> &board, int row, int col, bool searched[]) {
        if(searched[row]) return true;
        searched[row] = true;
        unordered_set<char> num_set;
        for(int i=0;i<9;i++) {
            if(num_set.find(board[row][i]) != num_set.end()) return false;
            if(board[row][i] != '.') num_set.insert(board[row][i]);
        }
        return true;
    }
    
    bool checkBox(vector<vector<char>> &board, int row, int col, bool searched[]) {
        int box = getBox(row,col);
        if(searched[box]) return true;
        searched[box] = true;
        unordered_set<char> num_set;
        for(int i=3*(row/3);i<3*(row/3)+3;i++) {
            for(int j=3*(col/3);j<3*(col/3)+3;j++) {
                if(num_set.find(board[i][j]) != num_set.end()) return false;
                if(board[i][j] != '.') num_set.insert(board[i][j]);
            }
        }
        return true;
    }
};
