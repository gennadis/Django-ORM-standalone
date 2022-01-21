# Bank vault security system

This project is a site for a bank vault security system.

![Screenshot](Screenshot.png)

## Installation notes
1. Clone project
```bash
git clone https://github.com/gennadis/bank-vault-security.git
cd bank-vault-security
```

2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install requirements
```bash
pip install -r requirements.txt
```
4. Rename `.env.example` to `.env` and fill your secrets in it

5. Run
```bash
python manage.py runserver 0.0.0.0:8000
```

6. Open
Open site in browser [http://0.0.0.0:8000/](http://0.0.0.0:8000/)
