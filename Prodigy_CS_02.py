from PIL import Image
import os

def encrypt_image(image_path, key):
    """
    Encrypts the image using a simple XOR operation with the key.
    
    Parameters:
    - image_path (str): Path to the input image file.
    - key (int): Encryption key.
    
    Returns:
    - encrypted_image (Image): Encrypted image object.
    """
    try:
        # Open the image
        img = Image.open(image_path)
    except IOError:
        print(f"Error: Cannot open image file {image_path}. Please check the file path and format.")
        return None
    
    # Get the image dimensions
    width, height = img.size
    
    # Create a new image object to store the encrypted image
    encrypted_img = Image.new(mode="RGB", size=(width, height))
    
    # Iterate through each pixel and apply XOR operation with the key
    for x in range(width):
        for y in range(height):
            # Get pixel value at position (x, y)
            pixel = img.getpixel((x, y))
            
            # Encrypt pixel value using XOR with the key
            encrypted_pixel = tuple([(p ^ key) for p in pixel])
            
            # Set the encrypted pixel value in the new image
            encrypted_img.putpixel((x, y), encrypted_pixel)
    
    return encrypted_img

def decrypt_image(encrypted_image, key):
    """
    Decrypts the encrypted image using the same XOR operation with the key.
    
    Parameters:
    - encrypted_image (Image): Encrypted image object.
    - key (int): Encryption key (same as used during encryption).
    
    Returns:
    - decrypted_image (Image): Decrypted image object.
    """
    # Get the image dimensions
    width, height = encrypted_image.size
    
    # Create a new image object to store the decrypted image
    decrypted_img = Image.new(mode="RGB", size=(width, height))
    
    # Iterate through each pixel and apply XOR operation with the key
    for x in range(width):
        for y in range(height):
            # Get encrypted pixel value at position (x, y)
            encrypted_pixel = encrypted_image.getpixel((x, y))
            
            # Decrypt pixel value using XOR with the key
            decrypted_pixel = tuple([(p ^ key) for p in encrypted_pixel])
            
            # Set the decrypted pixel value in the new image
            decrypted_img.putpixel((x, y), decrypted_pixel)
    
    return decrypted_img

# Main function
def main():
    # Example usage:
    image_path = "image.png"
    key = 123  # Encryption/Decryption key
    
    # Check if the file exists
    if not os.path.isfile(image_path):
        print(f"Error: The file {image_path} does not exist.")
        return
    
    # Encrypt the image
    encrypted_image = encrypt_image(image_path, key)
    if encrypted_image:
        encrypted_image.save("encrypted_image.png")
        print("Image encrypted successfully.")
        encrypted_image.show(title="Encrypted Image")

        
        # Decrypt the image (using the same key)
        decrypted_image = decrypt_image(encrypted_image, key)
        decrypted_image.save("decrypted_image.png")
        print("Image decrypted successfully.")
        decrypted_image.show(title="Decrypted Image")


if __name__ == "__main__":
    main()
