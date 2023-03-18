#this file is unti tests for create_game.py
import unittest
from unittest.mock import MagicMock
import create_game
import chess

class TestCreateGame(unittest.TestCase):
    
    def test_create_game_state(self):
        create_game.dynamodb = MagicMock()
        table_mock = create_game.dynamodb.Table.return_value
        
        game_id = create_game.create_game_state()
        
        self.assertIsNotNone(game_id, "The returned game ID should not be None")
        self.assertTrue(create_game.dynamodb.Table.called, "The Table method should be called")
        self.assertTrue(table_mock.put_item.called, "The put_item method should be called")
        
        put_item_args = table_mock.put_item.call_args[1]['Item']
        self.assertEqual(put_item_args['status'], 'in_progress', "The initial game status should be 'in_progress'")
        self.assertEqual(put_item_args['fen'], chess.Board().fen(), "The initial FEN should match the default chess board FEN")

if __name__ == '__main__':
    unittest.main()
