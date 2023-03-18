#unit test for make_move.py
import unittest
from unittest.mock import MagicMock, patch
import make_move
import chess

class TestMakeMove(unittest.TestCase):

    # ... (previous test methods)

    @patch('make_move.get_game_state')
    @patch('make_move.update_game_state')
    @patch('make_move.send_sms')
    @patch('make_move.render_board')
    def test_lambda_handler(self, render_board_mock, send_sms_mock, update_game_state_mock, get_game_state_mock):
        test_game_id = "test-uuid"
        test_phone_number = "+1234567890"
        test
        test_move = "e2e4"
        test_event = {
            'game_id': test_game_id,
            'move': test_move,
            'phone_number': test_phone_number
        }
        test_initial_fen = chess.STARTING_FEN
        test_new_fen = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1"

        # Mock get_game_state to return a sample game state
        get_game_state_mock.return_value = {
            'game_id': test_game_id,
            'fen': test_initial_fen,
            'status': 'in_progress'
        }

        # Mock render_board to return a sample rendered board
        render_board_mock.return_value = "sample_rendered_board"

        response = make_move.lambda_handler(test_event, None)

        get_game_state_mock.assert_called_once_with(test_game_id)
        update_game_state_mock.assert_called_once_with(test_game_id, test_new_fen, 'in_progress')
        render_board_mock.assert_called_once_with(test_new_fen)
        send_sms_mock.assert_called_once_with(test_phone_number, f"Move: {test_move}\n{render_board_mock.return_value}")

        self.assertEqual(response['game_id'], test_game_id)
        self.assertEqual(response['new_fen'], test_new_fen)
        self.assertEqual(response['status'], 'in_progress')

if __name__ == '__main__':
    unittest.main()


