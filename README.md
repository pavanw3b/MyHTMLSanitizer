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
- [Install git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) if not installed already.
- Clone the repo: `git clone https://gitlab.com/pavanw3b/MySanitizer.git`
- Navigate to the cloned folder: `cd MySanitizer`
- [Install pip](https://pip.pypa.io/en/stable/installing/) if not installed earlier.
- [Install virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
- Create a new python3 env: `virtualenv -p python3 venv`
- Activate the env: `source venv/bin/activate`
- Set up the dependencies: `pip install -r requirements.txt`
- Set up the database: `python manage.py migrate`
- Set up an admin account: `python manage.py createsuperuser`
- Start Server: `python manage.py runserver`

**Author & Presenter:**

Pavan: [@pavanw3b](https://twitter.com/pavanw3b)<br />
Core Member Null Hyd
