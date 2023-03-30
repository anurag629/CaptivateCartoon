import os

def delete_image(img_path):
    """Deletes the image file from the directory
    
    Parameters:
        img_path (str): location of the image file
    
    Returns:
        None
    """
    try:
        os.remove(img_path)
        return f"Deleted {img_path} successfully!"
    except OSError as e:
        return f"Error deleting {img_path}: {e}"
