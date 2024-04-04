class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Depth-First Search (DFS):
        # Perform a DFS on the grid starting from each cell.
        
        # Define the DFS function to search for the word starting from position (i, j)
        def dfs(board, word, i, j, idx):
            # Check if (i, j) is out of bounds or if the character at (i, j) does not match the next character in the word
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx]:
                return False
            
            # If idx reaches the end of the word, it means the entire word is found
            if idx == len(word) - 1:
                return True
            
            # Temporarily store the current character at (i, j)
            tmp = board[i][j]
            # Mark the current cell as visited by replacing its character with a special character '*'
            board[i][j] = '*'
            
            # Recursively search in adjacent cells to find the remaining characters of the word
            res = dfs(board, word, i + 1, j, idx + 1) or dfs(board, word, i - 1, j, idx + 1) \
                or dfs(board, word, i, j + 1, idx + 1) or dfs(board, word, i, j - 1, idx + 1)
            
            # Restore the character at (i, j) to its original value
            board[i][j] = tmp
            
            return res
        
        # Iterate through each cell in the grid
        for i in range(len(board)):
            for j in range(len(board[0])):
                # Start DFS from each cell to search for the word
                if dfs(board, word, i, j, 0):
                    return True  # If the word is found, return True
        
        # If the word is not found after searching all cells, return False
        return False
