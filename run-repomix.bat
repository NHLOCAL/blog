@echo off
npx repomix --ignore "_site/,.jekyll-cache/,repomix-output.*,_posts/" "docs" --style markdown --remove-comments
pause