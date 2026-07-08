# LLM-XAI Evaluation Report

## Scope

- LLM evidence samples: 30
- Compared XAI rows: 360
- Compared model-method pairs: 12
- XAI top-k used for overlap: 3

This report treats the LLM explanation as a qualitative reference, not as ground truth.
The main question is whether each XAI method highlights the same eojeol-level evidence and polarity direction as the LLM response.

## Metric Guide

- `topk_recall`: share of LLM evidence words included in XAI top-k words.
- `jaccard`: set overlap between LLM evidence words and XAI top-k words.
- `signed_cosine`: polarity-aware cosine between the LLM evidence vector and the XAI score vector.
- `evidence_mass`: total absolute XAI score mass assigned to LLM evidence words.
- `polarity_agreement`: sign agreement on overlapping evidence words.
- `llm_match_score`: presentation score combining the above metrics; use it for ranking, not as a truth label.

## Overall Ranking

| rank | model | method | n | match | top-k recall | jaccard | signed cosine | evidence mass | polarity agreement | pred agreement |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | transformer | integrated_gradients_steps100 | 30 | 0.612 | 0.542 | 0.530 | 0.629 | 0.883 | 0.894 | 0.967 |
| 2 | transformer | occlusion | 30 | 0.607 | 0.526 | 0.501 | 0.604 | 0.944 | 0.928 | 0.967 |
| 3 | cnn | ngram_occlusion | 30 | 0.606 | 0.501 | 0.481 | 0.713 | 0.859 | 0.950 | 0.967 |
| 4 | transformer | integrated_gradients_steps50 | 30 | 0.604 | 0.542 | 0.530 | 0.569 | 0.881 | 0.850 | 0.967 |
| 5 | cnn | filter_activation | 30 | 0.580 | 0.488 | 0.465 | 0.634 | 0.849 | 0.889 | 0.967 |
| 6 | cnn | integrated_gradients_steps100 | 30 | 0.575 | 0.503 | 0.476 | 0.588 | 0.889 | 0.872 | 0.967 |
| 7 | cnn | integrated_gradients_steps50 | 30 | 0.575 | 0.503 | 0.476 | 0.588 | 0.889 | 0.872 | 0.967 |
| 8 | cnn | unigram_occlusion | 30 | 0.569 | 0.504 | 0.476 | 0.547 | 0.905 | 0.889 | 0.967 |
| 9 | fnn | integrated_gradients_steps50 | 30 | 0.552 | 0.476 | 0.442 | 0.587 | 0.853 | 0.922 | 0.933 |
| 10 | fnn | integrated_gradients_steps100 | 30 | 0.552 | 0.476 | 0.442 | 0.587 | 0.852 | 0.911 | 0.933 |
| 11 | fnn | occlusion | 30 | 0.547 | 0.476 | 0.440 | 0.559 | 0.868 | 0.906 | 0.933 |
| 12 | fnn | lime | 30 | 0.546 | 0.467 | 0.435 | 0.584 | 0.849 | 0.867 | 0.933 |

## Model-Level Summary

| model | n rows | mean match | mean signed cosine | mean evidence mass | prediction agreement |
| --- | ---: | ---: | ---: | ---: | ---: |
| cnn | 150 | 0.581 | 0.614 | 0.878 | 0.967 |
| fnn | 120 | 0.549 | 0.580 | 0.855 | 0.933 |
| transformer | 90 | 0.608 | 0.601 | 0.903 | 0.967 |

## Key Findings

- Best aligned method by `mean_llm_match_score`: `transformer / integrated_gradients_steps100` (0.612).
- Weakest aligned method by `mean_llm_match_score`: `fnn / lime` (0.546).
- Strongest model family by average match: `transformer` (0.608).

## Best Aligned Rows

| sample | model | method | match | LLM evidence | XAI top words |
| --- | --- | --- | ---: | --- | --- |
| case_010 | transformer | integrated_gradients_steps100 | 1.000 | 개노잼임 , ㅡㅡ | 개노잼임 , ㅡㅡ |
| case_010 | transformer | integrated_gradients_steps50 | 1.000 | 개노잼임 , ㅡㅡ | 개노잼임 , ㅡㅡ |
| case_001 | cnn | filter_activation | 0.999 | 정말 , 재미있어요 , 추천합니다 | 정말 , 재미있어요 , 추천합니다 |
| case_010 | cnn | filter_activation | 0.996 | 개노잼임 , ㅡㅡ | 개노잼임 , ㅡㅡ |
| case_010 | fnn | integrated_gradients_steps100 | 0.995 | 개노잼임 , ㅡㅡ | 개노잼임 , ㅡㅡ |

## Weak Or Divergent Rows

| sample | model | method | match | signed cosine | LLM evidence | XAI top words |
| --- | --- | --- | ---: | ---: | --- | --- |
| case_030 | fnn | lime | 0.058 | 0.067 | 잘 , 담아낸 , 의미 , 있는 , 영화입니다. , 먹먹하네요. | 가슴 , 아픈 , 사실을 |
| case_030 | cnn | integrated_gradients_steps50 | 0.088 | 0.209 | 잘 , 담아낸 , 의미 , 있는 , 영화입니다. , 먹먹하네요. | 가슴 , 아픈 , 사실을 |
| case_030 | cnn | integrated_gradients_steps100 | 0.089 | 0.211 | 잘 , 담아낸 , 의미 , 있는 , 영화입니다. , 먹먹하네요. | 가슴 , 아픈 , 사실을 |
| case_030 | cnn | filter_activation | 0.133 | 0.326 | 잘 , 담아낸 , 의미 , 있는 , 영화입니다. , 먹먹하네요. | 아픈 , 역사적 , 사실을 |
| case_006 | cnn | ngram_occlusion | 0.179 | -0.418 | 수면제 , 대신 , 보면 , 딱 , 좋은 | 좋은 , 훌륭한 , 영화입니다 |

## Per-Sample Assessment

### case_001

- text: 이 영화 정말 재미있어요 추천합니다
- LLM sentiment: positive
- LLM evidence: 정말 재미있어요, 추천합니다
- model prediction agreement: 12/12 rows
- best XAI: `cnn / filter_activation` (0.999)
- weakest XAI: `fnn / occlusion` (0.656)

### case_002

- text: 스토리가 지루하고 배우들 연기도 별로네요
- LLM sentiment: negative
- LLM evidence: 스토리가 지루하고, 배우들 연기도 별로네요
- model prediction agreement: 12/12 rows
- best XAI: `cnn / ngram_occlusion` (0.723)
- weakest XAI: `transformer / integrated_gradients_steps50` (0.510)

### case_003

- text: 처음엔 지루했는데 갈수록 정말 재미있어지네요
- LLM sentiment: positive
- LLM evidence: 처음엔 지루했는데, 갈수록 정말 재미있어지네요
- model prediction agreement: 12/12 rows
- best XAI: `cnn / ngram_occlusion` (0.739)
- weakest XAI: `cnn / filter_activation` (0.510)

### case_004

- text: 배우들의 연기는 명품인데 각본이 너무 쓰레기네요
- LLM sentiment: negative
- LLM evidence: 배우들의 연기는 명품인데, 각본이 너무 쓰레기네요
- model prediction agreement: 12/12 rows
- best XAI: `cnn / integrated_gradients_steps100` (0.634)
- weakest XAI: `transformer / integrated_gradients_steps50` (0.450)

### case_005

- text: 와... 이런 영화에 내 피 같은 돈을 쓰다니 대단하다
- LLM sentiment: negative
- LLM evidence: 내 피 같은 돈을 쓰다니, 이런 영화에, 대단하다
- model prediction agreement: 12/12 rows
- best XAI: `cnn / ngram_occlusion` (0.533)
- weakest XAI: `fnn / integrated_gradients_steps50` (0.320)

### case_006

- text: 수면제 대신 보면 딱 좋은 훌륭한 영화입니다
- LLM sentiment: negative
- LLM evidence: 수면제 대신 보면 딱 좋은
- model prediction agreement: 3/12 rows
- best XAI: `transformer / occlusion` (0.625)
- weakest XAI: `cnn / ngram_occlusion` (0.179)

### case_007

- text: 와 진짜 개존잼!!! 꼭보세요 ㅋㅋㅋ
- LLM sentiment: positive
- LLM evidence: 개존잼!!!, 꼭보세요, ㅋㅋㅋ
- model prediction agreement: 12/12 rows
- best XAI: `cnn / ngram_occlusion` (0.975)
- weakest XAI: `fnn / integrated_gradients_steps100` (0.378)

### case_008

- text: 시간낭비 오지구요 지리구요 다신 안봄 ㅡㅡ
- LLM sentiment: negative
- LLM evidence: 시간낭비, 다신 안봄, ㅡㅡ
- model prediction agreement: 12/12 rows
- best XAI: `fnn / lime` (0.799)
- weakest XAI: `cnn / filter_activation` (0.361)

### case_009

- text: 스토리가 지루하긴 한데 배우들은 멋있음
- LLM sentiment: positive
- LLM evidence: 스토리가 지루하긴, 배우들은 멋있음
- model prediction agreement: 5/12 rows
- best XAI: `cnn / integrated_gradients_steps100` (0.712)
- weakest XAI: `cnn / filter_activation` (0.401)

### case_010

- text: 개노잼임 ㅡㅡ
- LLM sentiment: negative
- LLM evidence: 개노잼임, ㅡㅡ
- model prediction agreement: 12/12 rows
- best XAI: `transformer / integrated_gradients_steps100` (1.000)
- weakest XAI: `fnn / lime` (0.941)

### case_011

- text: 평점 알바들만 넘치네 진짜 돈 아깝다
- LLM sentiment: negative
- LLM evidence: 평점 알바들만 넘치네, 진짜 돈 아깝다
- model prediction agreement: 12/12 rows
- best XAI: `cnn / ngram_occlusion` (0.670)
- weakest XAI: `transformer / integrated_gradients_steps50` (0.557)

### case_012

- text: 어설픈 신파보다 백배 천배 낫다. 가슴 먹먹해지는 수작.
- LLM sentiment: positive
- LLM evidence: 어설픈 신파보다 백배 천배 낫다., 가슴 먹먹해지는 수작.
- model prediction agreement: 12/12 rows
- best XAI: `transformer / integrated_gradients_steps50` (0.542)
- weakest XAI: `fnn / lime` (0.411)

### case_013

- text: 솔직히 재미는 없음... 시간 때우기용도 안됨
- LLM sentiment: negative
- LLM evidence: 재미는 없음..., 시간 때우기용도 안됨
- model prediction agreement: 12/12 rows
- best XAI: `transformer / integrated_gradients_steps100` (0.732)
- weakest XAI: `cnn / unigram_occlusion` (0.661)

### case_014

- text: 개연성이 밥말아먹었나 스토리가 왜 이 모양임?
- LLM sentiment: negative
- LLM evidence: 개연성이 밥말아먹었나, 스토리가 왜 이 모양임?
- model prediction agreement: 12/12 rows
- best XAI: `cnn / filter_activation` (0.651)
- weakest XAI: `cnn / unigram_occlusion` (0.581)

### case_015

- text: 연출, 연기, 음악 삼박자가 완벽하다. 꼭 극장가서 보세요.
- LLM sentiment: positive
- LLM evidence: 연출, 연기, 음악 삼박자가 완벽하다., 꼭 극장가서 보세요.
- model prediction agreement: 12/12 rows
- best XAI: `transformer / integrated_gradients_steps100` (0.595)
- weakest XAI: `cnn / integrated_gradients_steps50` (0.449)

### case_016

- text: 하도 재밌다길래 봤는데 진짜 개노잼임 절대보지마셈
- LLM sentiment: negative
- LLM evidence: 진짜 개노잼임, 절대보지마셈
- model prediction agreement: 12/12 rows
- best XAI: `cnn / ngram_occlusion` (0.941)
- weakest XAI: `fnn / integrated_gradients_steps100` (0.564)

### case_017

- text: 오랜만에 가슴 따뜻해지는 웰메이드 영화 한 편 봤네요. 강추!!
- LLM sentiment: positive
- LLM evidence: 가슴 따뜻해지는, 웰메이드 영화, 강추!!
- model prediction agreement: 12/12 rows
- best XAI: `cnn / integrated_gradients_steps100` (0.708)
- weakest XAI: `transformer / occlusion` (0.490)

### case_018

- text: 뻔하디 뻔한 한국식 억지 감동 짜내기 영화 극혐
- LLM sentiment: negative
- LLM evidence: 뻔하디 뻔한, 억지 감동 짜내기, 극혐
- model prediction agreement: 12/12 rows
- best XAI: `cnn / filter_activation` (0.643)
- weakest XAI: `cnn / ngram_occlusion` (0.437)

### case_019

- text: 내 돈이랑 시간 돌려내라 ㅋㅋㅋ 감독 누구냐 진짜
- LLM sentiment: negative
- LLM evidence: 내 돈이랑 시간 돌려내라, 감독 누구냐 진짜
- model prediction agreement: 12/12 rows
- best XAI: `cnn / filter_activation` (0.601)
- weakest XAI: `transformer / integrated_gradients_steps50` (0.437)

### case_020

- text: 배우들 얼굴 보러 갔다가 힐링 제대로 하고 옴 ㅠㅠ 연기도 찰떡
- LLM sentiment: positive
- LLM evidence: 힐링 제대로 하고 옴, 연기도 찰떡
- model prediction agreement: 12/12 rows
- best XAI: `transformer / integrated_gradients_steps50` (0.618)
- weakest XAI: `fnn / lime` (0.249)

### case_021

- text: 초반엔 오? 하다가 후반 갈수록 산으로 가네 ㅋㅋㅋ 어이없음
- LLM sentiment: negative
- LLM evidence: 초반엔 오?, 후반 갈수록 산으로 가네, 어이없음
- model prediction agreement: 12/12 rows
- best XAI: `cnn / filter_activation` (0.583)
- weakest XAI: `cnn / ngram_occlusion` (0.457)

### case_022

- text: 인생작입니다. 살면서 본 시트콤 중에 감히 최고라고 말하고 싶네요.
- LLM sentiment: positive
- LLM evidence: 인생작입니다., 감히 최고라고 말하고 싶네요.
- model prediction agreement: 12/12 rows
- best XAI: `transformer / occlusion` (0.689)
- weakest XAI: `fnn / occlusion` (0.435)

### case_023

- text: 지루해서 중간에 나왔어요 돈날림주의;;;
- LLM sentiment: negative
- LLM evidence: 지루해서, 중간에 나왔어요, 돈날림주의;;;
- model prediction agreement: 12/12 rows
- best XAI: `fnn / lime` (0.828)
- weakest XAI: `transformer / integrated_gradients_steps100` (0.727)

### case_024

- text: 연기도 좋고 영상도 아름답고 음악도 훌륭했지만 정작 스토리가 너무 엉성해서 전체적으로는 실망스러웠습니다.
- LLM sentiment: negative
- LLM evidence: 연기도 좋고 영상도 아름답고 음악도 훌륭했지만, 스토리가 너무 엉성해서, 전체적으로는 실망스러웠습니다.
- model prediction agreement: 12/12 rows
- best XAI: `cnn / filter_activation` (0.522)
- weakest XAI: `transformer / occlusion` (0.237)

### case_025

- text: 킬링타임으로 제격임 ㅋㅋ 유치하긴 한데 가볍게 웃기 좋네요
- LLM sentiment: positive
- LLM evidence: 킬링타임으로 제격임, 유치하긴, 가볍게 웃기 좋네요
- model prediction agreement: 12/12 rows
- best XAI: `transformer / occlusion` (0.600)
- weakest XAI: `cnn / filter_activation` (0.279)

### case_026

- text: 평점 왜 이럼? 생각보다 완전 명작인데 억까들 많네
- LLM sentiment: positive
- LLM evidence: 생각보다 완전 명작인데, 억까들 많네
- model prediction agreement: 12/12 rows
- best XAI: `cnn / ngram_occlusion` (0.699)
- weakest XAI: `transformer / integrated_gradients_steps50` (0.453)

### case_027

- text: 원작 웹툰이 훨씬 나음.. 실사화는 그냥 폭망 수준
- LLM sentiment: negative
- LLM evidence: 실사화는 그냥 폭망 수준, 원작 웹툰이 훨씬 나음..
- model prediction agreement: 12/12 rows
- best XAI: `cnn / filter_activation` (0.612)
- weakest XAI: `fnn / occlusion` (0.523)

### case_028

- text: 가볍게 볼 로맨틱 코미디 찾다가 완전 인생 영화 건짐... 설렘 터짐
- LLM sentiment: positive
- LLM evidence: 완전 인생 영화 건짐..., 설렘 터짐
- model prediction agreement: 12/12 rows
- best XAI: `transformer / integrated_gradients_steps100` (0.636)
- weakest XAI: `fnn / lime` (0.342)

### case_029

- text: 1점도 아깝다 스토리 연출 캐스팅 다 엉망진창임
- LLM sentiment: negative
- LLM evidence: 1점도 아깝다, 스토리 연출 캐스팅 다 엉망진창임
- model prediction agreement: 12/12 rows
- best XAI: `cnn / ngram_occlusion` (0.641)
- weakest XAI: `transformer / integrated_gradients_steps50` (0.483)

### case_030

- text: 가슴 아픈 역사적 사실을 잘 담아낸 의미 있는 영화입니다. 먹먹하네요.
- LLM sentiment: positive
- LLM evidence: 잘 담아낸, 의미 있는 영화입니다., 먹먹하네요.
- model prediction agreement: 12/12 rows
- best XAI: `transformer / integrated_gradients_steps50` (0.577)
- weakest XAI: `fnn / lime` (0.058)
