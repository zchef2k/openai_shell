#!/bin/bash

response=$(exec ~/bin/openai_complete.py $@)

echo $response

read -p "--> Look reasonsable? (y/n) "
    case $REPLY in
        [yY]) echo "OK, executing" && eval $response;;
        *) exit;;
    esac