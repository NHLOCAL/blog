@echo off
pushd "%~dp0docs"

:: הפעלת השרת
start "" cmd /c "bundle exec jekyll serve"

:: המתנה קלה כדי לוודא שהשרת עלה
timeout /t 3 > nul

:: פתיחת דפדפן בכתובת Jekyll המקומית
start http://localhost:4000/admin

popd

exit