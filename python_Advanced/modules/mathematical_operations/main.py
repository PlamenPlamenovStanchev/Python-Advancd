from pythonAdvanced.modules.mathematical_operations.core import mapper

expression = input()
num_as_string, sign, num2_as_string = expression.split()
num1 = float(num_as_string)
num2 = int(num2_as_string)

result = mapper[sign](num1, num2)

if isinstance(result, str):
    print(result)
else:
    print(f"{result:.2f}")


