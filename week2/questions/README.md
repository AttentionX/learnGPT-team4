1. 왜 학습 모드 일 때 BlockVer4의 출력은 항상 다를까요?
> Dropout이 랜덤하게 노드를 mute해서 항상 다른 노드가 출력에 영향을 주기 때문입니다.

2. 왜 평가 모드 일 때 BlockVer4의 출력은 항상 같을까요?
> 평가 모드에서는 모든 노드가 작동하고 dropout이 학습 때 쓰인 것을 감안해서 output이 (1-dropout) 만큼 scale됩니다. 

```Python
x = x * (1-dropout)
```

3. BlockVer3와 BlockVer4 중 어떤 것이 더 좋은 성능을 보이나요? 그 이유는 무엇인가요?  
이론적으로, dropout을 통해 더 좋은 regularization을 할 수 있어 BlockVer3가 BlockVer4보다 training loss는 작지만 validation loss는 더 커야 합니다.  
Regularization을 더 잘하는 이유는 소수의 node에 reliant하지 않기 때문에 전반적으로 노드들이 모두 데이터의 학습에 영향을 받기 때문입니다.
