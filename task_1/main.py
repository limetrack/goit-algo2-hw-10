import random
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]  # Вибір останнього елемента як опорного
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return deterministic_quick_sort(left) + [pivot] + deterministic_quick_sort(right)


def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for i, x in enumerate(arr) if x <= pivot and i != pivot_index]
    right = [x for i, x in enumerate(arr) if x > pivot]

    return randomized_quick_sort(left) + [pivot] + randomized_quick_sort(right)


def measure_sorting_time(sort_function, arr, runs=5):
    times = []
    for _ in range(runs):
        arr_copy = arr.copy()
        start_time = time.time()
        sort_function(arr_copy)
        times.append(time.time() - start_time)

    return np.mean(times)


if __name__ == "__main__":
    sizes = [10_000, 50_000, 100_000, 500_000]
    results = []

    for size in sizes:
        test_array = [random.randint(0, 1_000_000) for _ in range(size)]
        rand_time = measure_sorting_time(randomized_quick_sort, test_array)
        det_time = measure_sorting_time(deterministic_quick_sort, test_array)
        results.append((size, rand_time, det_time))
        print(f"Розмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {rand_time:.4f} секунд")
        print(f"   Детермінований QuickSort: {det_time:.4f} секунд")
        print()

    df_results = pd.DataFrame(
        results,
        columns=[
            "Розмір масиву",
            "Рандомізований QuickSort",
            "Детермінований QuickSort",
        ],
    )

    plt.figure(figsize=(8, 6))
    plt.plot(
        df_results["Розмір масиву"],
        df_results["Рандомізований QuickSort"],
        label="Рандомізований QuickSort",
    )
    plt.plot(
        df_results["Розмір масиву"],
        df_results["Детермінований QuickSort"],
        label="Детермінований QuickSort",
        linestyle="--",
    )
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (секунди)")
    plt.title("Порівняння рандомізованого та детермінованого QuickSort")
    plt.legend()
    plt.grid(True)
    plt.show()
