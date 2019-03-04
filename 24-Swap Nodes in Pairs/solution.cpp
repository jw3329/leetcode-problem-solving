/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if(!head || !head->next) return head;
        ListNode *rest = swapPairs(head->next->next);
        ListNode *cur = head;
        ListNode *curNext = head->next;
        curNext->next = cur;
        cur->next = rest;
        return curNext;
    }
};
