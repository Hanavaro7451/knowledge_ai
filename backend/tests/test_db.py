from unittest.mock import AsyncMock, Mock

from _pytest.monkeypatch import MonkeyPatch
from sqlalchemy.ext.asyncio import AsyncSession

import backend.core.db as db



async def test_db(monkeypatch):
    test_session = Mock()
    test_session_close = AsyncMock()
    test_factory = Mock(return_value=test_session)
    monkeypatch.setattr(db, "async_session_factory", test_factory)
    test_session.close = test_session_close
    generator = db.get_session()
    try:
        session = await anext(generator)
        assert test_session is session
        test_session_close.assert_not_awaited()
    finally:
        await generator.aclose()
        test_session.close.assert_awaited_once()
