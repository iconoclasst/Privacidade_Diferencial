import pandas as pd
from collections import Counter

def isKAnonymized(df, k):
    registros = list(zip(df['idade'], df['pretestscore'], df['postestscore']))
    qtd = Counter(registros)
    group = min(qtd.values())

    if group < k:
        return False
    return True

df = pd.DataFrame({
    "idade":[42, 52, 36, 24, 73],
    "pretestscore":[4, 24, 31, 2, 3],
    "postestscore":[25, 94, 57, 62, 70]
})

print(isKAnonymized(df, 1))





