#include "screenshot.h"

#include "common.h"

#if defined(SCREENSHOT_USING_LINUX)		
#include <X11/Xlib.h>
#elif defined(SCREENSHOT_USING_WINDOWS)
#include <windows.h>
#else 
#include <ApplicationServices/ApplicationServices.h>

static PyObject* screenshot__bgr_pixel_tuple();

PyObject* screenshot(void)
{
	Py_Initialize();
	// PySys_SetPath("/usr/home");

	PyObject* numpy_string = PyString_FromString("numpy");
	if (numpy_string == NULL) goto error;

	PyObject* numpy_module_handler = PyImport_Import(numpy_string);
	if (numpy_module_handler == NULL) goto error;

	PyObject* numpy_asarray = PyObject_GetAttrString(numpy_module_handler, "asarray");
	if (numpy_asarray == NULL || PyCallable_Check(numpy_asarray)) goto error;

	PyObject* img_bgr_pixel_tuple = screenshot__bgr_pixel_tuple();	


	PyObject* screenshot = PyObject_CallObject(numpy_asarray, img_bgr_pixel_tuple);
	if (screenshot == NULL) goto error;

	Py_Finalize();

	return screenshot;

	// may have to do frees also
	error:
		PyErr_Print();		
		Py_Finalize();
		return NULL;
}

	for (int img_pixel_index = 0; img_pixel_index < img_data.width * img_data.height; ++img_pixel_index) {
		PyObject* img_pixel_info = PyTuple_New(3); 
		PyTuple_SetItem(img_pixel_info, 0, *img_data.bgr_pixels++);
		PyTuple_SetItem(img_pixel_info, 1, *img_data.bgr_pixels++);
		PyTuple_SetItem(img_pixel_info, 2, *img_data.bgr_pixels++);

		PyTuple_SetItem(img_pixel_list, index, img_pixel_info);
	}

static PyObject* screenshot__bgr_pixel_tuple(void)
{
#if defined(SCREENSHOT_USING_LINUX)
	Display* display = XOpenDisplay("");
	Window root = DefaultRootWindow(display);

	XWindowAttributes window_attributes;
	XGetWindowAttributes(display, root, &window_attributes);

	XImage* image = XGetImage(
								display, 
								root, 
								0, 
								0, 
								window_attributes.width,
								window_attributes.height,
								AllPlanes,
								ZPixmap
							); 

unsigned long red_mask = image->red_mask;
	unsigned long green_mask = image->green_mask;
	unsigned long blue_mask = image->blue_mask;

	unsigned char arr[width * height][3] = { 0 };

	for (int x = 0; x < width; x++) {
		for (int y = 0; y < height; y++) {
			unsigned long pixel = XGetPixel(image, x, y);

			unsigned char red = pixel & red_mask;
			unsigned char green = pixel & green_mask;
			unsigned char blue = pixel & blue_mask;

			

		}
	}

	XCloseDisplay(display);

}

PyObject* IBU__windows_screenshot(void)
{
	int screen_width = GetSystemMetrics(SM_CXVIRTUALSCREEN);			
	int screen_height = GetSystemMetrics(SM_CYVIRTUALSCREEN);			

	HDC window_device_context = CreateCompatibleDC(NULL);

	for (int x = 0; x < screen_width; ++x) {
		for (int y = 0; y < screen_height; ++y) {
			COLORREF rgb_pixel = GetPixel(window_device_context, x, y);		
			unsigned char red_pixel = GetRValue(rgb_pixel);
			unsigned char green_pixel = GetGValue(rgb_pixel);
			unsigned char blue_pixel = GetBValue(rgb_pixel);
		}		
	} 

	DeleteDC(window_device_context);
}

// link to ApplicationServices.framework --> find_library(ApplicationServices)
PyObject* IBU__mac_screenshot(void)
{
	// core graphics
	CGImageRef image_ref = CGDisplayCreateImage(CGMainDisplayID());
	int image_width = CGImageGetWidth(image_ref);
	int image_height = CGImageGetHeight(image_ref);

	CGDataProviderRef provider = CGImageGetDataProvider(image_ref);
	CFDataRef dataref = CGDataProviderCopyData(provider);

	unsigned char* pixels = CFDataGetBytePtr(dataref);

	for (int x = 0; x < image_width; ++x) {
		for (int y = 0; y < image_width; ++y) {
			unsigned char red_pixel = *pixels++;
			unsigned char green_pixel = *pixels++;
			unsigned char blue_pixel = *pixels++;
		}		
	}

	// create list [[b, g, r], [b, g, r], ...]
	// numpy.asarray(list)

	CFRelease(dataref);
	CGImageRelease(image_ref);

}






// want BGR
numpy.asarray(numpy.clip(), dtype="uint8")
