# maverage - Moving Average

`maverage` provides a Simple Moving Average implementation that delays the
average calculation until requested - useful for programs that collect data in
real-time and delay processing until later.


## Basic Usage - `Simple`

```python
>>> s = Simple(5)  # Simple object with internal buffer of size 5.
>>> s.input(4)
>>> s.input(2)
>>> s.average
3
>>>s.input(6).average
4
```


## Building and Testing

`maverage` uses [`hatch`]() for building and `pytest` for testing. The `dev`
hatch environment includes `pytest` as a dependency. Create it using:
`hatch env create dev`.  Alternatively, use `hatch shell -e dev` to created it
if it doesn't exist and enter it.

> Note: To use the environment within VS Code, use the directory pointed to by
> the `hatch find env dev` command.

> TODO: Include build and versioning instructions.

Within the project directory, run the tests with the `pytest` command.
