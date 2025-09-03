integer_var = 42
float_var = 3.14159
complex_var = 3 + 4j

print("Numeric Types:")
print(f"Integer: {integer_var} (type: {type(integer_var)})")
print(f"Float: {float_var} (type: {type(float_var)})")
print(f"Complex: {complex_var} (type: {type(complex_var)})")

string_var = "Hello, Python!"
print(f"\nString: {string_var} (type: {type(string_var)})")

bool_true = True
bool_false = False
print(f"\nBoolean True: {bool_true} (type: {type(bool_true)})")
print(f"Boolean False: {bool_false} (type: {type(bool_false)})")

list_var = [1, 2, 3, 4, 5]
tuple_var = (10, 20, 30)
range_var = range(5)

print(f"\nList: {list_var} (type: {type(list_var)})")
print(f"Tuple: {tuple_var} (type: {type(tuple_var)})")
print(f"Range: {list(range_var)} (type: {type(range_var)})")

dict_var = {"name": "Alice", "age": 25, "city": "New York"}
print(f"\nDictionary: {dict_var} (type: {type(dict_var)})")

set_var = {1, 2, 3, 4, 5}
frozenset_var = frozenset([1, 2, 3, 4, 5])

print(f"\nSet: {set_var} (type: {type(set_var)})")
print(f"Frozenset: {frozenset_var} (type: {type(frozenset_var)})")

print("\n=== Type Conversion Examples ===")
num_str = "123"
num_int = int(num_str)
num_float = float(num_str)

print(f"String '{num_str}' to Integer: {num_int} (type: {type(num_int)})")
print(f"String '{num_str}' to Float: {num_float} (type: {type(num_float)})")

num = 42
num_to_str = str(num)
print(f"Integer {num} to String: '{num_to_str}' (type: {type(num_to_str)})")

my_variable = "valid"
_myVariable = "also valid"
variable123 = "valid too"

radius = 5
area = 3.14159 * radius ** 2
print(f"\nArea of circle with radius {radius}: {area:.2f}")