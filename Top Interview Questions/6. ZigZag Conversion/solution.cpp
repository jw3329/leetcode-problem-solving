class Solution {
public:
    string convert(string s, int numRows) {
        vector<char *> arr;
        int i=0;
        int vertical = 0;
	// vertical == 0 ? copying vertical index : index of one single char index to copy
        while(i < s.size()) {
            char *ch_arr = new char[numRows]();
            // vertical
            if(vertical == 0) {
                for(int j=0;j<numRows && i < s.size();j++) {
                    ch_arr[j] = s[i++];
                }
                vertical = numRows >= 2 ? numRows - 2 : 0;
            } else {
                ch_arr[vertical--] = s[i++];
            }
            arr.push_back(ch_arr);
        }
        // make it into correct form and store it in res
        string res = "";
        for(int i=0;i<numRows;i++) {
            for(int j=0;j<arr.size();j++) {
                if(arr[j][i]) res += arr[j][i];
            }
        }
        // delete heap memory
        for(auto &ch_arr : arr) {
            delete[] ch_arr;
        }
        return res;
    }
};
