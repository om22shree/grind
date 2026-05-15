from collections import defaultdict
from functools import lru_cache
from typing import Dict, List, Optional


class TrieNode:
    def __init__(self):
        self.children: Dict[str, "TrieNode"] = defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self._find(word)
        return bool(node and node.is_word)

    def starts_with(self, prefix: str) -> bool:
        return self._find(prefix) is not None

    def _find(self, prefix: str) -> Optional[TrieNode]:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node


def word_break(s: str, word_dict: List[str]) -> bool:
    words = set(word_dict)
    max_len = max(map(len, words), default=0)

    @lru_cache(None)
    def can_break(i: int) -> bool:
        if i == len(s):
            return True
        for j in range(i + 1, min(len(s), i + max_len) + 1):
            if s[i:j] in words and can_break(j):
                return True
        return False

    return can_break(0)
