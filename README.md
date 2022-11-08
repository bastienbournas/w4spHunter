# W4SP Hunter
W4SP Hunter is a simple script which searches for usage of malicious python packages which contains the W4SP stealer malware. 

## Context
On the 2022-11-05, cybersecurity researchers have uncovered 29 malicious packages in Python Package Index (PyPI), the official third-party software repository for the Python programming language. These packages are named closely to official ones, with a a small typo, and aim to infect developers machines with a malware called W4SP Stealer. See https://thehackernews.com/2022/11/researchers-uncover-29-malicious-pypi.html and https://github.com/loTus04/W4SP-Stealer.

## Usage
```console
odin@valhalla:~$ python3 w4spHunter.py
```

By default the scripts looks for the list of malicious packages in the malicious_packages.txt file located in the same folder.
The file path can be specified with -f or --file

```console
odin@valhalla:~$ python3 w4spHunter.py -f /home/odin/malicious_packages.txt
```

## References
* https://thehackernews.com/2022/11/researchers-uncover-29-malicious-pypi.html
* https://github.com/loTus04/W4SP-Stealer