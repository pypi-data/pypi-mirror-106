# json_autoarray

Write JSON-serializable python objects to file as JSON array.

Raises a SerializationError if you send it an object that cannot be serialized by whatever json module you are using..
        
Tries to use python-cjson (python2.x only) or UltraJSON  for serializing objects, because you wouldn't be needing a silly thing like this if you weren't handling big old objects.

Objects successfully sent to the writer are always contained in an array. JSONAutoArray will always attempt to close the array upon file closure, regardless of any exceptions which may lead to a premature end of your process.

## Why?

Suppose you are making with the ETL, and are pulling objects from a janky stream. Should your stream close prematurely, or send you some sort of madness, JSONAutoArray will throw out the bad object, and close the array before closing the file. 

## Installation
Install using pip:
```bash
pip install JSONAutoArray
```

## Usage
```python
import random
import logging
from tempfile import TemporaryDirectory
from json_autoarray import JSONAutoArray
from pathlib import Path

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
```
