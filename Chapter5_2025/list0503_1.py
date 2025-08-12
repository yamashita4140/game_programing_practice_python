pl_pos = 6  # プレイヤーの位置
com_pos = 3  # コンピュータの位置


def banmen():
    print("・" * (pl_pos - 1) + "P" + "・" * (30 - pl_pos))
    print("・" * (com_pos - 1) + "C" + "・" * (30 - com_pos))

banmen()
