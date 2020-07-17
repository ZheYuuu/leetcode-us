from typing import List
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        def add(word: str):
            node = trie
            for c in word:
                node = node.setdefault(c, {})

        def get(word: str) -> bool:
            node = trie
            for c in word:
                node = node.get(c)
                if node is None:
                    return False
            return True

        words.sort(key=len, reverse=True)
        trie, result = {}, []
        for word in words:
            if get(word): result.append(word)
            for i in range(len(word)):
                # add each sub-word in trie
                add(word[i:])
        return result

if __name__ == "__main__":
    t = Solution().stringMatching(["mass","as","hero","superhero"])