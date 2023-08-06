import pytest
import pytz
from datetime import datetime

from tests.factories import session_window_dm

from shuttl_time import SessionWindow, MilitaryTime


class TestSessionWindow:
    def test_from_json_and_to_json(self):
        session_window = session_window_dm()
        session_window2 = SessionWindow.from_json(session_window.to_json())
        assert session_window.from_time == session_window2.from_time
        assert session_window.to_time == session_window2.to_time
        assert session_window.tz == session_window2.tz

    @pytest.mark.xfail(strict=True)
    def test_init_fails_on_from_time_greater_than_to_time(self):
        SessionWindow(from_time=1000, to_time=500)

    def test_get_session_time_window_from_dt(self):
        session_window = session_window_dm()
        time_window = session_window.get_session_time_window_from_dt(
            dt=datetime(2021, 1, 1, 10, 10)
        )
        assert (
            MilitaryTime.extract_from_datetime(time_window.from_date)
            == session_window.from_time
        )
        assert (
            MilitaryTime.extract_from_datetime(time_window.to_date)
            == session_window.to_time
        )
        assert session_window.contains_datetime(
            dt=time_window.from_date
        ) and session_window.contains_datetime(dt=time_window.to_date)

    def test_contains_datetime(self):
        tz_utc = pytz.utc
        tz_in = pytz.timezone("Asia/Kolkata")
        session_window = session_window_dm(1000, 1500, timezone=tz_utc)
        assert session_window.contains_datetime(
            dt=tz_utc.localize(datetime(2021, 1, 1, 12, 0))
        )
        assert not session_window.contains_datetime(
            dt=tz_utc.localize(datetime(2021, 1, 1, 17, 0))
        )
        assert session_window.contains_datetime(
            dt=tz_in.localize(datetime(2021, 1, 1, 17, 0))
        )
