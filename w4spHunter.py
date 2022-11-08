import os, sys
import argparse
from pkgutil import iter_modules

#############################################################################################
#                                                                                           #
#   searchInInstalledModules                                                                #
#   List all the locally installed modules, and search for occurences of malicious ones     #
#   containing the W4SP stealer                                                             #
#   params:                                                                                 #
#       - maliciousModulesList : list of the modules inncluding the W4SP stealer            #
#                                                                                           #
#############################################################################################
def searchInInstalledModules(maliciousModulesList):
    print("Searching for malicious modules with W4SP Stealer locally installed... ")

    found = 0
    installedModules = []
    for module in iter_modules():
        installedModules.append(module.name)

    for maliciousModule in maliciousModulesList:
        if maliciousModule in installedModules:
            print("/!\ Malicious module containing W4SP stealer found (locally installed): " + maliciousModule)
            found = found + 1

    print(str(found) + " module(s) with W4SP Stealer found.")

#############################################################################################
#                                                                                           #
#   displayBanner                                                                           #
#   Displays the tool banner                                                                #
#                                                                                           #
#############################################################################################
def displayBanner():
    print("\n\
 _    _    ___  ___________   _   _             _            \n\
| |  | |  /   |/  ___| ___ \ | | | |           | |           \n\
| |  | | / /| |\ `--.| |_/ / | |_| |_   _ _ __ | |_ ___ _ __ \n\
| |/\| |/ /_| | `--. \  __/  |  _  | | | | '_ \| __/ _ \ '__|\n\
\  /\  /\___  |/\__/ / |     | | | | |_| | | | | ||  __/ |   \n\
 \/  \/     |_/\____/\_|     \_| |_/\__,_|_| |_|\__\___|_|   \n\
", file=sys.stderr)

#############################################################################################
#                                                                                           #
#   main                                                                                    #
#                                                                                           #
#############################################################################################
if __name__ == "__main__":
    displayBanner()

    # Agrs processing
    text = 'W4SP Hunter is a simple script which searches for usage of malicious python modules including the W4SP stealer malware. \
    See https://thehackernews.com/2022/11/researchers-uncover-29-malicious-pypi.html and https://github.com/loTus04/W4SP-Stealer'
    parser = argparse.ArgumentParser(description=text)
    parser.add_argument("-f", "--file", help="Specify the path of the file listing the malicious modules.\
        Default is current folder", default="malicious_modules.txt")
    args = parser.parse_args()

    # Open the list of known malicious modules, and search for them in installed ones.
    maliciousModulesFilePath = args.file
    with open(maliciousModulesFilePath) as maliciousModulesFile:
        lines = maliciousModulesFile.readlines()
        maliciousModulesList = [x for x in lines if not x.startswith("#")] # remove comments in the file
        searchInInstalledModules(maliciousModulesList)

