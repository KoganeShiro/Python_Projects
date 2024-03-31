# Fractals
A fractal is a complex geometric shape that can be split into parts, each of which is a reduced-scale copy of the whole. Fractals often exhibit self-similar patterns, meaning they repeat themselves at different scales. They are generated through iterative processes and are characterized by their intricate, irregular, and infinitely repeating structures.

### Canopy Fractal:
The Canopy fractal, also known as the Barnsley Fern, is a type of fractal that resembles the shape of a fern leaf. It was discovered by the mathematician Michael Barnsley. This fractal is created using an iterated function system (IFS), where a set of affine transformations is applied repeatedly to a starting point. Each transformation corresponds to a different part of the fern leaf, such as the stem or the leaflets. Through iteration, the fern leaf pattern emerges, exhibiting self-similar structures at different levels of magnification.
```
x' = a*x + b*y + e
y' = c*x + d*y + f
```
Where:

    (x, y) are the coordinates of the current point.
    (x', y') are the coordinates of the transformed point.
    a, b, c, d, e, and f are coefficients specific to each transformation.



### Koch Snowflake:
The Koch Snowflake is a fractal curve that starts with an equilateral triangle and iteratively replaces the middle third of each line segment with an outward equilateral triangle. This process is then repeated indefinitely for each new line segment created. As iterations progress, the Koch Snowflake develops intricate, self-similar patterns with infinitely many sides. Despite its infinite perimeter, the Koch Snowflake encloses a finite area, making it a fascinating example of a fractal with paradoxical properties.

STEPS:

    Start with an equilateral triangle.
    For each line segment of the triangle:
        Divide the segment into three equal parts.
        Replace the middle part with two segments to form an outward equilateral triangle.
    Repeat the above steps for each new line segment created in each iteration.

The Koch Snowflake can be represented recursively or iteratively. The recursive formulation is based on dividing each line segment into smaller segments and applying the same process recursively to each smaller segment.

The equation for the Koch Snowflake involves determining the coordinates of the points after each iteration, based on the length and angles of the initial equilateral triangle.

By iterating these steps, the Koch Snowflake develops intricate self-similar patterns with infinitely many sides.
