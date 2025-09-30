@echo off
call bundle install || exit /b 1
call bundle exec jekyll build || exit /b 1 
call pip install -r requirements.txt --quiet || exit /b 1  
if not exist junit-reports mkdir junit-reports
call python -m pytest tests/ --junit-xml=junit-reports/results.xml || exit /b 1
