# Monotone Derivatives are Continuous

**[📥 Download the latest compiled PDF of this paper here](https://github.com/jhune-yim/Monotone_derivatives_are_continuous/releases/latest/download/continuity_1.pdf)**


This repository contains the LaTeX source and PDF for the expository note **“Monotone Derivatives are Continuous.”**

## Overview

The note proves the following classical fact from real analysis:

> If \( f : I \to \mathbb{R} \) is differentiable on an open interval \( I \), and if \( f' \) is monotone on \( I \), then \( f' \) is continuous on \( I \).

The main idea is simple and elegant:

- monotone functions can only be discontinuous by jumps;
- derivatives satisfy the Intermediate Value Property by Darboux's Theorem;
- therefore a monotone derivative cannot be discontinuous.

The note includes two proofs:
1. a proof using Darboux's Theorem;
2. a proof using one-sided limits and the Mean Value Theorem.

## Files

- `continuity_1.tex` — LaTeX source
- `continuity_1.pdf` — compiled PDF
- `README.md` — repository description
- `LICENSE` — license for this work
- `
## References

The note includes references to the following texts:

- Stephen Abbott, *Understanding Analysis*
- Andrew M. Bruckner, *Differentiation of Real Functions*
- Richard Courant and Fritz John, *Introduction to Calculus and Analysis, Vol. I*
- Serge Lang, *Undergraduate Analysis*
- Walter Rudin, *Principles of Mathematical Analysis*

## Compilation

Compile with  `lualatex`:

```bash
lualatex continuity_1.tex
lualatex continuity_1.tex
