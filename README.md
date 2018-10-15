# Cr3dOv3r (Massive) [![Python 2.7](https://img.shields.io/badge/Python-2.7-yellow.svg)](http://www.python.org/download/) 

**Your best friend in credential reuse attacks.**

You give Cr3dOv3r Massive a list of emails then it does two simple useful jobs with it:
- Search for public leaks for the emails and returns the result with the most useful details about the leak (Using haveibeenpwned API).
- Tries to get the plain text passwords from leaks it find (Using [@GhostProjectME](https://twitter.com/GhostProjectME)).

### Some of the scenarios Cr3dOv3r (Massive) can be used for:
- Check if the targeted emails are in any leaks.
- Get the password of these emails

# Screenshots
![screenshot](https://github.com/HeroS3c/Cr3dOv3r/blob/master/Data/Screen1.png)


# Usage
```
Put your list of emails in email.json file (in the correct form, e.g. ["example@example.com", "example1@example.com"] )
Otherwise you can run:
....................................
python getlistemail.py # (python 2)
....................................

and follow the steps.

next type:
....................................
python Cr3d0v3r.py
....................................
 
To run the script.
```
## Installing and requirements
### To make the tool work at its best you must have :
- Python 2.x 
- Linux or Windows system.
- Worked on some machines with MacOS and python2.
- The requirements mentioned in the next few lines.

### Installing
**+For windows : (After downloading ZIP and upzip it)**
```
cd Cr3dOv3r-master
python -m pip install -r win_requirements.txt
python Cr3d0v3r.py 
```
**+For Linux :**
```
git clone https://github.com/D4Vinci/Cr3dOv3r.git
cd Cr3dOv3r
python -m pip install -r requirements.txt
python Cr3d0v3r.py 
```

**+For docker :**
```bash
git clone https://github.com/D4Vinci/Cr3dOv3r.git
docker build -t cr3dov3r Cr3dOv3r/
docker run -it cr3dov3r 
```


**If you want to add a website to the tool, follow the instructions in the [wiki](https://github.com/D4Vinci/Cr3dOv3r/wiki)**

## Contact

D4Vinci- [Twitter](https://twitter.com/D4Vinci1)
 
HeroS3c- [Telegram](https://t.me/HeroS3c)
## Disclaimer
Cr3dOv3r is created to show how could credential reuse attacks get dangerous and it's not responsible for misuse or illegal purposes. Use it only for Pen-test or educational purpose !!!

Copying a code from this tool or using it in another tool is accepted as you mention where you get it from :smile:

> Pull requests are always welcomed :D
