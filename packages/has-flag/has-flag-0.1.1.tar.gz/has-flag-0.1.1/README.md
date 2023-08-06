# has-flag

Check if argv has a specific flag.

This is a port of the Node.js package [`has-flag`](https://github.com/sindresorhus/has-flag) to Python.

## Install

```
python3 -m pip install -U has-flag
```

(That strange-looking setup command is because I've found it to be the most reliable. The `pip` command often aliases to python 2, and `pip3` often installs to the wrong Python package directory.)

## Usage

```py
from has_flag import has_flag

has_flag('unicorn');
#>>> True

has_flag('--unicorn');
#>>> True

has_flag('f');
#>>> True

has_flag('-f');
#>>> True

has_flag('foo=bar');
#>>> True

has_flag('foo');
#>>> False

has_flag('rainbow');
#>>> False
```

```
$ python3 foo.py -f --unicorn --foo=bar -- --rainbow
```


## License

MIT

## Contact

A library by [Shawn Presser](https://www.shawwn.com). If you found it useful, please consider [joining my patreon](https://www.patreon.com/shawwn)!

My Twitter DMs are always open; you should [send me one](https://twitter.com/theshawwn)! It's the best way to reach me, and I'm always happy to hear from you.

- Twitter: [@theshawwn](https://twitter.com/theshawwn)
- Patreon: [https://www.patreon.com/shawwn](https://www.patreon.com/shawwn)
- HN: [sillysaurusx](https://news.ycombinator.com/threads?id=sillysaurusx)
- Website: [shawwn.com](https://www.shawwn.com)

