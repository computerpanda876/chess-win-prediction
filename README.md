# Goal
Predict the outcome of a chess game based on factors such as: time pressure, position complexity, king safety, etc.

# Parameters
1. Clock pressure: own_time / opp_time and min(own_time, opp_time) - ratio of own and opponent time and urgency (3 sec more urgent than 300 sec)
2. Material imbalance: own_material - opp_material
3. Legal moves: # of own legal moves
4. King safety: # of pieces that can attack a 3x3 area surrounding king in 0/1/2 moves
5. Center control: # of own pieces attacking the 4 central squares (e4, e5, d4, d5)
6. Space advantage: # of opponent squares that own pieces control
7. Threats: # of own pieces that are under attack - total # of attacks / threats to measure complexity
8. Piece safety: # of own undefended pieces - measures potential risk
9. Development: # of own pieces off back rank
10. Pawn structure: doubled / isolated / passed pawns
11. Piece activity: legal_moves / # of own pieces
