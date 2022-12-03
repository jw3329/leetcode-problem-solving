class Solution:
    def longestWord(self, words: List[str]) -> str:
        # one char at a time,
        # make word set
        # queue all letter starting, a to z,
        # then check if available, then append it into queue,
        # if curr is maximum, make it to max length, then move forward, update max length, then return
        queue = deque([])
        word_set = set(words)
        for i in range(26):
            c = chr(ord('a') + i)
            if c in word_set:
                queue.append(c)
        # now we have queue set up
        curr_max = ''
        while queue:
            popped = queue.popleft()
            # update curr max based on length
            if len(popped) > len(curr_max):
                curr_max = popped
            # put into queue if available in word set
            for i in range(26):
                c = chr(ord('a') + i)
                new_word = popped + c
                if new_word in word_set:
                    queue.append(new_word)
        return curr_max
            
