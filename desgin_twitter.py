## K is the number of followee of user. 
## We have O(log(K)) runtime for getting news feed 
## because we do maximum 10 extractions in a heap that holds maximum K elements 
## (similar to what is done in merge K linked lists). The other ops are obviously O(1).
import heapq
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.tweet = {}
        self.followee = {}
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.time+=1
        self.tweet[userId] = self.tweet.get(userId, []) + [(-self.time, tweetId)]
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        h = []
        tweets = self.tweet
        people = set(self.followee.get(userId, []) + [userId])
        for person in people:
            if person in tweets and tweets[person]:
                time, tweet = tweets[person][len(tweets[person]) - 1]
                h.append((time, tweet, person, len(tweets[person]) - 1))
        heapq.heapify(h)
        news = []
        for _ in range(10):
            if h:
                time, tweet, person, idx = heapq.heappop(h)
                news.append(tweet)
                if idx:
                    newtime, newtweet = tweets[person][idx-1]
                    heapq.heappush(h, (newtime, newtweet, person, idx-1))
        return news
            
        
        
        
    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.followee[followerId] = self.followee.get(followerId, []) + [followeeId]
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId in self.followee.get(followerId, []):
            self.followee[followerId].remove(followeeId)