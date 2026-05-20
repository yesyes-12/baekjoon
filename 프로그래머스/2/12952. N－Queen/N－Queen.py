def solution(n):
	answer=0
	
	# 1차원 배열
	board = [0] * n
	
	# 가지치기 대각선에 있는지? 같은 열인지?
	def is_safe(c_row):
		for i in range(c_row):
			if board[c_row] == board[i] or abs(c_row - i) == abs(board[c_row] - board[i]):
				return False
		return True
	
	def dfs(row):
		nonlocal answer
		
		if row==n:
			answer+=1
			return
		
		for col in range(n):
			board[row] = col # 퀸 배치 시도
		
			if is_safe(row):
				dfs(row+1)
	dfs(0)
	return answer		
	