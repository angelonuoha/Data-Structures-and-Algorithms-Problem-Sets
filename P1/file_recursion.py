import os

def find_files(suffix, path):

    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    return _find_files(suffix, path, [])

def _find_files(suffix, path, result):
    files = os.listdir(path)
    new_paths = []
    
    # If the folder has no files, return nothing
    if files == ['.gitkeep']:
        return

    # Each path will either be a file or another directory. If it's a file that ends in the desired suffix, add it to the result array. If it's a directory, create a new path for it and it to the new_paths array
    for item in files:
        new_path = os.path.join(path, item)
        if os.path.isfile(new_path):
            if item.endswith(suffix):
                result.append(new_path)
        else:
            new_paths.append(new_path)
    
    # Call a recursive function replacing the original directory paths with the new paths
    for item in new_paths:
        _find_files(suffix, item, result)
    
    print(result)
    return result

# Inputs
print("Input 1: .c, ./testdir")
print("Input 2: .h, ./testdir")
print("Input 2: 0, ./testdir")
print("Input 1: .py, ./testdir")

# Test Cases
find_files(".c", "./testdir") # Will return ['./testdir/t1.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']
find_files(".h", "./testdir") # Will return ['./testdir/t1.h', './testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/subdir1/a.h']
find_files("0", "./testdir") # Will return [] because this is not a valid file suffix
find_files(".py", "./testdir") # Will return [] because there are no python files in testdir