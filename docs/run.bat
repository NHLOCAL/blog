@echo off

echo [1/3] Cleaning previous build...
if exist "_site" (
    rmdir /s /q "_site"
)

echo.
echo [2/3] Building the site with Jekyll...
bundle exec jekyll build

echo.
echo [3/3] Indexing the built site with Pagefind...
rem Using the modern --site flag instead of the deprecated --source
pagefind --site "_site"

echo.
echo --- Build and Indexing Complete ---
echo Starting the local server. It will NOT rebuild the site on changes.
echo Your site is available at http://127.0.0.1:4000
echo To see new changes, you must stop the server (Ctrl+C) and run this script again.
echo.

rem Serve the STATIC _site directory without any rebuilding.
start http://127.0.0.1:4000
bundle exec jekyll serve --skip-initial-build