# consider implementing Vim autosave feature
"""
'''
PILLOW:
'''
'''
PYAUTOGUI:
linux --> scrot
'''
import pyautogui



# moment is a weighted average of the pixels, giving a rough description of the shape
# radius will be tweaked
def zernike_moment(image, polynomial_radius):
  return mahotas.features.zernike_moments(image, polynomial_radius)

# requires mahotas-imread
img = mahotas.imread("image.jpeg", as_grey=True)
numpy_img = img.astype(numpy.uint8)
otsu_threshold = mahotas.thresholding.otsu(numpy_img)
binary_img = (numpy_img > otsu_threshold)
"""
# numpy.whl (could use mlk version if require more speed)
# opencv.whl (available of pypi)


# for this to work with mypy, set $MYPYPATH = location of package (same as $PYTHONPATH?)
import numpy
import cv2

# pixel[blue, green, red]
# pixel[intensity]
greyscale_image: numpy.ndarray = cv2.imread("ITest/image.JPG", cv2.IMREAD_GREYSCALE)

# remove noise, whilst preserving edges
blurred_greyscale_image = cv2.bilateralFilter(greyscale_image, 11, 17, 17)

edges_image = cv2.Canny(blurred_greyscale_image, 30, 200)

contoured_image, contours, hierarchy = cv2.findContours(edges_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# only want largest contours
pruned_contoured_image = sorted(contoured_image, key=cv2.contourArea, reverse=True)[:10]

game_screen_contour = None

for contour in pruned_contoured_image:
    contour_perimeter = cv2.arcLength(contour, True)
    # 2% of 
    approximated_contour = cv2.approxPolyDP(contour, 0.02 * contour_perimeter, True)

    # if it has 4 edges
    if len(approximated_contour) == 4:
        game_screen_contour = approximated_contour
        break


cv2.drawContours(greyscale_image, [game_screen_contour], -1, (0, 255, 0), 3)

game_screen_rectangle = cv2.minAreaRect(game_screen_contour)
game_screen_box = cv2.boxPoints(game_screen_rectangle)

for p in box:
    pt = (p[0],p[1])
    print pt
    cv2.circle(im,pt,5,(200,0,0),2)




print(type(image))
cv2.imshow("my-image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
