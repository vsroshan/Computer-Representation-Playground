import math
import struct
import wave
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    Image = None


def explore_text():
    print("\n— TEXT REPRESENTATION —")

    text = input("Enter some text: ")
    if not text:
        print("Please enter at least one character.")
        return
    print("\nYour text:", text)
    print("UTF-8 bytes:", list(text.encode("utf-8")))
    for character in text:
        code_point = ord(character)
        print(f"\nCharacter: {character!r}")
        print(f"Unicode code point: U+{code_point:04X}")
        print(f"Decimal: {code_point}")
        print(f"Hexadecimal: {hex(code_point)}")
        print(f"Binary: {code_point:b}")
        print(f"UTF-8 bytes: {list(character.encode('utf-8'))}")
        if code_point <= 127:
            print(f"ASCII value: {code_point}")
        else:
            print("ASCII value: Not an ASCII character")


def explore_image():
    print("\n— IMAGE REPRESENTATION —")

    if Image is None:
        print("The Pillow library is not installed.")
        print("Install it using: python3 -m pip install pillow")
        return
    image_path = input("Enter the path to an image: ").strip()
    try:
        with Image.open(image_path) as image:
            image = image.convert("RGB")
            width, height = image.size
            print(f"\nImage dimensions: {width} x {height}")
            print("Each RGB pixel contains three colour values.")
            try:
                x = int(input(f"Enter pixel x coordinate (0-{width - 1}): "))
                y = int(input(f"Enter pixel y coordinate (0-{height - 1}): "))
            except ValueError:
                print("Coordinates must be integers.")
                return
            if not (0 <= x < width and 0 <= y < height):
                print("Those coordinates are outside the image.")
                return
            red, green, blue = image.getpixel((x, y))
            print(f"\nPixel coordinates: ({x}, {y})")
            print(f"RGB: ({red}, {green}, {blue})")
            print(f"Hexadecimal: #{red:02X}{green:02X}{blue:02X}")
            print(f"Red in binary:   {red:08b}")
            print(f"Green in binary: {green:08b}")
            print(f"Blue in binary:  {blue:08b}")
            print("\nEach colour channel uses 8 bits.")
            print("An RGB pixel therefore uses 24 bits.")
    except FileNotFoundError:
        print("Image not found. Check the file path.")
    except Exception as error:
        print(f"Could not open the image: {error}")


def explore_sound():
    print("\n— SOUND REPRESENTATION —")

    try:
        sample_rate_input = input("Sample rate in Hz [8000]: ").strip()
        duration_input = input("Duration in seconds [1]: ").strip()
        bit_depth_input = input("Bit depth (8 or 16) [16]: ").strip()
        sample_rate = int(sample_rate_input or "8000")
        duration = float(duration_input or "1")
        bit_depth = int(bit_depth_input or "16")
        if sample_rate <= 0 or duration <= 0:
            print("Sample rate and duration must be positive.")
            return
        if bit_depth not in (8, 16):
            print("Choose a bit depth of 8 or 16.")
            return
        if duration > 60:
            print("For this demo, duration must be 60 seconds or less.")
            return
    except ValueError:
        print("Please enter valid numbers.")
        return

    number_of_samples = int(sample_rate * duration)
    frequency = 440
    output_file = Path("sample_tone.wav")
    try:
        with wave.open(str(output_file), "wb") as sound:
            sound.setnchannels(1)
            sound.setsampwidth(bit_depth // 8)
            sound.setframerate(sample_rate)
            frames = bytearray()
            for index in range(number_of_samples):
                time = index / sample_rate
                # Generate a simple 440 Hz sine wave.
                amplitude = math.sin(2 * math.pi * frequency * time)
                if bit_depth == 8:
                    # 8-bit PCM WAV uses unsigned samples.
                    sample = int(128 + 127 * amplitude)
                    frames.extend(struct.pack("<B", sample))
                else:
                    # 16-bit PCM WAV uses signed samples.
                    sample = int(32767 * amplitude)
                    frames.extend(struct.pack("<h", sample))
            sound.writeframes(frames)
        print("\nSound file created:", output_file.resolve())
        print(f"Sample rate: {sample_rate} samples per second")
        print(f"Duration: {duration} seconds")
        print(f"Bit depth: {bit_depth} bits per sample")
        print(f"Number of samples: {number_of_samples}")
        print(f"Audio data size: {len(frames)} bytes")
        print("The tone frequency is 440 Hz.")
    except OSError as error:
        print(f"Could not create the sound file: {error}")


def main():
    while True:
        print("\n" + "=" * 40)
        print("   COMPUTER REPRESENTATION PLAYGROUND")
        print("=" * 40)
        print("1. Explore Text Representation")
        print("2. Explore Image Representation")
        print("3. Explore Sound Representation")
        print("4. Exit")

        choice = input("\nChoose an option: ").strip()
        if choice == "1":
            explore_text()
        elif choice == "2":
            explore_image()
        elif choice == "3":
            explore_sound()
        elif choice == "4":
            print("Thanks for exploring computer representation!")
            break
        else:
            print("Invalid choice. Enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()