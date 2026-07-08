# LLM-XAI Qualitative Case Report

## case_001

text: 이 영화 정말 재미있어요 추천합니다

- LLM sentiment: positive
- LLM evidence: 정말 재미있어요, 추천합니다
- LLM reason: 재미있다고 평가하고 추천 의사를 밝혀 전반적으로 긍정적인 리뷰입니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| cnn | filter_activation | positive | 정말 , 재미있어요 , 추천합니다 | 0.999423 |
| cnn | ngram_occlusion | positive | 정말 , 재미있어요 , 추천합니다 | 0.973118 |
| transformer | integrated_gradients_steps50 | positive | 정말 , 재미있어요 , 추천합니다 | 0.949574 |
| transformer | integrated_gradients_steps100 | positive | 정말 , 재미있어요 , 추천합니다 | 0.949521 |
| fnn | integrated_gradients_steps50 | positive | 영화 , 재미있어요 , 추천합니다 | 0.694362 |
| fnn | integrated_gradients_steps100 | positive | 영화 , 재미있어요 , 추천합니다 | 0.693115 |
| transformer | occlusion | positive | 영화 , 재미있어요 , 추천합니다 | 0.688232 |
| cnn | integrated_gradients_steps50 | positive | 영화 , 정말 , 재미있어요 | 0.660879 |
| cnn | integrated_gradients_steps100 | positive | 영화 , 정말 , 재미있어요 | 0.660639 |
| fnn | lime | positive | 영화 , 재미있어요 , 추천합니다 | 0.660489 |
| cnn | unigram_occlusion | positive | 영화 , 정말 , 재미있어요 | 0.659106 |
| fnn | occlusion | positive | 영화 , 재미있어요 , 추천합니다 | 0.656038 |

## case_002

text: 스토리가 지루하고 배우들 연기도 별로네요

- LLM sentiment: negative
- LLM evidence: 스토리가 지루하고, 배우들 연기도 별로네요
- LLM reason: 스토리와 연기 모두 부정적으로 평가하고 있어 전체 감정은 negative입니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| cnn | ngram_occlusion | negative | 배우들 , 연기도 , 별로네요 | 0.722685 |
| transformer | occlusion | negative | 지루하고 , 연기도 , 별로네요 | 0.715905 |
| cnn | filter_activation | negative | 지루하고 , 배우들 , 별로네요 | 0.71306 |
| fnn | lime | negative | 지루하고 , 배우들 , 별로네요 | 0.697209 |
| fnn | integrated_gradients_steps100 | negative | 지루하고 , 배우들 , 별로네요 | 0.675723 |
| cnn | integrated_gradients_steps100 | negative | 스토리가 , 지루하고 , 별로네요 | 0.675274 |
| cnn | integrated_gradients_steps50 | negative | 스토리가 , 지루하고 , 별로네요 | 0.675205 |
| fnn | integrated_gradients_steps50 | negative | 지루하고 , 배우들 , 별로네요 | 0.674963 |
| fnn | occlusion | negative | 스토리가 , 지루하고 , 별로네요 | 0.64451 |
| transformer | integrated_gradients_steps100 | negative | 스토리가 , 연기도 , 별로네요 | 0.633338 |
| cnn | unigram_occlusion | negative | 지루하고 , 연기도 , 별로네요 | 0.620326 |
| transformer | integrated_gradients_steps50 | negative | 스토리가 , 연기도 , 별로네요 | 0.51 |

## case_003

text: 처음엔 지루했는데 갈수록 정말 재미있어지네요

- LLM sentiment: positive
- LLM evidence: 처음엔 지루했는데, 갈수록 정말 재미있어지네요
- LLM reason: 초반에는 지루했지만 뒤로 갈수록 정말 재미있어졌다는 내용이므로 전체적으로 긍정적입니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| cnn | ngram_occlusion | positive | 갈수록 , 정말 , 재미있어지네요 | 0.73898 |
| transformer | integrated_gradients_steps50 | positive | 처음엔 , 정말 , 재미있어지네요 | 0.70802 |
| transformer | integrated_gradients_steps100 | positive | 처음엔 , 정말 , 재미있어지네요 | 0.705329 |
| cnn | unigram_occlusion | positive | 지루했는데 , 정말 , 재미있어지네요 | 0.682059 |
| cnn | integrated_gradients_steps50 | positive | 지루했는데 , 정말 , 재미있어지네요 | 0.672391 |
| cnn | integrated_gradients_steps100 | positive | 지루했는데 , 정말 , 재미있어지네요 | 0.672186 |
| fnn | lime | positive | 지루했는데 , 정말 , 재미있어지네요 | 0.658537 |
| transformer | occlusion | positive | 지루했는데 , 갈수록 , 재미있어지네요 | 0.651148 |
| fnn | occlusion | positive | 지루했는데 , 갈수록 , 재미있어지네요 | 0.638829 |
| fnn | integrated_gradients_steps50 | positive | 처음엔 , 지루했는데 , 재미있어지네요 | 0.614528 |
| fnn | integrated_gradients_steps100 | positive | 처음엔 , 지루했는데 , 재미있어지네요 | 0.613964 |
| cnn | filter_activation | positive | 처음엔 , 갈수록 , 정말 | 0.51 |

## case_004

text: 배우들의 연기는 명품인데 각본이 너무 쓰레기네요

- LLM sentiment: negative
- LLM evidence: 배우들의 연기는 명품인데, 각본이 너무 쓰레기네요
- LLM reason: 연기에 대한 칭찬이 있지만, 각본을 '너무 쓰레기'라고 강하게 비판해 전체 감정은 부정적입니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| cnn | integrated_gradients_steps100 | negative | 명품인데 , 각본이 , 쓰레기네요 | 0.633506 |
| cnn | integrated_gradients_steps50 | negative | 명품인데 , 각본이 , 쓰레기네요 | 0.633204 |
| cnn | filter_activation | negative | 명품인데 , 너무 , 쓰레기네요 | 0.629282 |
| cnn | ngram_occlusion | negative | 각본이 , 너무 , 쓰레기네요 | 0.624665 |
| fnn | lime | negative | 명품인데 , 각본이 , 쓰레기네요 | 0.615512 |
| fnn | integrated_gradients_steps100 | negative | 연기는 , 명품인데 , 쓰레기네요 | 0.608459 |
| fnn | integrated_gradients_steps50 | negative | 연기는 , 명품인데 , 쓰레기네요 | 0.608366 |
| fnn | occlusion | negative | 명품인데 , 각본이 , 쓰레기네요 | 0.596665 |
| cnn | unigram_occlusion | negative | 각본이 , 너무 , 쓰레기네요 | 0.585147 |
| transformer | integrated_gradients_steps100 | negative | 각본이 , 너무 , 쓰레기네요 | 0.508492 |
| transformer | occlusion | negative | 연기는 , 명품인데 , 쓰레기네요 | 0.45 |
| transformer | integrated_gradients_steps50 | negative | 각본이 , 너무 , 쓰레기네요 | 0.45 |

## case_005

text: 와... 이런 영화에 내 피 같은 돈을 쓰다니 대단하다

- LLM sentiment: negative
- LLM evidence: 내 피 같은 돈을 쓰다니, 이런 영화에, 대단하다
- LLM reason: 소중한 돈을 쓴 것을 후회하며 비꼬는 표현이므로 부정적 리뷰입니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| cnn | ngram_occlusion | negative | 피 , 같은 , 돈을 | 0.533095 |
| cnn | filter_activation | negative | 돈을 , 쓰다니 , 대단하다 | 0.524568 |
| transformer | occlusion | negative | 이런 , 영화에 , 쓰다니 | 0.506666 |
| fnn | occlusion | negative | 피 , 돈을 , 대단하다 | 0.491982 |
| cnn | integrated_gradients_steps100 | negative | 돈을 , 쓰다니 , 대단하다 | 0.475877 |
| cnn | integrated_gradients_steps50 | negative | 돈을 , 쓰다니 , 대단하다 | 0.475697 |
| cnn | unigram_occlusion | negative | 같은 , 돈을 , 대단하다 | 0.418648 |
| transformer | integrated_gradients_steps100 | negative | 이런 , 내 , 쓰다니 | 0.387397 |
| transformer | integrated_gradients_steps50 | negative | 이런 , 내 , 쓰다니 | 0.372368 |
| fnn | lime | negative | 와... , 돈을 , 대단하다 | 0.37073 |
| fnn | integrated_gradients_steps100 | negative | 와... , 돈을 , 대단하다 | 0.320533 |
| fnn | integrated_gradients_steps50 | negative | 와... , 돈을 , 대단하다 | 0.320412 |

## case_006

text: 수면제 대신 보면 딱 좋은 훌륭한 영화입니다

- LLM sentiment: negative
- LLM evidence: 수면제 대신 보면 딱 좋은
- LLM reason: 겉으로는 '좋은', '훌륭한'이라고 하지만, 수면제 대신 볼 만하다는 말은 지루하다는 비꼼이므로 부정적입니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| transformer | occlusion | negative | 수면제 , 보면 , 딱 | 0.624692 |
| fnn | lime | positive | 수면제 , 좋은 , 훌륭한 | 0.401038 |
| cnn | integrated_gradients_steps100 | positive | 수면제 , 좋은 , 훌륭한 | 0.364013 |
| cnn | integrated_gradients_steps50 | positive | 수면제 , 좋은 , 훌륭한 | 0.363739 |
| fnn | integrated_gradients_steps50 | positive | 수면제 , 좋은 , 훌륭한 | 0.361101 |
| fnn | integrated_gradients_steps100 | positive | 수면제 , 좋은 , 훌륭한 | 0.361031 |
| cnn | unigram_occlusion | positive | 보면 , 좋은 , 훌륭한 | 0.306112 |
| cnn | filter_activation | positive | 수면제 , 훌륭한 , 영화입니다 | 0.287375 |
| transformer | integrated_gradients_steps100 | negative | 딱 , 훌륭한 , 영화입니다 | 0.274458 |
| transformer | integrated_gradients_steps50 | negative | 딱 , 훌륭한 , 영화입니다 | 0.256589 |
| fnn | occlusion | positive | 좋은 , 훌륭한 , 영화입니다 | 0.183547 |
| cnn | ngram_occlusion | positive | 좋은 , 훌륭한 , 영화입니다 | 0.178807 |

## case_007

text: 와 진짜 개존잼!!! 꼭보세요 ㅋㅋㅋ

- LLM sentiment: positive
- LLM evidence: 개존잼!!!, 꼭보세요, ㅋㅋㅋ
- LLM reason: 강한 재미 표현과 관람 추천이 있어 전반적으로 매우 긍정적인 리뷰입니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| cnn | ngram_occlusion | positive | 개존잼!!! , 꼭보세요 , ㅋㅋㅋ | 0.975077 |
| transformer | integrated_gradients_steps100 | positive | 개존잼!!! , 꼭보세요 , ㅋㅋㅋ | 0.971576 |
| cnn | filter_activation | positive | 개존잼!!! , 꼭보세요 , ㅋㅋㅋ | 0.962892 |
| transformer | integrated_gradients_steps50 | positive | 개존잼!!! , 꼭보세요 , ㅋㅋㅋ | 0.96074 |
| cnn | unigram_occlusion | positive | 개존잼!!! , 꼭보세요 , ㅋㅋㅋ | 0.906227 |
| transformer | occlusion | positive | 진짜 , 개존잼!!! , 꼭보세요 | 0.714457 |
| cnn | integrated_gradients_steps50 | positive | 진짜 , 개존잼!!! , 꼭보세요 | 0.70052 |
| cnn | integrated_gradients_steps100 | positive | 진짜 , 개존잼!!! , 꼭보세요 | 0.700418 |
| fnn | occlusion | positive | 와 , 개존잼!!! , 꼭보세요 | 0.569343 |
| fnn | lime | positive | 와 , 진짜 , 꼭보세요 | 0.419234 |
| fnn | integrated_gradients_steps50 | positive | 와 , 진짜 , 꼭보세요 | 0.378983 |
| fnn | integrated_gradients_steps100 | positive | 와 , 진짜 , 꼭보세요 | 0.377875 |

## case_008

text: 시간낭비 오지구요 지리구요 다신 안봄 ㅡㅡ

- LLM sentiment: negative
- LLM evidence: 시간낭비, 다신 안봄, ㅡㅡ
- LLM reason: 시간낭비라고 평가하고 다시 보지 않겠다고 해 전반적으로 강한 부정 감정입니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| fnn | lime | negative | 시간낭비 , 다신 , ㅡㅡ | 0.798702 |
| cnn | integrated_gradients_steps100 | negative | 시간낭비 , 다신 , 안봄 | 0.778709 |
| cnn | integrated_gradients_steps50 | negative | 시간낭비 , 다신 , 안봄 | 0.778372 |
| transformer | occlusion | negative | 시간낭비 , 다신 , 안봄 | 0.761717 |
| transformer | integrated_gradients_steps100 | negative | 시간낭비 , 안봄 , ㅡㅡ | 0.75019 |
| cnn | unigram_occlusion | negative | 시간낭비 , 다신 , 안봄 | 0.745718 |
| transformer | integrated_gradients_steps50 | negative | 시간낭비 , 다신 , 안봄 | 0.730862 |
| fnn | occlusion | negative | 시간낭비 , 지리구요 , ㅡㅡ | 0.570454 |
| fnn | integrated_gradients_steps50 | negative | 시간낭비 , 지리구요 , ㅡㅡ | 0.564578 |
| fnn | integrated_gradients_steps100 | negative | 시간낭비 , 지리구요 , ㅡㅡ | 0.564188 |
| cnn | ngram_occlusion | negative | 시간낭비 , 오지구요 , 지리구요 | 0.387328 |
| cnn | filter_activation | negative | 시간낭비 , 오지구요 , 지리구요 | 0.36064 |

## case_009

text: 스토리가 지루하긴 한데 배우들은 멋있음

- LLM sentiment: positive
- LLM evidence: 스토리가 지루하긴, 배우들은 멋있음
- LLM reason: 스토리가 지루하다는 부정 평가가 있지만, '한데' 이후 배우들이 멋있다는 긍정 평가가 최종적으로 강조되어 약한 긍정으로 판단함.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| cnn | integrated_gradients_steps100 | positive | 지루하긴 , 배우들은 , 멋있음 | 0.711962 |
| cnn | integrated_gradients_steps50 | positive | 지루하긴 , 배우들은 , 멋있음 | 0.711755 |
| transformer | integrated_gradients_steps50 | negative | 지루하긴 , 배우들은 , 멋있음 | 0.665202 |
| transformer | integrated_gradients_steps100 | negative | 지루하긴 , 배우들은 , 멋있음 | 0.627532 |
| cnn | ngram_occlusion | positive | 한데 , 배우들은 , 멋있음 | 0.618915 |
| cnn | unigram_occlusion | positive | 지루하긴 , 한데 , 멋있음 | 0.568718 |
| fnn | integrated_gradients_steps100 | negative | 지루하긴 , 한데 , 멋있음 | 0.506923 |
| fnn | integrated_gradients_steps50 | negative | 지루하긴 , 한데 , 멋있음 | 0.506517 |
| fnn | lime | negative | 지루하긴 , 한데 , 멋있음 | 0.487626 |
| fnn | occlusion | negative | 지루하긴 , 한데 , 멋있음 | 0.464262 |
| transformer | occlusion | negative | 스토리가 , 한데 , 배우들은 | 0.421834 |
| cnn | filter_activation | positive | 지루하긴 , 한데 , 배우들은 | 0.40068 |

## case_010

text: 개노잼임 ㅡㅡ

- LLM sentiment: negative
- LLM evidence: 개노잼임, ㅡㅡ
- LLM reason: 영화가 매우 재미없고 짜증스럽다는 부정적 평가입니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| transformer | integrated_gradients_steps100 | negative | 개노잼임 , ㅡㅡ | 0.999865 |
| transformer | integrated_gradients_steps50 | negative | 개노잼임 , ㅡㅡ | 0.99975 |
| cnn | filter_activation | negative | 개노잼임 , ㅡㅡ | 0.996348 |
| fnn | integrated_gradients_steps100 | negative | 개노잼임 , ㅡㅡ | 0.994566 |
| fnn | integrated_gradients_steps50 | negative | 개노잼임 , ㅡㅡ | 0.994375 |
| cnn | integrated_gradients_steps100 | negative | 개노잼임 , ㅡㅡ | 0.990666 |
| cnn | integrated_gradients_steps50 | negative | 개노잼임 , ㅡㅡ | 0.990626 |
| cnn | ngram_occlusion | negative | 개노잼임 , ㅡㅡ | 0.986875 |
| transformer | occlusion | negative | 개노잼임 , ㅡㅡ | 0.980941 |
| fnn | occlusion | negative | 개노잼임 , ㅡㅡ | 0.969019 |
| cnn | unigram_occlusion | negative | 개노잼임 , ㅡㅡ | 0.961764 |
| fnn | lime | negative | 개노잼임 , ㅡㅡ | 0.941022 |

## case_011

text: 평점 알바들만 넘치네 진짜 돈 아깝다

- LLM sentiment: negative
- LLM evidence: 평점 알바들만 넘치네, 진짜 돈 아깝다
- LLM reason: 평점 알바가 많다고 비판하고 돈이 아깝다고 말해 강한 부정 평가입니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| cnn | ngram_occlusion | negative | 알바들만 , 돈 , 아깝다 | 0.670158 |
| transformer | occlusion | negative | 넘치네 , 진짜 , 아깝다 | 0.621377 |
| cnn | filter_activation | negative | 알바들만 , 넘치네 , 진짜 | 0.618831 |
| cnn | unigram_occlusion | negative | 알바들만 , 돈 , 아깝다 | 0.616544 |
| fnn | lime | negative | 알바들만 , 돈 , 아깝다 | 0.60894 |
| fnn | occlusion | negative | 알바들만 , 돈 , 아깝다 | 0.594737 |
| cnn | integrated_gradients_steps100 | negative | 알바들만 , 돈 , 아깝다 | 0.576134 |
| cnn | integrated_gradients_steps50 | negative | 알바들만 , 돈 , 아깝다 | 0.575664 |
| fnn | integrated_gradients_steps50 | negative | 알바들만 , 돈 , 아깝다 | 0.575376 |
| fnn | integrated_gradients_steps100 | negative | 알바들만 , 돈 , 아깝다 | 0.574633 |
| transformer | integrated_gradients_steps100 | negative | 평점 , 돈 , 아깝다 | 0.558429 |
| transformer | integrated_gradients_steps50 | negative | 알바들만 , 돈 , 아깝다 | 0.556616 |

## case_012

text: 어설픈 신파보다 백배 천배 낫다. 가슴 먹먹해지는 수작.

- LLM sentiment: positive
- LLM evidence: 어설픈 신파보다 백배 천배 낫다., 가슴 먹먹해지는 수작.
- LLM reason: 어설픈 신파보다 훨씬 낫고, 가슴을 먹먹하게 하는 수작이라고 평가해 전반적으로 긍정적이다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| transformer | integrated_gradients_steps50 | positive | 신파보다 , 백배 , 수작. | 0.54161 |
| transformer | integrated_gradients_steps100 | positive | 신파보다 , 백배 , 수작. | 0.539828 |
| transformer | occlusion | positive | 신파보다 , 먹먹해지는 , 수작. | 0.529204 |
| cnn | unigram_occlusion | positive | 가슴 , 먹먹해지는 , 수작. | 0.52622 |
| cnn | ngram_occlusion | positive | 가슴 , 먹먹해지는 , 수작. | 0.526012 |
| cnn | filter_activation | positive | 신파보다 , 가슴 , 먹먹해지는 | 0.481361 |
| cnn | integrated_gradients_steps50 | positive | 가슴 , 먹먹해지는 , 수작. | 0.476561 |
| cnn | integrated_gradients_steps100 | positive | 가슴 , 먹먹해지는 , 수작. | 0.4765 |
| fnn | occlusion | positive | 어설픈 , 가슴 , 수작. | 0.473579 |
| fnn | integrated_gradients_steps100 | positive | 어설픈 , 가슴 , 수작. | 0.4186 |
| fnn | integrated_gradients_steps50 | positive | 어설픈 , 가슴 , 수작. | 0.418338 |
| fnn | lime | positive | 어설픈 , 가슴 , 수작. | 0.411171 |

## case_013

text: 솔직히 재미는 없음... 시간 때우기용도 안됨

- LLM sentiment: negative
- LLM evidence: 재미는 없음..., 시간 때우기용도 안됨
- LLM reason: 재미가 없고 시간 때우기용으로도 안 된다는 강한 부정 평가이다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| transformer | integrated_gradients_steps100 | negative | 재미는 , 없음... , 때우기용도 | 0.732117 |
| transformer | integrated_gradients_steps50 | negative | 재미는 , 없음... , 때우기용도 | 0.725826 |
| fnn | integrated_gradients_steps100 | negative | 없음... , 때우기용도 , 안됨 | 0.718859 |
| fnn | integrated_gradients_steps50 | negative | 없음... , 때우기용도 , 안됨 | 0.718635 |
| transformer | occlusion | negative | 재미는 , 없음... , 때우기용도 | 0.716897 |
| cnn | filter_activation | negative | 재미는 , 없음... , 시간 | 0.700827 |
| cnn | ngram_occlusion | negative | 없음... , 시간 , 때우기용도 | 0.699603 |
| cnn | integrated_gradients_steps50 | negative | 재미는 , 없음... , 때우기용도 | 0.694656 |
| cnn | integrated_gradients_steps100 | negative | 재미는 , 없음... , 때우기용도 | 0.69442 |
| fnn | lime | negative | 없음... , 때우기용도 , 안됨 | 0.693406 |
| fnn | occlusion | negative | 없음... , 때우기용도 , 안됨 | 0.684831 |
| cnn | unigram_occlusion | negative | 재미는 , 없음... , 때우기용도 | 0.660849 |

## case_014

text: 개연성이 밥말아먹었나 스토리가 왜 이 모양임?

- LLM sentiment: negative
- LLM evidence: 개연성이 밥말아먹었나, 스토리가 왜 이 모양임?
- LLM reason: 개연성과 스토리를 강하게 비판하는 부정적 리뷰입니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| cnn | filter_activation | negative | 개연성이 , 밥말아먹었나 , 스토리가 | 0.650738 |
| cnn | integrated_gradients_steps50 | negative | 개연성이 , 밥말아먹었나 , 모양임? | 0.644367 |
| cnn | integrated_gradients_steps100 | negative | 개연성이 , 밥말아먹었나 , 모양임? | 0.644351 |
| cnn | ngram_occlusion | negative | 개연성이 , 밥말아먹었나 , 스토리가 | 0.635092 |
| fnn | integrated_gradients_steps50 | negative | 개연성이 , 밥말아먹었나 , 스토리가 | 0.630417 |
| fnn | integrated_gradients_steps100 | negative | 개연성이 , 밥말아먹었나 , 스토리가 | 0.628904 |
| transformer | occlusion | negative | 밥말아먹었나 , 스토리가 , 모양임? | 0.623012 |
| transformer | integrated_gradients_steps100 | negative | 밥말아먹었나 , 스토리가 , 모양임? | 0.620152 |
| fnn | lime | negative | 개연성이 , 밥말아먹었나 , 모양임? | 0.618854 |
| transformer | integrated_gradients_steps50 | negative | 밥말아먹었나 , 이 , 모양임? | 0.613172 |
| fnn | occlusion | negative | 개연성이 , 밥말아먹었나 , 스토리가 | 0.590903 |
| cnn | unigram_occlusion | negative | 개연성이 , 밥말아먹었나 , 스토리가 | 0.58112 |

## case_015

text: 연출, 연기, 음악 삼박자가 완벽하다. 꼭 극장가서 보세요.

- LLM sentiment: positive
- LLM evidence: 연출, 연기, 음악 삼박자가 완벽하다., 꼭 극장가서 보세요.
- LLM reason: 연출, 연기, 음악을 완벽하다고 칭찬하고 관람을 추천하는 긍정적 리뷰입니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| transformer | integrated_gradients_steps100 | positive | 삼박자가 , 극장가서 , 보세요. | 0.595279 |
| transformer | integrated_gradients_steps50 | positive | 삼박자가 , 극장가서 , 보세요. | 0.595265 |
| transformer | occlusion | positive | 완벽하다. , 꼭 , 보세요. | 0.55815 |
| fnn | integrated_gradients_steps100 | positive | 음악 , 완벽하다. , 꼭 | 0.547763 |
| fnn | integrated_gradients_steps50 | positive | 음악 , 완벽하다. , 꼭 | 0.545123 |
| cnn | filter_activation | positive | 음악 , 완벽하다. , 꼭 | 0.533718 |
| cnn | ngram_occlusion | positive | 삼박자가 , 완벽하다. , 꼭 | 0.527403 |
| fnn | occlusion | positive | 음악 , 완벽하다. , 꼭 | 0.505475 |
| fnn | lime | positive | 완벽하다. , 꼭 , 극장가서 | 0.499298 |
| cnn | unigram_occlusion | positive | 삼박자가 , 완벽하다. , 극장가서 | 0.456095 |
| cnn | integrated_gradients_steps100 | positive | 삼박자가 , 완벽하다. , 꼭 | 0.449418 |
| cnn | integrated_gradients_steps50 | positive | 삼박자가 , 완벽하다. , 꼭 | 0.449337 |

## case_016

text: 하도 재밌다길래 봤는데 진짜 개노잼임 절대보지마셈

- LLM sentiment: negative
- LLM evidence: 진짜 개노잼임, 절대보지마셈
- LLM reason: 재미없다고 강하게 비판하고 관람을 말리고 있어 부정적 리뷰입니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| cnn | ngram_occlusion | negative | 진짜 , 개노잼임 , 절대보지마셈 | 0.941351 |
| transformer | occlusion | negative | 재밌다길래 , 개노잼임 , 절대보지마셈 | 0.664559 |
| cnn | filter_activation | negative | 재밌다길래 , 개노잼임 , 절대보지마셈 | 0.659786 |
| cnn | unigram_occlusion | negative | 재밌다길래 , 개노잼임 , 절대보지마셈 | 0.654876 |
| fnn | occlusion | negative | 재밌다길래 , 개노잼임 , 절대보지마셈 | 0.643033 |
| transformer | integrated_gradients_steps50 | negative | 하도 , 개노잼임 , 절대보지마셈 | 0.611059 |
| fnn | lime | negative | 재밌다길래 , 개노잼임 , 절대보지마셈 | 0.604629 |
| cnn | integrated_gradients_steps50 | negative | 재밌다길래 , 개노잼임 , 절대보지마셈 | 0.59513 |
| cnn | integrated_gradients_steps100 | negative | 재밌다길래 , 개노잼임 , 절대보지마셈 | 0.595112 |
| transformer | integrated_gradients_steps100 | negative | 하도 , 개노잼임 , 절대보지마셈 | 0.594104 |
| fnn | integrated_gradients_steps50 | negative | 재밌다길래 , 개노잼임 , 절대보지마셈 | 0.564209 |
| fnn | integrated_gradients_steps100 | negative | 재밌다길래 , 개노잼임 , 절대보지마셈 | 0.563865 |

## case_017

text: 오랜만에 가슴 따뜻해지는 웰메이드 영화 한 편 봤네요. 강추!!

- LLM sentiment: positive
- LLM evidence: 가슴 따뜻해지는, 웰메이드 영화, 강추!!
- LLM reason: 따뜻한 감동, 높은 완성도, 강한 추천 표현이 있어 긍정적인 리뷰입니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| cnn | integrated_gradients_steps100 | positive | 가슴 , 따뜻해지는 , 웰메이드 | 0.70775 |
| cnn | integrated_gradients_steps50 | positive | 가슴 , 따뜻해지는 , 웰메이드 | 0.707677 |
| transformer | integrated_gradients_steps100 | positive | 따뜻해지는 , 웰메이드 , 강추!! | 0.686469 |
| transformer | integrated_gradients_steps50 | positive | 따뜻해지는 , 웰메이드 , 강추!! | 0.681089 |
| fnn | occlusion | positive | 따뜻해지는 , 웰메이드 , 강추!! | 0.670002 |
| cnn | filter_activation | positive | 가슴 , 따뜻해지는 , 웰메이드 | 0.668383 |
| cnn | ngram_occlusion | positive | 가슴 , 따뜻해지는 , 웰메이드 | 0.662165 |
| fnn | lime | positive | 오랜만에 , 따뜻해지는 , 웰메이드 | 0.529334 |
| fnn | integrated_gradients_steps50 | positive | 오랜만에 , 따뜻해지는 , 강추!! | 0.519722 |
| fnn | integrated_gradients_steps100 | positive | 오랜만에 , 따뜻해지는 , 강추!! | 0.517921 |
| cnn | unigram_occlusion | positive | 오랜만에 , 따뜻해지는 , 웰메이드 | 0.503315 |
| transformer | occlusion | positive | 따뜻해지는 , 웰메이드 , 봤네요. | 0.490311 |

## case_018

text: 뻔하디 뻔한 한국식 억지 감동 짜내기 영화 극혐

- LLM sentiment: negative
- LLM evidence: 뻔하디 뻔한, 억지 감동 짜내기, 극혐
- LLM reason: 진부함, 억지 감동, 강한 혐오 표현이 모두 부정적입니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| cnn | filter_activation | negative | 억지 , 감동 , 짜내기 | 0.643067 |
| transformer | occlusion | negative | 뻔하디 , 억지 , 극혐 | 0.641036 |
| fnn | occlusion | negative | 뻔한 , 억지 , 극혐 | 0.637847 |
| fnn | lime | negative | 억지 , 감동 , 극혐 | 0.610703 |
| cnn | unigram_occlusion | negative | 억지 , 짜내기 , 극혐 | 0.599962 |
| fnn | integrated_gradients_steps50 | negative | 억지 , 감동 , 극혐 | 0.581036 |
| fnn | integrated_gradients_steps100 | negative | 억지 , 감동 , 극혐 | 0.5807 |
| transformer | integrated_gradients_steps50 | negative | 억지 , 감동 , 극혐 | 0.565521 |
| transformer | integrated_gradients_steps100 | negative | 억지 , 감동 , 극혐 | 0.559985 |
| cnn | integrated_gradients_steps50 | negative | 한국식 , 억지 , 극혐 | 0.455269 |
| cnn | integrated_gradients_steps100 | negative | 한국식 , 억지 , 극혐 | 0.45513 |
| cnn | ngram_occlusion | negative | 한국식 , 억지 , 짜내기 | 0.437326 |

## case_019

text: 내 돈이랑 시간 돌려내라 ㅋㅋㅋ 감독 누구냐 진짜

- LLM sentiment: negative
- LLM evidence: 내 돈이랑 시간 돌려내라, 감독 누구냐 진짜
- LLM reason: 돈과 시간을 돌려달라는 표현과 감독을 비꼬는 말투로 강한 불만을 나타냅니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| cnn | filter_activation | negative | 돈이랑 , 감독 , 누구냐 | 0.60122 |
| fnn | lime | negative | 돈이랑 , 감독 , 누구냐 | 0.598235 |
| cnn | ngram_occlusion | negative | 돈이랑 , 감독 , 누구냐 | 0.584924 |
| fnn | integrated_gradients_steps50 | negative | 돈이랑 , 감독 , 누구냐 | 0.57601 |
| fnn | integrated_gradients_steps100 | negative | 돈이랑 , 감독 , 누구냐 | 0.575919 |
| transformer | occlusion | negative | 돈이랑 , 돌려내라 , 감독 | 0.565428 |
| fnn | occlusion | negative | 돈이랑 , 감독 , 누구냐 | 0.548422 |
| cnn | unigram_occlusion | negative | 돈이랑 , 감독 , 누구냐 | 0.537402 |
| cnn | integrated_gradients_steps100 | negative | 돌려내라 , 감독 , 누구냐 | 0.52897 |
| cnn | integrated_gradients_steps50 | negative | 돌려내라 , 감독 , 누구냐 | 0.528776 |
| transformer | integrated_gradients_steps100 | negative | 내 , 시간 , ㅋㅋㅋ | 0.450292 |
| transformer | integrated_gradients_steps50 | negative | 내 , 시간 , ㅋㅋㅋ | 0.436904 |

## case_020

text: 배우들 얼굴 보러 갔다가 힐링 제대로 하고 옴 ㅠㅠ 연기도 찰떡

- LLM sentiment: positive
- LLM evidence: 힐링 제대로 하고 옴, 연기도 찰떡
- LLM reason: 영화를 통해 힐링을 느꼈고 연기도 좋게 평가해 전반적으로 긍정적인 리뷰입니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| transformer | integrated_gradients_steps50 | positive | 힐링 , 옴 , 찰떡 | 0.61768 |
| transformer | integrated_gradients_steps100 | positive | 힐링 , 옴 , 찰떡 | 0.609846 |
| transformer | occlusion | positive | 힐링 , 연기도 , 찰떡 | 0.586998 |
| cnn | filter_activation | positive | 힐링 , 옴 , ㅠㅠ | 0.490211 |
| cnn | ngram_occlusion | positive | 갔다가 , 힐링 , 제대로 | 0.444747 |
| fnn | occlusion | positive | 힐링 , ㅠㅠ , 연기도 | 0.398232 |
| cnn | integrated_gradients_steps100 | positive | 힐링 , 제대로 , ㅠㅠ | 0.393058 |
| cnn | integrated_gradients_steps50 | positive | 힐링 , 제대로 , ㅠㅠ | 0.392511 |
| fnn | integrated_gradients_steps50 | positive | 힐링 , ㅠㅠ , 연기도 | 0.368295 |
| fnn | integrated_gradients_steps100 | positive | 힐링 , ㅠㅠ , 연기도 | 0.368244 |
| cnn | unigram_occlusion | positive | 힐링 , ㅠㅠ , 찰떡 | 0.347803 |
| fnn | lime | positive | 배우들 , 힐링 , ㅠㅠ | 0.248896 |

## case_021

text: 초반엔 오? 하다가 후반 갈수록 산으로 가네 ㅋㅋㅋ 어이없음

- LLM sentiment: negative
- LLM evidence: 초반엔 오?, 후반 갈수록 산으로 가네, 어이없음
- LLM reason: 초반에는 약간 기대감을 보였지만, 후반 전개가 산으로 가고 어이없다고 평가해 전체적으로 부정적이다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| cnn | filter_activation | negative | 갈수록 , 산으로 , 가네 | 0.582515 |
| transformer | occlusion | negative | 갈수록 , 산으로 , 어이없음 | 0.564891 |
| fnn | integrated_gradients_steps100 | negative | 초반엔 , 산으로 , 어이없음 | 0.564753 |
| fnn | integrated_gradients_steps50 | negative | 초반엔 , 산으로 , 어이없음 | 0.564593 |
| fnn | lime | negative | 갈수록 , 산으로 , 어이없음 | 0.552531 |
| transformer | integrated_gradients_steps100 | negative | 오? , 산으로 , 어이없음 | 0.548073 |
| transformer | integrated_gradients_steps50 | negative | 오? , 산으로 , 어이없음 | 0.544797 |
| fnn | occlusion | negative | 초반엔 , 오? , 어이없음 | 0.541106 |
| cnn | integrated_gradients_steps50 | negative | 오? , 산으로 , 어이없음 | 0.533632 |
| cnn | integrated_gradients_steps100 | negative | 오? , 산으로 , 어이없음 | 0.533618 |
| cnn | unigram_occlusion | negative | 오? , 산으로 , 어이없음 | 0.51819 |
| cnn | ngram_occlusion | negative | 산으로 , ㅋㅋㅋ , 어이없음 | 0.457048 |

## case_022

text: 인생작입니다. 살면서 본 시트콤 중에 감히 최고라고 말하고 싶네요.

- LLM sentiment: positive
- LLM evidence: 인생작입니다., 감히 최고라고 말하고 싶네요.
- LLM reason: 인생작이라고 표현하고 시트콤 중 최고라고 평가해 매우 긍정적인 리뷰입니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| transformer | occlusion | positive | 인생작입니다. , 최고라고 , 싶네요. | 0.689176 |
| transformer | integrated_gradients_steps50 | positive | 인생작입니다. , 최고라고 , 싶네요. | 0.608154 |
| transformer | integrated_gradients_steps100 | positive | 인생작입니다. , 최고라고 , 싶네요. | 0.605763 |
| cnn | unigram_occlusion | positive | 인생작입니다. , 살면서 , 최고라고 | 0.510137 |
| cnn | filter_activation | positive | 인생작입니다. , 시트콤 , 최고라고 | 0.499344 |
| cnn | ngram_occlusion | positive | 중에 , 감히 , 최고라고 | 0.496862 |
| cnn | integrated_gradients_steps100 | positive | 인생작입니다. , 시트콤 , 최고라고 | 0.477618 |
| cnn | integrated_gradients_steps50 | positive | 인생작입니다. , 시트콤 , 최고라고 | 0.47739 |
| fnn | lime | positive | 인생작입니다. , 중에 , 최고라고 | 0.441438 |
| fnn | integrated_gradients_steps50 | positive | 인생작입니다. , 중에 , 최고라고 | 0.43913 |
| fnn | integrated_gradients_steps100 | positive | 인생작입니다. , 중에 , 최고라고 | 0.437388 |
| fnn | occlusion | positive | 인생작입니다. , 중에 , 최고라고 | 0.434515 |

## case_023

text: 지루해서 중간에 나왔어요 돈날림주의;;;

- LLM sentiment: negative
- LLM evidence: 지루해서, 중간에 나왔어요, 돈날림주의;;;
- LLM reason: 지루함, 중도 퇴장, 돈이 아깝다는 표현이 모두 명확한 부정 감정을 나타냅니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| fnn | lime | negative | 지루해서 , 중간에 , 돈날림주의;;; | 0.827598 |
| cnn | ngram_occlusion | negative | 중간에 , 나왔어요 , 돈날림주의;;; | 0.823806 |
| cnn | filter_activation | negative | 중간에 , 나왔어요 , 돈날림주의;;; | 0.812839 |
| transformer | occlusion | negative | 지루해서 , 나왔어요 , 돈날림주의;;; | 0.798221 |
| fnn | integrated_gradients_steps50 | negative | 지루해서 , 나왔어요 , 돈날림주의;;; | 0.79811 |
| fnn | integrated_gradients_steps100 | negative | 지루해서 , 나왔어요 , 돈날림주의;;; | 0.796752 |
| cnn | unigram_occlusion | negative | 지루해서 , 중간에 , 돈날림주의;;; | 0.77801 |
| fnn | occlusion | negative | 지루해서 , 나왔어요 , 돈날림주의;;; | 0.772698 |
| cnn | integrated_gradients_steps100 | negative | 지루해서 , 중간에 , 돈날림주의;;; | 0.769094 |
| cnn | integrated_gradients_steps50 | negative | 지루해서 , 중간에 , 돈날림주의;;; | 0.768912 |
| transformer | integrated_gradients_steps50 | negative | 지루해서 , 중간에 , 돈날림주의;;; | 0.737503 |
| transformer | integrated_gradients_steps100 | negative | 지루해서 , 중간에 , 돈날림주의;;; | 0.727285 |

## case_024

text: 연기도 좋고 영상도 아름답고 음악도 훌륭했지만 정작 스토리가 너무 엉성해서 전체적으로는 실망스러웠습니다.

- LLM sentiment: negative
- LLM evidence: 연기도 좋고 영상도 아름답고 음악도 훌륭했지만, 스토리가 너무 엉성해서, 전체적으로는 실망스러웠습니다.
- LLM reason: 연기·영상·음악은 좋았다고 했지만, 스토리가 엉성하고 전체적으로 실망스럽다고 결론내려 부정적입니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| cnn | filter_activation | negative | 음악도 , 엉성해서 , 실망스러웠습니다. | 0.521704 |
| cnn | ngram_occlusion | negative | 엉성해서 , 전체적으로는 , 실망스러웠습니다. | 0.511811 |
| cnn | integrated_gradients_steps50 | negative | 아름답고 , 엉성해서 , 실망스러웠습니다. | 0.50623 |
| cnn | integrated_gradients_steps100 | negative | 아름답고 , 엉성해서 , 실망스러웠습니다. | 0.506109 |
| transformer | integrated_gradients_steps50 | negative | 좋고 , 아름답고 , 실망스러웠습니다. | 0.489334 |
| transformer | integrated_gradients_steps100 | negative | 좋고 , 아름답고 , 실망스러웠습니다. | 0.47839 |
| fnn | integrated_gradients_steps50 | negative | 훌륭했지만 , 엉성해서 , 실망스러웠습니다. | 0.458127 |
| fnn | integrated_gradients_steps100 | negative | 훌륭했지만 , 엉성해서 , 실망스러웠습니다. | 0.458046 |
| fnn | lime | negative | 아름답고 , 엉성해서 , 실망스러웠습니다. | 0.457233 |
| cnn | unigram_occlusion | negative | 훌륭했지만 , 스토리가 , 실망스러웠습니다. | 0.445857 |
| fnn | occlusion | negative | 정작 , 엉성해서 , 실망스러웠습니다. | 0.373191 |
| transformer | occlusion | negative | 훌륭했지만 , 정작 , 실망스러웠습니다. | 0.236753 |

## case_025

text: 킬링타임으로 제격임 ㅋㅋ 유치하긴 한데 가볍게 웃기 좋네요

- LLM sentiment: positive
- LLM evidence: 킬링타임으로 제격임, 유치하긴, 가볍게 웃기 좋네요
- LLM reason: 유치하다는 단점은 있지만 킬링타임용으로 좋고 가볍게 웃기 좋다는 평가가 중심이라 긍정적입니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| transformer | occlusion | positive | 킬링타임으로 , 제격임 , 좋네요 | 0.599732 |
| fnn | lime | positive | 제격임 , 유치하긴 , 좋네요 | 0.589544 |
| fnn | integrated_gradients_steps50 | positive | 제격임 , 유치하긴 , 좋네요 | 0.586563 |
| fnn | integrated_gradients_steps100 | positive | 제격임 , 유치하긴 , 좋네요 | 0.586171 |
| cnn | unigram_occlusion | positive | 유치하긴 , 가볍게 , 좋네요 | 0.571388 |
| cnn | integrated_gradients_steps100 | positive | 제격임 , 유치하긴 , 좋네요 | 0.555111 |
| cnn | integrated_gradients_steps50 | positive | 제격임 , 유치하긴 , 좋네요 | 0.554978 |
| transformer | integrated_gradients_steps100 | positive | 제격임 , ㅋㅋ , 좋네요 | 0.486007 |
| transformer | integrated_gradients_steps50 | positive | 제격임 , ㅋㅋ , 좋네요 | 0.485114 |
| fnn | occlusion | positive | 유치하긴 , 한데 , 좋네요 | 0.470774 |
| cnn | ngram_occlusion | positive | 제격임 , ㅋㅋ , 유치하긴 | 0.389369 |
| cnn | filter_activation | positive | 유치하긴 , 한데 , 가볍게 | 0.279054 |

## case_026

text: 평점 왜 이럼? 생각보다 완전 명작인데 억까들 많네

- LLM sentiment: positive
- LLM evidence: 생각보다 완전 명작인데, 억까들 많네
- LLM reason: 평점과 비판자들에게 불만을 표하지만, 영화는 '완전 명작'이라고 강하게 긍정 평가한다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| cnn | ngram_occlusion | positive | 생각보다 , 완전 , 명작인데 | 0.69891 |
| fnn | integrated_gradients_steps100 | positive | 명작인데 , 억까들 , 많네 | 0.658258 |
| fnn | integrated_gradients_steps50 | positive | 명작인데 , 억까들 , 많네 | 0.65724 |
| transformer | occlusion | positive | 이럼? , 명작인데 , 억까들 | 0.502183 |
| cnn | unigram_occlusion | positive | 왜 , 완전 , 명작인데 | 0.502119 |
| fnn | occlusion | positive | 왜 , 명작인데 , 억까들 | 0.495345 |
| cnn | integrated_gradients_steps50 | positive | 왜 , 명작인데 , 억까들 | 0.49532 |
| cnn | integrated_gradients_steps100 | positive | 왜 , 명작인데 , 억까들 | 0.49503 |
| fnn | lime | positive | 왜 , 명작인데 , 억까들 | 0.473923 |
| cnn | filter_activation | positive | 이럼? , 완전 , 명작인데 | 0.470449 |
| transformer | integrated_gradients_steps100 | positive | 이럼? , 명작인데 , 억까들 | 0.464427 |
| transformer | integrated_gradients_steps50 | positive | 왜 , 명작인데 , 억까들 | 0.453262 |

## case_027

text: 원작 웹툰이 훨씬 나음.. 실사화는 그냥 폭망 수준

- LLM sentiment: negative
- LLM evidence: 실사화는 그냥 폭망 수준, 원작 웹툰이 훨씬 나음..
- LLM reason: 실사화를 '폭망 수준'이라고 표현하며 원작보다 못하다고 평가하므로 부정적 리뷰입니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| cnn | filter_activation | negative | 그냥 , 폭망 , 수준 | 0.612401 |
| cnn | ngram_occlusion | negative | 그냥 , 폭망 , 수준 | 0.592724 |
| transformer | occlusion | negative | 나음.. , 폭망 , 수준 | 0.574875 |
| transformer | integrated_gradients_steps50 | negative | 실사화는 , 폭망 , 수준 | 0.57415 |
| transformer | integrated_gradients_steps100 | negative | 그냥 , 폭망 , 수준 | 0.555806 |
| fnn | integrated_gradients_steps50 | negative | 그냥 , 폭망 , 수준 | 0.552998 |
| fnn | integrated_gradients_steps100 | negative | 나음.. , 그냥 , 폭망 | 0.551946 |
| cnn | unigram_occlusion | negative | 웹툰이 , 그냥 , 수준 | 0.544239 |
| fnn | lime | negative | 훨씬 , 폭망 , 수준 | 0.540714 |
| cnn | integrated_gradients_steps50 | negative | 웹툰이 , 그냥 , 수준 | 0.528952 |
| cnn | integrated_gradients_steps100 | negative | 웹툰이 , 그냥 , 수준 | 0.528661 |
| fnn | occlusion | negative | 웹툰이 , 그냥 , 폭망 | 0.523257 |

## case_028

text: 가볍게 볼 로맨틱 코미디 찾다가 완전 인생 영화 건짐... 설렘 터짐

- LLM sentiment: positive
- LLM evidence: 완전 인생 영화 건짐..., 설렘 터짐
- LLM reason: 인생 영화라고 평가하고 설렘이 크다고 표현해 전반적으로 매우 긍정적인 리뷰입니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| transformer | integrated_gradients_steps100 | positive | 인생 , 설렘 , 터짐 | 0.635806 |
| transformer | integrated_gradients_steps50 | positive | 인생 , 설렘 , 터짐 | 0.628035 |
| transformer | occlusion | positive | 완전 , 인생 , 설렘 | 0.612137 |
| cnn | integrated_gradients_steps100 | positive | 인생 , 건짐... , 설렘 | 0.549677 |
| cnn | integrated_gradients_steps50 | positive | 인생 , 건짐... , 설렘 | 0.548984 |
| fnn | occlusion | positive | 볼 , 인생 , 설렘 | 0.444812 |
| cnn | filter_activation | positive | 로맨틱 , 인생 , 영화 | 0.425894 |
| cnn | ngram_occlusion | positive | 찾다가 , 완전 , 인생 | 0.42337 |
| cnn | unigram_occlusion | positive | 볼 , 인생 , 설렘 | 0.418611 |
| fnn | integrated_gradients_steps100 | positive | 볼 , 인생 , 설렘 | 0.409004 |
| fnn | integrated_gradients_steps50 | positive | 볼 , 인생 , 설렘 | 0.408154 |
| fnn | lime | positive | 볼 , 건짐... , 설렘 | 0.341977 |

## case_029

text: 1점도 아깝다 스토리 연출 캐스팅 다 엉망진창임

- LLM sentiment: negative
- LLM evidence: 1점도 아깝다, 스토리 연출 캐스팅 다 엉망진창임
- LLM reason: 1점도 아깝고 스토리, 연출, 캐스팅이 모두 엉망이라는 강한 부정 평가입니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| cnn | ngram_occlusion | negative | 1점도 , 아깝다 , 엉망진창임 | 0.640753 |
| cnn | filter_activation | negative | 1점도 , 아깝다 , 스토리 | 0.616066 |
| fnn | lime | negative | 1점도 , 아깝다 , 엉망진창임 | 0.608818 |
| fnn | integrated_gradients_steps100 | negative | 1점도 , 아깝다 , 엉망진창임 | 0.584926 |
| fnn | integrated_gradients_steps50 | negative | 1점도 , 아깝다 , 엉망진창임 | 0.583626 |
| cnn | unigram_occlusion | negative | 1점도 , 아깝다 , 엉망진창임 | 0.575085 |
| cnn | integrated_gradients_steps100 | negative | 1점도 , 아깝다 , 엉망진창임 | 0.571033 |
| cnn | integrated_gradients_steps50 | negative | 1점도 , 아깝다 , 엉망진창임 | 0.570967 |
| fnn | occlusion | negative | 1점도 , 아깝다 , 엉망진창임 | 0.544305 |
| transformer | occlusion | negative | 아깝다 , 스토리 , 엉망진창임 | 0.532796 |
| transformer | integrated_gradients_steps100 | negative | 아깝다 , 다 , 엉망진창임 | 0.529653 |
| transformer | integrated_gradients_steps50 | negative | 아깝다 , 캐스팅 , 엉망진창임 | 0.483257 |

## case_030

text: 가슴 아픈 역사적 사실을 잘 담아낸 의미 있는 영화입니다. 먹먹하네요.

- LLM sentiment: positive
- LLM evidence: 잘 담아낸, 의미 있는 영화입니다., 먹먹하네요.
- LLM reason: 가슴 아픈 역사적 소재를 잘 담아낸 의미 있는 영화라고 평가하며, 먹먹한 여운도 긍정적 감상으로 읽힙니다.

| model | method | prediction | top words | score |
| --- | --- | --- | --- | ---: |
| transformer | integrated_gradients_steps50 | positive | 잘 , 담아낸 , 먹먹하네요. | 0.576558 |
| transformer | integrated_gradients_steps100 | positive | 잘 , 담아낸 , 먹먹하네요. | 0.573801 |
| transformer | occlusion | positive | 담아낸 , 영화입니다. , 먹먹하네요. | 0.572472 |
| fnn | integrated_gradients_steps100 | positive | 가슴 , 사실을 , 영화입니다. | 0.292898 |
| fnn | integrated_gradients_steps50 | positive | 가슴 , 사실을 , 영화입니다. | 0.291299 |
| fnn | occlusion | positive | 가슴 , 사실을 , 영화입니다. | 0.286426 |
| cnn | ngram_occlusion | positive | 역사적 , 사실을 , 영화입니다. | 0.278472 |
| cnn | unigram_occlusion | positive | 가슴 , 사실을 , 영화입니다. | 0.272122 |
| cnn | filter_activation | positive | 아픈 , 역사적 , 사실을 | 0.132959 |
| cnn | integrated_gradients_steps100 | positive | 가슴 , 아픈 , 사실을 | 0.089111 |
| cnn | integrated_gradients_steps50 | positive | 가슴 , 아픈 , 사실을 | 0.088416 |
| fnn | lime | positive | 가슴 , 아픈 , 사실을 | 0.057842 |
