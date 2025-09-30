from collections import deque


class TreeNode:
    def __init__(self, letter: str = "", next: dict = {}):
        self.letter = letter
        self.next = next


class PrefixTree:
    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word) -> None:
        curr = self.root

        letters = deque(list(word))

        while letters:
            l = letters.popleft()
            if l not in curr.next:
                curr.next[l] = TreeNode(l)

            curr = curr.next[l]

        # Add end of word chracter
        curr.next["#"] = None

    def searchWord(self, word) -> bool:
        curr = self.root
        letters = deque(list(word))

        while letters:
            l = letters.popleft()
            if l not in curr.next:
                return False

            curr = curr.next[l]

        return "#" in curr.next
