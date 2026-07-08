# LLM Comparison과 Model Analysis 비교 리포트

작성일: 2026-07-08
기준 산출물: 현재 로컬 `XAI/LLMComparison/comparison_outputs` 및 `XAI/Model_Analysis/outputs` 결과

## 1. 결론 요약

`LLMComparison`과 `Model_Analysis`는 같은 XAI 산출물을 일부 공유하지만, 분석 질문이 다르다.

`Model_Analysis`는 모델과 XAI 출력 자체의 구조적 특성을 본다. 예측 확신도, 예측 방향과 설명 부호의 정합도, 설명 score가 특정 단어에 얼마나 집중되는지, 여러 XAI 방법이 같은 단어를 고르는지 등을 계산한다. 즉 "이 모델의 설명이 내부적으로 어떤 모양을 갖는가"를 보는 분석이다.

`LLMComparison`은 OpenAI API로 수집한 LLM의 감정 판단 근거를 reference explanation으로 두고, CNN/FNN/Transformer XAI가 같은 어절과 같은 감정 방향을 잡는지 비교한다. 즉 "작은 모델의 XAI 설명이 LLM이 사람이 읽기 쉽게 제시한 감정 근거와 얼마나 가까운가"를 보는 분석이다.

따라서 두 결과가 다르게 보이는 것은 모순이 아니다. `Model_Analysis`에서 FNN이 XAI 방법 간 일관성 1위로 나오더라도, `LLMComparison`에서는 FNN이 LLM식 감정 근거와 덜 겹칠 수 있다. 전자는 내부 일관성이고, 후자는 외부 의미 정렬이다.

## 2. 분석 목적 차이

| 구분 | Model Analysis | LLM Comparison |
| --- | --- | --- |
| 핵심 질문 | 모델/XAI 출력 자체가 어떤 특성을 갖는가 | XAI가 LLM의 감정 판단 근거와 얼마나 겹치는가 |
| 비교 기준 | 모델의 prediction, probability, 단어별 XAI score | LLM sentiment, LLM evidence vector, XAI score |
| 정답 라벨 사용 | 사용하지 않음 | 사용하지 않음 |
| LLM 사용 | 사용하지 않음 | reference explanation으로 사용 |
| 주 분석 단위 | 모델별 평균 특성, 모델 내부 XAI 방법 특성 | `model x method`별 LLM evidence 정렬 |
| 대표 산출물 | `model_strength_report.md`, `model_strength_summary.csv` | `llm_xai_method_summary.csv`, `llm_xai_evaluation_report.md` |

두 분석 모두 분류 정확도 평가는 아니다. `Model_Analysis`는 정답 라벨 없이 모델이 자기 예측에 대해 얼마나 확신하는지와 설명 score의 형태를 본다. `LLMComparison`도 LLM을 정답으로 놓지 않고, 자연어 설명 reference로만 사용한다.

## 3. 진행 흐름 차이

### 3.1 Model Analysis 진행

`Model_Analysis`는 `XAI/outputs_json/output_*.json`을 직접 읽는다.

1. 모델별 XAI JSON 파일을 읽는다.
2. prediction, probability, words, scores를 추출한다.
3. 최종 모델 비교에서는 모든 모델에 공통으로 존재하는 XAI 방법만 사용한다.
4. 현재 공통 방법은 `Integrated Gradients 100 steps`, `Integrated Gradients 50 steps`, `Occlusion`이다.
5. CNN의 모델 간 비교용 `Occlusion` 대표값은 `Unigram Occlusion`으로 매핑된다.
6. Attention, Filter Activation, LIME처럼 특정 모델에만 있거나 참고 성격이 강한 방법은 최종 모델 순위에서는 제외하고, 방법별 참고표에는 남긴다.
7. 공통 입력 문장 30개에 대해 모델별 평균 지표를 계산한다.

최종 모델 비교의 목적은 "CNN, FNN, Transformer 중 어떤 모델이 어떤 설명 특성에서 강한가"를 보는 것이다.

### 3.2 LLM Comparison 진행

`LLMComparison`은 XAI 결과를 LLM evidence와 비교할 수 있는 공통 형식으로 변환한 뒤 분석한다.

1. `selected_reviews.csv`의 30개 분석 문장을 기준으로 잡는다.
2. `XAI/outputs_json`의 CNN/FNN/Transformer XAI 결과를 `xai_unified.jsonl`로 통합한다.
3. LLM prompt를 생성한다. 이때 LLM에게 XAI 결과는 보여주지 않는다.
4. LLM이 원문과 어절 리스트만 보고 sentiment, evidence word index, polarity, strength를 JSON으로 반환한다.
5. LLM 응답을 `llm_vectors.jsonl`로 정규화한다.
6. `xai_unified.jsonl`과 `llm_vectors.jsonl`을 `sample_id` 기준으로 join한다.
7. LLM evidence와 XAI top words 및 score vector를 비교한다.

현재 LLM comparison 산출물 기준으로 `xai_unified.jsonl`은 360 rows, `llm_vectors.jsonl`은 30 rows, `llm_xai_overlap_scores.csv`는 360 rows, `llm_xai_method_summary.csv`는 12 rows다.

## 4. 지표 차이

### 4.1 Model Analysis 지표

| 지표 | 의미 | 해석 |
| --- | --- | --- |
| 예측 확신도 | 모델이 예측 클래스에 부여한 평균 probability | 높을수록 모델이 자기 예측을 강하게 믿음 |
| 예측 방향-설명 정합도 | 예측 감성과 같은 방향의 attribution mass 비율 | 높을수록 설명 score가 모델 예측 방향을 잘 지지함 |
| 핵심 단어 집중도 | 가장 큰 절대 score 단어 하나가 전체 설명량에서 차지하는 비율 | 높을수록 단일 핵심 단어에 설명이 선명하게 몰림 |
| 유효 단어 커버리지 | 전체 설명량의 2% 이상을 가진 단어 비율 | 높을수록 여러 단어에 의미 있는 설명 신호가 퍼짐 |
| 상위 3개 단어 집중도 | 절대 score 상위 3개 단어의 설명량 비율 | 높을수록 핵심 단어 3개에 설명이 집중됨 |
| XAI 방법 간 일관성 | 같은 모델 안에서 여러 XAI 방법의 top-3 단어와 score 순위가 비슷한 정도 | 높을수록 방법을 바꿔도 비슷한 설명이 나옴 |

이 지표들은 모델 내부 설명의 형태를 본다. LLM이 어떤 단어를 감정 근거로 봤는지는 고려하지 않는다.

### 4.2 LLM Comparison 지표

| 지표 | 의미 | 해석 |
| --- | --- | --- |
| `topk_recall` | LLM evidence 어절 중 XAI top-k에 포함된 비율 | LLM이 본 핵심 근거를 XAI가 얼마나 놓치지 않았는가 |
| `jaccard` | LLM evidence set과 XAI top-k set의 겹침 | evidence set의 대칭적 유사도 |
| `signed_cosine` | LLM evidence vector와 XAI score vector의 방향 유사도 | 어절 위치와 긍정/부정 방향이 함께 맞는가 |
| `evidence_mass` | LLM evidence 위치에 배정된 XAI 절대 score mass | XAI 중요도가 LLM 근거 주변에 얼마나 집중됐는가 |
| `polarity_agreement` | 겹친 evidence 어절의 감정 부호 일치율 | 같은 단어를 볼 때 감정 방향도 같은가 |
| `llm_match_score` | 위 지표를 결합한 ranking score | LLM reference와의 설명 정렬 정도 |

`llm_match_score`가 높다는 말은 "그 XAI 방법이 LLM처럼 설명했다"에 가깝다. "그 방법이 절대적으로 옳다"는 뜻은 아니다.

## 5. 결과 비교

### 5.1 Model Analysis 결과

`Model_Analysis`의 부문별 우수 모델은 다음과 같다.

| 평가 부문 | 우수 모델 | 점수 |
| --- | --- | ---: |
| 예측 확신도 | Transformer | 0.9721 |
| 예측 방향-설명 정합도 | Transformer | 0.8620 |
| 핵심 단어 집중도 | CNN | 0.5074 |
| 유효 단어 커버리지 | FNN | 0.8607 |
| 상위 3개 단어 집중도 | CNN | 0.8156 |
| XAI 방법 간 일관성 | FNN | 0.8648 |

모델별 요약은 다음과 같다.

| 모델 | 예측 확신도 | 예측 방향-설명 정합도 | 핵심 단어 집중도 | 유효 단어 커버리지 | 상위 3개 단어 집중도 | 방법 간 일관성 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| CNN | 0.9429 | 0.8609 | 0.5074 | 0.7860 | 0.8156 | 0.8015 |
| FNN | 0.9092 | 0.8190 | 0.4216 | 0.8607 | 0.7760 | 0.8648 |
| Transformer | 0.9721 | 0.8620 | 0.4382 | 0.8599 | 0.7754 | 0.5776 |

이 결과만 보면 Transformer는 예측 확신도와 예측 방향-설명 정합도에서 강하고, CNN은 설명 집중도에서 강하며, FNN은 커버리지와 방법 간 일관성에서 강하다.

### 5.2 LLM Comparison 결과

`LLMComparison`의 method-level 상위 결과는 다음과 같다.

| rank | model | method | mean LLM match | top-k | jaccard | signed | mass | polarity |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | Transformer | Integrated Gradients 100 steps | 0.612 | 0.542 | 0.530 | 0.629 | 0.883 | 0.894 |
| 2 | Transformer | Occlusion | 0.607 | 0.526 | 0.501 | 0.604 | 0.944 | 0.928 |
| 3 | CNN | N-gram Occlusion | 0.606 | 0.501 | 0.481 | 0.713 | 0.859 | 0.950 |
| 4 | Transformer | Integrated Gradients 50 steps | 0.604 | 0.542 | 0.530 | 0.569 | 0.881 | 0.850 |
| 5 | CNN | Filter Activation | 0.580 | 0.488 | 0.465 | 0.634 | 0.849 | 0.889 |

모델군 평균은 다음과 같이 해석할 수 있다.

| 모델군 | 평균 LLM match | 해석 |
| --- | ---: | --- |
| Transformer | 0.608 | LLM evidence와 가장 안정적으로 겹침 |
| CNN | 0.581 | n-gram 기반 감정 방향성에서 강함 |
| FNN | 0.549 | LLM식 문맥 근거와의 정렬이 가장 낮음 |

이 결과는 Transformer IG100이 대표 방법으로 가장 적합하고, Transformer Occlusion은 evidence mass 관점에서 강하며, CNN N-gram Occlusion은 감정 방향성 부호에서 강하다는 메시지를 준다.

## 6. 왜 결과가 다르게 보이는가

### 6.1 FNN: 내부 일관성은 높지만 LLM 근거 정렬은 낮음

`Model_Analysis`에서 FNN은 `유효 단어 커버리지`와 `XAI 방법 간 일관성`에서 1위다. 이는 FNN의 여러 XAI 방법이 비교적 비슷한 top words를 고르고, 설명 신호가 여러 단어에 넓게 분포한다는 뜻이다.

하지만 `LLMComparison`에서 FNN은 평균 match가 가장 낮다. 이는 FNN 설명이 내부적으로 일관되더라도, LLM이 감정 근거로 본 어절과 반드시 잘 겹치지는 않는다는 뜻이다. 특히 반어, 양보절, 최종 평가처럼 문맥 구조가 중요한 문장에서 FNN은 LLM식 의미 근거와 멀어질 수 있다.

따라서 "FNN은 설명이 안정적이다"와 "FNN은 LLM식 감정 근거와 덜 맞는다"는 동시에 성립할 수 있다.

### 6.2 CNN: 집중도와 polarity는 강하지만 전체 문맥 정렬은 Transformer보다 낮음

`Model_Analysis`에서 CNN은 `핵심 단어 집중도`와 `상위 3개 단어 집중도`에서 1위다. 이는 CNN 설명이 적은 수의 강한 단어 또는 구절에 잘 모인다는 뜻이다.

`LLMComparison`에서도 CNN의 장점은 유지된다. 특히 `CNN N-gram Occlusion`은 signed cosine 0.713, polarity agreement 0.950으로 감정 방향성 지표가 가장 강하다. CNN이 지역 구절 패턴에 강하기 때문에 명시적 감정 표현에는 날카롭게 반응한다.

다만 전체 LLM match에서는 Transformer가 앞선다. CNN은 local n-gram에는 강하지만, 문장 전체의 양보 구조나 반어 구조를 반영하는 데는 Transformer보다 불리하다.

### 6.3 Transformer: 외부 의미 정렬은 높지만 방법 간 일관성은 낮음

`Model_Analysis`에서 Transformer는 예측 확신도와 예측 방향-설명 정합도에서 1위다. `LLMComparison`에서도 평균 LLM match가 가장 높다. 즉 Transformer는 모델 예측 측면에서도 강하고, LLM reference와의 설명 정렬 측면에서도 가장 안정적이다.

반대로 `Model_Analysis`의 XAI 방법 간 일관성은 Transformer가 가장 낮다. 이는 Transformer의 IG와 Occlusion이 항상 같은 단어를 고르지는 않는다는 뜻이다. 하지만 이것이 곧 설명이 나쁘다는 의미는 아니다. 문맥 모델에서는 gradient 기반 방법과 제거 기반 방법이 서로 다른 관점의 근거를 잡을 수 있다.

## 7. 해석상 주의할 점

첫째, 두 분석 모두 정답 라벨 기반 성능 평가가 아니다. Model Analysis는 모델 출력과 XAI score 형태를 보고, LLMComparison은 LLM reference와의 설명 정렬을 본다.

둘째, LLMComparison의 LLM evidence는 ground truth가 아니다. LLM은 사람이 읽기 쉬운 외부 reference 설명이며, 그 자체가 절대 정답은 아니다.

셋째, Model Analysis의 CNN `Occlusion` 대표값과 LLMComparison의 CNN occlusion 결과를 1:1로 혼동하면 안 된다. Model Analysis의 최종 모델 비교에서는 CNN의 `Unigram Occlusion`을 공통 `Occlusion`으로 매핑한다. LLMComparison은 `unigram_occlusion`과 `ngram_occlusion`을 별도 방법으로 비교한다.

넷째, Attention은 LLMComparison의 최종 ranking에서 제외되어 있다. Attention score는 다른 attribution score와 의미가 달라 같은 ranking 표에 섞기 어렵기 때문이다.

다섯째, 상위권 차이는 작다. LLMComparison에서 `Transformer IG100` 0.612, `Transformer Occlusion` 0.607, `CNN N-gram Occlusion` 0.606은 거의 붙어 있다. 발표에서는 단일 절대 승자보다 역할별 강점을 나누는 해석이 안전하다.

## 8. 발표용 정리

발표에서는 두 분석을 다음처럼 나누어 설명하는 것이 가장 명확하다.

| 메시지 | 근거 분석 | 설명 |
| --- | --- | --- |
| Transformer는 전체적으로 가장 안정적인 모델이다 | Model Analysis, LLM Comparison | 예측 확신도와 예측 방향-설명 정합도가 높고, LLM evidence와의 평균 match도 가장 높다 |
| CNN은 짧고 명시적인 감정 구절에 강하다 | Model Analysis, LLM Comparison | 설명 집중도가 높고, CNN N-gram Occlusion은 polarity 지표가 가장 강하다 |
| FNN은 baseline으로 두는 것이 적절하다 | LLM Comparison | 내부 일관성은 높지만 LLM식 감정 근거와의 정렬이 낮다 |
| XAI 방법별 역할을 구분해야 한다 | LLM Comparison | IG100은 문맥 evidence 정렬, Occlusion은 evidence mass, CNN N-gram은 polarity 정렬에 강하다 |

최종 문장으로는 다음 표현이 가장 안전하다.

> Model Analysis는 모델 내부 설명 특성을 비교한 결과이고, LLMComparison은 LLM reference와의 의미적 근거 정렬을 비교한 결과이다. 내부 특성에서는 Transformer, CNN, FNN이 각각 다른 강점을 보이지만, LLM이 제시한 감정 판단 근거와의 정렬에서는 Transformer IG100이 가장 안정적이었다. 다만 CNN N-gram Occlusion은 감정 방향성에서는 가장 강하므로, 하나의 절대적 우승자보다 Transformer IG100은 문맥 근거 정렬, CNN N-gram은 polarity 정렬, Transformer Occlusion은 evidence mass 분석으로 역할을 나누어 해석하는 것이 적절하다.

## 9. 문서와 산출물 위치

| 용도 | 파일 |
| --- | --- |
| LLM comparison 결과 해석 | `XAI/LLMComparison/LLM_COMPARISON_RESULT_ANALYSIS_REPORT_KO.md` |
| LLM comparison 파이프라인 설명 | `XAI/LLMComparison/LLM_COMPARISON_PIPELINE_GUIDE.md` |
| LLM-XAI method-level summary | `XAI/LLMComparison/comparison_outputs/llm_xai_method_summary.csv` |
| LLM-XAI row-level scores | `XAI/LLMComparison/comparison_outputs/llm_xai_overlap_scores.csv` |
| 정성 사례 리포트 | `XAI/LLMComparison/comparison_outputs/qualitative_case_report.md` |
| Model Analysis 결과 리포트 | `XAI/Model_Analysis/outputs/model_strength_report.md` |
| Model Analysis 방법론 | `XAI/Model_Analysis/outputs/model_analysis_methodology.md` |
| 모델별 XAI 방법 프로파일 | `XAI/Model_Analysis/outputs/xai_method_profile_by_model.md` |
