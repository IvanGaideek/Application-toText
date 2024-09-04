def check_file_extension(filename, valid_extensions):
    """Check if a file has a valid extension"""
    valid_extensions = valid_extensions[1:].split(" *")
    return any(filename.lower().endswith(ext) for ext in valid_extensions)
