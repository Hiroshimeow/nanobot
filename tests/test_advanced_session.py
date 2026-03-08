import unittest
import os
import json
import shutil
from pathlib import Path
from nanobot.session.advanced_manager import AdvancedSessionManager

class TestAdvancedSessionManager(unittest.TestCase):
    def setUp(self):
        self.test_workspace = Path("/tmp/nanobot_test_workspace")
        if self.test_workspace.exists():
            shutil.rmtree(self.test_workspace)
        self.test_workspace.mkdir(parents=True)
        self.manager = AdvancedSessionManager(str(self.test_workspace))

    def tearDown(self):
        if self.test_workspace.exists():
            shutil.rmtree(self.test_workspace)

    def test_create_and_list_sessions(self):
        # Test default session
        sessions = self.manager.list_sessions()
        self.assertIn("default", sessions)

        # Test creating a new named session
        session_id = self.manager.create_session("research")
        self.assertEqual(session_id, "session_research")
        
        sessions = self.manager.list_sessions()
        self.assertIn("research", sessions)
        self.assertIn("default", sessions)

    def test_switch_session(self):
        self.manager.create_session("coding")
        session_id = self.manager.switch_session("coding")
        self.assertEqual(session_id, "session_coding")
        self.assertEqual(self.manager.current_session_name, "coding")

        # Test switching to non-existent session
        session_id = self.manager.switch_session("ghost")
        self.assertIsNone(session_id)

    def test_persistence(self):
        self.manager.create_session("persistent_session")
        
        # Create a new manager instance pointing to the same workspace
        new_manager = AdvancedSessionManager(str(self.test_workspace))
        sessions = new_manager.list_sessions()
        self.assertIn("persistent_session", sessions)

if __name__ == "__main__":
    unittest.main()
