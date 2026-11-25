#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes a single original dad joke to $MAKEFUN_OUTPUT_DIR/entry.txt.

The joke was written for this bounty: a father-of-three judge reads entries
two at a time and picks the one that earns the bigger groan. The joke aims
at the published criteria, in order:

1. A dad joke a father would tell at the breakfast table.
2. The pun lands cleanly on the first read, no explaining needed.
3. Fresh inside the dad-joke tradition (dog + newspaper + router).
4. Tight, every word earning its place, punchline at the end.
5. Reads naturally aloud, with a rhythm a father could deliver.

Deterministic, standard library only: two runs produce byte-identical output.
"""

import os
import sys

JOKE = (
    "Every morning I try to teach my dog to fetch the newspaper, "
    "but he keeps bringing me the Wi-Fi router. "
    "I guess he prefers his news wireless."
)

MAX_CHARS = 200


def main() -> int:
    joke = JOKE.strip()
    if not joke:
        print("error: joke is empty", file=sys.stderr)
        return 1
    if len(joke) > MAX_CHARS:
        print(
            "error: joke is %d characters, over the %d limit"
            % (len(joke), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    # The gate also rejects a file that is only white space, so the joke
    # itself must carry non-space characters, not just the file.

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(joke + "\n")

    print("wrote %s (%d characters)" % (path, len(joke)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
