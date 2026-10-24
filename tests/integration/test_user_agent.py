"""@file test_user_agent.py
@brief Integration tests of the User-Agent header of UrllibHttpGateway, local only.
"""

import pytest

from exercise_tracker import constants
from exercise_tracker.infrastructure.http.urllib_http_gateway import UrllibHttpGateway
from tests.integration.local_server import serve

USER_AGENT_KEY = constants.HEADER_USER_AGENT.lower()


@pytest.mark.parametrize(
    "path",
    ["/v2/natural/exercise", "/token/sheet/workouts"],
    ids=["nutritionix", "sheety"],
)
def test_post_sends_exercise_tracker_user_agent(path: str) -> None:
    with serve() as server:
        UrllibHttpGateway().post_json(server.url_for(path), {}, {})
    sent = server.requests[0].headers[USER_AGENT_KEY]
    assert sent == "exercise-tracker/0.1"
    assert "Python-urllib" not in sent


@pytest.mark.parametrize("name", ["User-Agent", "user-agent"])
def test_caller_user_agent_wins(name: str) -> None:
    with serve() as server:
        UrllibHttpGateway().post_json(server.url, {name: "custom/9"}, {})
    assert server.requests[0].headers[USER_AGENT_KEY] == "custom/9"
