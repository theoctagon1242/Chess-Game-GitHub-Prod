import unittest
from unittest.mock import MagicMock, patch
import create_game
import chess   

# ...

class TestCreateGame(unittest.TestCase):
    
    # ...

    @patch('create_game.create_game_state')
    @patch('create_game.send_sms')
    @patch('create_game.render_board')
    def test_lambda_handler(self, render_board_mock, send_sms_mock, create_game_state_mock):
        test_game_id = "test-uuid"
        test_phone_number = "+1234567890"
        test_event = {'phone_number': test_phone_number}
        test_initial_board = "test_initial_board"
        create_game_state_mock.return_value = test_game_id
        render_board_mock.return_value = test_initial_board
        
        response = create_game.lambda_handler(test_event, None)
        
        create_game_state_mock.assert_called_once()
        render_board_mock.assert_called_once_with(chess.Board().fen())
        send_sms_mock.assert_called_once_with(test_phone_number, f"Your game ID is {test_game_id}\n{test_initial_board}")
        self.assertEqual(response['game_id'], test_game_id, "The response game ID should match the test game ID")
        self.assertEqual(response['initial_board'], test_initial_board, "The response initial board should match the test initial board")

if __name__ == '__main__':
    unittest.main()
