[![Build Status](https://travis-ci.org/agateau/doxyqml.svg?branch=master)](https://travis-ci.org/agateau/doxyqml)
[![Coverage Status](https://coveralls.io/repos/github/agateau/doxyqml/badge.svg?branch=master)](https://coveralls.io/github/agateau/doxyqml?branch=master)

# Goals

Doxyqml turns .qml into pseudo-C++ which Doxygen can then use to generate
documentation.

# Installing

Doxyqml uses the standard Python setup tools, so you can install it with pip:

    pip3 install doxyqml

or manually with:

    python3 setup.py install

# Telling Doxygen to use Doxyqml

To tell Doxygen about Doxyqml you must make a few changes to your Doxygen file.

1. Add the .qml extension to the `FILTER_PATTERNS` key:

        FILTER_PATTERNS = *.qml=doxyqml

    Note: On Windows you may need to use the full path of the `doxyqml.py` file
    instead. For example if you installed Python 3.5 in `C:\Python35`, use this:

        FILTER_PATTERNS = *.qml=C:\Python35\Lib\site-packages\doxyqml\doxyqml.py

2. Add the .qml extension to `FILE_PATTERNS`:

        FILE_PATTERNS = *.qml

3. Since Doxygen 1.8.8, you must also add the .qml extension to
   `EXTENSION_MAPPING`:

        EXTENSION_MAPPING = qml=C++

# Documenting types

QML is partly-typed: functions are untyped, properties and signals are. Doxyqml
provides a way to define types when they are missing or not precise enough.

## Functions

Functions in QML are untyped, but you can define types in the documentation
like this:

    /**
     * Create a user
     * @param type:string firstname User firstname
     * @param type:string lastname User lastname
     * @param type:int User age
     * @return type:User The User object
     */
    function createUser(firstname, lastname, age);

## Properties

QML properties are typed, so Doxyqml uses them by default. You can nevertheless
overwrite the type using the same `type:<name>` syntax. This is useful to
document property aliases:

    /** type:string The user lastname */
    property alias lastname: someObject.text

## Signals

QML signals are typed, so there is no need to use the `type:<name>` syntax to
document their parameters. Using `type:<name>` syntax in signal documentation
will not work: Doxyqml won't strip it out and Doxygen will confuse it with the
parameter name.

    /**
     * User just logged in
     * @param user The user which logged in
     */
    signal loggedIn(User user)
