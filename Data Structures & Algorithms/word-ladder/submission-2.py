class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0

        graph = defaultdict(list)       
        q = deque()
        q.append(beginWord)
        count = 1
        visited = set()
        visited.add(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                graph[pattern].append(word)
        
        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return count

                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for neighbor in graph[pattern]:
                        if neighbor not in visited:
                            q.append(neighbor)
                            visited.add(neighbor)
            count += 1
        
        return 0


        