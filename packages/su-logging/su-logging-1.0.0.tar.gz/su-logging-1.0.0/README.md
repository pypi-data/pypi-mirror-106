# Logging for Stockholm University

Easy to use logging for Stockholm University.

## Usage

### Syslog

For normal usage which logs to syslog:
```python
from su.logging import logging

logger = logging.getLogger("myapp")
logger.warning("My WARNING message")
```

### Console
For easier developing you can also switch to console logging:
```python
from su.logging import console, logging

logger = logging.getLogger("myapp")
logger.warning("My WARNING message")
```

### Structured logging
We use
[logstash_formatter](https://github.com/ulule/python-logstash-formatter/)'s
`LogstashFormatterV1` and remove some unused/unnecesary fields.

Depend on `su-logging[structured]` in e.g. your `requirements.txt` and then:
```python
from su.logging import logging, structured

logger = logging.getLogger("myapp")
logger.warning("User logged in", extra={"user": "simlu"})

try:
    raise Exception("User performed illegal activity")
except Exception as e:
    logger.exception(e, extra={"user": "simlu"})
```

### Container usage
In Containers, which usually adhere to the 12 factor apps manifesto, you
usually log to STDOUT and let your container engine deal with them.
```python
from su.logging import console, logging, structured

logger = logging.getLogger("myapp")
logger.warning("My WARNING message")
```

## TODO
* [ ] [Some sort of versioning?](https://github.com/sdispater/poetry/issues/1036#issuecomment-489880822)
