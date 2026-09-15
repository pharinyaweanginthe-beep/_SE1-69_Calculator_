def add(x, y):
    """ฟังก์ชั่นสำหรับการบวกเลข"""
    return x + y


def subtract(x, y):
    """ฟังก์ชั่นสำหรับการลบเลข"""
    return x - y


def multiply(x, y):
    """ฟังก์ชั่นสำหรับการคูณเลข"""
    return x * y


def divide(x, y):
    """ฟังก์ชั่นสำหรับการหารเลข"""
    if y == 0:
        return "ไม่สามารถหารด้วย 0 ได้"
    return x / y


print("================================")
print("       Simple Calculator")
print("================================")

num1 = float(input("กรุณากรอกเลขตัวที่ 1: "))
num2 = float(input("กรุณากรอกเลขตัวที่ 2: "))

print("--------------------------------")

print("Addition (+):", add(num1, num2))
print("Subtraction (-):", subtract(num1, num2))
print("Multiplication (*):", multiply(num1, num2))
print("Division (/):", divide(num1, num2))
