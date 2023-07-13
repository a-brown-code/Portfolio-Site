#!/bin/sh
NAME=$( $RANDOM | md5sum | head -c 6; echo; )
EMAIL=$( $RANDOM | md5sum | head -c 15; echo; )
CONTENT=$( $RANDOM | md5sum | head -c 40; echo; )

curl --request POST http://127.0.0.1:5000/api/timeline_post -d 'name=$NAME&email=$EMAIL&content=$CONTENT'
curl http://127.0.0.1:5000/api/timeline_post | jq '.timeline_posts | {name, email, content} | join(" ")' | grep -q "$NAME\|$EMAIL\|$CONTENT"
if [[ $? -ne 0 ]]
then
echo "Get request did not contain posted information."
exit 1
else
echo "Everything went well!"
fi