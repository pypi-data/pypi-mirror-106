def clean(folder_path, exclude_list):
    dirs = os.listdir( folder_path )
    for item in dirs:
        if item in exclude_list:
            continue
        full_path = folder_path + "\\" +  item
        if os.path.isdir(full_path):
            shutil.rmtree(full_path)
        else:
            os.remove(full_path)
