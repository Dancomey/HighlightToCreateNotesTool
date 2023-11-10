###
### By: Dan Comey



#Prompts the user to select a file store the notes


import pyperclip
import keyboard
from tkinter import filedialog, Tk

def main():
	#Use Tkinter to choose a file to record the notes
	root = Tk()
	root.withdraw()
	file_path = filedialog.askopenfilename(title="Select a text file to paste into")

	if not file_path:
		print("No file selected. Exiting.")
		return
	
	print(f"Selected file: {file_path}")
	print("Waiting for |...")

	script_running = True
	while script_running is True:
		if keyboard.is_pressed("|"):
			print("top of the loop")
			# Get the copied text from the clipboard
			copied_text = pyperclip.paste()

			# Prepend the bullet point character to the copied text
			bullet_point_text = "• " + copied_text

			# Append the bullet point text to the selected file
			with open(file_path, 'a') as file:
				file.write(bullet_point_text + "\n")

			print("Bullet point text appended to file!")
			keyboard.wait("|", suppress=True)  # Wait for the key to be released

			print("bottom of the loop")

		if keyboard.is_pressed("~"):
			script_running = False
			print("Exiting")



if __name__ == "__main__":
	main()