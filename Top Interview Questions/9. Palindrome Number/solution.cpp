class Solution {
public:
    bool isPalindrome(int x) {
        string x_str = to_string(x);
        int left, right;
        if(x_str.size() % 2 == 0) {
            left = x_str.size() / 2 - 1;
            right = x_str.size() / 2;
        } else {
            left = x_str.size() / 2 - 1;
            right = x_str.size() / 2 + 1;
        }
        while(left >= 0 && right < x_str.size()) {
            if(x_str[left--] != x_str[right++]) return false;
        }
        return true;
    }
};
