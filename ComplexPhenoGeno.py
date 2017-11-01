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
print("The folder should be named files/") 
print("Some toy datasets are already provided and will be used if you don't have the necessary folder.") 

from os import system
import os

if os.path.exists('./../files/') == False:
	yn = input("I cannot find a directory named files/. Proceed with dummy files? (yes/no)").lower()
	if yn != "yes":
		print("Bye!")
		exit()
	else:
		system("mv files/ ./../files/")
#Need to enter checks for the correct file formats and presence 
#make a class!
system("mkdir ./../Outputs/")
import rsIDs
print("#####################################################################################")
print("################################	MODELLING CLINICAL DATA ############################")
print("#####################################################################################")
import Models
print("#####################################################################################")
print("################################	PROCESSING THE GENOTYPES ###########################")
print("#####################################################################################")
#import Genotypes
	

#if __name__ == "__main__":
#	main()

