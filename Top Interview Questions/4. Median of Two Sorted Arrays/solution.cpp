class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int x = nums1.size();
        int y = nums2.size();
        
        if(x > y) return findMedianSortedArrays(nums2,nums1);
        int low = 0;
        int high = x;
        while(low <= high) {
            int partition_x = (low + high) / 2;
            int partition_y = (x + y + 1) / 2 - partition_x;
            
            int max_left_x = partition_x == 0 ? INT_MIN : nums1[partition_x-1];
            int min_right_x = partition_x == x ? INT_MAX : nums1[partition_x];
            
            int max_left_y = partition_y == 0 ? INT_MIN : nums2[partition_y-1];
            int min_right_y = partition_y == y ? INT_MAX : nums2[partition_y];
            
            if(max_left_x <= min_right_y && max_left_y <= min_right_x) {
                if((x + y) % 2 == 0) {
                    return ((double) max(max_left_x,max_left_y) + 
                            min(min_right_x, min_right_y)) / 2;
                } else {
                    return max(max_left_x,max_left_y);
                }
            } else if(max_left_x > min_right_y) {
                high = partition_x - 1;
            } else {
                low = partition_x + 1;
            }
        }
        return -1;
    }
};
