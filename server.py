import serial

PORT = "COM10"         
BAUD = 921600
SAVE_FILE = r"C:\Images\photo1.jpg"
ser = serial.Serial("COM10", 921600, timeout=10)

print("Waiting for image...")

header = ser.readline().decode().strip()

if header.startswith("IMGSTART:"):
    size = int(header.split(":")[1])

    print(f"Receiving {size} bytes")

    image_data = ser.read(size)

    footer = ser.readline()
    footer = ser.readline().decode().strip()

    if footer == "IMGEND":
        with open(SAVE_FILE, "wb") as f:
            f.write(image_data)

        print("Saved:", SAVE_FILE)
    else:
        print("Footer not received")
else:
    print("Invalid header")

ser.close()








