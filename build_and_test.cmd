@echo off
call bundle exec jekyll build
call npx jest
