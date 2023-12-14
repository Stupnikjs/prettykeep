import unittest
from app import create_app


class TestMainRoute(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()

    
