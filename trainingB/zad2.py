import numpy

a = numpy.array([1,2,3])
b = numpy.array([-1,3,5])

scalar_product = numpy.dot(a,b)
norm_a = numpy.sqrt(numpy.dot(a,a))
norm_b = numpy.sqrt(numpy.dot(b,b))

cos_alpha = scalar_product/(norm_a*norm_b)

alpha = numpy.arccos(cos_alpha)
alpha_g = (alpha*360)/(2*numpy.pi)

print(alpha_g)