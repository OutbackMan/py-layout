#include <Python.h>

// IBU (image bot utils)
#if defined(__linux__)		
#define HOST_OS "LINUX"
#include <X11/Xlib.h>
#elif defined(_WIN32)
#include <windows.h>
#define HOST_OS "WINDOWS"
#elif defined(__APPLE__)
#define HOST_OS "MAC"
#include <ApplicationServices/ApplicationServices.h>
#else
#error "Your OS is not supported. Supported OSs are windows, mac and linux"

PyObject* IBU_screenshot(void)
{
	Py_Initialize();
	// PySys_SetPath("/usr/home");

	PyObject* numpy_string = PyString_FromString("numpy");
	// if (numpy_string != NULL)
	PyObject* numpy_module = PyImport_Import(numpy_string);
	if (numpy_module != NULL) {

	} else {
		PyErr_Print();		
		return NULL;
	}
}

PyObject* IBU__linux_screenshot(void)
{
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


int main(int argc, char** argv)
{

	PyObject* argument_holder = PyTuple_New(1); 
	PyObject* argument = PyString_FromString("arg1");
	PyTuple_SetItem(argument_holder, 0, argument);


	// if (numpy_asarray != NULL && PyCallable_Check(numpy_asarray))
	PyObject* numpy_asarray = PyObject_GetAttrString(numpy_module, "asarray");
	PyObject* ret_val = PyObject_CallObject(numpy_asarray, argument_holder);


	

	Py_Finalize();

	return 0;
}





// want BGR
numpy.asarray(numpy.clip(), dtype="uint8")
