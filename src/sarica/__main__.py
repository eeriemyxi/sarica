import argparse
import webbrowser
from random import Random

import phub

from sarica import constants

parser = argparse.ArgumentParser(
    description="Select a random video from a random Pornhub subscription."
)
parser.add_argument(
    "-S",
    "--seed",
    default=constants.SEED,
    help=f"Set randomizer seed. Defaults to {str(constants.SEED)!r}.",
)
cli_args = parser.parse_args()
constants.SEED = cli_args.seed

rand = Random(constants.SEED)


def get_random_channel(channels):
    return rand.choice(list(channels))


def get_random_video(videos):
    return rand.choice(list(videos))


def main() -> None:
    client = phub.Client(email=constants.EMAIL, password=constants.PASSWORD, login=True)
    print("Selecting a random channel...")
    selected_channel = get_random_channel(client.account.subscriptions)
    print("Selected channel:", selected_channel.name)
    print("Selecting a random video from", "them" + "...")
    selected_video = get_random_video(selected_channel.videos)
    print("Selected video:", selected_video.title)
    print("Opening the video link in your default browser...")
    webbrowser.open(selected_video.url)


if __name__ == "__main__":
    main()
