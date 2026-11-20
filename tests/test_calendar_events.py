import re
from html import unescape
from pathlib import Path

SITE = Path("_site")
ICS = SITE / "society/events/open-space.ics"
EVENT_PAGE = SITE / "society/events/open-space.html"


def read(path):
    assert path.exists(), f"{path} was not generated. Run 'bundle exec jekyll build' first."
    return path.read_text(encoding="utf-8")


def unfold(ics):
    # iCalendar folds long lines with CRLF + space
    return re.sub(r"\r?\n[ \t]", "", ics)


def test_open_space_ics_has_berlin_times_and_stable_uid():
    ics = unfold(read(ICS))

    assert ics.startswith("BEGIN:VCALENDAR")
    assert "TZID:Europe/Berlin" in ics
    assert "DTSTART;TZID=Europe/Berlin:20261209T160000" in ics
    assert "DTEND;TZID=Europe/Berlin:20261209T170000" in ics
    assert "UID:open_space@sammancoaching.org" in ics
    assert "TRIGGER:-PT30M" in ics


def test_open_space_event_page_has_calendar_buttons_and_details_link():
    html = read(EVENT_PAGE)

    for label in ["Google", "Apple", "Outlook", "Outlook.com", "Office 365", "Yahoo", "Other (.ics)"]:
        assert re.search(rf"</svg>{re.escape(label)}</a>", html), f"Missing '{label}' button on {EVENT_PAGE}"
    assert 'href="/society/events/open-space.ics"' in html
    assert 'href="/society/events/next_open_space.html"' in html


def test_google_link_converts_berlin_time_to_utc():
    html = read(EVENT_PAGE)

    google = re.search(r'href="(https://calendar\.google\.com/[^"]+)"', html)
    assert google, "No Google Calendar link on the event page"
    assert "dates=20261209T150000Z/20261209T160000Z" in unescape(google.group(1))
