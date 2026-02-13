# AIM: SUM & AVERAGE
# Coder: Shiburaj
# Date: 13/02/26

print("SUM & AVERAGE\n")

nums = input("Enter numbers: ")
num_list = nums.split(",")
num_list = [int(num) for num in num_list]
sum = sum(num_list)
avg = sum / len(num_list)
print("Sum:", sum)
print("Average:", avg)