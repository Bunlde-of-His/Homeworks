from typing import List, Tuple

class ChessPiece:
    WHITE = "white"
    BLACK = "black"

    def __init__(self, color: str, position: Tuple[int, int]):
        self.color = color
        self.position = position

    def change_color(self):
        self.color = ChessPiece.BLACK if self.color == ChessPiece.WHITE else ChessPiece.WHITE

    def change_position(self, new_position: Tuple[int, int]):
        if 0 <= new_position[0] <= 7 and 0 <= new_position[1] <= 7:
            self.position = new_position

    def can_move_to(self, new_position: Tuple[int, int]):
        pass

class Pawn(ChessPiece):
    def can_move_to(self, new_position: Tuple[int, int]):
        x_diff = abs(new_position[0] - self.position[0])
        y_diff = abs(new_position[1] - self.position[1])
        if self.color == "white":
            return x_diff == 1 and y_diff == 0
        else:
            return x_diff == 1 and y_diff == 0

class Knight(ChessPiece):
    def can_move_to(self, new_position: Tuple[int, int]):
        x_diff = abs(new_position[0] - self.position[0])
        y_diff = abs(new_position[1] - self.position[1])
        return (x_diff == 2 and y_diff == 1) or (x_diff == 1 and y_diff == 2)

class Bishop(ChessPiece):
    def can_move_to(self, new_position: Tuple[int, int]):
        x_diff = abs(new_position[0] - self.position[0])
        y_diff = abs(new_position[1] - self.position[1])
        return x_diff == y_diff

class Rook(ChessPiece):
    def can_move_to(self, new_position: Tuple[int, int]):
        return new_position[0] == self.position[0] or new_position[1] == self.position[1]

class Queen(ChessPiece):
    def can_move_to(self, new_position: Tuple[int, int]):
        x_diff = abs(new_position[0] - self.position[0])
        y_diff = abs(new_position[1] - self.position[1])
        return (x_diff == y_diff) or (new_position[0] == self.position[0] or new_position[1] == self.position[1])

class King(ChessPiece):
    def can_move_to(self, new_position: Tuple[int, int]):
        x_diff = abs(new_position[0] - self.position[0])
        y_diff = abs(new_position[1] - self.position[1])
        return x_diff <= 1 and y_diff <= 1

def get_possible_moves(pieces: List[ChessPiece], new_position: Tuple[int, int]) -> List[ChessPiece]:
    return [piece for piece in pieces if piece.can_move_to(new_position)]

def main():
    white_pawn = Pawn("white", (1, 2))
    black_king = King("black", (7, 8))
    white_bishop = Bishop("white", (2, 2))
    black_rook = Rook("black", (4, 3))
    black_queen = Queen("black", (6, 3))
    white_knight = Knight("white", (7, 1))
    
    pieces = [white_pawn, black_king, white_bishop, black_rook, black_queen, white_knight]
    
    new_position = (3, 3)
    possible_moves = get_possible_moves(pieces, new_position)
    
    for piece in possible_moves:
        print(piece.color, piece.__class__.__name__, "can move to", new_position)

if __name__ == "__main__":
    main()
