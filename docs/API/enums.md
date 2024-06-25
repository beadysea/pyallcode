# Module allcode.enums

The allcode enums module provides enumerated types to support the use of various peripheral devices connected to the formula allcode buggy.

An enumeration is a set of symbolic names (members) bound to unique, constant values. Within an enumeration, the members can be compared by identity, and the enumeration itself can be iterated over.

This module defines seven enumeration classes derived from the Enum base class.

## class enums.Axis

>X = 0
>
>Y = 1
>
>Z = 2

## class Button(Enum)

>LEFT = 0
>
>RIGHT = 1

## class Colour(Enum)

>WHITE = 0
>
>BLACK = 1

## class LineSensor(Enum)

>LEFT = 0
>
>RIGHT = 1

## class BitDepth(Enum)

> constant    B_8 = 0
>
> constant   B_16 = 1

## class SampleRate(Enum)

>F_8K = 0
>
>F_16K = 1

## class Servo(Enum)

>ONE = 0
>
>TWO = 1
>
>THREE = 2
>
>FOUR = 3
