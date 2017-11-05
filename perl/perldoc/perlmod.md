# perlmod - Perl modules (packages and symbol tables)
Perl's packages, namespaces, and some info on classes.

## Packages
Perl 5 provides two mechanisms for protecting code from having its variables stomped on by other code:
1) __lexically scoped variables__ created with **my** or **state**
2) __namespaced global variables__, which are exposed via the **vars** pragma, or the **our** keyword.
   Any global variable is considered to be part of a namespace and can be accessed via a "fully qualified form".
   Conversely, any lexically scoped variable is considered to be part of that lexical-scope, and does not have a "fully qualified form".

In Perl, namespaces are called "packages" and the package declaration tells the compiler
which namespace to prefix to our variables and unqualified dynamic names.
This both protects against accidental stomping and provides an interface for deliberately
clobbering global dynamic variables declared and used in other scopes or packages, when that is what you want to do.

Typically, a **package** statement is the first declaration in a file included in a program
by one of the **do**, **require**, or **use** operators.

You can refer to variables and filehandles in other packages by prefixing the identifier
with the package name and a double colon: __$Package::Variable__.
If the package name is null, the main package is assumed. That is, __$::sail__ is equivalent to __$main::sail__.

Only identifiers starting with letters (or underscore) are stored in a package's symbol table.
All other symbols are kept in package main , including all punctuation variables, like $\_.
In addition, when unqualified, the identifiers STDIN, STDOUT, STDERR, ARGV, ARGVOUT, ENV, INC, and SIG
are forced to be in package main, even when used for other purposes than their built-in ones.

## Symbol Tables
The symbol table for a package happens to be stored in the hash of that name with two colons appended.
The main symbol table's name is thus %main:: , or %:: for short.
Likewise the symbol table for the nested package mentioned earlier is named %OUTER::INNER::.

The value in each entry of the hash is what you are referring to when you use the \*name typeglob notation.
```
    local *main::foo = *main::bar;
```

Assignment to a typeglob performs an aliasing operation, i.e.,
```
    *dick = *richard;
```

