# 引数と戻り値のある関数

def add(a: int, b: int) -> int:
    return a + b    # <- 2つの引数の加算結果を戻り値として返している


c = add(1, 2)   # <- 関数を呼び出す際に引数として1,2を渡している
print(c)
