def print_hi(name):
    print("Hi", {name})  # 按 Ctrl+F8 切换断s点。


if __name__ == '__main__':
    param_1 = param_2 = result_value = 0
    while True:  # 使用无限循环
        param_1 = int(input("输入乘数："))  # 将输入的字符串转换为整数
        param_2 = int(input("输入被乘数："))
        print("请计算你刚才所出的这道题：", param_2, "*", param_1, "=")
        result_value = int(input())
        right_result_value = param_2 * param_1
        if (right_result_value == result_value):
            print("恭喜，答案正确！")  # 当答案正确时，跳出循环
            break
        else:
            print("抱歉，答案错误！")  # 当答案错误时，重新循环
    print("结果正确，你所计算的结果为：", param_2, "*", param_1, "=", result_value)
