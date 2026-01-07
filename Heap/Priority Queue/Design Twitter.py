from typing import List
from collections import deque

class Twitter:

    def __init__(self):
        self.userTweets = dict()
        self.connections = dict()
        self.numOfTweets = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.numOfTweets += 1
        if userId not in self.userTweets:
            

    def getNewsFeed(self, userId: int) -> List[int]:
        print(self.tweets)
        res = []
        i = 0
        while i < len(self.tweets) and len(res) < 10:
            tweet = self.tweets[i]
            if tweet[0] == userId or (userId in self.connections and tweet[0] in self.connections[userId]):
                res.append(tweet[1])
            i += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.connections:
            self.connections[followerId] = []
        self.connections[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.connections and followeeId in self.connections[followerId]:
            self.connections[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)