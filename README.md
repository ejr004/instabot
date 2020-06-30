# instabot
Instagram bot

Implementation of Instapy: https://github.com/InstaPy

##Install:
- Python 3: https://www.python.org/downloads/
- Pip: https://github.com/pypa/pip
- Virtualenv:  ```pip3 install virtualenv``` 

```
git clone https://github.com/ejr004/instabot
cd ./instabot
python -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
```

Create your settings.ini:

```
[USERPASS]
username = username
password = password

[SETTINGS]
photo_comments = [':sunny: Be green! @{} :earth_americas:',
                  ':herb: Live green! @{} :earth_americas:',
                  ':leaves: Save the Planet! :earth_americas:',
                  ]
# User's followers
u_followers = ['greenguy',
              'greeninstitution',
              'minimalistinfluencer',
              ]
# Follow likers
f_likers = ['greenguy',
            'greeninstitution',
            'minimalistinfluencer',
            ]
# Follow tags
f_tags = ['#zerowaste',
          '#begreen',
          '#plasticfree',
          '#minimalist'
          ]
```

Run:
```
python mail.py -s settings.ini
```