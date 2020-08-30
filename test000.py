# 1. リストにお客さんの名前を格納する
n = int(input())
out_ans = []

person_list = []
for i in range(n):
    person_list.append(input())
    ## 2. その名前がリストに初めて格納されたことを「1つだけ存在すること」で判定する
    if(person_list.count(person_list[i]) == 1):
        # print("YES")
        out_ans.append("YES")
    else:
        # print("NO")
        out_ans.append("NO")

# print(out_ans)

for k in range(len(out_ans)):
    print(out_ans[k])

