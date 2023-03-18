#get_game_state.py Lambda function. This function will allow users to retrieve the current game state using the game ID. Here's a template for the get_game_state.py :

import os
import boto3

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

def lambda_handler(event, context):
    """
    AWS Lambda function handler for getting the game state.

    Args:
        event (dict): The Lambda function input event.
        context (LambdaContext): The Lambda function execution context.

    Returns:
        dict: The response containing the game state.
    """
    game_id = event['game_id']
    game_state = get_game_state(game_id)
    return game_state
