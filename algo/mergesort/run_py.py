from mergesort import mergesort
from utils import read_numbers, write_answer


if __name__ == "__main__":
    input_fp = input()
    output_fp = input()
    a = read_numbers(input_fp)
    mergesort(a, 0, len(a) - 1)
    write_answer(a, output_fp)
