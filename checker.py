def сatalog_weight(final_path = "C:/Windows/Temp"):
    from os import walk, stat, path
    quantity_of_bytes = 0

    list_with_everything = []
    for path, no, files in walk(final_path):
        list_with_everything.append([path, files])

    while True:
        for step in list_with_everything:
            path_arg, files_arg = "", []
            for types in step:
                if type(types) == str:
                    path_arg = types
                    continue
                else:
                    files_arg = types
                    pass

                for file in files_arg:
                    quantity_of_bytes += stat(path.join(path_arg, file)).st_size

        return quantity_of_bytes
    
