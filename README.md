
<!-- README.md is generated from README.Rmd. Please edit that file -->

[![Lifecycle:
experimental](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://lifecycle.r-lib.org/articles/stages.html#experimental)
<!-- badges: end -->

# ggtex

# Description

This is a tiny Python 3 script to translate from modified
![\\LaTeX](https://latex.codecogs.com/png.latex?%5CLaTeX "\LaTeX") math
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

The file you pass to `ggtex` contains
![\\LaTeX](https://latex.codecogs.com/png.latex?%5CLaTeX "\LaTeX") math
code with one extra feature: you can *embed Geogebra commands that
generate text* — values and definitions of Geogebra objects, fractions,
formulae etc. — using the `@` delimiter.

For example, if you pass `ggtex` a file `example.tex` containing

``` latex
\[
  @a@ x^2 + @FractionText(2.5)@ x = 0
\]
```

where `a` is a number defined in your Geogebra session with value, say,
![10](https://latex.codecogs.com/png.latex?10 "10"), then `ggtex` will
output a file `example.tex.ggtex` with contents

    FormulaText(Simplify(
    a + " x^2 + " + FractionText(2.5) + " x = 0"
    ))

This code, when entered in the Geogebra input bar, will produce a text
object containing:

![
10x^2 + \\frac{5}{2}x = 0
](https://latex.codecogs.com/png.latex?%0A10x%5E2%20%2B%20%5Cfrac%7B5%7D%7B2%7Dx%20%3D%200%0A "
10x^2 + \frac{5}{2}x = 0
")

## Useful Geogebra functions