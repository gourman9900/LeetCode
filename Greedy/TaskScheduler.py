"""
题号 621 任务调度器
给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。

然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的最短时间。

示例 1：

输入: tasks = ["A","A","A","B","B","B"], n = 2
输出: 8
执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
注：

任务的总个数为 [1, 10000]。
n 的取值范围为 [0, 100]。

毫无思路，不知道在说啥

参考1:https://leetcode-cn.com/problems/task-scheduler/solution/python-xiang-jie-by-jalan/
参考2:https://leetcode-cn.com/problems/task-scheduler/solution/621-ren-wu-diao-du-qi-java-jie-ti-zhu-shi-ying-gai/

"""
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_map = {}
        for task in tasks:
            task_map[task] = task_map.get(task,0) + 1
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)
        max_task_count = task_sort[0][1]
        res = (max_task_count - 1) * (n + 1)
        for sort in task_sort:
            if sort[1] == max_task_count:
                res += 1
        return max(res,len(tasks))

if __name__ == '__main__':
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    solution = Solution()
    print(solution.leastInterval(tasks,n))