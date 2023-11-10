class Tweet:
    
        def __init__(self, _id):
            self.id = _id
            self.time = Twitter.time
            Twitter.time += 1
            self.next = None

class User:

    def __init__(self, _id):
        self.id = _id
        self.tweets = None
        self.followers = set([_id])

    def follow(self, user_id):
        self.followers.add(user_id)

    def unfollow(self, user_id):
        if user_id in self.followers:
            self.followers.remove(user_id)

    def create_tweet(self, tweet_id):
        tweet = Tweet(tweet_id)
        # make it into head
        head = self.tweets
        if not head:
            self.tweets = tweet
        else:
            tweet.next = self.tweets
            self.tweets = tweet

class Twitter:    
    time = 0

    def __init__(self):
        # grabs user map
        self.user_map = dict()
    
    def get_user(self, user_id: int):
        if user_id not in self.user_map:
            self.user_map[user_id] = User(user_id)
        return self.user_map[user_id]
        
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # create user if necessary
        user = self.get_user(userId)
        user.create_tweet(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        # grab user
        # iterate all followers
        # put all their tweets first into heap
        # then pop up by 10
        user = self.get_user(userId)
        heap = []
        for follower_id in user.followers:
            follower = self.get_user(follower_id)
            tweets = follower.tweets
            if not tweets: continue
            heapq.heappush(heap, (-tweets.time, tweets))
        # now up to 10, put into feed
        res = []
        while heap and len(res) < 10:
            # pop first
            time, tweets = heapq.heappop(heap)
            # append into res
            res.append(tweets.id)
            # put next of tweets
            next_tweets = tweets.next
            if not next_tweets: continue
            heapq.heappush(heap, (-next_tweets.time, next_tweets))
        return res
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        user1 = self.get_user(followerId)
        user2 = self.get_user(followeeId)
        user1.follow(user2.id)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        user1 = self.get_user(followerId)
        user2 = self.get_user(followeeId)
        user1.unfollow(user2.id)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
