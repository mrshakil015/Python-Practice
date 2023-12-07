import os
import qrcode

# Sample data
data = [
    {"URN": "9385210768887", "FamilySize": "3/3", "Score": 15, "HofName": "MORSEDA"},
    {"URN": "9385210768890", "FamilySize": "4/4", "Score": 15, "HofName": "MINHAJ"},
    {"URN": "9385210768891", "FamilySize": "2/6", "Score": 12, "HofName": "MST SOPNA AKTER"},
    {"URN": "9385210768892", "FamilySize": "2/3", "Score": 4, "HofName": "MST KAMALA AKTER"},
]

# Define the folder path
folder_path = "Python Helpful Program/QR Code Generator/QR code images"

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Generate QR codes and save them in the folder
for item in data:
    urn = item["URN"]
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(str(item))
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    file_path = os.path.join(folder_path, f"{urn}_QR.png")
    img.save(file_path)
    # print(f"QR code for URN {urn} saved at {file_path}")
