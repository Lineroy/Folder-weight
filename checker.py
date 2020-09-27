def how_much_weight_of_directory(final_path):
    # Made so that the variables in the program do not conflict with each other.
    from os import walk as os_walk, stat as os_stat, path as os_path, environ as os_environ
    quantity_of_bytes = 0

    list_with_everything = []
    for path, no, files in os_walk(final_path):
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
                    quantity_of_bytes += os_stat(os_path.join(path_arg, file)).st_size

        return quantity_of_bytes
    
