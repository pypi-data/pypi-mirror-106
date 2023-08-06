"""
@Description: 针对多线程任务的tqdm进度条封装
@Author: yuantianyu
@Datetime: 2021/5/22 10:04 上午
@Software: PyCharm
"""
import unittest
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from functools import partial

from tqdm import tqdm


def multi_thread_tqdm(task, data, workers: int = 20) -> list:
    """
    多线程任务进度条
    @param task: 任务函数
    @param data: 需要处理的数据，可迭代对象
    @param workers: 线程数
    @return: 任务函数返回结果的列表
    """
    executor = ThreadPoolExecutor(max_workers=workers)
    result = list(tqdm(executor.map(task, data), total=len(data)))
    return result


def partial_multi_thread_tqdm(task, data, workers: int = 20, **kwargs) -> list:
    """
    带常量参数的多线程任务进度条
    @param task: 任务函数
    @param data: 需要处理的数据，可迭代对象
    @param workers: 线程数
    @param kwargs: 常量参数：以key word形式传参
    @return: 任务函数返回结果的列表
    """
    new_task = partial(task, **kwargs)
    return multi_thread_tqdm(new_task, data, workers)


class TestMultiThreadTqdm(unittest.TestCase):
    """The test for multi-threading tqdm methods"""
    def setUp(self) -> None:
        """prepare test data"""
        self.data = [i for i in range(1000)]

    def test_multi_thread_tqdm(self):
        # task function
        def square(x):
            sleep(0.1)
            return x * x
        result = multi_thread_tqdm(square, self.data, workers=10)
        answer = [i*i for i in self.data]
        self.assertEqual(result, answer)

    def test_partial_multi_thread_tqdm(self):
        # task function
        def plus_c(x, c):
            sleep(0.1)
            return x + c
        constant = 1
        result = partial_multi_thread_tqdm(plus_c, self.data, workers=20, c=constant)
        answer = [i+constant for i in self.data]
        self.assertEqual(result, answer)


if __name__ == '__main__':
    unittest.main()

