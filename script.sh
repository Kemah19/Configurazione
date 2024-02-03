#!/bin/bash

remote_user=""
remote_host=""
remote_path=""
local_path=""
file_to_copy=""


#scp "${remote_user}@${remote_host}:${remote_path}${file_to_copy}" "${local_path}"

scp "${local_path}${file_to_copy}" "${remote_user}@${remote_host}:${remote_path}"

expect "password: "
#altrimenti provare ad utilizzare scp -B abilita batch mode e non richiede la password spero
send "PASSWORD\r"

if [ $? -eq 0]; then
    echo "copia completata"
else
    echo "error"
fi