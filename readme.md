# maverage - Moving Average


## About maverage

maverage provides a Simple Moving Average implementation that delays the
average calculation until requested - useful for programs that collect data in
real-time and delay processing until later.


## Basic Usage - `Simple`

```python
>>> s = Simple(5)  # Simple object with internal buffer of size 5.
>>> s.input(4)
>>> s.input(2)
>>> s.average
3.0
>>>s.input(6).average
4.0
```


## Testing

maverage tests are written using pytest. The `dev` Hatch environment
includes pytest (refer to the [Building](#building) section for details on how
to set it up). Once inside the dev environment, run the tests by simply running
`pytest`.


## Building

maverage is set up to use [Hatch](https://hatch.pypa.io/latest/) for building.

Create a development environment using: `hatch env create dev`. Alternatively,
use `hatch shell -e dev` to (1) created it if it doesn't exist and (2) open it
in a shell session.

> Note: To use the environment within VS Code, use the directory pointed to by
> the `hatch find env dev` command.

The project can be built, reversioned, and published with hatch's `build`,
`version`, and `publish` commands, respectively.
<!-- To publish, use username=__token__ and the API token as the password. -->


## License

This project uses the MIT License. Refer to the project's LICENSE.txt for
details.
