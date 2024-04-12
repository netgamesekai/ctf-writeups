# RITSEC24

## [Forensic] Ransom Note

## Approach

`README.txt`가 주어집니다.
가상의 공격자가 BTC 송금을 요구하기 위해 사인된 비트코인 메세지, 시그니처, 그리고 주소를 남깁니다: `bc1qd7qtdayjnl382qmfl4tl4yaejuv5py0n3uwq6p` 해당 비트코인 메세지와 시그니처를 검증하면 위 주소를 얻을 수 있기도 합니다.
<br />

해당 주소에서 일어난 트랜잭션을 추적합니다. Bitcoin transaction `42baaa9ce6828c1e5f2b1db3a771777e73aa32f44664223972fb59de88cea4a7`에서 `OP_RETURN`으로 출력된 플래그를 찾을 수 있습니다.
