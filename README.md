# learnGPT - team 4

## week 1

### `test_6.py` (1)?

> `gpt_v1` & `gpt_2` do not preserve orders  - why?

### `test_6.py` (2)?

> pos_encodings is designed such that each pos is different - how?

### `test_6.py` (3)?

> pos_encodings is designed such that  |PE(pos + k) - PE(pos)| stays constant - why & how?


[hint 1 ](https://www.facebook.com/groups/TensorFlowKR/posts/1580740202267032)| 
--- | 
<img width="692" alt="image" src="https://user-images.githubusercontent.com/56193069/217115798-8bbc5eab-9888-42ea-9215-09fb40bd8939.png"> |



### `test_6.py` (4)?

>  `gpt_v3` does preserve order  - how?

-  what changes did you make to `token_emb`?


## week 2 - `test_10.py` (Team 4)

```shell
pytest tests/test_10.py -s -vv
```
### test_block_ver_4_output_is_always_different_in_train_mode & test_block_ver_4_output_is_always_the_same_in_eval_mode

<img src='img/BlockVer4.png' width=250>

> TODO 4: `BlockVer4.__init__`을 구현해주세요. Dropout layer를 추가하면됩니다. Dropout은 Multi-Head의 output, FeedForward의 output 총 2곳에 추가하시면 됩니다.

테스트를 돌려보고 다음의 질문에 답해주세요.
1. 왜 학습 모드 일 때 `BlockVer4`의 출력은 항상 다를까요?
2. 왜 평가 모드 일 때 `BlockVer4`의 출력은 항상 같을까요?

### test_dropout_helps

테스트를 돌려보고 다음의 질문에 답해주세요.
1. `BlockVer3`와 `BlockVer4` 





