class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low=0,high=nums.size()-1;
        while(low < high) {
            int mid = (high - low) / 2 + low;
            if(nums[mid] > nums[high]) low = mid + 1;
            else high = mid;
        }
        int rot = low;
        low = 0, high = nums.size()-1;
        while(low <= high) {
            cout << low << ' ' << high << endl;
            int temp_mid = (high - low) / 2 + low;
            int mid = (temp_mid + rot) % nums.size();
            if(nums[mid] == target) return mid;
            else if(nums[mid] < target) low = temp_mid + 1;
            else high = temp_mid - 1;
        }
        return -1;
    }
};
