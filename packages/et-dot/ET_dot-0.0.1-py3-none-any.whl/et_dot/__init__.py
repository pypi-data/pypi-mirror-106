# -*- coding: utf-8 -*-
"""
Package et_dot
==============
Python module for computing the dot product of two arrays.
"""
import et_dot.cli_dotfiles
__version__ = "0.0.1"



try:
    import et_dot.dotc
except ModuleNotFoundError as e:
    # Try to build this binary extension:
    from pathlib import Path
    import click
    from et_micc2.project import auto_build_binary_extension
    msg = auto_build_binary_extension(Path(__file__).parent, 'dotc')
    if not msg:
        import et_dot.dotc
    else:
        click.secho(msg, fg='bright_red')

try:
    import et_dot.dotf
except ModuleNotFoundError as e:
    # Try to build this binary extension:
    from pathlib import Path
    import click
    from et_micc2.project import auto_build_binary_extension
    msg = auto_build_binary_extension(Path(__file__).parent, 'dotf')
    if not msg:
        import et_dot.dotf
    else:
        click.secho(msg, fg='bright_red')

def dot(a,b):
    """Compute the dot product of *a* and *b*.

    :param a: a 1D array.
    :param b: a 1D array of the same length as *a*.
    :returns: the dot product of *a* and *b*.
    :raises: ValueError if ``len(a)!=len(b)``.
    """
    n = len(a)
    if len(b)!=n:
        raise ValueError("dot(a,b) requires len(a)==len(b).")
    result = 0
    for i in range(n):
        result += a[i]*b[i]
    return result
