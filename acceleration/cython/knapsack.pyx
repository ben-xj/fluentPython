import numpy as np
cimport numpy as cnp
from cython import boundscheck, wraparound

def knapsack_2d_dp_cy(values, weights, capacity):
    n = len(values)
    
    # 创建一个二维数组dp，其中dp[i,j]表示前i个物品，在容量为j的情况下的最大价值
    dp_raw = np.zeros((n + 1, capacity + 1), dtype=np.int32)
    cdef int[:,:] dp = dp_raw
    
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


@boundscheck(False)
@wraparound(False)
def knapsack_2d_dp_cy_full_power(list[int] values, list[int] weights, int capacity):
    cdef:
        int n = len(values)
    
    # 创建一个二维数组dp，其中dp[i,j]表示前i个物品，在容量为j的情况下的最大价值
        cnp.ndarray[int, ndim=2] dp_raw = np.zeros((n + 1, capacity + 1), dtype=np.int32)
        int[:,:] dp = dp_raw
        int i, j, max_value
    
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