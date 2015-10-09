import argparse


# def swap(List, Idx, swapIdx):
#     temp = List[Idx]
#     List[Idx] = List[swapIdx]
#     List[swapIdx] = temp
#     #print("After Swap: ",List)


# def qsort(List, startIdx, EndIdx):
#     if startIdx < EndIdx:
#         pivotPos = Partition(List, startIdx, EndIdx)
#         qsort(List, startIdx, pivotPos - 1)
#         qsort(List, pivotPos + 1, EndIdx)


# def Partition(List, startIdx, EndIdx):
#     pivot = List[startIdx]
#     #print("pivot : " ,pivot)
#     swap_Idx = startIdx+1
#     for i in range(startIdx + 1, EndIdx):
#         if (List[i] < pivot):
#             swap(List, swap_Idx, i)
#             swap_Idx += 1
#     swap(List, startIdx, swap_Idx-1)
#     return swap_Idx-1


def Simple_Sorting():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip('\n')
            List = [float(i) for i in line.split(" ")]
            List.sort()
            for i in List:
                print('{0:.3f}'.format(i), end=" ")
            print()
Simple_Sorting()
