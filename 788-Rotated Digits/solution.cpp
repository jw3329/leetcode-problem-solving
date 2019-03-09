class Solution {
public:
    int rotatedDigits(int N) {
        char valid[] = {'2','5','6','9'};
        char valid_helper[] = {'0','1','8'};
        int count = 0;
        for(int i=1;i<=N;i++) {
            string str_num = to_string(i);
            bool is_valid = false;
            for(int j=0;j<str_num.size();j++) {
                bool validated = false;
                bool validated_helper = false;
                for(int k=0;k<4;k++) {
                    if(str_num[j] == valid[k]) {
                        validated = true;
                        is_valid = true;
                        break;
                    }
                }
                if(!validated) {
                    for(int k=0;k<3;k++) {
                        if(str_num[j] == valid_helper[k]) {
                            validated_helper = true;
                            break;
                        }
                    }
                }
                if(!validated && !validated_helper) {
                    is_valid = false;
                    break;
                }
            }
            if(is_valid) count++;
        }
        return count;
    }
};
