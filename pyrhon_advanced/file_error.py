# File: file_handling_demo.py

def write_to_file(filename):
    try:
        with open(filename, "w") as f:
            f.write("Hello, this is a file handling example.\n")
            f.write("Line 2: Writing to the file.\n")
            f.write("Line 3: File handling in Python.\n")
        print("✅ File written successfully.")
    except IOError as e:
        print("❌ Failed to write to file:", e)

def append_to_file(filename):
    try:
        with open(filename, "a") as f:
            f.write("Line 4: Appending new content.\n")
        print("✅ Content appended successfully.")
    except IOError as e:
        print("❌ Failed to append to file:", e)

def read_file(filename):
    try:
        with open(filename, "r") as f:
            print("📖 Reading file content:")
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("❌ File not found:", filename)
    except IOError as e:
        print("❌ Error reading file:", e)

def read_file_line_by_line(filename):
    try:
        with open(filename, "r") as f:
            print("🔍 Reading file line-by-line:")
            lines = f.readlines()
            for index, line in enumerate(lines):
                print(f"Line {index+1}: {line.strip()}")
    except Exception as e:
        print("❌ Error:", e)

def delete_file(filename):
    import os
    try:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"🗑️ File '{filename}' deleted.")
        else:
            print(f"⚠️ File '{filename}' does not exist.")
    except Exception as e:
        print("❌ Error deleting file:", e)

# 🧪 Testing all file operations
filename = "demo_file.txt"

write_to_file(filename)             # Write content
append_to_file(filename)           # Append more content
read_file(filename)                # Read full file
read_file_line_by_line(filename)   # Read line by line
delete_file(filename)              # Delete file at the end
