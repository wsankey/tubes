# Generate summaries for keywords
import argparse
import wikipedia

def main(term="Cleveland"):
    """
    Return a wikipedia summary of the term.
    """
    summary = None

    try:
        page = wikipedia.page(term)
        summary = page.summary
    except wikipedia.exceptions.DisambiguationError:
        pass

    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--term",
                        type=str,
                        default="Cleveland",
                        help="Search term to pass into wikipedia..")
    args = parser.parse_args()
    summary = main(term=args.term)
    print(summary)
