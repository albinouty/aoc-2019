# assign initial value to param var
# while loop, incrementing number by one until the end of the range
# break number into array of six
# compare array values
# if the numbers from left to right are equal or increasing
# AND at least two of the numbers next to eachother are equal
# Then increment the answer variable by 1

ans = 0
param = 402328

while True:
    arr_param = [int(a) for a in str(param)]
    if arr_param[0] <= arr_param[1] \
        and arr_param[1] <= arr_param[2] \
        and arr_param[2] <= arr_param[3] \
        and arr_param[3] <= arr_param[4] \
        and arr_param[4] <= arr_param[5]:
        if arr_param[0] == arr_param[1] \
            or arr_param[1] == arr_param[2] \
            or arr_param[2] == arr_param[3] \
            or arr_param[3] == arr_param[4] \
            or arr_param[4] == arr_param[5]:
            ans += 1
            param += 1
            if param > 864247:
                break
        else:
            param += 1
            if param > 864247:
                break
    else:
        param += 1
        if param > 864247:
                break
print(ans)
