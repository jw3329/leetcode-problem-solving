class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        # shortest k
        # do bfs
        # go until k turn
        # do videos
        res = set()
        turn = 0
        queue = deque([id])
        visited = set([id])
        # do bfs
        while queue and turn < level:
            for _ in range(len(queue)):
                curr = queue.popleft()
                # now append friends visit
                for person in friends[curr]:
                    if person not in visited:
                        queue.append(person)
                        visited.add(person)
            # after done, add up turn
            turn += 1
        # now we have either turn or empty queue
        # for existing queue, it means, it's eligible
        # add up all videos of it
        freq = defaultdict(int)
        while queue:
            person = queue.popleft()
            for video in watchedVideos[person]:
                freq[video] += 1
        # now sort
        return list(map(lambda x: x[0], sorted(freq.items(), key=lambda x: (x[1], x[0]))))
