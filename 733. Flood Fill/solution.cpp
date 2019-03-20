class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        bool **visited = new bool*[image.size()];
        for(int i=0;i<image.size();i++) {
            bool *bool_arr = new bool[image[0].size()];
            for(int j=0;j<image[0].size();j++) {
                bool_arr[j] = false;
            }
            visited[i] = bool_arr;
        }
        dfs(image,sr,sc,image[sr][sc], newColor, visited);
        return image;
    }
    
    void dfs(vector<vector<int>> &image, int sr, int sc, 
             int orig_color, int newColor, bool **visited) {
        if(sr < 0 || sr >= image.size() || sc < 0 || sc >= image[0].size()) return;
        if(visited[sr][sc]) return;
        visited[sr][sc] = true;
        if(image[sr][sc] != orig_color) return;
        image[sr][sc] = newColor;
        int row[] = {-1,0,1,0};
        int col[] = {0,1,0,-1};
        for(int i=0;i<4;i++) {
            dfs(image,sr + row[i], sc + col[i], orig_color, newColor, visited);
        }
    }
};
