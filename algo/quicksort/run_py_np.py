from quicksort import quicksort
from utils import write_answer
from utilsnp import read_numbers


if __name__ == "__main__":
    input_fp = input()
    output_fp = input()
    a = read_numbers(input_fp)
    quicksort(a, 0, len(a) - 1)
    write_answer(a, output_fp)
