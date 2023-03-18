import os
import chess
import boto3
from sns_service import send_sms

# Initialize a DynamoDB client
dynamodb = boto3.resource('dynamodb')

def get_game_state(game_id):
    """
    Retrieve the game state from the DynamoDB table.

    Args:
        game_id (str): The unique identifier for the game.

    Returns:
        dict: The game state.
    """
    table = dynamodb.Table('TextChessGames')
    response = table.get_item(Key={'game_id': game_id})
    return response['Item']

def update_game_state(game_id, new_fen, status):
    """
    Update the game state in the DynamoDB table.

    Args:
        game_id (str): The unique identifier for the game.
        new_fen (str): The updated FEN.
        status (str): The updated game status.
    """
    table = dynamodb.Table('TextChessGames')
    table.update_item(
        Key={'game_id': game_id},
        UpdateExpression='SET fen=:fen, status=:status',
        ExpressionAttributeValues={
            ':fen': new_fen,
            ':status': status
        }
    )

def render_board(fen):
    # Implement your preferred rendering method for the board (ASCII or emoji-based)
    pass

def lambda_handler(event, context):
    """
    AWS Lambda function handler for making a move.

    Args:
        event (dict): The Lambda function input event.
        context (LambdaContext): The Lambda function execution context.

    Returns:
        dict: The response containing the updated board state.
    """
    game_id = event['game_id']
    move = event['move']
    phone_number = event['phone_number']
    game_state = get_game_state(game_id)

    # Load the current game state and make the move
    board = chess.Board(game_state['fen'])
    try:
        board.push_san(move)
    except ValueError:
        # Invalid move
        send_sms(phone_number, "Invalid move. Please try again.")
        return {'error': 'Invalid move'}

    # Update the game state in DynamoDB
    new_fen = board.fen()
    status = 'in_progress' if not board.is_game_over() else 'finished'
    update_game_state(game_id, new_fen, status)

    # Render the updated board
    rendered_board = render_board(new_fen)

    # Send the updated board to the user via SMS
    send_sms(phone_number, f"Move: {move}\n{rendered_board}")

    return {
        'game_id': game_id,
        'new_fen': new_fen,
        'status': status
    }
