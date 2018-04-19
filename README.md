```
___  ___        _____             _ _   _
|  \/  |       /  ___|           (_) | (_)
| .  . |_   _  \ `--.  __ _ _ __  _| |_ _ _______ _ __
| |\/| | | | |  `--. \/ _` | '_ \| | __| |_  / _ \ '__|
| |  | | |_| | /\__/ / (_| | | | | | |_| |/ /  __/ |
\_|  |_/\__, | \____/ \__,_|_| |_|_|\__|_/___\___|_|
         __/ |
        |___/
```

My Sanitizer is an app to demonstrate how to build an (in)secure Sanitizer.

**Setup:**
- Clone the repo: `git clone https://gitlab.com/pavanw3b/MySanitizer.git`
- Install venv
- Create a new env: `virtualenv env`
- Activate the env: `source env/bin/activate`
- Navigate to the folder: `cd mysanitizer`
- Set up the dependencies: `pip install -r requirements.txt`
- Set up the database: `python manage.py migrate`
- Set up an admin account: `python manage.py createsuperuser`
- Start Server: `python manage.py runserver`

**Author & Presenter:**
Pavan: [@pavanw3b](https://twitter.com/pavanw3b)<br />
Core Member Null Hyd
