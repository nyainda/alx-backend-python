# 0x02. Python - Async Comprehension


![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/12/ee85b9f67c384e29525b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220609%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220609T005321Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6595c702c51698dc7c3e5eae53ffb2d8aa1351cd6efd4e1cb3a0f8eb5701714f)

## Resources

**Read or watch**:

-   [PEP 530 – Asynchronous Comprehensions](https://intranet.hbtn.io/rltoken/aQqNRbmT_juGeeSdKdyjGQ "PEP 530 -- Asynchronous Comprehensions")
-   [What’s New in Python: Asynchronous Comprehensions / Generators](https://intranet.hbtn.io/rltoken/GeSDerenxLAcZuCZJoCN-Q "What’s New in Python: Asynchronous Comprehensions / Generators")
-   [Type-hints for generators](https://intranet.hbtn.io/rltoken/ShdGGW-q9VjtvF45H40VeA "Type-hints for generators")

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/D11mbVMDmbcxRtGz_HT31Q "explain to anyone"),  **without the help of Google**:

-   How to write an asynchronous generator
-   How to use async comprehensions
-   How to type-annotate generators

## Requirements

### General
-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted/compiled on Ubuntu 18.04 LTS using  `python3`  (version 3.7)
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/usr/bin/env python3`
-   A  `REDME.md`  file, at the root of the folder of the project, is mandatory
-   Your code should use the  `pycodestyle`  style (version 2.5.x)
-   The length of your files will be tested using  `wc`
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`
-   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
-   All your functions and coroutines must be type-annotated.

## Tasks

### 0. Async Generator
Write a coroutine called  `async_generator`  that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the  `random`  module.

```py
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())


