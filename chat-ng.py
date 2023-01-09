import colorama
import openai
import os
import sys

from colorama import Fore, Back, Style

# Initialize Colorama with print() fixes
colorama.init(autoreset=True)

######################
# API KEY GOES HERE
######################

openai.api_key = ""

######################
# API KEY GOES ABOVE
######################

def print_banner():
	print("""
____ _  _ ____ ___    _  _ ____ 
|    |__| |__|  |  __ |\ | | __ 
|___ |  | |  |  |     | \| |__] 
			   v1.0
	""")

def ask_chatgpt(prompt):
	# Set the model
	model = "text-davinci-003"

	# Make the request to the ChatGPT API
	response = openai.Completion.create(engine=model, \
		prompt=prompt, max_tokens=1024, temperature=0.5, \
		top_p=1, frequency_penalty=0, presence_penalty=0)

	# Construct the response
	response_text = response['choices'][0]['text']
	output = f"\n"
	output += f"{Fore.GREEN}ChatGPT>{Fore.WHITE}{response_text}"
	output += f"\n"

	return output

def print_help():
	help_msg = "\nAvailable commands:\n\n"
	help_msg += "- banner   Display ASCII art\n"
	help_msg += "- clear    Clear terminal\n"
	help_msg += "- help     Display this menu\n"
	help_msg += "- quit     Exit the script\n\n"
	help_msg += "- exit     If you forget quit\n\n"
	print(f"{help_msg}")

def clear_screen():
	os.system("clear")

def main():
	commands = {
		"banner": print_banner,
		"clear": clear_screen,
		"help": print_help,
		"quit": sys.exit,
		"exit": sys.exit # for me :(
	}

	print("\n")
	while True:
		try:
			prompt = input(f"{Fore.GREEN}Input>{Fore.WHITE} ")
			command = None

			for key in commands:
				if key in prompt:
					command = commands[key]
					break

			if command:
				command()

			else:
				answer = ask_chatgpt(prompt)
				print(answer)

		except Exception as e:
			print(repr(e))

if __name__ == "__main__":
	print_banner()
	main()
