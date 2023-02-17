1. 왜 학습 모드 일 때 BlockVer4의 출력은 항상 다를까요?
> Dropout이 랜덤하게 노드를 mute해서 항상 다른 노드가 출력에 영향을 주기 때문입니다.

2. 왜 평가 모드 일 때 BlockVer4의 출력은 항상 같을까요?
> 평가 모드에서는 모든 노드가 작동하고 dropout이 학습 때 쓰인 것을 감안해서 output이 (1-dropout) 만큼 scale됩니다. 

'''Python
x = x * (1-dropout)
'''