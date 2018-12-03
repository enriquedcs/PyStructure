# Prime Number

def IsPrime(nums):
    if nums <= 0:
       return False

    if (nums%2) == 0:
        print ("Number is not Prime: ")
    else:
        print("Number is Prime: ")

    return nums


nums = 0

print(IsPrime(nums))