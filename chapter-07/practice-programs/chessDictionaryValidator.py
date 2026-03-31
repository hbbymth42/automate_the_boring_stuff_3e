"""
Conditions to Check:
- Number of Dictionary Key-Value pairs does not exceed 32 (number of pieces betweeen both white and black)
- Dictionary Keys contain valid board spaces (e.g. '1h')
- Dictionary Values contain valid chess pieces (e.g. 'bking' for black king)
- Between each side (white and black), there should only be:
  - 1 King
  - 1 Queen
  - 2 Rooks
  - 2 Knights
  - 2 Bishops
  - 8 Pawns
"""

def isValidChessBoard(chessBoard):
    boardSpaceList = ['1a','1b','1c','1d','1e','1f','1g','1h',
                      '2a','2b','2c','2d','2e','2f','2g','2h',
                      '3a','3b','3c','3d','3e','3f','3g','3h',
                      '4a','4b','4c','4d','4e','4f','4g','4h',
                      '5a','5b','5c','5d','5e','5f','5g','5h',
                      '6a','6b','6c','6d','6e','6f','6g','6h',
                      '7a','7b','7c','7d','7e','7f','7g','7h',
                      '8a','8b','8c','8d','8e','8f','8g','8h'
                      ]
    chessPieceList = ['wking','bking',
                      'wqueen','bqueen',
                      'wrook','brook',
                      'wknight','bknight',
                      'wbishop','bbishop',
                      'wpawn','bpawn'
                      ]
    wKingNum = 0
    bKingNum = 0
    wQueenNum = 0
    bQueenNum = 0
    wRookNum = 0
    bRookNum = 0
    wKnightNum = 0
    bKnightNum = 0
    wBishopNum = 0
    bBishopNum = 0
    wPawnNum = 0
    bPawnNum = 0
    for boardSpace, chessPiece in chessBoard.items():
        # Valid Space & Piece Check
        if boardSpace not in boardSpaceList:
            return False
        if chessPiece not in chessPieceList:
            return False
        # Count Number of Pieces on Chess Board by Piece Type
        if chessPiece == chessPieceList[0]: # White King Check
            wKingNum += 1
        elif chessPiece == chessPieceList[1]: # Black King Check
            bKingNum += 1
        elif chessPiece == chessPieceList[2]: # White Queen Check
            wQueenNum += 1
        elif chessPiece == chessPieceList[3]: # Black Queen Check
            bQueenNum += 1
        elif chessPiece == chessPieceList[4]: # White Rook Check
            wRookNum += 1
        elif chessPiece == chessPieceList[5]: # Black Rook Check
            bRookNum += 1
        elif chessPiece == chessPieceList[6]: # White Knight Check
            wKnightNum += 1
        elif chessPiece == chessPieceList[7]: # Black Knight Check
            bKnightNum += 1
        elif chessPiece == chessPieceList[8]: # White Bishop Check
            wBishopNum += 1
        elif chessPiece == chessPieceList[9]: # Black Bishop Check
            bBishopNum += 1
        elif chessPiece == chessPieceList[10]: # White Pawn Check
            wPawnNum += 1
        elif chessPiece == chessPieceList[11]: # Black Pawn Check
            bPawnNum += 1

    if (wKingNum > 1) or (bKingNum > 1) or (wQueenNum > 1) or (bQueenNum > 1):
        return False
    elif (wRookNum > 2) or (bRookNum > 2) or (wKnightNum > 2) or (bKnightNum > 2) or (wBishopNum > 2) or (bBishopNum > 2):
        return False
    elif (wPawnNum > 8) or (bPawnNum > 8):
        return False
    else:
        return True

theBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

print(isValidChessBoard(theBoard))