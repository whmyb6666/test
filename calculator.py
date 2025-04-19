def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("选择操作:")
    print("1.加")
    print("2.减") 
    print("3.乘")
    print("4.除")

    choice = input("输入选择(1/2/3/4): ")
    
    num1 = float(input("输入第一个数字: "))
    num2 = float(input("输入第二个数字: "))

    if choice == '1':
        print(f"结果: {add(num1, num2)}")
    elif choice == '2':
        print(f"结果: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"结果: {multiply(num1, num2)}")
    elif choice == '4':
        try:
            print(f"结果: {divide(num1, num2)}")
        except ValueError as e:
            print(e)
    else:
        print("无效输入")