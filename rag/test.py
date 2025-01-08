import pkgutil
import chromadb.api as api_module

# Print all submodules and items in the chromadb.api package
print("Inspecting chromadb.api package:")
for importer, modname, ispkg in pkgutil.iter_modules(api_module.__path__):
    module = importer.find_module(modname).load_module(modname)
    print(f"Module: {modname}, Is a package: {ispkg}")
    print(f"Contents: {dir(module)}")
