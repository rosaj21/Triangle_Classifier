# Triangle classifier — Part 1

`triangle.py` provides `is_valid_triangle(a, b, c)` and
`classify_triangle(a, b, c)`. Side order does not matter.

Sides must be positive finite real numbers and satisfy the strict triangle
inequality. Zero or negative sides, degenerate triangles, and sides that cannot
form a triangle return `False` from the validity function and `"Invalid"` from
the classifier. Non-numeric inputs, booleans, NaN, and infinity are also invalid.

Valid triangles are classified as `"Equilateral"`, `"Isosceles"`, or `"Scalene"`.
A right triangle receives the prefix `"Right "`. Equal sides use exact equality;
the right-angle calculation uses `math.isclose` with relative tolerance `1e-9`.
Sides are divided by the longest side before squaring to avoid overflow.

An equilateral triangle with positive side length s would need s² + s² = s²
to be right, which implies s = 0. This contradicts the positive-side requirement.

## Try it

From this folder, run:

```shell
python -c "from triangle import classify_triangle; print(classify_triangle(3, 4, 5))"
```

Expected output: `Right Scalene`.

## Scope and AI use

Only Part 1 is included. OpenAI Codex supplied the implementation and README
and checked representative cases against the specification. No GitHub Copilot
review, unit-test submission, or acceptance-test work is claimed here.
