#ifndef __screenshot_h__
#define __screenshot_h__

#if defined(__linux__)		
#define SCREENSHOT_USING_LINUX
#include <X11/Xlib.h>
#elif defined(_WIN32)
#define SCREENSHOT_USING_WINDOWS
#include <windows.h>
#elif defined(__APPLE__)
#define SCREENSHOT_USING_MAC
#include <ApplicationServices/ApplicationServices.h>
#else
#error "Your OS is not supported. Supported OSs are windows, mac and linux"

// windows --> os.path.dirname(sys.executable) + "include"
#include <Python.h>

#include <stddef.h>
#include <stdint.h>

// memcpy
typedef struct {
	size_t width;
	size_t height;
	uint8_t* bgr_pixels;
} SCREENSHOT__ImgData;

PyObject* screenshot(void);

#endif
