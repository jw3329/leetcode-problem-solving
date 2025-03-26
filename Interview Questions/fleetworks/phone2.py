# Write a class RateLimiter which takes two arguments in the constructor:
# time_period_seconds and max_calls.
#
# Write a single method call() which returns true if and only if
# call() has previously been called at least `max_calls` times
# in the last `time_period_seconds`.


# assume financial services API
# 1000s of API keys (i.e. users)
# 1000s requests/s per API key per API endpoint

# 1. we should make sure if it's working
# 2. latency -> rate limiter impacting service calling

# user_id -> call_list (redis)

# RateLimiter -> fetch user_id -> get call_list -> load call_list



from datetime import datetime

class RateLimiter:
    
    def __init__(self, time_period_seconds, max_calls):
        self.time_period_seconds = time_period_seconds
        self.max_calls = max_calls
        self.call_list = []
        
    def call(self):
        # when you make call
        # you insert call into list
        # check last calls, within time period seconds
        # if count >= max_calls, then we return true
        # otherwise we return false
        
        # check from backward, if there's count more than max_calls
        # 
        now = datetime.now()
        count = 0
        for i in range(len(self.call_list)-1,-1,-1):
            # check if now 
            if self.call_list[i] + self.time_period_seconds >= now.timestamp():
                count += 1
            else:
                break
    
        # put into the list
        self.call_list.append(now.timestamp())
        # check if count is more than max calls
        return True if count >= self.max_calls else False
        

rl = RateLimiter(1, 3)

for i in range(3):
    print(rl.call())

import time

time.sleep(1)

for i in range(4):
    print(rl.call())
    




