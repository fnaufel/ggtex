
<!-- README.md is generated from README.Rmd. Please edit that file -->

[![Lifecycle:
experimental](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://lifecycle.r-lib.org/articles/stages.html#experimental)
<!-- badges: end -->

# ggtex

# Description

This is a tiny Python 3 script to translate from modified $\\LaTeX$ math
mode to Geogebra code for text objects.

# Instalation

Simply download the file `ggtex.py` and, if necessary, make it
executable.

You need to have the [docopt module](https://github.com/docopt/docopt),
which can be installed with

    pip install docopt==0.6.2

# Usage

    Converts modified LaTeX math-mode code to Geogebra code.
    See http://github.com/fnaufel/ggtex for syntax and more info.

    Usage:
      ggtex.py FILE
      ggtex.py -h | --help
      ggtex.py -v | --version

    Arguments:
      FILE                File containing code to convert to Geogebra

    Options:
      -h, --help          Show this screen.
      -v, --version       Show version.

## Syntax

The file you pass to `ggtex` contains $\\LaTeX$ math code with one extra
feature: you can *embed Geogebra commands that generate text* — values
and definitions of Geogebra objects, fractions, formulae etc. — using
the `@` delimiter.

For example, if you pass `ggtex` a file `math.tex` containing

``` latex
\[
  @a@ x^2 + @FractionText(2.5)@ x = 0
\]
```

where `a` is a number defined in your Geogebra session with value, say,
10, then `ggtex` will output a file `math.tex.ggtex` with contents

    FormulaText(Simplify(
    a + " x^2 + " + FractionText(2.5) + " x = 0"
    ))

This code, when entered in the Geogebra input bar, will produce a text
object containing:

$$
10x^2 + \\frac{5}{2}x = 0
$$
