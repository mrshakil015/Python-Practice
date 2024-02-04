from PIL import Image
import os

def compress_image(input_path, output_folder, quality=20):
    try:
        # Open an image file
        with Image.open(input_path) as img:
            # Get the filename and extension from the input path
            file_name, file_extension = os.path.splitext(os.path.basename(input_path))

            # Compose the output path using the same filename and extension
            output_path = os.path.join(output_folder, f"{file_name}_compressed{file_extension}")

            # Save the image with compression
            img.save(output_path, quality=quality)
            print(f"Image compressed successfully. Saved at: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
input_image_path = "Pic.jpg"
output_folder = "output_folder"
compress_image(input_image_path, output_folder)
