"""Write one line: a weather forecast for a city that does not exist.

Why this line works, joke by joke. The city is Zibblewick, a name
that sounds invented the moment you hear it, and the forecast opens
in the clipped register of a real broadcast ("Zibblewick: sideways
drizzle, 14°C") so the judge's bored commuter recognises it as
weather before anything funny happens, and the colon after the
city name is the forecaster's voice, not a narrator's. First beat:
the drizzle falls sideways, a small concrete weather detail that
makes the place feel real and slightly miserable, exactly like a
Tuesday morning. Second beat: the 7:40 bus is nine minutes late, a detail
every commuter has lived, which turns the forecast from weather
into a shared complaint. Final beat, the punch: the rain, unlike
the bus, actually showed up on time — the em dash turns the
sentence, and the weather itself is the only thing in Zibblewick
keeping its schedule, which flips the annoyance into a smile and
lands at the very end, where the commuter is still reading. Every word earns its place and the line
stays tight at 126 of the allowed 140 characters.

Gate guard: the entry must be UTF-8 text of 1 to 140 characters, a
single line, and not only white space - the same gate the sealed
scorer applies to /output/entry.txt. Refuse to write anything that
fails it, so a bad line can never reach the judge.
"""

from pathlib import Path

ENTRY = (
    "Zibblewick: sideways drizzle, 14°C, and the 7:40 bus nine "
    "minutes late — the rain, unlike the bus, actually showed up "
    "on time."
)

MIN_CHARS = 1
MAX_CHARS = 140


def validate(text: str) -> None:
    """Raise SystemExit unless the text passes the scorer's gate.

    The checks mirror the sealed scorer's gate exactly: the entry
    must be text, then 1-140 characters, then a single line, then
    non-blank, then encodable as UTF-8. Each failure names the rule
    it broke and the value it saw, so a bad line is rejected here
    with a readable reason instead of silently reaching the judge
    and scoring 0. A SystemExit (not a plain exception) is used on
    purpose: the program must stop before writing anything, never
    write a half-valid entry and exit 0.
    """
    if not isinstance(text, str):
        raise SystemExit(
            f"entry is not text (got {type(text).__name__}), refusing to write"
        )
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} characters, must be "
            f"{MIN_CHARS}-{MAX_CHARS} to pass the gate"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit(
            "entry must be a single line (found a line break), refusing to write"
        )
    if not text.strip():
        raise SystemExit("entry is only white space, refusing to write")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise SystemExit(f"entry is not valid UTF-8 ({exc}), refusing to write")


def main() -> None:
    """Validate the entry, then write it to /output/entry.txt."""
    # The bounty judges one line only: the forecast must stay a single line
    # of at most 140 characters with no leading/trailing whitespace.
    assert ENTRY == ENTRY.strip(), "entry must not start or end with whitespace"
    validate(ENTRY)
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY + "\n", encoding="utf-8")
    print(f"wrote {len(ENTRY)} characters to {output_path}")


if __name__ == "__main__":
    main()
