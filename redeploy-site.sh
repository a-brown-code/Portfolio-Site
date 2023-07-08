#!/bin/sh
tmux kill-server
git fetch && git reset origin/main --hard
tmux new
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt
if [[ $? -ne 0 ]]
then
REQS=$( grep -o "[[:alnum:]]*=" requirements.txt | sed 's/=//' )
for REQ in $REQS
do
pip install $REQ
done
fi
export FLASK_ENV=development
flask run --host=0.0.0.0
