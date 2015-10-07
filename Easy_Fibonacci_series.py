import argparse


def Fibonacci_Series():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    indices = []
    max_Idx = -20
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip("\n")
            indices.append(int(line))
            max_Idx = max_Idx if (max_Idx > int(line)) else int(line)
        Fib_series = [0, 1]
        for i in range(2, max_Idx + 1):
            Fib_series.append(Fib_series[i - 1] + Fib_series[i - 2])
        for i in indices:
        	print(Fib_series[i])

Fibonacci_Series()
