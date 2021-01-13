from konlpy.tag import Okt
from collections import Counter
from get_texts import Texts

texts = Texts()
texts.get_texts()
texts.title_corpus
texts.content_corpus

nouns_tagger = Okt()
nouns = nouns_tagger.nouns(texts.content_corpus)
count = Counter(nouns)

# 편의를 위해 한 글자인 키워드 제거하기
remove_char_counter = Counter({x : count[x] for x in count if len(x) > 1})

# 한국어 약식 불용어 사전을 이용해 키워드 가다듬기 (https://www.ranks.nl/stopwords/korean)
korean_stopwords_path = "./data/korean_stopwords.txt"

with open(korean_stopwords_path, encoding='utf8') as f:
    stopwords = f.readlines()
stopwords = [x.strip() for x in stopwords]

# 문서의 특징에 따른 불용어를 추가하기 
namu_news_stopwords = ['연합뉴스', '저작권', '배포', '무단', '제공', '금지', '기자', '특파원', '사진', '시간', '지난해', \
    '지난', '이후', '관련', '자료', '오후', '이번', '내용', '영상', '대표', '지역', '혐의', '정부', '문제', '대해', '가장', '로이터', '보도']
for stopword in namu_news_stopwords:
    stopwords.append(stopword)

# 키워드 데이터에서 불용어를 제거하기 
remove_char_counter = Counter({x : remove_char_counter[x] for x in count if x not in stopwords})
print(remove_char_counter)