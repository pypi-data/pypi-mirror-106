import os,sys

args = sys.argv[1]


if args == "sniper":
    os.system("python Enchanted.py")
if args == "website":
    print("https://enchantedsniper.ga/")
if args == "help":
    print("You can do the following command arguments :")
    print("")
    print("'sniper' this command starts the main sniper")
    print("'website' this will print the website url")
    print("'help' this will show this help message")
else:
    print("error")