# -*- coding: utf-8 -*-
# :Project:   pglast -- PostgreSQL Languages AST
# :Created:   mer 02 ago 2017 15:11:02 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019, 2021 Lele Gaifax
#

from . import enums
from .error import Error
from .node import Missing, Node
try:
    from .parser import fingerprint, get_postgresql_version, parse_sql, scan, split
except ModuleNotFoundError:  # pragma: no cover
    # bootstrap
    pass


# This is injected automatically at release time
__version__ = 'v3.0.dev1'
"Package's version."

__author__ = 'Lele Gaifax <lele@metapensiero.it>'
"Package's author."


def parse_plpgsql(statement):
    from json import loads
    from .parser import parse_plpgsql_json

    return loads(parse_plpgsql_json(statement))


def _extract_comments(statement):
    from .printer import Comment

    lines = []
    lofs = 0
    for line in statement.splitlines(True):
        llen = len(line)
        lines.append((lofs, lofs+llen, line))
        lofs += llen
    comments = []
    continue_previous = False
    for token in scan(statement):
        if token.name in ('C_COMMENT', 'SQL_COMMENT'):
            for bol_ofs, eol_ofs, line in lines:
                if bol_ofs <= token.start < eol_ofs:
                    break
            else:  # pragma: no cover
                raise RuntimeError('Uhm, logic error!')
            at_start_of_line = not line[:token.start - bol_ofs].strip()
            text = statement[token.start:token.end+1]
            comments.append(Comment(token.start, text, at_start_of_line, continue_previous))
            continue_previous = True
        else:
            continue_previous = False
    return comments


def prettify(statement, safety_belt=True, preserve_comments=False, **options):
    r"""Render given `statement` into a prettified format.

    :param str statement: the SQL statement(s)
    :param bool safety_belt: whether to perform a safe check against bugs in pglast's
                             serialization
    :param bool preserve_comments: whether comments shall be preserved, defaults to not
    :param \*\*options: any keyword option accepted by :class:`~.printer.IndentedStream`
                        constructor
    :returns: a string with the equivalent prettified statement(s)

    When `safety_belt` is ``True``, the resulting statement is parsed again and its *AST*
    compared with the original statement: if they don't match, a warning is emitted and the
    original statement is returned. This is a transient protection against possible bugs in the
    serialization machinery that may disappear before 1.0.
    """

    # Intentional lazy imports, so the modules are loaded on demand

    import warnings
    from .printer import IndentedStream
    from . import printers  # noqa

    if preserve_comments:
        options['comments'] = _extract_comments(statement)

    orig_pt = parse_sql(statement)
    prettified = IndentedStream(**options)(Node(orig_pt))
    if safety_belt:
        try:
            pretty_pt = parse_sql(prettified)
        except Error as e:  # pragma: no cover
            print(prettified)
            warnings.warn("Detected a bug in pglast serialization, please report: %s\n%s"
                          % (e, prettified), RuntimeWarning)
            return statement

        if pretty_pt != orig_pt:  # pragma: no cover
            print(prettified)
            warnings.warn("Detected a non-cosmetic difference between original and"
                          " prettified statements, please report", RuntimeWarning)
            return statement

    return prettified


__all__ = ('Error', 'Missing', 'Node', 'enums', 'fingerprint', 'get_postgresql_version',
           'parse_plpgsql', 'parse_sql', 'prettify', 'split')
