import pytest
from pathlib import Path
from nanobot.session.advanced_manager import AdvancedSessionManager

def test_advanced_session_manager(tmp_path: Path):
    manager = AdvancedSessionManager(tmp_path)
    
    # Test default session
    assert manager.get_active_session_name("telegram:123") == "default"
    
    # Test switching session
    manager.set_active_session("telegram:123", "coding")
    assert manager.get_active_session_name("telegram:123") == "coding"
    
    # Test full key generation
    assert manager._get_full_key("telegram:123") == "telegram:123::coding"
    
    # Test get_or_create with active session
    session = manager.get_or_create("telegram:123")
    assert session.key == "telegram:123::coding"
    
    # Test saving and listing
    manager.save(session)
    sessions = manager.get_user_sessions("telegram:123")
    assert len(sessions) == 1
    assert sessions[0]["name"] == "coding"
    
    # Test switching back to default
    manager.set_active_session("telegram:123", "default")
    assert manager.get_active_session_name("telegram:123") == "default"
    assert manager._get_full_key("telegram:123") == "telegram:123"
