
import pkgutil
import custompack.custom as custom


# See https://stackoverflow.com/questions/1707709/list-all-the-modules-that-are-part-of-a-python-package/1707786#
package = custom
for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
    print("Found submodule %s (is a package: %s)" % (modname, ispkg))
