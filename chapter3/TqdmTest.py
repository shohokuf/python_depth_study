# 进度条库
import time

from tqdm import tqdm
# 一共100个，每次更新10
with tqdm(total=100) as pbar:
    for i in range(10):
        pbar.update(10)
        time.sleep(1)
