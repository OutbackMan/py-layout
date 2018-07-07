# LOGGING
# require __init__.py to mark a directory to be searched for a package, i.e. import statement



def assert(condition, msg):
    if (!condition):
        ITEST_Logging.logger.critical(msg)
        if __debug__:
            breakpoint()
        else:
            pass

# pip freeze > requirements.txt
# pip install -r requirements.txt
