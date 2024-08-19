#!/usr/bin/env bash
# build_files.sh

python3.9 -m venv venv

# activate the virtual environment
source venv/bin/activate

pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput