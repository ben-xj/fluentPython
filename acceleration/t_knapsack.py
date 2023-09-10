import numpy as np
import random
from util.stopwatch import StopWatch
from acceleration.knapsack import knapsack_2d_dp_cy, knapsack_2d_dp_cy_full_power

"""
cython memoryview test
"""

def knapsack_2d_dp(values, weights, capacity):
    n = len(values)
    
    # 创建一个二维数组dp，其中dp[i,j]表示前i个物品，在容量为j的情况下的最大价值
    dp = np.zeros((n + 1, capacity + 1), dtype=np.int32)
    
    # 填充dp数组
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            # 如果当前物品的重量大于背包容量j，则无法放入
            if weights[i - 1] > j:
                dp[i, j] = dp[i - 1, j]
            else:
                # 否则，可以选择放入或不放入当前物品，选择最大价值
                dp[i, j] = max(dp[i - 1, j], dp[i - 1, j - weights[i - 1]] + values[i - 1])
    
    # 从dp数组中找到最优解的最大价值
    max_value = dp[n, capacity]
    return max_value


if __name__ == "__main__":
    # 测试
    random.seed(42)  # 设置随机种子以确保结果可复现
    num_items = 10
    values = [random.randint(1, 100) for _ in range(num_items)]
    weights = [random.randint(1, 20) for _ in range(num_items)]
    capacity = 50

    repeat  = 10000

    sw = StopWatch()
    for _ in range(repeat):
        max_value = knapsack_2d_dp(values, weights, capacity)
    sw.stop()
    t1 = sw.getElapsedTime()
    print(f"原生Python: {t1} ms")
    # print(f"max value: {max_value}")

    sw.start()
    for _ in range(repeat):
        max_value = knapsack_2d_dp_cy(values, weights, capacity)
    sw.stop()
    t2 = sw.getElapsedTime()
    print(f"内存视图优化: {t2} ms, 加速 {t1 / t2:.1f} 倍")
    # print(f"max value: {max_value}")

    sw.start()
    for _ in range(repeat):
        max_value = knapsack_2d_dp_cy_full_power(values, weights, capacity)
    sw.stop()
    t3 = sw.getElapsedTime()
    print(f"优化拉满: {t3} ms, 加速 {t1 / t3:.2f} 倍")
    # print(f"max value: {max_value}")
