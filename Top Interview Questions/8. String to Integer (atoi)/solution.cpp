class Solution {
public:
    int myAtoi(string str) {
        if(str.empty()) return 0;
        bool is_negative = false;
        bool other = true;
        // let i as the starting digit
        int i=0;
        // remove white spaces
        while(str[i] == ' ') i++;
        // check the sign
        if(str[i] == '-') {
            is_negative = true;
            i++;
            other = false;
            // if next index is not digit, it is not a number, checking if index is less than size of string
            if(i >= str.size() || !isDigit(str[i])) return 0;
        } else if(str[i] == '+' || isDigit(str[i])) {
            if(str[i] == '+') {
                i++;
                // same condition going through
                if(i >= str.size() || !isDigit(str[i])) return 0;
            }
            other = false;
        }
        // if it is not in above conditions, return 0 since it is nothing
        if(other) return 0;
        // remove start 0s
        while(str[i] == '0') i++;
        // if next value is not digit, return 0
        if(i >= str.size() || !isDigit(str[i])) return 0;
        // now we found the index, get the number until it is not the number
        string res = "";
        while(isDigit(str[i])) {
            res += str[i++];
        }
        // now check if the number is in boundary, and return the correct value
        return checkBoundary(res,is_negative);
    }
    
    bool isDigit(char c) {
        return '0' <= c && c <= '9';
    }
    
    int checkBoundary(string str, bool is_negative) {
        if(is_negative) {
            str = '-' + str;
            if(compare(str,to_string(INT_MIN)) == -1) return INT_MIN;
        } else {
            if(compare(str,to_string(INT_MAX)) == 1) return INT_MAX;            
        }
        // cout << "here" << endl;
        return stoi(str);
    }
    
    
    // if s1 > s2, return 1, if it is equal, return 0, if s1 < s2, then returns -1
    int compare(string s1, string s2) {
        // if it is same, return 0
        if(s1 == s2) return 0;
        int start = 0;
        int sign = 1;
        if(s1[0] == '-') {
            start = 1;
            sign = -1;
        }
        if(s1.size() < s2.size()) return -sign;
        else if(s1.size() > s2.size()) return sign;
        for(int i=start;i<s1.size();i++) {
            if(s1[i] == s2[i]) continue;
            if(s1[i] > s2[i]) return sign;
            else return -sign;
        }
        return 0;
    }
    
};
