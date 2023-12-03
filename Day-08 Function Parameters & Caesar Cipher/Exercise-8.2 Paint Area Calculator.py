
def calculation(height,width,coverage):
    result = round((height*width) / coverage)
    return result
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage=5
result = calculation(test_h,test_w,coverage)
print(f"You'll need {result} cans of paing.")
    