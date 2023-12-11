#chess rules engine lambda function
#Accepts a chess board state and checks against a list of legal moves
#Returns a list of legal moves
#first we define the lambda function


import json
import boto3
import chess
import chess.pgn
import chess.engine
import chess.svg
import chess.polyglot
import chess.syzygy
import chess.uci
import chess.gaviota



#this is the lambda function
def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

#this is the main chess rules engine function

def chess_rules_engine(board_state):
    # TODO implement


#this is the main chess rules engine function


def chess_rules_engine(board_state):

    # TODO implement
    
    return {
    
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }






        
