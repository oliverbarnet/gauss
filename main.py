from matrix import *

test = generate_matrix(3)

print("Original matrix:")
test.show_matrix()

while True:
    transformation = input("Enter a row transformation (or 'exit' to quit): ")
    if transformation.lower() == 'exit':
        break
    test.update(transformation)
    print("Updated matrix:")
    test.show_matrix()
    
    # Check if matrix is in RREF
    if test.is_rref():
        print(f"\n✓ Matrix is in RREF! Completed in {test.moves_count} moves!")
        break