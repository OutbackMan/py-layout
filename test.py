# consider implementing Vim autosave feature

'''
PILLOW:
'''
'''
PYAUTOGUI:
linux --> scrot
'''

# could optimise via c binding
import pyautogui

desktop_screenshot = pyautogui.screenshot()
pyautogui.keyDown("shift")
pyautogui.press("left")
pyautogui.press("left")
pyautogui.keyUp("shift")
pyautogui.typewrite("text here")


# moment is a weighted average of the pixels, giving a rough description of the shape
# radius will be tweaked
def zernike_moment(image, polynomial_radius):
  return mahotas.features.zernike_moments(image, polynomial_radius)

# requires mahotas-imread
img = mahotas.imread("image.jpeg", as_grey=True)
numpy_img = img.astype(numpy.uint8)
otsu_threshold = mahotas.thresholding.otsu(numpy_img)
binary_img = (numpy_img > otsu_threshold)
