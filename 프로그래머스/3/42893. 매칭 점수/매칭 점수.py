import re


def solution(word, pages):
    word = word.lower()
    page_count = len(pages)

    # URL -> pages에서의 인덱스
    url_to_index = {}
    basic_scores = [0] * page_count
    outgoing_links = [[] for _ in range(page_count)]

    # 1단계: 각 페이지의 정보 수집
    for index, page in enumerate(pages):
        url = re.search(
            r'<meta property="og:url" content="([^"]+)"',
            page
        ).group(1)
        url_to_index[url] = index

        body = re.search(
            r"<body>(.*?)</body>",
            page,
            re.DOTALL | re.IGNORECASE
        ).group(1)

        # 태그를 제외한 본문 텍스트에서 알파벳 단어만 추출한다.
        text = re.sub(r"<[^>]+>", " ", body).lower()
        words = re.findall(r"[a-z]+", text)
        basic_scores[index] = sum(token == word for token in words)

        # 현재 페이지가 가리키는 모든 외부 링크
        outgoing_links[index] = re.findall(r'<a href="([^"]+)"', page)

    # 기본 점수로 매칭 점수를 초기화한다.
    matching_scores = [float(score) for score in basic_scores]

    # 2단계: 각 페이지의 링크 점수를 목적지 페이지에 분배한다.
    for source_index, links in enumerate(outgoing_links):
        if not links:
            continue

        shared_score = basic_scores[source_index] / len(links)

        for url in links:
            destination_index = url_to_index.get(url)

            # 입력으로 주어진 페이지에 없는 URL은 점수를 받을 대상이 없다.
            if destination_index is not None:
                matching_scores[destination_index] += shared_score

    # 동점이면 먼저 등장한 페이지를 유지한다.
    answer = 0
    for index in range(1, page_count):
        if matching_scores[index] > matching_scores[answer]:
            answer = index

    return answer