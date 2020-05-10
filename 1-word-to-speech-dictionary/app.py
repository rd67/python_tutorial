import json
import difflib
import os

from gtts import gTTS

language = 'en'
increment = 1

def print_values(user_input, values):
  for index, value in enumerate(values):

    audio_file = "audios/{}_{}.mp3".format(user_input, index)
    if not os.path.exists(audio_file):
      print("Generating audio file please wait: "+ audio_file)
      audio_obj = gTTS(text=value, lang=language, slow=False)
      audio_obj.save(audio_file)

    os.system("mpg321 {}".format(audio_file))

    print("Def {}: {}".format(index+1, value))

while True:
  print("\nNote: Enter exit to exit the dictionary")
  user_input = input("Please enter word number {}: ".format(increment))
  user_input = user_input.lower();

  increment = increment + 1
  
  if user_input == "exit":
    print("Thank you for using our dictionary")
    break

  file = open("data.json")
  json_data = json.load(file)

  if user_input in json_data:
    print_values(user_input, json_data[user_input])
  else:
    close_matches = difflib.get_close_matches(user_input, json_data.keys(), 4, 0.8)
    close_matches_len = len(close_matches)

    if close_matches_len == 0:
      print("Incorrect Word, kindly check the entry")
      continue

    print("Input meaning not found. Did you by any chance mean? ")
    for index, value in enumerate(close_matches):
      print("\n{}. Press {} to get its meaning".format(value.capitalize(), index+1))
    # print("\nElse enter 0 to search the web.")

    user_input = eval(input("Input: "))
    if (isinstance(user_input, int) == False) or (user_input <= 0) or (user_input > close_matches_len):
      print("Invalid value entered. Exiting Dictionary")
      break
      
    print_values(user_input, json_data[close_matches[user_input-1]])
