import sys

reveal_type(sys.stdout)
# consider implementing Vim autosave feature

# moment is a weighted average of the pixels, giving a rough description of the shape
# radius will be tweaked
def zernike_moment(image, polynomial_radius):
  return mahotas.features.zernike_moments(image, polynomial_radius)

# requires mahotas-imread
img = mahotas.imread("image.jpeg", as_grey=True)
numpy_img = img.astype(numpy.uint8)
otsu_threshold = mahotas.otsu(numpy_img)
binary_img = (numpy_img > otsu_threshold)
