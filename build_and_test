#!/usr/bin/env bash
set -euo pipefail

bundle install
bundle exec jekyll build
pip install -r requirements.txt --quiet
python -m unittest discover tests
