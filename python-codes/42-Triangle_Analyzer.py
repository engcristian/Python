'''
Analysing a triangle by its segments, if they form a triangle, if it's equilateral,
isosceles or scalene type.
'''
print('-='*20)
print('       Triangle Analyzer')
print('-='*20)
# a, b and c letters represent each segment or edges or lines
a = float(input('First segment:')) 
b = float(input('Second segment:'))
c = float(input('Third segment:'))
if a < b + c and b < c + a and c < a + b: #Main condition to form a triangle
    print('The segments FORM a triangle!')
    if a == b == c:
        print('The triangle is EQUILATERAL!')
    elif a != b != c != a:
        print('The triangle is SCALENE!')
    else:
        print('The triangle is ISOSCELES!')
else:
    print("The segments don't form a triangle!")
