@echo off
npx repomix --ignore "_site/,.jekyll-cache/,repomix-output.*" "docs" --style markdown --remove-comments
pause