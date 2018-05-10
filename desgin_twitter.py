## K is the number of followee of user. 
## We have O(log(K)) runtime for getting news feed 
## because we do maximum 10 extractions in a heap that holds maximum K elements 
## (similar to what is done in merge K linked lists). The other ops are obviously O(1).

import heapq

class Twitter():
	def __init__(self):
		self.time = 0
		self.tweet = {}
		self.followee = {}


	def postTweet(self, userId, tweetId):
		self.time+=1
		self.tweet[userId] = self.tweets.get(user, []) + [(-self.time,  tweet)]


	def getNewsFeed(self, userId):
		h, tweets = [], self.tweets
		peope = self.followee.get(userId, set()) | set([userId])
		for person in people:
			if person in tweets and tweets[person]:
				time, tweet = tweets[person][-1]
				h.append((time, tweet, person, len(tweets[person]) -1 ))
		heapq.heapify(h)
		news = []
		for _ in range(10):
			if h:
				time, tweet, person, idx = heapq.heappop(h)
				news.append(tweet)
				if idx:
					new_time, new_tweet = tweet[person][idx-1]
					heapq.heappush(h, (new_time, new_tweet, person, idx - 1))
		return news


	def follow(self, follower, other):
		self.followee[follower] = self.followee.get(follower, set()) | set([other])

	def unfollow(self, follower, other):
        if follower in self.followee:
            self.followee[follower].discard(other)

