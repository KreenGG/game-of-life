import logging

from game import Game

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s", # noqa
)

if __name__ == "__main__":
    Game().run()
