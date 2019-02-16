class Solution {
public:
    bool reachingPoints(int sx, int sy, int tx, int ty) {
        while(tx >= 1 && ty >= 1) {
            if(sx == tx && sy == ty) return true;
            if(ty > tx) {
                ty -= tx;
            } else {
                tx -= ty;
            }
        }
        return false;
    }
};