@echo off

if "%1" == "prod" (
    set JEKYLL_ENV=production
)
call bundle exec jekyll serve --livereload
    