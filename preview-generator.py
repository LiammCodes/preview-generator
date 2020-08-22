# Preview Generator
# Created by Liam Moore
# June 12th, 2020

import os
import glob
import subprocess

# find current working directory
cwd = os.getcwd()

# take initial input
print(".-------------------------------------------------.")
print("|------------- Preview Generator v1.0 ------------|")
print("| MAKE SURE THIS PROGRAM IS IN THE SAME FOLDER AS |")
print("|    THE VIDEOS YOU WISH TO MAKE Previews FOR     |")
print("'-------------------------------------------------'")

# main menu
print("[1] Manual tool")
print("[2] Automatic tool")
print("[3] exit")

user_input = input("> ")

while user_input != "3":

    if user_input == "1":
        video_file = input("Enter filename or type quit: ")

        while video_file != "quit":
            # locate file
            video_input_path = cwd + '/' + video_file

            # check if file exists
            if not os.path.exists(video_input_path):
                print("The file specified does not exist. Please try again.")
            else:
                print("File located.")
                # convert video file name into segment file name
                prev_name_list = video_file.split(".")
                prev_name = prev_name_list[0]

                # check if Previews path exists, make the directory if not
                if not os.path.exists(cwd + '/Previews'):
                    print("No previews folder found, creating one now...")
                    os.mkdir(cwd + "/Previews")
                    print("Previews folder created.")


                # take start and end timestamps and convert them to seconds
                time_start = input("Enter segment START timestamp (MM:SS): ")
                time_start_list = time_start.split(":")
                time_start_min = time_start_list[0]
                time_start_sec = time_start_list[1]
                time_start = (int(time_start_min) * 60) + int(time_start_sec)

                time_end = input("Enter segment END timestamp (MM:SS): ")
                time_end_list = time_end.split(":")
                time_end_min = time_end_list[0]
                time_end_sec = time_end_list[1]
                time_end = (int(time_end_min) * 60) + int(time_end_sec)

                # duration = input("Enter segment DURATION: ")
                duration = time_end - time_start

                # output segment
                video_output_path = cwd + '/Previews/' + prev_name + " Prev.mp4"
                print("Working...")
                subprocess.call(['ffmpeg', '-loglevel', 'quiet', '-ss', str(time_start), '-i', video_input_path, '-t', str(duration), '-c', 'copy', video_output_path])

                # completion message
                print("Preview created for " + video_file + " successfully.")
                            
            # take input to continue loop
            video_file = input("Enter filename or type quit: ")
        

    elif user_input == "2":

        # allow user to leave tool
        user_input2 = input("Press enter to begin or type 'quit': ")

        if user_input2 != 'quit':
            # take start and end timestamps and convert them to seconds
            time_start = input("Enter segment START timestamp (MM:SS): ")
            time_start_list = time_start.split(":")
            time_start_min = time_start_list[0]
            time_start_sec = time_start_list[1]
            time_start = (int(time_start_min) * 60) + int(time_start_sec)

            time_end = input("Enter segment END timestamp (MM:SS): ")
            time_end_list = time_end.split(":")
            time_end_min = time_end_list[0]
            time_end_sec = time_end_list[1]
            time_end = (int(time_end_min) * 60) + int(time_end_sec)

            # check if Previews path exists, make the directory if not
            if not os.path.exists(cwd + '/Previews'):
                print("No previews folder found, creating one now...")
                os.mkdir(cwd + "/Previews")
                print("Previews folder created.")

            # duration
            duration = time_end - time_start

            for video_file in glob.glob("*.mp4"):
                # locate file
                video_input_path = cwd + '/' + video_file
                
                # convert video file name into segment file name
                prev_name_list = video_file.split(".")
                prev_name = prev_name_list[0]

                # output segment
                video_output_path = cwd + '/Previews/' + prev_name + " Prev.mp4"
                print("Working...")
                subprocess.call(['ffmpeg', '-loglevel', 'quiet', '-ss', str(time_start), '-i', video_input_path, '-t', str(duration), '-c', 'copy', video_output_path])

                # completion message
                print("Preview created for " + video_file + " successfully.")

    
    # take initial input
    print(".-------------------------------------------------.")
    print("|------------- Preview Generator v1.0 ------------|")
    print("| MAKE SURE THIS PROGRAM IS IN THE SAME FOLDER AS |")
    print("|    THE VIDEOS YOU WISH TO MAKE Previews FOR     |")
    print("'-------------------------------------------------'")

    # main menu
    print("[1] Manual tool")
    print("[2] Automatic tool")
    print("[3] exit")

    user_input = input("> ")

print("exiting...")