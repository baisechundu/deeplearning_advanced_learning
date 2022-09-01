# /usr/bin/python3
# -*- coding:utf-8 -*-
"""
# @time: 2022/9/1 22:40
# @Author: baiyang
# Email: 308982012@qq.com
# File: random_shuffle.py
# @software: PyCharm
# 洗牌算法的运用 https://www.zhihu.com/question/358255792/answer/974431591
"""


def _randbelow(self, n, int=int, maxsize=1 << BPF, type=type,
               Method=_MethodType, BuiltinMethod=_BuiltinMethodType):
    "Return a random int in the range [0,n).  Raises ValueError if n==0."

    random = self.random
    getrandbits = self.getrandbits
    # Only call self.getrandbits if the original random() builtin method
    # has not been overridden or if a new getrandbits() was supplied.
    if type(random) is BuiltinMethod or type(getrandbits) is Method:
        k = n.bit_length()  # don't use (n-1) here because n can be 1
        r = getrandbits(k)  # 0 <= r < 2**k
        while r >= n:
            r = getrandbits(k)
        return r
    # There's an overridden random() method but no new getrandbits() method,
    # so we can only use random() from here.
    if n >= maxsize:
        print("Underlying random() generator does not supply \n"
              "enough bits to choose from a population range this large.\n"
              "To remove the range limitation, add a getrandbits() method.")
        return int(random() * n)
    if n == 0:
        raise ValueError("Boundary cannot be zero")
    rem = maxsize % n
    limit = (maxsize - rem) / maxsize  # int(limit * maxsize) % n == 0
    r = random()
    while r >= limit:
        r = random()
    return int(r * maxsize) % n


def shuffle(x, random=None):
    """Shuffle list x in place, and return None.

    Optional argument random is a 0-argument function returning a
    random float in [0.0, 1.0); if it is the default None, the
    standard random.random will be used.

    """

    if random is None:
        randbelow = _randbelow()
        for i in reversed(range(1, len(x))):
            # pick an element in x[:i+1] with which to exchange x[i]
            j = randbelow(i + 1)
            x[i], x[j] = x[j], x[i]
    else:
        _int = int
        for i in reversed(range(1, len(x))):
            # pick an element in x[:i+1] with which to exchange x[i]
            j = _int(random() * (i + 1))
            x[i], x[j] = x[j], x[i]
