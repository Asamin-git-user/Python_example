# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

input_cnt = int(input())
# print(input_cnt)

input_user = []
input_user_exists = ""

for i in range(input_cnt):
    # print(i)

    input_user.append(input().rstrip())
    # print(input_user)

    # if i == 0:
    #     input_user[i] = str(input_user_exists)

    # if input_user_exists == input_user[i]:
    #     print("YES")
    # else:
    #     print("NO")

# print(input_user)
# print("input_user_exists=" + input_user_exists)

# for k in input_user:
#     input_user_exists = k
#     # print(input_user_exists)
#     # print(k)

#     if k in input_user:
#         print("YES")
#     else:
#         print("NO")

# for_cnt = 0

# for k in input_user:
#     # print("k=" + k)
#     for j in range(len(input_user)):
#         # print("input_user =" + input_user[j])
#         if input_user[j] == k:
#             print("NO")
#         else:
#             print("YES")


# 4
# Jimmy
# Bob
# James
# Jimmy

int_cnt = 0
ans_list = []

for k in input_user:
    input_user_exists = k
    print("------------------------")
    print("k = " + k)

    for j in range(len(input_user)):
        print("j = " + str(j))
        print("input_user = " + input_user[j])

        if k == input_user[j]:
            int_cnt += 1
            print(int_cnt)
            # ans_list.insert(j, int_cnt)
            # ans_list[j] = int_cnt
            # print(ans_list)
        else:
            print("false")
            print(int_cnt)
            # ans_list.insert(j, int_cnt)
            # ans_list[j] = int_cnt

    # if int_cnt == 1:
    #     ans_list.append("YES")
    # elif int_cnt >= 2:
    #     ans_list.append("NO")
    # else:
    #     ans_list.append("NO")
    
    print(ans_list)
    int_cnt = 0

# for out_ans in ans_list:
#     print(out_ans)
