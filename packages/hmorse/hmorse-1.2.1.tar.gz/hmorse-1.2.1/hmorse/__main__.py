from click import command, option

from . import encode as _encode, decode as _decode


@command()
@option("--encode", "-e", default=None)
@option("--decode", "-d", default=None)
@option("--csep", "-c", default=" ")
@option("--wsep", "-w", default="/")
def morse(encode: str, decode: str, csep: str, wsep: str):
    if (
        (encode and decode) or
        not (encode or decode)
    ):
        print("You must provide either --encode or --decode to translate text.")
        return

    if encode:
        print(_encode(encode, csep=csep, wsep=wsep))
    else:
        print(_decode(decode, csep=csep, wsep=wsep))

if __name__ == "__main__":
    morse()
