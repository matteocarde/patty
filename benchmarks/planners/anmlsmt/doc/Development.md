Development
===========

Testing
-------

We use Google C++ Unit Testing Framework for the tests that are in the
test folder of the project.


Compilation Dependencies
------------------------

TAMER currently depends on the following packages and libraries that
need to be installed for correct compilation:

* Boost.Multiprecision 1.58+ (http://www.boost.org/libs/multiprecision/)
* Flex 2.5.35 (http://flex.sourceforge.net/)
* Bison 3.0.2 (https://www.gnu.org/software/bison/)
* Google C++ Test Framework 1.7.0+ (https://github.com/google/googletest) [Optional]


Code Style
----------

Tamer uses `clang-format` to automatically maintain a consistent code
formatting. All the commits are checked to be adherent to the coding
rules defined in `.clang-format` by the continuous integration.

All the developers are expected to run `format-all.sh` before every commit.

To simplify things and avoid unneeded test failures we recommend to
add the following to your `.git/hooks/pre-commit` file:

```bash
#!/bin/sh

python3 CI/run-clang-format.py -r src test -e 'src/code_generation/autogen/*' > /dev/null

if [ $? -eq 0 ]; then
    exit 0
else
    echo "There are some files to be formateed with clang-format before committing!"
    exit 1
fi
```

In this way, each commit is checked for code syntax before being sent
to the server.