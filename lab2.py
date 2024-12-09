print("The autor of this program is Kateryna Drachuk. This program calculates the value of a function at a given point. Variant 5.")
import math

def s(x, eps):
    n = 0
    term = (-1)**n/(4*n+3)*x**(4*n+3)
    total_sum = term

    while abs(term) > eps:
        n += 1
        term = (-1)**n/(4*n+3)*x**(4*n+3)
        total_sum += term

    return total_sum

def main():
    try:
        x = float(input("Enter x: "))
        eps = float(input("Enter eps:"))
        print("*** do calculations ...", end="")
        if not -1 <= x <= 1:
            raise ValueError("x must be in the range  [-1, 1].")
        
        if eps <= 0:
            raise ValueError("eps must be greated than 0.")
        print("done")
        
        print(f"\nfor x = {x:.7f}")
        print(f"for eps = {eps:.8E}")

        result = s(x, eps)
        print(f"result = {result:.10f}")

    except KeyboardInterrupt:
        print("\nprogram aborted")
    except Exception as e:
        print("\n***** error")
        print(e)
if __name__ == "__main__":
    main()
