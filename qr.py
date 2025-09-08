# Import the required libraries
import qrcode
from PIL import Image

# Create a QRCode object with specific configuration
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 = smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction level
    box_size=10,  # Size of each box in pixels
    border=4  # Width of the border (minimum is 4 for QR code standard)
  )

# Add the data to be encoded in the QR code
qr.add_data("https://github.com/Devipriya-Dasari")

# Compile the data into a QR code array
qr.make(fit=True)

# Create an image from the QR code with custom colors
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("image.png")

