# USAGE
# python simple_example.py --name Adrian
# python simple_example.py --name Stephanie

# import the necessary packages
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True,
	help="name of the user")
args = vars(ap.parse_args())
print(args)

# display a friendly message to the user
print("Hi there {}, it's nice to meet you!".format(args["name"]))