# # potential = input()
def main(potential):
    totals = []
    total = []
    totalW = []
    ingredients = ["cheese", "basil", "mushrooms", "peppers", "tomatoes", "pineapple"]
    for i in range(int(potential)):
        liked = input()
        ds = input()
        v = liked.split(" ")[1:]
        w = ds.split(" ")[1:]
        for j in v:
            total.append(j)
        for k in w:
            totalW.append(k)
    for i in total:
        for j in ingredients:
            if i == j:
                totals.append(i)
    for i in totalW:
        if i in totals:
            totals.remove(i)
    print(f"{len(totals)} {' '.join(totals)}")
main(input())

# L=[4,2,1,3]
# def main(T):
#     for z in range(int(T)):
#         newL = []
#         newScore = 0
#         Ls = []
#         N = input()
#         L = input().split(" ")
#         for i in L:
#             Ls.append(int(i))
#         # sortedL = sorted(Ls)
#         sortedL = Ls
#         v = 0
#         for i in range(len(Ls)):
#             if Ls[i] == min(Ls):
#                 v = i
#         for i in range(v+1):
#             for j in range(v+1):
#                 if sortedL[i] < sortedL[j]:
#                     sortedL[i], sortedL[j] = sortedL[j], sortedL[i]
#         for i in range(len(L)):
#             for j in range(len(L)):
#                 if sortedL[i] == Ls[j]:
#                     newL.append(j)
#         print(newL)
#         print(Ls)
#         print(sortedL)
#         p = [i for i in range(len(L))]
#         for q in range(len(L)-1):
#             score = (newL[q] - p[q]) + 1
#             newScore += score
#         print(f"Case #{z+1}: {newScore}")
# main(input())

# for i in range(v+1):
#     for j in range(v+1):
#         if Ls[i] < Ls[j]:
#             Ls[i], Ls[j] = Ls[j], Ls[i]



# def main(T):
#     for z in range(int(T)):
#         newL = []
#         newScore = 0
#         Ls = []
#         N = input()
#         L = input().split(" ")
#         for i in L:
#             Ls.append(int(i))
#         for i in range(len(Ls)):
#             if Ls[i] == min(Ls):
#                 mins = i
#         sortedL = sorted(Ls)
#         for i in range(len(L)):
#             for j in range(len(L)):
#                 if sortedL[i] == Ls[j]:
#                     newL.append(j)
#         p = [i for i in range(len(L))]
#         for q in range(len(L)-1):
#             score = (newL[q] - p[q]) + 1
#             newScore += score
#         print(f"Case #{z+1}: {newScore}")
# main(input())