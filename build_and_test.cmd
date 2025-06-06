@echo off
call bundle exec jekyll build || exit /b 1 
call pip install -r requirements.txt || exit /b 1  
call python -m unittest discover tests || exit /b 1
