from collections import deque
def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    words.append(begin)
    print(words)
    # 한글자만 다른지 확인
    def diff_word(word1, word2):
        diff = 0
        for a, b in zip(word1, word2):
            if a != b:
                diff += 1
        return diff==1
    
    # bfs
    
    # (현재 단어, 현재까지 변환 횟수)
    que = deque([(begin, 0)])
    visited = [0] * len(words)

    while que:
        # 현재 단어
        cur_word, cur_step = que.popleft()
        # 일치하면 종료
        if cur_word == target:
            return cur_step
        # 다음 단어 찾기
        for i in range(len(words)):
            # 방문 x, 1글자만 다름
            if diff_word(cur_word, words[i]) and not visited[i]:
                # 다음단어, 횟수+1
                que.append((words[i], cur_step+1))

    return answer