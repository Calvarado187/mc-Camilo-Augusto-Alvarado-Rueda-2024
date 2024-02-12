def main():
    
    U = set(input("Ingrese los elementos del conjunto universal (U) separados por espacios: ").split())

    
    A = set(input("Ingrese los elementos del conjunto A separados por espacios: ").split())

    
    if not A.issubset(U):
        print("Error: A no es un subconjunto de U.")
        return

    
    union_intersection = U.union(A).intersection(A)
    intersection_xor = U.intersection(A) ^ A
    difference_xor = (U - A) ^ A

    
    print(f"(U⋃A)⋂A: {union_intersection}")
    print(f"(U⋂A) ⨁A: {intersection_xor}")
    print(f"(U − A) ⨁A: {difference_xor}")

if __name__ == "__main__":
    main()
