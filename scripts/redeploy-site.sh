#!/bin/sh
cd ..
git fetch && git reset origin/main --hard
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
if [[ $? -ne 0 ]]
then
REQS=$( grep -o "[a-zA-Z0-9\-]*=" requirements.txt | sed 's/=//' )
for REQ in $REQS
do
pip install $REQ
done
fi
systemctl restart myportfolio
