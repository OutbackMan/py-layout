#ifndef __common_h__
#define __common_h__

#if defined(__linux__)		
#define SCREENSHOT_USING_LINUX
#elif defined(_WIN32)
#define SCREENSHOT_USING_WINDOWS
#elif defined(__APPLE__)
#define SCREENSHOT_USING_MAC
#else
#error "Your OS is not supported. Supported OSs are windows, mac and linux"

#endif
