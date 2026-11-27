import re
from html import unescape
from pathlib import Path

SITE = Path("_site")


def read(path):
    assert path.exists(), f"{path} was not generated. Run 'bundle exec jekyll build' first."
    return path.read_text(encoding="utf-8")


def unfold(ics):
    # iCalendar folds long lines with CRLF + space
    return re.sub(r"\r?\n[ \t]", "", ics)


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
