# LLM Comparison 1-2분 발표자료 구성 브리프

작성일: 2026-07-08
목적: LLM comparison 결과를 1-2분 발표용 슬라이드로 만들 때 필요한 핵심 자료, 설명 흐름, 시각자료 구성을 정리한다.

## 1. 발표 핵심 메시지

한 문장으로 말하면 다음과 같다.

> 작은 감정분류 모델의 XAI 결과가 LLM이 제시한 감정 판단 근거와 얼마나 겹치는지 비교했고, Transformer IG100이 가장 안정적으로 LLM evidence와 정렬되었으며, CNN N-gram Occlusion은 감정 방향성 지표에서 가장 강했다.

이 발표에서 강조할 점은 "정답률 비교"가 아니라 "설명 근거 정렬 비교"라는 점이다. LLM은 ground truth가 아니라 reference explanation이다.

## 2. 필수 배경 자료

| 항목 | 발표에 넣을 내용 |
| --- | --- |
| 분석 목적 | CNN/FNN/Transformer의 XAI가 LLM의 감정 판단 evidence와 얼마나 겹치는지 비교 |
| 데이터 | `selected_reviews.csv` 기준 30개 custom 영화 리뷰 문장 |
| LLM reference | `gpt-5.5-pro-2026-04-23`, prompt version `llm_sentiment_evidence_v1` |
| 비교 단위 | `model x XAI method` |
| 현재 비교 규모 | `xai_unified.jsonl` 360 rows, `llm_vectors.jsonl` 30 rows, `llm_xai_overlap_scores.csv` 360 rows, `llm_xai_method_summary.csv` 12 rows |
| 주요 지표 | `llm_match_score`, `topk_recall`, `jaccard`, `signed_cosine`, `evidence_mass`, `polarity_agreement` |
| 제외 범위 | Transformer Attention은 최종 ranking에서 제외 |
| 해석 주의 | LLM evidence는 정답 annotation이 아니라 외부 설명 기준 |

## 3. 1-2분 발표 흐름

| 시간 | 슬라이드/화면 | 말할 내용 |
| --- | --- | --- |
| 0:00-0:15 | 문제 제기 | 기존 XAI는 모델별로 중요 단어를 보여주지만, 그 단어가 사람이 읽는 감정 근거와 얼마나 맞는지는 별도 확인이 필요하다. |
| 0:15-0:35 | 파이프라인 | 30개 리뷰를 LLM에게 보여주고 감정 판단 근거 어절을 받았다. 그 뒤 같은 문장의 CNN/FNN/Transformer XAI top words와 비교했다. |
| 0:35-1:05 | 핵심 결과 | 평균 LLM match score 기준 1위는 Transformer IG100 0.612, 2위는 Transformer Occlusion 0.607, 3위는 CNN N-gram Occlusion 0.606이다. |
| 1:05-1:30 | 해석 | Transformer는 문맥 evidence 정렬이 강했고, CNN N-gram은 signed cosine 0.713과 polarity agreement 0.950으로 감정 방향성에서 가장 강했다. FNN은 baseline 성격이 강했다. |
| 1:30-2:00 | 결론 | 단일 절대 우승자보다 역할별로 해석하는 것이 안전하다. 문맥 근거 정렬은 Transformer IG100, evidence mass는 Transformer Occlusion, polarity 정렬은 CNN N-gram이 좋다. |

## 4. 발표에 반드시 들어갈 결과 숫자

### 4.1 Method-level 핵심 순위

| rank | model | method | mean match | top-k | jaccard | signed | mass | polarity |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | Transformer | Integrated Gradients 100 steps | 0.612 | 0.542 | 0.530 | 0.629 | 0.883 | 0.894 |
| 2 | Transformer | Occlusion | 0.607 | 0.526 | 0.501 | 0.604 | 0.944 | 0.928 |
| 3 | CNN | N-gram Occlusion | 0.606 | 0.501 | 0.481 | 0.713 | 0.859 | 0.950 |
| 4 | Transformer | Integrated Gradients 50 steps | 0.604 | 0.542 | 0.530 | 0.569 | 0.881 | 0.850 |
| 5 | CNN | Filter Activation | 0.580 | 0.488 | 0.465 | 0.634 | 0.849 | 0.889 |

발표에서는 상위 3개만 보여줘도 충분하다. 4-5위는 질문 대응용 backup으로 두면 된다.

### 4.2 Model-level 평균

| model | rows | mean match | mean signed cosine | mean evidence mass | prediction agreement |
| --- | ---: | ---: | ---: | ---: | ---: |
| Transformer | 90 | 0.608 | 0.601 | 0.903 | 0.967 |
| CNN | 150 | 0.581 | 0.614 | 0.878 | 0.967 |
| FNN | 120 | 0.549 | 0.580 | 0.855 | 0.933 |

해석은 다음처럼 짧게 말한다.

- Transformer: LLM evidence와 전체적으로 가장 잘 맞음.
- CNN: 평균 match는 Transformer보다 낮지만 signed cosine은 더 높음.
- FNN: LLM식 문맥 근거와의 정렬이 가장 낮아 baseline으로 해석.

### 4.3 대표 사례

| case | 왜 보여줄 만한가 | 핵심 수치 | 발표용 메시지 |
| --- | --- | --- | --- |
| `case_010` | 명시적 감정 표현 sanity check | 평균 match 0.984, prediction agreement 1.000 | 감정 단서가 직접적이면 LLM과 XAI가 거의 같은 근거를 고른다. |
| `case_006` | 반어 표현에서 모델 차이가 큼 | 평균 match 0.330, prediction agreement 0.250 | 겉보기 긍정어가 있어도 실제 감정은 부정일 수 있으며 Transformer가 문맥을 더 잘 잡는다. |
| `case_024` | 긴 mixed sentence | 평균 match 0.454, prediction agreement 1.000 | 예측은 맞아도 어떤 근거에 가중치를 두는지는 방법별로 달라진다. |
| `case_030` | prediction과 explanation 분리 | 평균 match 0.293, prediction agreement 1.000 | 예측이 맞아도 LLM이 본 근거와 XAI 근거는 다를 수 있다. |

1-2분 발표에서는 `case_006` 또는 `case_030` 하나만 쓰는 것이 좋다. 시간이 매우 짧으면 사례 없이 순위 그래프만 보여준다.

## 5. 삽입할 그래프와 시각자료 구성

| 우선순위 | 시각자료 | 사용할 파일 | 구성 방법 | 화면에서 전달할 메시지 |
| ---: | --- | --- | --- | --- |
| 1 | LLM-XAI 비교 파이프라인 다이어그램 | `LLM_COMPARISON_PIPELINE_GUIDE.md` 내용 기반 | `selected_reviews.csv -> LLM prompt -> LLM evidence vector -> XAI unified output -> overlap metrics` 5단계 화살표로 구성. 각 단계 아래 산출 파일명을 작게 표시한다. | LLM은 XAI 결과를 보지 않고 독립적으로 evidence를 만든 뒤, 나중에 XAI와 비교한다. |
| 2 | Method-level mean match bar chart | `comparison_outputs/llm_xai_method_summary.csv` | x축은 상위 5개 method, y축은 mean LLM match. 색상은 모델별로 구분한다. Transformer는 파란색, CNN은 초록색, FNN은 회색 계열로 둔다. y축은 0.50-0.63 범위 또는 0-0.65 범위를 사용하고, 상위 3개 값 0.612/0.607/0.606을 막대 위에 표시한다. | Transformer IG100이 1위지만 상위 3개 차이는 작다. |
| 3 | 역할별 강점 비교 미니 표 또는 레이더형 카드 | `llm_xai_method_summary.csv` | 세 카드를 나란히 배치한다. `Transformer IG100: match/top-k/Jaccard`, `Transformer Occlusion: evidence mass`, `CNN N-gram: signed cosine/polarity`처럼 각자 1개 강점을 크게 표시한다. | 하나의 절대 우승자가 아니라 지표별 역할이 다르다. |
| 4 | Model-level average bar chart | `comparison_outputs/llm_xai_overlap_scores.csv` | Transformer 0.608, CNN 0.581, FNN 0.549 세 막대만 표시한다. 막대 아래에 rows 수를 함께 적는다: Transformer 90, CNN 150, FNN 120. | 모델군 평균으로는 Transformer가 LLM reference와 가장 잘 맞는다. |
| 5 | Case evidence visual | `XAI/outputs_graph/llm_evidence/sentence_6.png` 또는 `sentence_30.png`, `qualitative_case_report.md` | 왼쪽에는 LLM evidence 이미지, 오른쪽에는 해당 case의 XAI top words 요약 2-3줄을 배치한다. `case_006`은 반어, `case_030`은 예측은 맞지만 설명이 다름을 보여주는 용도로 쓴다. | prediction agreement와 explanation agreement는 별개의 문제다. |
| 6 | Backup: 전체 method ranking table | `llm_xai_method_summary.csv` | 발표 본문에는 넣지 말고 appendix에 전체 12개 method 표를 둔다. FNN 계열이 하위권임을 질문 대응용으로 확인할 수 있게 한다. | 상세 질의가 들어왔을 때 전체 순위를 보여준다. |

시각자료 제작 시 주의할 점:

- `llm_match_score`는 발표용 ranking score이므로 "정답률"이라고 쓰면 안 된다.
- y축을 너무 좁게 잡으면 0.612와 0.606 차이가 과장된다. 좁은 축을 쓰면 반드시 "상위권 차이는 작음"이라는 주석을 넣는다.
- Attention은 이번 ranking에 포함하지 않는다.
- case 이미지는 LLM evidence만 보여주면 XAI와 비교가 약하므로, `qualitative_case_report.md`의 XAI top words를 함께 붙인다.

## 6. 추천 슬라이드 구성

### 슬라이드 1: 실험 목적과 파이프라인

제목: "XAI 설명은 LLM의 감정 근거와 얼마나 겹치는가?"

포함 요소:

- 30개 영화 리뷰 문장
- LLM reference evidence 생성
- CNN/FNN/Transformer XAI 결과와 비교
- 파이프라인 다이어그램

말할 문장:

> 이 실험은 정답률을 보는 것이 아니라, 각 XAI가 LLM이 감정 판단 근거로 본 어절을 얼마나 같이 잡는지 비교한 것입니다.

### 슬라이드 2: 핵심 결과

제목: "Transformer IG100이 평균적으로 가장 안정적"

포함 요소:

- Method-level top 5 bar chart
- 상위 3개 수치: 0.612, 0.607, 0.606
- 역할별 강점 3개 카드

말할 문장:

> 평균 match는 Transformer IG100이 가장 높았지만, Transformer Occlusion과 CNN N-gram Occlusion도 거의 같은 수준입니다. 차이는 우승자 하나보다 역할별 강점으로 보는 것이 안전합니다.

### 슬라이드 3: 해석과 결론

제목: "문맥 정렬은 Transformer, 방향성은 CNN N-gram"

포함 요소:

- Model-level average bar chart
- 선택 사례 1개: `case_006` 또는 `case_030`
- 최종 한 줄 결론

말할 문장:

> Transformer는 문맥과 대비 구조를 반영해 LLM evidence와 잘 정렬되었고, CNN N-gram은 감정 방향 부호를 가장 잘 맞췄습니다. FNN은 내부적으로 일관된 baseline이지만 LLM식 의미 근거와는 덜 맞았습니다.

## 7. 1분 발표 스크립트

> 이번 LLM comparison은 CNN, FNN, Transformer의 XAI 결과가 LLM이 감정 판단 근거로 지목한 어절과 얼마나 겹치는지 본 실험입니다. LLM은 정답 라벨이 아니라 reference explanation으로 사용했고, 30개 리뷰 문장에 대해 LLM evidence vector와 XAI score vector를 비교했습니다.
>
> 결과적으로 mean LLM match score는 Transformer Integrated Gradients 100 steps가 0.612로 1위였습니다. 다만 Transformer Occlusion 0.607, CNN N-gram Occlusion 0.606과 차이가 작아서 단일 승자보다는 역할별 해석이 적절합니다.
>
> Transformer IG100은 LLM evidence와 가장 안정적으로 겹쳤고, Transformer Occlusion은 LLM evidence 위치에 가장 많은 score mass를 배정했습니다. CNN N-gram Occlusion은 signed cosine 0.713, polarity agreement 0.950으로 감정 방향성에서는 가장 강했습니다. 따라서 발표 결론은 문맥 근거 정렬은 Transformer IG100, polarity 정렬은 CNN N-gram, evidence mass는 Transformer Occlusion으로 나누어 보는 것입니다.

## 8. 2분 발표 스크립트

> 기존 XAI 결과는 각 모델이 어떤 단어를 중요하게 봤는지는 보여주지만, 그 설명이 사람이 읽는 감정 판단 근거와 얼마나 가까운지는 별도로 확인해야 합니다. 그래서 이번 실험에서는 LLM을 reference explanation으로 두고, CNN/FNN/Transformer XAI와 비교했습니다.
>
> 절차는 간단합니다. 먼저 30개 영화 리뷰 문장을 LLM에게 보여주고, 감정 라벨과 근거 어절, 그리고 각 근거의 polarity를 JSON으로 받았습니다. 이때 LLM에게 XAI 결과는 보여주지 않았습니다. 그 다음 LLM evidence를 벡터로 바꾸고, 각 XAI method의 top words와 score vector를 비교했습니다.
>
> 핵심 결과는 mean LLM match score 기준 Transformer Integrated Gradients 100 steps가 0.612로 1위라는 점입니다. 2위는 Transformer Occlusion 0.607, 3위는 CNN N-gram Occlusion 0.606입니다. 상위 3개 차이가 매우 작기 때문에, 이 결과는 단일 절대 우승자보다 역할별 강점으로 해석하는 것이 좋습니다.
>
> 역할별로 보면 Transformer IG100은 top-k recall과 Jaccard가 높아 LLM evidence와 같은 어절을 가장 안정적으로 고릅니다. Transformer Occlusion은 evidence mass가 0.944로 가장 높아 LLM evidence 주변에 중요도를 많이 배정합니다. CNN N-gram Occlusion은 signed cosine 0.713, polarity agreement 0.950으로 감정 방향성을 가장 잘 맞춥니다.
>
> 결론적으로 Transformer는 문맥 기반 evidence 정렬에 강하고, CNN은 명시적 감정 구절의 방향성 포착에 강합니다. FNN은 이번 비교에서는 LLM식 의미 근거와 정렬이 낮아 baseline으로 보는 것이 적절합니다.

## 9. 발표에서 피해야 할 표현

| 피해야 할 표현 | 안전한 표현 |
| --- | --- |
| LLM이 정답이다 | LLM을 사람이 읽기 쉬운 reference explanation으로 사용했다 |
| Transformer가 무조건 제일 좋다 | Transformer IG100이 LLM evidence와 가장 안정적으로 정렬되었다 |
| CNN은 Transformer보다 나쁘다 | CNN N-gram은 감정 방향성 지표에서 가장 강했다 |
| FNN 설명은 틀렸다 | FNN은 LLM식 문맥 evidence와의 정렬이 낮아 baseline 성격이 강하다 |
| 이 점수는 정확도다 | 이 점수는 LLM reference와 XAI explanation의 정렬 score다 |

## 10. 참고해야 할 파일

| 목적 | 파일 |
| --- | --- |
| 발표 브리프 원본 | `XAI/LLMComparison/LLM_COMPARISON_PRESENTATION_BRIEF_KO.md` |
| 결과 해석 상세 보고서 | `XAI/LLMComparison/LLM_COMPARISON_RESULT_ANALYSIS_REPORT_KO.md` |
| Model Analysis와 비교 | `XAI/LLMComparison/LLM_COMPARISON_VS_MODEL_ANALYSIS_REPORT_KO.md` |
| 파이프라인 설명 | `XAI/LLMComparison/LLM_COMPARISON_PIPELINE_GUIDE.md` |
| method-level 결과 | `XAI/LLMComparison/comparison_outputs/llm_xai_method_summary.csv` |
| row-level 결과 | `XAI/LLMComparison/comparison_outputs/llm_xai_overlap_scores.csv` |
| 정성 사례 | `XAI/LLMComparison/comparison_outputs/qualitative_case_report.md` |
| LLM evidence 시각화 | `XAI/outputs_graph/llm_evidence/` |
| LLM evidence index | `XAI/outputs_graph/llm_index.html` |
