# PowerMod Function

## Introduction

The `powermodf` function calculates the power and modulo of a given base number raised to a specified exponent, considering a provided modulus. This can be particularly useful in applications involving modular arithmetic, cryptography, and number theory.

## Usage

### Function Signature

```python
def powermodf(a, b, m):
    """
    Calculate the power and modulo of a^b (mod m).

    Parameters:
    - a (int): Base number.
    - b (int): Exponent.
    - m (int): Modulus.

    Returns:
    None. Prints the result of a^b and a^b (mod m).
    """
    print(f"The power is {pow(a, b)}")
    print(f"The mod is {pow(a, b, m)}")
```

### How to Use

1. **Input**: Run the function by providing the base number, exponent, and modulus when prompted.

   ```python
   powermodf(int(input("Enter the base number: ")), int(input("Enter the exponent: ")),
             int(input("Enter the modulus: ")))
   ```

2. **Output**: The function will display the result of the base number raised to the exponent and the result modulo the specified modulus.

## Example

```python
# Example Usage
powermodf(3, 4, 5)
```

Output:

```
The power is 81
The mod is 1
```

## Note

- Ensure that the input values are integers, as the function does not handle non-integer inputs.
