import os

quantity_of_bytes = 0

list_with_everything = []
for path, no, files in os.walk(os.environ["TMP"]):
    list_with_everything.append([path, files])

while True:
    for step in list_with_everything:
        path_arg, files_arg = "", []
        for types in step[0]:
            if type(types) == str:
                path_arg = types
                continue
            else:
                files_arg = types
                pass

            for file in files_arg:
                quantity_of_bytes += os.stat(os.path.join(path_arg, file)).st_size

    print(quantity_of_bytes)
    
    break