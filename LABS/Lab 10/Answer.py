class ComplexNumber:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def set_complex_number(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def display(self):
        print(f"{self.real} + {self.imaginary}i")

    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def subtract(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def multiply(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)


# Getting input from user
real_user = float(input("Enter the real part of the first complex number: "))
imaginary_user = float(input("Enter the imaginary part of the first complex number: "))

# First complex number
c1 = ComplexNumber(real_user, imaginary_user)

# Second complex number, predefined
c2 = ComplexNumber(3, 4)

# Displaying the complex numbers
print("First Complex Number:")
c1.display()
print("Second Complex Number:")
c2.display()

# Operations
sum_result = c1.add(c2)
diff_result = c1.subtract(c2)
prod_result = c1.multiply(c2)

# Displaying results
print("Sum of the two complex numbers:")
sum_result.display()
print("Difference of the two complex numbers:")
diff_result.display()
print("Product of the two complex numbers:")
prod_result.display()
