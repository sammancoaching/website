import re
from html import unescape
from pathlib import Path

SITE = Path("_site")
ICS = SITE / "society/events/open-space.ics"
EVENT_PAGE = SITE / "society/events/next_open_space.html"


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


def test_open_space_event_page_has_calendar_buttons():
    html = read(EVENT_PAGE)

    for label in ["Google", "Apple", "Outlook", "Outlook.com", "Office 365", "Yahoo", "Other (.ics)"]:
        assert re.search(rf"</svg>{re.escape(label)}</a>", html), f"Missing '{label}' button on {EVENT_PAGE}"
    assert 'href="/society/events/open-space.ics"' in html


def test_google_link_converts_berlin_time_to_utc():
    html = read(EVENT_PAGE)

    google = re.search(r'href="(https://calendar\.google\.com/[^"]+)"', html)
    assert google, "No Google Calendar link on the event page"
    assert "dates=20261209T150000Z/20261209T160000Z" in unescape(google.group(1))


def test_ensemble_ics_repeats_weekly_from_the_series_start():
    ics = unfold(read(SITE / "society/events/ensemble.ics"))

    assert "DTSTART;TZID=Europe/Berlin:20261120T150000" in ics
    assert "RRULE:FREQ=WEEKLY;COUNT=23;INTERVAL=1;BYDAY=FR" in ics


def test_ensemble_google_link_carries_the_repeat_rule():
    html = read(SITE / "society/events/next_ensemble.html")

    google = re.search(r'href="(https://calendar\.google\.com/[^"]+)"', html)
    assert google, "No Google Calendar link on the ensemble page"
    assert "recur=RRULE%3AFREQ%3DWEEKLY" in unescape(google.group(1))


def test_past_ai_coding_dojo_has_no_date_or_calendar_buttons():
    html = read(SITE / "society/events/ai_coding_dojo.html")

    assert "Next event:" not in html
    assert 'id="add-to-calendar"' not in html
    assert "addcal" not in html


def test_past_ai_coding_dojo_ics_is_an_empty_calendar():
    ics = unfold(read(SITE / "society/events/ai-coding-dojo.ics"))

    assert ics.startswith("BEGIN:VCALENDAR")
    assert "BEGIN:VEVENT" not in ics


def test_past_training_courses_show_no_dates_or_calendar_buttons():
    for page in ["training/deliver_learning_hours.html", "training/learning_hours_masterclass.html"]:
        html = read(SITE / page)

        assert "There are no training dates scheduled at present." in html, page
        assert 'id="add-to-calendar"' not in html, page
        assert "addcal" not in html, page
