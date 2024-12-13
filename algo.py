
import random
import cProfile
from typing import List

MIN_VALUE = -1000
MAX_VALUE = 1000
LIST_SIZE = 1000
RANDOM_SEED = 42
''' A random seed value allows you to get consistent results when running randomisation multiple times.
    This can be useful when you want to be able to replicate some random behaviour. E.g. once you generate a random list,
    you may want to keep working with that same list and ensure that the changes in performance are due to other things
    that you are changing, not due to a different randomisation of a list.
'''

class ListGenerator:
    def __init__(self, min_value: int, max_value: int, list_size: int, seed: int):
        self.min_value = min_value
        self.max_value = max_value
        self.list_size = list_size
        self.seed = seed

    def generate_random_list(self) -> List[int]:
        random.seed(self.seed)
        return [random.randint(self.min_value, self.max_value) for _ in range(self.list_size)]

    def generate_sorted_list(self) -> List[int]:
        return list(range(self.min_value, self.min_value + self.list_size))

    def generate_reverse_sorted_list(self) -> List[int]:
        return list(range(self.max_value, self.max_value - self.list_size, -1))

    def generate_nearly_sorted_list(self) -> List[int]:
        lst = list(range(self.min_value, self.min_value + self.list_size))
        if self.list_size > 1:
            random.seed(self.seed)
            index = random.randint(0, self.list_size - 1)
            lst[index], lst[index + 1] = lst[index + 1], lst[index]
        return lst

class Sorter:
    def __init__(self):
        self.algorithms = {
            "quicksort_1": self.quicksort_1,
            "quicksort_2": self.quicksort_2,
            "my_algorithm": self.my_algorithm,
        }

    def sort(self, lst: List[int], algorithm_name: str) -> List[int]:
        if algorithm_name not in self.algorithms:
            raise ValueError(f"Unknown algorithm: {algorithm_name}")
        return self.algorithms[algorithm_name](lst)

    def quicksort_1(self, lst: List[int]) -> List[int]:

        if len(lst)  <= 1:
            return lst

        pivot = lst[0]
        left = [nr for nr in lst[1:] if nr < pivot]
        right = [nr for nr in lst[1:] if nr >= pivot]

        return self.quicksort_1(left) + [pivot] + self.quicksort_1(right)

    def quicksort_2(self, lst: List[int]) -> List[int]:
        if len(lst)  <= 1:
            return lst

        pivot = lst[-1]
        left = [nr for nr in lst[:-1] if nr < pivot]
        right = [nr for nr in lst[:-1] if nr >= pivot]

        return self.quicksort_1(left) + [pivot] + self.quicksort_1(right)

    def my_algorithm(self, lst: List[int]) -> List[int]:
        code = sorted(lst)
        return code

# Test the sorting functionality
def main():
    generator = ListGenerator(min_value=MIN_VALUE, max_value=MAX_VALUE, list_size=LIST_SIZE, seed=RANDOM_SEED)
    sorter = Sorter()

    # TODO. Expand this example to work with additional lists and to compare them
    random_list = generator.generate_random_list()

    for algo in ["quicksort_1", "quicksort_2", "my_algorithm"]:
        pr = cProfile.Profile()
        pr.enable()
        sorted_list = sorter.sort(random_list, algo)
        pr.disable()
        pr.print_stats(sort='time')

if __name__ == "__main__":
    main()
