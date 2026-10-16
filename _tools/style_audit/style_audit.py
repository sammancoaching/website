"""Audit the styles the running site actually renders.

Start the site first (./build_and_run), then:

    python _tools/style_audit/style_audit.py               # light mode, default pages
    python _tools/style_audit/style_audit.py --dark        # emulate prefers-color-scheme: dark
    python _tools/style_audit/style_audit.py --json out.json /some/page.html /other/

The report lists every distinct colour, font, border, radius and shadow with
how often it appears, plus text that fails WCAG AA contrast. Values seen on
only one or two pages name those pages, since they are usually the outliers.
"""
import argparse
import json
import os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# One or two of each page type.
DEFAULT_PAGES = [
    '/',
    '/404.html',
    '/kata_descriptions/',
    '/kata_descriptions/bank_account.html',
    '/learning_hours/',
    '/learning_hours/architecture.html',
    '/activities/',
    '/activities/4C_model.html',
    '/code_smells/bumpy_road.html',
    '/refactorings/command_to_function.html',
    '/reference/',
    '/training/',
    '/training/learning_hours_masterclass.html',
    '/society/',
    '/society/agentic_ai.html',
    '/society/offers/',
    '/society/offers/teams.html',
    '/society/contributors/emilybache.html',
    '/society/contributors/balp.html',
    '/society/events/ai-coding-dojo.html',
    '/newsletter.html',
    '/contact.html',
]

SCRIPT = Path(__file__).with_name('style_audit.js').read_text(encoding='utf-8')


def run_audit(base_url, pages, dark):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    if os.environ.get('CHROME_BIN'):
        options.binary_location = os.environ['CHROME_BIN']
    driver = webdriver.Chrome(options=options)
    try:
        driver.set_window_size(1280, 900)
        driver.set_script_timeout(30 + 5 * len(pages))
        if dark:
            driver.execute_cdp_cmd('Emulation.setEmulatedMedia', {
                'features': [{'name': 'prefers-color-scheme', 'value': 'dark'}]})
        driver.get(base_url)
        return driver.execute_async_script(
            SCRIPT + '\nstyleAudit(arguments[0]).then(arguments[arguments.length - 1]);', pages)
    finally:
        driver.quit()


def format_report(result, dark):
    lines = [f"Style audit ({'dark' if dark else 'light'} mode)", '']
    for page, info in result['perPage'].items():
        notes = []
        if not info['title']:
            notes.append('NO TITLE')
        if info['inlineStyles']:
            notes.append(f"{info['inlineStyles']} inline style(s)")
        if info['styleTags']:
            notes.append(f"{info['styleTags']} <style> tag(s) in body")
        lines.append(f"  {page}  {info['title']!r}  {'  '.join(notes)}")

    def entry(item):
        where = f"{len(item['pages'])} pages"
        if len(item['pages']) <= 2:
            where += '  [' + ' '.join(item['pages']) + ']'
        return f"  {item['count']:5}  {where:<14}  {item['value']}"

    for category, items in result['categories'].items():
        lines += ['', f'## {category} ({len(items)} distinct)']
        lines += [entry(item) for item in items]

    lines += ['', f"## low contrast text ({len(result['lowContrast'])} distinct pairs)"]
    for item in result['lowContrast']:
        lines.append(entry(item))
        lines.append(f"{'':24}e.g. {', '.join(item['examples'])}")
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('pages', nargs='*', default=DEFAULT_PAGES, help='site-relative paths to audit')
    parser.add_argument('--base-url', default='http://localhost:4000')
    parser.add_argument('--dark', action='store_true', help='emulate prefers-color-scheme: dark')
    parser.add_argument('--json', type=Path, help='also write the raw results to this file')
    args = parser.parse_args()

    result = run_audit(args.base_url, args.pages, args.dark)
    if args.json:
        args.json.write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(format_report(result, args.dark))


if __name__ == '__main__':
    main()
