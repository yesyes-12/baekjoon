from collections import Counter
def solution(genres, plays):
    genres_cnt = {} # 장르 재생수 카운트
    songs = [] # 번호, 장르, 재생수 형식저장
    
    for i in range(len(plays)):
        genres_cnt[genres[i]] = genres_cnt.get(genres[i], 0) + plays[i]
        songs.append([i, genres[i], plays[i]])
    
    # 정렬 장르 총 재생수 기준
    genres_sort = sorted(genres_cnt.items(), key=lambda x: x[1], reverse=True)
    # 정렬 재생수 기준 노래 정렬
    songs.sort(key=lambda x: x[2], reverse=True)

    answer = []
    for genres, _ in genres_sort:
        # (pop,3100)
        cnt = 0
        for song in songs:
            # [4, pop, 2500]
            if song[1] == genres:
                answer.append(song[0])
                cnt += 1
                if cnt == 2:
                    break
                    
    return answer
            