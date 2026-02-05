import io

import chess.pgn
import zstandard as zstd


def stream_games(file_path):
    dctx = zstd.ZstdDecompressor()

    with open(file_path, "rb") as fh:
        with dctx.stream_reader(fh) as reader:
            text_stream = io.TextIOWrapper(reader, encoding="utf-8")

            while True:
                game = chess.pgn.read_game(text_stream)
                if game is None:
                    break

                white_elo = int(game.headers.get("WhiteElo", 0))
                black_elo = int(game.headers.get("BlackElo", 0))

                if white_elo > 1800 and black_elo > 1800:
                    yield game


for game in stream_games("data/lichess_db_standard_rated_2025-01.pgn.zst"):
    result = game.headers.get("Result")
    print(
        f"Processing game: {game.headers.get('White')} vs {game.headers.get('Black')}"
    )
