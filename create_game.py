#create game and board
import os
import chess
import boto3
from uuid import uuid4
from sns_service import send_sms

# Initialize a DynamoDB client
dynamodb = boto3.resource('dynamodb')

def create_game_state():
    #
    Create a new game state and store it in the DynamoDB table.

    Returns:
    #

    # Create a new game state
    game_state = {
        'game_id': str(uuid4()),
        'board': chess.Board().fen(),
        'next_move': 'white',
        'game_over': False,
        'winner': None
    }

    # Get the table
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    game_id = str(uuid4())
    intial_fen = chess.Board().fen()
    
    table.put_item(
        Item={
            'game_id': game_id,
            'fen': intial_fen,
            'next_move': 'white',
            'game_over': False,
            'winner': None
        }
    )
    return game_id
def render_board(fen):
    # Implement your preferred rendering method here (ASCII)
    board = chess.Board(fen)
    return board.unicode()
    pass
"""AWS LAMNDAB FUNCTION HANDLER"""
    Args:
        event (dict): API Gateway Lambda Proxy Input Format
        context (object): Lambda Context runtime methods and attributes

    Returns:    
        # The response containing the game ID and the initial board state.
        dict: API Gateway Lambda Proxy Output Format


# Create a new game state
game_id = create_game_state()
board = chess.Board()

#Render the initial board
board_render = render_board(board.fen())

#Send the intial board to the user via SMS
phone_number = event['phone_number']
send_sms(phone_number, board_render, f"Your game Id is {game_id}\n{rendered_board}")

return {
    'game_id': game_id,
    'initial_board': rendered_board
}
