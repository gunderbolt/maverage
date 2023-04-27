# maverage - Moving Average

`maverage` provides a Simple Moving Average implementation that delays the
average calculation until requested - useful for programs that collect data in
real-time and delay processing until later.

## Basic Usage - `Simple`

## Future Ideas

- Add an optional type to `Simple`? Values would be checked/coerced when being
  added. Currently, any type that implements operators `+`, `-`, `*`, and `/`
  should work (assuming it works with the initial cumulative value of 0).
- Optionally initialize all values in `Simple` with an initial value.

  To implement: Add `ivalue=None` to `Simple.__init__`. If not `None`, set all
  `size` elements in the `deque` to the initial value.

  Would this be useful?
