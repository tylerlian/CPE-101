################################
# CPE 101
# Section: 15
# Lab #4: Polynomial
# Name: Tyler Lian
# Cal Poly ID: tklian
################################

# initializes three different polynomials
poly1 = [4,5,6]
poly2 = [1,8,3]
poly3 = [2,6,1]

# adds two given polynominals
def poly_add(poly1, poly2):
    o_poly = []
    
    # appends polynomial to array
    o_poly.append(poly2[0] + poly1[0])
    o_poly.append(poly2[1] + poly1[1])
    o_poly.append(poly2[2] + poly1[2])

    # returns array
    return o_poly

# testing if adding function works properly
assert poly_add(poly1, poly2) == [5,13,9]
assert poly_add(poly1, poly3) == [6,11,7]
assert poly_add(poly2, poly3) == [3,14,4]

# initialzes three different polynomials
poly1 = [4,1,1]
poly2 = [3,1,1]
poly3 = [1,2,2]

# multiplies two of given polynominals
def poly_mul(poly1, poly2):
    o_poly = []
    d_poly = []

    # appends power 0 to array
    d_poly.append(poly2[0] * poly1[0])
    
    # appends power 1 to array
    o_poly.append(poly2[0] * poly1[1])
    o_poly.append(poly2[1] * poly1[0])
    d_poly.append(o_poly[0] + o_poly[1])

    # appends power 2 to array
    o_poly.append(poly2[0] * poly1[2])
    o_poly.append(poly2[1] * poly1[1])
    o_poly.append(poly2[2] * poly1[0])
    d_poly.append(o_poly[2] + o_poly[3] + o_poly[4])

    # appends power 3 to array
    o_poly.append(poly2[1] * poly1[2])
    o_poly.append(poly2[2] * poly1[1])
    d_poly.append(o_poly[5] + o_poly[6])

    # appends power 4 to array
    d_poly.append(poly2[2] * poly1[2])

    # returns array
    return d_poly

# tests if the multiplying function works properly
assert poly_mul(poly1, poly2) == [12,7,8,2,1]
assert poly_mul(poly1, poly3) == [4,9,11,4,2]
assert poly_mul(poly3, poly2) == [3,7,9,4,2]




