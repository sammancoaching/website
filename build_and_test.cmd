@echo off
call bundle exec jekyll build
call npx jest
call pip install -r requirements.txt
call python -m unittest discover tests
