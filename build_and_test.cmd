@echo off
call bundle install || exit /b 1
call bundle exec jekyll build || exit /b 1 
call pip install -r requirements.txt --quiet || exit /b 1  
call python -m unittest discover tests || exit /b 1
