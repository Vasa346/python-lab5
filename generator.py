#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from concurrent.futures import ThreadPoolExecutor
import time
from functools import reduce

def apply_n_times(func, n, value):
    """Применяет функцию func к value n раз."""
    result = value
    for _ in range(n):
        result = func(result)
    return result

def significant_change_generator(sequence, func, n, threshold=0.1):
    """
    Генератор, применяющий функцию func к каждому элементу n раз.
    Возвращает только элементы, изменившиеся значительно (относительное изменение > threshold).
    """
    for item in sequence:
        transformed = apply_n_times(func, n, item)
        if isinstance(item, (int, float)) and item != 0:
            change = abs(transformed - item) / abs(item)
        elif isinstance(item, str):
            change = abs(len(transformed) - len(item)) / max(len(item), 1)
        else:
            change = 0
        if change > threshold:
            yield transformed

def parallel_significant_change_generator(sequence, func, n, threshold=0.1, max_workers=4):
    """
    Многопоточная версия генератора.
    """
    def process_item(item):
        transformed = apply_n_times(func, n, item)
        if isinstance(item, (int, float)) and item != 0:
            change = abs(transformed - item) / abs(item)
        elif isinstance(item, str):
            change = abs(len(transformed) - len(item)) / max(len(item), 1)
        else:
            change = 0
        return transformed if change > threshold else None

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = executor.map(process_item, sequence)
        for result in results:
            if result is not None:
                yield result

if __name__ == '__main__':
    # Пример использования
    data = [1, 2, 3, 4, 5, 10, 20, 50]
    
    def square(x):
        return x ** 2
    
    print("=== Обычный генератор ===")
    gen = significant_change_generator(data, square, 2, threshold=0.5)
    result = list(gen)
    print("Значительно изменившиеся элементы:", result)
    
    # Применение filter и reduce
    filtered = list(filter(lambda x: x > 10, result))
    print("После filter (>10):", filtered)
    if filtered:
        sum_reduce = reduce(lambda x, y: x + y, filtered)
        print("Сумма после reduce:", sum_reduce)
    
    print("\n=== Многопоточный генератор ===")
    start = time.time()
    gen_parallel = parallel_significant_change_generator(data * 1000, square, 2, threshold=0.5)
    result_parallel = list(gen_parallel)
    parallel_time = time.time() - start
    
    start = time.time()
    gen_normal = significant_change_generator(data * 1000, square, 2, threshold=0.5)
    result_normal = list(gen_normal)
    normal_time = time.time() - start
    
    print(f"Обычный: {normal_time:.4f} сек")
    print(f"Многопоточный: {parallel_time:.4f} сек")
    print(f"Ускорение: {normal_time / parallel_time:.2f}x")