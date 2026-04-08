#!/bin/bash
git pull --no-rebase

jpg_file=$(ls . | grep 'jpg')
if [ -z "$jpg_file" ]; then
    png_file=$(ls . | grep 'png')
    if [ -z "$png_file" ]; then
        echo "No jpg or png file found in the current directory."
        exit 1
    fi
    mv $png_file ./docs/community/images/wechat-group.jpg
else
    mv $jpg_file ./docs/community/images/wechat-group.jpg
fi

mkdocs gh-deploy --remote-name origin --remote-branch gh-pages
git add .
git commit -m "update"
git push