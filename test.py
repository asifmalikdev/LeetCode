# import cv2
# import numpy as np

# # Load original image
# image = cv2.imread(r"C:\Users\dell\Downloads\Aiedit.png")

# # Target size
# target_width, target_height = 242, 136
# target_aspect = target_width / target_height

# # Get original size and aspect
# h, w = image.shape[:2]
# original_aspect = w / h

# # Determine new dimensions (preserve aspect ratio)
# if original_aspect > target_aspect:
#     new_w = target_width
#     new_h = int(target_width / original_aspect)
# else:
#     new_h = target_height
#     new_w = int(target_height * original_aspect)

# # Resize with INTER_AREA for high quality
# resized = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)

# # Create black background (or white: use np.ones)
# output = np.zeros((target_height, target_width, 3), dtype=np.uint8)

# # Center the resized image
# x_offset = (target_width - new_w) // 2
# y_offset = (target_height - new_h) // 2
# output[y_offset:y_offset + new_h, x_offset:x_offset + new_w] = resized

# # Save result
# cv2.imwrite(r"C:\Users\dell\Downloads\THUMB_1_opencv_resized.png", output)

# print("Done resizing without distortion.")
# from PIL import Image

# # Load the image
# image = Image.open(r"C:\Users\dell\Downloads\THUMB_1_opencv_resized")  # Replace with your actual image path

# # Get dimensions
# width, height = image.size

# print(f"Image width: {width}px")
# print(f"Image height: {height}px")

from PIL import Image

# === SETTINGS ===
input_image_path = r"C:\Users\dell\Downloads\photo-1620712943543-bcc4688e7485.avif"  # Change this to your actual image
output_image_path = r"C:\Users\dell\Documents\LeetCode\LeetCode\resized_image.jpg"
target_width = 465
target_height = 581

# === PROCESS ===
# Open the original image
image = Image.open(input_image_path)

# Resize to target size using the modern Pillow API
resized_image = image.resize((target_width, target_height), Image.Resampling.LANCZOS)

# Save the resized image
resized_image.save(output_image_path)

# Optional: Show the resized image
resized_image.show()

print(f"Image saved at: {output_image_path}")
