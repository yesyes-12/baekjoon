def solution(id_list, report, k):
    answer = [0] * len(id_list)
    # 한번에 한명의 유저만 신고(횟수제한x)
    # 여러번 신고 가능하지만 1회 처리
    report_set = set(report)
    # k번 이상 신고된 유저는 정지, 정지사실 메일 발송(신고 내용 취합)
    report_map = {}
    
    # dict 초기화
    for name in id_list:
        report_map[name] = []

    # {신고당한사람: [신고자,...]} 
    for report in report_set:
        reporter, reported = report.split()
        who = report_map[reported]
        who.append(reporter)
    
    # k번 이상인 친구들 신고자들 idx 찾아 count +1
    for uid in report_map:
        count = len(report_map[uid])
        if count >= k:
            for i in report_map[uid]:
                idx = id_list.index(i)
                answer[idx] += 1
    return answer