print("""
  ____                      _           
 / ___|___  _ __ ___  _ __ | | _____  __
| |   / _ \| '_ ` _ \| '_ \| |/ _ \ \/ /
| |__| (_) | | | | | | |_) | |  __/>  < 
 \____\___/|_| |_| |_| .__/|_|\___/_/\_\\
                     |_|  
                     
                     
 ____  _                        ______                  
|  _ \| |__   ___ _ __   ___   / / ___| ___ _ __   ___  
| |_) | '_ \ / _ \ '_ \ / _ \ / / |  _ / _ \ '_ \ / _ \ 
|  __/| | | |  __/ | | | (_) / /| |_| |  __/ | | | (_) |
|_|   |_| |_|\___|_| |_|\___/_/  \____|\___|_| |_|\___/ 
                    """)

print("\n\nComplex Pheno/Geno is written for Python 3.6 and is under development.")
print("Please make sure plink 1.9 (https://www.cog-genomics.org/plink2) is installed in your computer before continuing.\nFor comments and suggestions e-mail rodoniki@gmail.com\n\n")
print("Please make sure all the input files are in a subdirectory in the same folder as Complex Pheno/Geno.")
print("The folder should be named Inputs/") 
yn = input("Do you want to proceed? (yes/no):")
if yn != 'yes':
	print("Bye!")
	exit()
else:
	from os import system
	import os

	if os.path.exists('./../Inputs/'):
		#Need to enter checks for the correct file formats and presence
		system("mkdir ./../Outputs/")
		import rsIDs
		import Genotypes
		
	else:
		print("I cannot find a directory named Inputs/")
		print("Bye!")
		exit()

#if __name__ == "__main__":
