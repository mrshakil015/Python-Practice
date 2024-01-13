from PIL import Image

def compress_image(input_path, output_path, quality=20):
    try:
        # Open an image file
        with Image.open(input_path) as img:
            # Save the image with compression
            img.save(output_path, quality=quality)
            print(f"Image compressed successfully. Saved at: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
input_image_path = "Pic.jpg"
output_image_path = "output_compressed.jpg"
compress_image(input_image_path, output_image_path)
