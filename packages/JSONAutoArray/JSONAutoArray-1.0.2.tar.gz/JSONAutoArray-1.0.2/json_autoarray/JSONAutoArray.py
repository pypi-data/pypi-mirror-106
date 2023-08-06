# -*- coding: utf-8 -*-
"""
Convenience module to "stream" ``json``-serializable python objects into an
array, automatically bound array on file open/close.

Supports python-cjson (python2.x) or UltraJSON for writing, because C go zoom.

Examples:
::
    import logging
    import random
    from pathlib import Path
    from tempfile import TemporaryDirectory
    from json_autoarray import JSONAutoArray

    if __name__ == "__main__":

        objects = [
            {"this": "that"},
            ["the", "other"],
            {"hippie": "joe"},
            {"facist": {"bullyboy": ["me", "you", "them"]}},
            list(set(["a", "a", "b"])),
            list(range(3)),
        ]

        # open with pathlib.Path
        with TemporaryDirectory() as tempdir:
            with JSONAutoArray.ArrayWriter(Path(tempdir, "foo.json")) as writer:
                for obj in objects:
                    writer.write(obj)

        # open with string
        with TemporaryDirectory() as tempdir:
            with JSONAutoArray.ArrayWriter(os.path.join(tempdir, "foo.json")) as writer:
                for obj in objects:
                    writer.write(obj)

        # will fail in python3 if file opened as binary!
        logging.warning("Expect TypeError for 'wb'")
        with TemporaryDirectory() as tempdir:
            f = open(Path(tempdir, "bar.json"), "wb")
            try:
                with JSONAutoArray.ArrayWriter(f) as writer:
                    for obj in objects:
                            writer.write(obj)
            except TypeError as error:
                logging.warning(error)

        # use encoding
        with TemporaryDirectory() as tempdir:
            f = open(Path(tempdir, "bar.json", encoding="utf-8"), "w")
            try:
                with JSONAutoArray.ArrayWriter(f) as writer:
                    for obj in objects:
                            writer.write(obj)
            except TypeError as error:
                logging.warning(error)


        logging.warning("Expect Serialization Error for lambda object.")
        with TemporaryDirectory() as tempdir:
            with JSONAutoArray.ArrayWriter(Path(tempdir, "foo.json")) as writer:
                try:
                    writer.write(lambda x: "foo")
                except JSONAutoArray.SerializationError as error:
                    logging.warning(error)

        # write ten thousand random flabberdabs
        with TemporaryDirectory() as tempdir:
            with JSONAutoArray.ArrayWriter(Path(tempdir, "flabberdabs.json")) as writer:
                try:
                    for i in range(10000):
                        writer.write([{"flabberdab": random.randint(1, 1000)}])
                except JSONAutoArray.SerializationError as error:
                    logging.warning(error)

        # close array on StopIteration error
        def rando_gen():
            for i in range(100):
                yield {
                    "".join(
                        [chr(random.randint(1, 100)) for i in range(5)]
                    ): random.randint(1, 100)
                }

        logging.warning("Expect uncaught StopIteration")
        with TemporaryDirectory() as tempdir:
            quux = Path(tempdir, "quux.json")
            with JSONAutoArray.ArrayWriter(quux) as writer:
                try:
                    rg = rando_gen()
                    while True:
                        if sys.version_info[0] < 3:
                            writer.write(rg.next())
                        else:
                            writer.write(next(rg))
                except JSONAutoArray.SerializationError as s_error:
                    logging.warning(s_error)
                except StopIteration as i_error:
                    logging.warning("%s - %s", i_error, "Hello StopIteration")
"""

import sys
from io import IOBase

# Try to use alternate json modules
try:
    import cjson as json

    json.dumps = json.encode
except ImportError:
    # cjson not yet supported by python3, try UltraJSON
    try:
        import ujson as json
    except ImportError:
        # No dice, fall back to python's standard json
        import json


class ArrayWriter(object):
    """
    Accept a file path or a file-like object.
    Writes the output as a json array.
    """

    def __init__(self, o):
        """
        Args:
            o (object): python class object
        """

        if isinstance(o, IOBase):
            self.obj = o

        else: self.obj = open(o, "w")


    def __enter__(self):
        """
        Bound input with open square bracket.
        """
        self.obj.write("[")
        return self

    def __exit__(self, _type, value, traceback):
        """
        Bound input with close square bracket, then close file.
        """
        self.obj.write("]")
        self.obj.close()

    def write(self, obj):
        """
        Writes the first row, then overloads self with delimited_write.

        Args:
            obj: A ``json``-serializable object.
        """
        try:
            self.obj.write(json.dumps(obj))
            setattr(self, "write", self.delimited_write)
        except:
            self.bad_obj(obj)

    def delimited_write(self, obj):
        """
        Prefix ``json`` object with a comma.

        Args:
            obj: A ``json``-serializable object.
        """
        try:
            self.obj.write("," + json.dumps(obj))
        except:
            self.bad_obj(obj)

    def bad_obj(self, obj):
        """
        Raise a ``SerializationError`` in the event of a garbage object
        (i.e. not ``json``-serializable.

        Args:
            obj: A ``json``-serializable object.
        """
        raise SerializationError("Object not json-serializable.")


class SerializationError(Exception):
    """
    Custom exception for ``SerializationError``. Yes, it's overkill.
    """

    def __init__(self, value):
        """
        Args:
            value: error value
        """
        self.value = value

    def __str__(self):
        """
        Return representation of value.
        """
        return repr(self.value)
