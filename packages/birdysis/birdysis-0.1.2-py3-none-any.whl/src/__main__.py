import sys
import argparse
from . import scrape, download

def main():
    
    tag = []
    filename = "all_ids.json"

    parser = argparse.ArgumentParser(
            description="Fetch all liked tweets and download basd on twitter user ID."
    )

    parser.add_argument(
            "-h",
            "--help",
            help="Prompt help menu."
            )
    parser.add_argument(
            "-f",
            "--fetch",
            help="Fetchs account information from file."
            )
    parser.add_argumnt(
            "-d",
            "--download",
            help="Downloads tweet IDs after fetching."
            )

    args = parser.parse_args()

    if args.help:
        print("birdysis: Fetches and downloads a user's liked tweets.")
        sys.exit()

    if args.fetch:
        scrape("-f")
    else:
        scrape("")

    if args.download:
        download(filename)

if __name__ == "__main__":
    main()


