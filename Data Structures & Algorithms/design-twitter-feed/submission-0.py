from typing import List

class Twitter:

    def __init__(self):
        self.tweets = []           # (time, userId, tweetId)
        self.following = {}        # follower -> set of followees
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets.append((self.time, userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []

        followees = self.following.get(userId, set())

        for time, uid, tweetId in reversed(self.tweets):
            if uid == userId or uid in followees:
                feed.append(tweetId)

            if len(feed) == 10:
                break

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)