def count_divisions(A, B):
    if B == 0:
        return "Division by zero is not allowed"
    
    count = 0
    while A % B == 0:
        A //= B
        count += 1
    
    return count

# Example usage:
A = int(input("Enter number A: "))
B = int(input("Enter number B: "))

times_divisible = count_divisions(A, B)

if times_divisible > 0:
    print(f"A is divisible by B {times_divisible} times.")
else:
    print("A is not purely divisible by B.")
