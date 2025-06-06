# Developer Machine Setup Guide

Welcome to the project! Follow these steps to set up your development environment on a new machine. This guide assumes you are starting with a fresh Windows installation, but the instructions are similar for Mac and Linux (substitute shell commands as appropriate).

## 1. Prerequisites

### a. Install [Node.js & npm](https://nodejs.org/)
- Download and install the latest LTS version of Node.js, which includes npm.
- Verify installation:
  ```sh
  node --version
  npm --version
  ```

### b. Install [Git](https://git-scm.com/)
- Download and install Git for your OS.
- Verify installation:
  ```sh
  git --version
  ```

## 2. Clone the Repository

Open a terminal (Command Prompt, PowerShell, or Terminal) and run:
```sh
git clone https://github.com/YOUR_ORG/YOUR_REPO.git
cd YOUR_REPO
```
(Replace with the actual repository URL and directory.)

## 3. Install Project Dependencies

Install all Node.js dependencies:
```sh
npm install
```
This will install all required packages listed in `package.json`.

## 4. Running Tests

All automated tests are located in the `tests` directory.

To run all tests:
```cmd
build_and_test.cmd
```

## 5. Running the Project Locally

- If this is a Jekyll project, ensure you have Ruby and Jekyll installed (see below).
- For JavaScript development, use the appropriate build or serve command for your stack (e.g., `npm start`, `npm run dev`).

## 6. (If applicable) Install Ruby & Jekyll
If you need to run Jekyll locally (for static site generation):
- Install [Ruby](https://www.ruby-lang.org/en/downloads/)
- Install Jekyll:
  ```sh
  gem install jekyll bundler
  ```
- Run the site locally:
  ```sh
  bundle install
  bundle exec jekyll serve
  ```

## 7. Troubleshooting
- If you have issues with missing packages, try running `npm install` again.
- If you change dependencies, commit the updated `package.json` and `package-lock.json`.
- For Windows users, you may need to run terminals as Administrator for some installs.

## 8. Additional Tools
- [VS Code](https://code.visualstudio.com/) or your favorite editor
- [Google Chrome](https://www.google.com/chrome/) or another modern browser

## 9. Keeping Dependencies Updated
- Regularly run `npm outdated` and `npm update` to keep Node packages fresh.
- For Ruby/Jekyll, run `bundle update`.

---

If you have any issues, contact the project maintainer or check the README for more project-specific instructions.
