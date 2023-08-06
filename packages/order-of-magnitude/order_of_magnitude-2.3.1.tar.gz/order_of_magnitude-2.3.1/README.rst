.. image:: https://badge.fury.io/py/order-of-magnitude.svg
    :target: https://badge.fury.io/py/order-of-magnitude

==================
Order of magnitude
==================
Pure Python 3 implementation to convert floats, lists of floats, NumPy arrays to International System
of Units (SI) strings.

Install by::

    pip install order-of-magnitude


Available functions
-------------------
- ``convert(x, scale)``: returns the input values as ``float`` in the scale provided
- ``order_of_magnitude(x)``: returns the order of magnitude exponent of the input values as ``float``
- ``power_of_ten(x)``: returns the power of ten corresponding to the order of magnitude of the input values as ``float``
- ``prefix(x, decimals=1, scale=None, omit_x=None, word=False)``: returns a ``tuple`` containing the scale on input
  ``x`` as ``float``, the prefix of the scale of ``x`` as ``string``, and the input ``x`` formatted in SI units.::

    print( order_of_magnitude.prefix( [ 1.1e-3, 100e3, 0 ] ) )
    # output:  ([0.001, 1000.0, 1.0], ['mili', 'kilo', ''], ['1.1 mili', '100.0 kilo', '0.0 '])

- ``symbol(x, decimals=1, scale=None, omit_x=None, word=False)``: returns a ``tuple`` containing the scale on input
  ``x`` as ``float``, the symbol of the scale of ``x`` as ``string``, and the input ``x`` formatted in SI units.::

    print( order_of_magnitude.symbol( [ 1.1e-3, 100e3, 0 ] ) )
    # output:  ([0.001, 1000.0, 1.0], ['m', 'k', ''], ['1.1 m', '100.0 k', '0.0 '])

- ``short_scale(x, decimals=1, scale=None, omit_x=None, word=True)``: returns a ``tuple`` containing the scale on input
  ``x`` as ``float``, the short scale identifier of ``x`` as ``string``, and the input ``x`` formatted in SI units.::

    print( order_of_magnitude.short_scale( [ 1.1e-3, 100e3, 0 ] ) )
    # output:  ([0.001, 1000.0, 1.0], ['thousandth', 'thousand', ''], ['one point one thousandth', 'one hundred thousand', 'zero '])

- ``long_scale(x, decimals=1, scale=None, omit_x=None, word=True)``:  returns a ``tuple`` containing the scale on input
  ``x`` as ``float``, the long scale identifier of ``x`` as ``string``, and the input ``x`` formatted in SI units.::

    print( order_of_magnitude.long_scale( [ 1.1e-3, 100e3, 0 ] ) )
    # output:  ([0.001, 1000.0, 1.0], ['thousandth', 'thousand', ''], ['one point one thousandth', 'one hundred thousand', 'zero '])

- ``prefixes_dict()``: returns the dictionary mapping order of magnitude to prefixes
- ``symbols_dict()``: returns the dictionary mapping order of magnitude to symbols
- ``short_scale_dict()``: returns the dictionary mapping order of magnitude to short scale measures
- ``long_scale_dict()``: returns the dictionary mapping order of magnitude to long scale measures

Function parameters
-------------------
- ``x`` can be a scalar, a list, or a NumPy array.
- ``decimals`` controls how many decimal points are printed.
- ``scale`` sets the conversion to use a fixed reference SI unit.  Can be a ``float`` or an entry among the
  dictionary values returned by ``prefixes_dict()``, ``symbols_dict()``, ``short_scale_dict()``, or
  ``long_scale_dict()``.
- ``word`` controls if the printed output is in word-form or as a number.

Examples
--------
::

    from order_of_magnitude import order_of_magnitude

    print( "Order of magnitude:", order_of_magnitude.order_of_magnitude( [ 1.1e-3, 100e3, 0 ] ) )
    print( "Power of ten:", order_of_magnitude.power_of_ten( [ 1.1e-3, 100e3, 0 ] ) )
    print( "Convert to mili:", order_of_magnitude.convert( [ 1.1e-3, 100e3, 0 ], scale="mili" ) )
    print( "Prefix:", order_of_magnitude.prefix( [ 1.1e-3, 100e3, 0 ] ) )
    print( "Prefix in mili:", order_of_magnitude.prefix( [ 1.1e-3, 100e3, 0 ], scale="mili" ) )
    print( "Prefix in kilo:", order_of_magnitude.prefix( [ 1.1e-3, 100e3, 0 ], scale="k", decimals=8 ) )
    print( "Prefix in kilo:", order_of_magnitude.prefix( [ 1.1e-3, 100e3, 0 ], scale=1e3 ) )
    print( "Symbol:", order_of_magnitude.symbol( [ 1.1e-3, 100e3, 0 ] ) )
    print( "Prefix in words:", order_of_magnitude.prefix( [ 1.1e-3, 100e3, 0 ], word=True ) )
    print( "Short scale:", order_of_magnitude.short_scale( [ 1.1e-3, 100e3, 0 ] ) )
    print( "Long scale:", order_of_magnitude.long_scale( [ 1.1e-3, 100e3, 0 ] ) )
    print( "Short scale in numbers:", order_of_magnitude.short_scale( [ 1.1e-3, 100e3, 0 ], word=False ) )
    print( "Long scale dictionary:", order_of_magnitude.long_scale_dict() )

    ## OUTPUT
    # Order of magnitude: [-3, 5, 0]
    # Power of ten: [0.001, 100000.0, 1.0]
    # Convert to mili: [1.1, 100000000.0, 0.0]
    # Prefix: ([0.001, 1000.0, 1.0], ['mili', 'kilo', ''], ['1.1 mili', '100.0 kilo', '0.0 '])
    # Prefix in mili: ([0.001, 0.001, 0.001], ['mili', 'mili', 'mili'], ['1.1 mili', '100000000.0 mili', '0.0 mili'])
    # Prefix in kilo: ([1000.0, 1000.0, 1000.0], ['kilo', 'kilo', 'kilo'], ['0.00000110 kilo', '100.00000000 kilo', '0.00000000 kilo'])
    # Prefix in kilo: ([1000.0, 1000.0, 1000.0], ['kilo', 'kilo', 'kilo'], ['0.0 kilo', '100.0 kilo', '0.0 kilo'])
    # Symbol: ([0.001, 1000.0, 1.0], ['m', 'k', ''], ['1.1 m', '100.0 k', '0.0 '])
    # Prefix in words: ([0.001, 1000.0, 1.0], ['mili', 'kilo', ''], ['one point one mili', 'one hundred kilo', 'zero '])
    # Short scale: ([0.001, 1000.0, 1.0], ['thousandth', 'thousand', ''], ['one point one thousandth', 'one hundred thousand', 'zero '])
    # Long scale: ([0.001, 1000.0, 1.0], ['thousandth', 'thousand', ''], ['one point one thousandth', 'one hundred thousand', 'zero '])
    # Short scale in numbers: ([0.001, 1000.0, 1.0], ['thousandth', 'thousand', ''], ['1.1 thousandth', '100.0 thousand', '0.0 '])
    # Long scale dictionary: {24: 'quadrillion', 21: 'trilliard', 18: 'trillion', 15: 'billiard', 12: 'billion', 9: 'milliard', 6: 'million', 3: 'thousand', 2: 'hundred', 1: 'ten', 0: '', -1: 'tenth', -2: 'hundredth', -3: 'thousandth', -6: 'millionth', -9: 'milliardth', -12: 'billionth', -15: 'billiardth', -18: 'trillionth', -21: 'trilliardth', -24: 'quadrillionth'}

