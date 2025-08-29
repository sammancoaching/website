@echo off
call bundle install || exit /b 1
call bundle exec jekyll build || exit /b 1 
call pip install -r requirements.txt --quiet || exit /b 1  
if not exist junit-reports mkdir junit-reports
call python -m xmlrunner discover -s tests -o junit-reports || exit /b 1
