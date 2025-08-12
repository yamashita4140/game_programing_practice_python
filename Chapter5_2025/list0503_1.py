pl_pos = 6  # プレイヤーの位置


def banmen():
    print("・" * (pl_pos - 1) + "P" + "・" * (30 - pl_pos))


banmen()
