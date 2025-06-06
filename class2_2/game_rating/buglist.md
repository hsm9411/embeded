# 버그 난이도 등급표 (함수 이름 및 줄 번호 포함)

| 버그 번호 | 함수 이름 (예상 위치)     | 버그 설명                                                | 난이도 레벨     |
|-----------|----------------------------|-----------------------------------------------------------|-----------------|
| 1         | normalize_path (1)         | 경로 문자열을 단순히 replace()로 처리                    | 레벨 2 (쉬움)   |
| 2         | is_valid_rating (2)        | is_valid_rating()에서 타입 검사 없음                     | 레벨 3 (보통)   |
| 3         | read_ratings (3)           | 파일이 없을 때 예외 처리 없음                            | 레벨 1 (매우 쉬움) |
| 4         | read_ratings (4)           | int() 변환 시 비정상 값 처리 없음                        | 레벨 4 (다소 어려움) |
| 5         | read_ratings (5)           | 빈 제목(title)을 허용                                     | 레벨 3 (보통)   |
| 6         | generate_report (6)        | 점수 리스트가 비어 있을 때 ZeroDivisionError 발생        | 레벨 5 (어려움) |
| 7         | generate_report (7)        | top_n 값이 리스트 크기보다 클 때 IndexError 발생         | 레벨 2 (쉬움)   |
| 8         | generate_report (8)        | 잘못된 동점(tie) 판단 로직                                | 레벨 4 (다소 어려움) |
| 9         | main (9)                   | 하드코딩된 윈도우 경로 사용                              | 레벨 2 (쉬움)   |
| 10        | generate_report (10)       | top_n = 10 고정값 → 유효 게임 수보다 클 경우 IndexError | 레벨 3 (보통)   |
