# LLM Comparison 결과 해석 리포트

작성일: 2026-07-08
기준 산출물: `XAI/LLMComparison/comparison_outputs` 최신 재분석 결과

## 1. 결론 요약

이번 LLM comparison은 각 XAI 방법이 모델의 정답률을 얼마나 높였는지를 평가한 것이 아니다. LLM이 영화 리뷰 문장에서 감정 판단 근거로 지목한 어절과, CNN/FNN/Transformer XAI가 중요하다고 표시한 어절이 얼마나 겹치고 같은 감정 방향을 갖는지를 비교한 결과다. 따라서 이 결과는 "모델 설명이 사람이 읽기에 그럴듯한 감정 근거와 얼마나 가까운가"를 보여주는 외부 의미 정렬 평가에 가깝다.

가장 LLM 근거와 잘 맞은 방법은 `Transformer / Integrated Gradients 100 steps`였다. 평균 LLM match score는 0.612로 1위이며, top-k recall과 Jaccard도 가장 높다. 즉 Transformer의 IG 100은 LLM이 감정 근거라고 본 어절을 비교적 안정적으로 함께 집어냈다.

다만 단일 우승자로 과도하게 해석하면 안 된다. 1위 `Transformer IG100` 0.612, 2위 `Transformer Occlusion` 0.607, 3위 `CNN N-gram Occlusion` 0.606의 차이는 매우 작다. 이번 결과는 "Transformer IG100이 대표 방법으로 가장 적합하지만, Transformer Occlusion과 CNN N-gram Occlusion도 거의 같은 수준의 상위권 설명력을 보인다"로 읽는 것이 안전하다.

모델군 평균으로는 Transformer가 가장 높았다. 평균 match score는 Transformer 0.608, CNN 0.581, FNN 0.549 순서다. Transformer는 문맥과 대비 구조를 반영한 근거 선택에서 강했고, CNN은 n-gram occlusion을 사용할 때 감정 방향 일치와 구절 단위 근거 포착이 강했다. FNN은 모든 방법에서 하위권에 머물렀고, 특히 예측 감정이 LLM 판단과 어긋나는 사례가 더 많았다.

## 2. 분석 대상과 재현 상태

이번 리포트는 clean worktree에서 전체 LLM comparison을 새로 실행한 산출물을 기준으로 한다.

| 항목 | 값 |
| --- | ---: |
| LLM evidence 샘플 수 | 30 |
| 비교된 XAI row 수 | 360 |
| 비교된 model-method pair 수 | 12 |
| 각 방법별 샘플 수 | 30 |
| XAI top-k 기준 | 3 |
| LLM evidence JSON row | 30 |
| `output_llm_evidence.json` row | 30 |
| 단어 정렬 mismatch | 0 |
| Transformer attention 포함 여부 | 제외 |

해석상 중요한 점은 모든 non-LLM XAI output이 같은 30개 문장과 같은 순서로 정렬된 상태에서 비교되었다는 점이다. 이전 산출물의 stale sample 문제였던 case_010, case_024도 최신 입력 기준으로 다시 생성되었다.

## 3. 지표가 의미하는 것

| 지표 | 의미 | 해석 |
| --- | --- | --- |
| `topk_recall` | LLM evidence 어절 중 XAI top-k에 들어간 비율 | LLM이 본 핵심 근거를 XAI가 얼마나 놓치지 않았는가 |
| `jaccard` | LLM evidence set과 XAI top-k set의 교집합 비율 | 두 설명이 같은 단어 집합을 공유하는 정도 |
| `signed_cosine` | LLM evidence polarity와 XAI score 방향의 cosine | 같은 단어를 보더라도 긍정/부정 방향까지 맞는가 |
| `evidence_mass` | LLM evidence 어절에 배정된 XAI score mass | XAI 중요도가 LLM 근거 주변에 얼마나 집중되었는가 |
| `polarity_agreement` | 겹친 evidence 어절의 감정 부호 일치 | 겹친 근거의 방향성이 일치하는가 |
| `llm_match_score` | 위 지표를 합친 presentation ranking score | 방법 간 설명 정렬 정도를 비교하기 위한 요약값 |
| `prediction_llm_agreement_rate` | 모델 예측 감정과 LLM 감정의 일치율 | 설명 이전에 예측 방향 자체가 맞는가 |

즉 `llm_match_score`가 높다는 말은 "그 방법이 LLM처럼 설명했다"는 뜻이지, "그 방법이 절대적으로 옳다"는 뜻은 아니다. LLM도 기준 annotator가 아니라 외부 reference다.

## 4. 전체 순위

| rank | model | method | match | top-k | jaccard | signed | mass | polarity | pred |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | transformer | integrated_gradients_steps100 | 0.612 | 0.542 | 0.530 | 0.629 | 0.883 | 0.894 | 0.967 |
| 2 | transformer | occlusion | 0.607 | 0.526 | 0.501 | 0.604 | 0.944 | 0.928 | 0.967 |
| 3 | cnn | ngram_occlusion | 0.606 | 0.501 | 0.481 | 0.713 | 0.859 | 0.950 | 0.967 |
| 4 | transformer | integrated_gradients_steps50 | 0.604 | 0.542 | 0.530 | 0.569 | 0.881 | 0.850 | 0.967 |
| 5 | cnn | filter_activation | 0.580 | 0.488 | 0.465 | 0.634 | 0.849 | 0.889 | 0.967 |
| 6 | cnn | integrated_gradients_steps100 | 0.575 | 0.503 | 0.476 | 0.588 | 0.889 | 0.872 | 0.967 |
| 7 | cnn | integrated_gradients_steps50 | 0.575 | 0.503 | 0.476 | 0.588 | 0.889 | 0.872 | 0.967 |
| 8 | cnn | unigram_occlusion | 0.569 | 0.504 | 0.476 | 0.547 | 0.905 | 0.889 | 0.967 |
| 9 | fnn | integrated_gradients_steps50 | 0.552 | 0.476 | 0.442 | 0.587 | 0.853 | 0.922 | 0.933 |
| 10 | fnn | integrated_gradients_steps100 | 0.552 | 0.476 | 0.442 | 0.587 | 0.852 | 0.911 | 0.933 |
| 11 | fnn | occlusion | 0.547 | 0.476 | 0.440 | 0.559 | 0.868 | 0.906 | 0.933 |
| 12 | fnn | lime | 0.546 | 0.467 | 0.435 | 0.584 | 0.849 | 0.867 | 0.933 |

## 5. 모델군별 해석

| model | rows | mean match | top-k | jaccard | signed | mass | polarity | pred |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| transformer | 90 | 0.608 | 0.537 | 0.520 | 0.601 | 0.903 | 0.891 | 0.967 |
| cnn | 150 | 0.581 | 0.499 | 0.475 | 0.614 | 0.878 | 0.894 | 0.967 |
| fnn | 120 | 0.549 | 0.474 | 0.440 | 0.580 | 0.855 | 0.901 | 0.933 |

Transformer는 평균 match, top-k recall, Jaccard, evidence mass에서 가장 좋다. LLM이 선택한 근거 단어를 놓치지 않고 포착하는 능력이 가장 강하게 나타났다. 이는 Transformer가 문장 전체 문맥과 대비 구조를 보는 모델이기 때문에, LLM의 설명 단위와 비교적 잘 맞았기 때문으로 해석된다.

CNN은 평균 match에서는 Transformer보다 낮지만 signed cosine이 Transformer보다 약간 높다. 특히 `CNN N-gram Occlusion`은 전체 방법 중 signed cosine 1위, polarity agreement 1위다. CNN이 지역 구절 패턴을 강하게 쓰기 때문에, 감정 표현이 명시적인 n-gram에는 매우 강하게 반응한 것으로 보인다.

FNN은 평균 match가 가장 낮다. 단어 단위 feature를 사용하더라도 문맥 조합, 반어, 양보절 같은 구조를 반영하기 어렵고, 예측 감정 자체도 case_006, case_009에서 LLM과 자주 어긋났다. 그래서 설명 겹침과 예측 일치가 모두 상대적으로 낮게 나온다.

## 6. 방법별 핵심 해석

### Transformer Integrated Gradients 100 steps

이번 결과의 대표 방법으로 가장 적합하다. 평균 match 0.612로 1위이며, top-k recall 0.542와 Jaccard 0.530도 공동 최고다. LLM evidence와 같은 어절을 고르는 능력이 가장 안정적이라는 뜻이다.

50 steps와 비교하면 top-k recall, Jaccard는 같지만 signed cosine이 0.569에서 0.629로 오른다. 즉 step 수를 100으로 늘린 것이 단순히 같은 단어를 고르는 수준을 넘어, 감정 방향의 부호 정렬까지 개선한 것으로 해석할 수 있다.

### Transformer Occlusion

평균 match 0.607로 2위이며 evidence mass가 0.944로 전체 1위다. LLM이 중요하다고 본 evidence 어절에 XAI score가 가장 많이 몰려 있다는 뜻이다. 하지만 signed cosine은 CNN N-gram보다 낮다. 따라서 Transformer Occlusion은 "LLM 근거 주변을 넓게 잘 덮는 방법"이지, "감정 방향까지 가장 날카롭게 맞추는 방법"은 아니다.

### CNN N-gram Occlusion

평균 match 0.606으로 3위지만 사실상 상위권과 거의 차이가 없다. signed cosine 0.713, polarity agreement 0.950으로 방향성 지표는 전체 1위다. 이는 문장 전체 의미보다 감정 구절의 지역 패턴이 중요한 리뷰에서 특히 강하다. 발표에서는 Transformer IG100의 보조 근거로 사용하기 좋다. "Transformer가 LLM evidence와 가장 잘 겹쳤고, CNN N-gram은 감정 방향성을 가장 잘 맞췄다"는 식으로 설명하면 균형이 좋다.

### CNN Filter Activation

평균 match 0.580으로 CNN 내에서는 N-gram Occlusion 다음이다. case_001, case_010처럼 감정 신호가 직접적인 문장에서는 거의 완벽하게 맞는다. 필터가 특정 감정 표현 패턴에 반응하는 장점이 보인다. 다만 긴 대비 문장이나 복합 감정 문장에서는 top-k overlap이 제한된다.

### CNN IG와 Unigram Occlusion

CNN IG 50/100은 거의 같은 점수다. CNN 구조와 embedding 기준에서는 IG step 수 증가가 Transformer만큼 큰 차이를 만들지 않았다. Unigram Occlusion은 evidence mass는 높지만 signed cosine이 낮다. 단어 하나를 제거하는 방식은 LLM evidence 주변의 중요도는 잘 잡지만, 구절 전체의 감정 방향을 안정적으로 해석하기에는 한계가 있다.

### FNN 계열

FNN의 네 방법은 모두 하위권이다. LIME이 0.546으로 가장 낮고, IG/Occlusion도 0.55 전후에 머문다. FNN은 단어 조합과 문장 구조를 보는 능력이 약하기 때문에 LLM처럼 "하지만", "대신", "전체적으로는" 같은 담화 신호를 근거로 삼기 어렵다. 따라서 이번 비교에서 FNN은 주요 발표 모델보다는 baseline 역할로 두는 것이 적절하다.

## 7. 사례별 해석

### case_010: 직접 감정 표현에서는 모든 체계가 잘 맞음

문장: `개노잼임 ㅡㅡ`
LLM sentiment: negative
LLM evidence: `개노잼임`, `ㅡㅡ`

이 사례는 Transformer IG 100/50이 거의 1.0, CNN filter activation도 0.996으로 매우 높다. 감정 단서가 짧고 명시적이면 LLM과 XAI가 같은 토큰을 고른다. 이 결과는 pipeline이 정상적으로 어절 정렬과 evidence 비교를 수행하고 있음을 보여주는 sanity check 역할을 한다.

### case_006: 반어 표현에서 모델 차이가 크게 드러남

문장: `수면제 대신 보면 딱 좋은 훌륭한 영화입니다`
LLM sentiment: negative
LLM evidence: `수면제 대신 보면 딱 좋은`

이 문장은 겉으로는 `좋은`, `훌륭한`이라는 긍정어가 있지만, 실제 의미는 "지루해서 수면제 같다"는 반어적 부정이다. 전체 예측 일치율은 0.25에 그쳤다. CNN은 0/5, FNN은 0/4로 모두 LLM 감정과 어긋났고, Transformer만 3/3 모두 negative로 맞췄다.

이 사례는 Transformer가 문맥적 반어를 더 잘 처리한다는 근거다. 특히 Transformer Occlusion은 `수면제`, `보면`, `딱`을 top words로 잡아 0.625로 가장 높았다. 반대로 CNN N-gram Occlusion은 `좋은`, `훌륭한`, `영화입니다` 쪽에 반응해 0.179로 낮았다.

### case_009: 양보절과 최종 평가의 방향 문제

문장: `스토리가 지루하긴 한데 배우들은 멋있음`
LLM sentiment: positive
LLM evidence: `스토리가 지루하긴`, `배우들은 멋있음`

LLM은 `지루하긴`이라는 부정 평가를 인정하면서도, `한데` 뒤의 `배우들은 멋있음`이 최종적으로 강조된다고 보고 약한 positive로 판단했다. 전체 예측 일치율은 0.417이다. CNN은 5/5로 LLM과 같은 positive였지만, FNN과 Transformer는 모두 negative로 예측했다.

흥미로운 점은 Transformer IG가 top words로 `지루하긴`, `배우들은`, `멋있음`을 잘 잡았음에도 예측 sentiment는 negative였다는 점이다. 이 사례는 "근거 단어를 잘 잡는 것"과 "최종 polarity를 LLM처럼 해석하는 것"이 분리될 수 있음을 보여준다.

### case_024: 긴 mixed sentence에서 점수가 낮아짐

문장: `연기도 좋고 영상도 아름답고 음악도 훌륭했지만 정작 스토리가 너무 엉성해서 전체적으로는 실망스러웠습니다.`

LLM은 앞부분의 긍정 평가를 양보 표현으로 보고, `스토리가 너무 엉성해서`, `전체적으로는 실망스러웠습니다`를 최종 negative 근거로 해석했다. 평균 match는 0.454로 낮은 편이다.

가장 높은 방법은 CNN Filter Activation 0.522였고, CNN N-gram Occlusion도 0.512로 뒤를 이었다. 반면 Transformer Occlusion은 `훌륭했지만`, `정작`, `실망스러웠습니다`를 잡아 evidence 일부는 맞췄지만 점수는 0.237로 낮았다. 이 문장은 긍정 표면어와 부정 결론이 함께 있어, 어떤 방법이 "최종 결론"에 얼마나 가중치를 주는지가 점수를 크게 갈랐다.

### case_030: 예측은 맞아도 설명은 다를 수 있음

문장: `가슴 아픈 역사적 사실을 잘 담아낸 의미 있는 영화입니다. 먹먹하네요.`
LLM sentiment: positive
LLM evidence: `잘 담아낸`, `의미 있는 영화입니다.`, `먹먹하네요.`

모든 방법이 LLM sentiment와는 일치했지만, 평균 match는 0.293으로 전체 최저다. 일부 XAI 방법은 `가슴`, `아픈`, `사실을` 같은 소재 설명 단어에 높은 중요도를 줬고, LLM은 `잘 담아낸`, `의미 있는`, `먹먹하네요`처럼 평가와 감상에 해당하는 단어를 근거로 삼았다.

이 사례는 prediction agreement와 explanation agreement가 다르다는 점을 가장 잘 보여준다. 모델이 positive라고 맞게 예측했더라도, 그 예측을 뒷받침한 내부 근거가 LLM이 보는 의미적 근거와 다를 수 있다.

## 8. 왜 차이가 나는가

첫째, 모델 구조의 차이가 크다. Transformer는 self-attention 기반 문맥 표현을 쓰므로 양보, 반어, 최종 평가 같은 문장 구조를 상대적으로 잘 반영한다. CNN은 local n-gram 패턴에 강해서 명시적 감정 표현이나 짧은 구절 기반 근거에서 강하다. FNN은 문맥 조합 능력이 가장 약해, 단어별 긍부정 신호가 충돌하는 문장에서 흔들린다.

둘째, XAI 방법이 보는 단위가 다르다. Occlusion은 단어를 제거했을 때 예측이 얼마나 변하는지 보므로 evidence mass가 높게 나올 수 있다. Integrated Gradients는 embedding 경로상의 기여도를 누적하므로 전체 표현의 방향성이 반영된다. Filter Activation은 CNN 필터가 반응한 지역 패턴을 보여주기 때문에 특정 감정 표현에는 강하지만, 긴 담화 구조 전체를 설명하기는 어렵다.

셋째, LLM reference는 의미론적 설명에 가깝다. LLM은 `하지만`, `대신`, `전체적으로는` 같은 담화 신호를 이용해 최종 감정을 설명한다. 반면 XAI는 실제 모델 내부 decision signal을 보여준다. 따라서 LLM과 XAI가 다르다는 것은 반드시 XAI가 틀렸다는 뜻이 아니다. 오히려 모델이 인간이 기대하는 근거와 다른 단서를 사용하고 있다는 신호일 수 있다.

넷째, 한국어 영화 리뷰의 특성이 영향을 준다. 짧은 비속어, 이모티콘, 반어, 양보절, 복합 감정이 섞여 있다. 이런 문장에서는 단순 긍정어/부정어보다 문장 마지막 결론이나 담화 연결어가 중요하다. Transformer가 평균적으로 강한 이유도 이 지점과 연결된다.

## 9. 이번 결과가 말해주는 것과 말해주지 않는 것

말해주는 것은 다음과 같다.

- Transformer IG100은 LLM이 보는 감정 근거와 가장 안정적으로 정렬된다.
- Transformer Occlusion은 LLM evidence 주변에 가장 많은 중요도 mass를 배정한다.
- CNN N-gram Occlusion은 감정 방향 부호를 가장 잘 맞춘다.
- FNN은 LLM식 의미 설명과의 정렬이 가장 낮고, baseline 성격이 강하다.
- prediction이 맞는 것과 explanation이 맞는 것은 별개의 문제다.
- 반어, 양보, mixed sentence가 모델 설명 차이를 가장 크게 만든다.

말해주지 않는 것은 다음과 같다.

- 이 결과만으로 어떤 XAI 방법이 절대적으로 진실한 설명이라고 말할 수는 없다.
- LLM reference가 인간 정답 annotation을 대체한다고 볼 수는 없다.
- Attention 방식은 이번 비교에서 제외되었으므로 attention에 대한 결론은 내릴 수 없다.
- 모델 성능 자체의 우열을 말하는 평가는 아니다. 감정 예측 정확도와 설명 정렬은 별도 축이다.

## 10. 발표와 보고서에서 권장하는 해석

대표 결과는 `Transformer Integrated Gradients 100 steps`를 중심으로 제시하는 것이 좋다. 평균 match, top-k recall, Jaccard가 모두 상위권이므로 "LLM 근거와 가장 일관되게 겹친 방법"이라고 설명할 수 있다.

보조 결과로는 `CNN N-gram Occlusion`을 함께 제시하는 것이 좋다. 평균 순위는 3위지만 signed cosine과 polarity agreement가 1위이므로, "감정 방향성은 CNN의 구절 단위 occlusion이 가장 날카롭게 맞췄다"는 메시지를 만들 수 있다.

`Transformer Occlusion`은 evidence mass 관점의 보조 분석으로 적합하다. "LLM이 중요하다고 본 단어 주변에 가장 많은 중요도를 배정한 방법"이라고 해석하면 좋다.

FNN은 주요 성과 모델로 내세우기보다 baseline으로 두는 것이 좋다. 낮은 평균 match와 낮은 prediction agreement는 구조적 한계를 설명하는 데 유용하다.

최종 문장으로는 다음 해석이 가장 안전하다.

> 이번 LLM-XAI comparison은 Transformer 기반 설명, 특히 Integrated Gradients 100 steps가 LLM의 감정 판단 근거와 가장 안정적으로 정렬됨을 보여준다. 다만 CNN N-gram Occlusion은 감정 방향성에서는 가장 강했고, Transformer Occlusion은 evidence 집중도에서 가장 강했다. 따라서 하나의 절대적 승자보다, 문맥 근거 정렬은 Transformer IG100, 구절 polarity 정렬은 CNN N-gram, evidence mass 분석은 Transformer Occlusion으로 역할을 구분해 해석하는 것이 적절하다.

## 11. 다음 단계

1. 현재 clean worktree의 pipeline 수정 사항을 반영해야 한다. 특히 CNN IG 파일명 매핑이 최신 output 파일명과 맞아야 360 rows가 재현된다.
2. LLM reference가 하나뿐이므로, 가능하면 LLM 응답을 2-3회 반복하거나 다른 LLM reference와 비교해 안정성을 확인한다.
3. 사람이 직접 표시한 evidence annotation이 있다면 LLM reference와 함께 삼각 검증한다.
4. 평균 점수 차이가 작은 상위 3개 방법은 bootstrap confidence interval로 유의미한 차이인지 확인한다.
5. case_006, case_009, case_024, case_030을 qualitative slide로 사용하면 방법 차이를 가장 잘 설명할 수 있다.
