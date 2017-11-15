Ref: http://www.perlmonks.org/?node_id=15838

# The Ties That Bind
Programmers are used to ``modules'' as a way of reusing code. Some modules provide subroutines, others provide an object-oriented interface. New in Perl 5 are ties, a way of intercepting accesses to a Perl variable (array, hash, scalar, or filehandle). This article will show you how to provide reusable code using ties.

## What is a tie
 To solve this inflexibility, Perl 5 introduced tie(), a more general mechanism for hiding complex behavior behind a variable, be it a hash, array, scalar, or filehandle.

Perl basically keeps an object for each variable you tie(). Each access to the tied variable results in method calls on the object. You can tie() a variable to just about anything; a database, a text file, a directory, even the Windows registry. You can even use tie() to trace accesses to a variable.

The methods automatically called by Perl have predefined names, in CAPS. There are only a few implicitly called methods your tying class should, and can, provide, which will be discussed later. The tying class is the invisible glue that holds your variable and resource together.

The example I'll work through will be a tie to a hash, since that is the most involved, the longest and best-supported, and (consequently) the most common. By the end of this article, you should have a good understanding of the tie() function, tying classes, and the knowlege to begin writting your own tie() class.

## Invoking a Tie
Invoking a tie() is similar to other Perl functions. tie() uses this syntax:
    tie VARIABLE, CLASSNAME, LIST

VARIABLE will be the variable being tied, which could be a hash, array, scalar, or filehandle.
CLASSNAME is the class we are using to handle the tied object.
LIST can be any optional flags or arguments that the class may use to construct the tied variable.

After calling tie(), the class will return an object, which can be either stored or ignored. Either way, when you access the VARIABLE, methods are called on the object.

To see what this looks like in practice, below is an example of tying a hash to the current directory using the Tie::Dir class. The result will be a tied interface between %hash and an object in the Tie::Dir class. The Tie::Dir class' methods will handle the manipulation of the directory via %hash:

    use Tie::Dir;
    tie %hash, Tie::Dir, "./";

## Method Names
As stated earlier, Perl will implicitly call a class' methods when the variable is accessed. When tie() is invoked it calls the appropriate TIESCALAR, TIEARRAY, TIEHASH, or TIEHANDLE method depending on the type of variable being tied.

Hash methods:
    TIEHASH classname, LIST
    DESTROY this
    FETCH this, key
    STORE this, key, value
    DELETE this, key
    EXISTS this, key
    FIRSTKEY this
    NEXTKEY this, lastkey

Array methods:
    TIEARRAY classname, LIST
    DESTROY this
    FETCH this, key
    STORE this, key, value

Scalar methods:
    TIESCALAR classname, LIST
    DESTROY this
    FETCH this,
    STORE this, value

Filehandle methods:
    TIEHANDLE classname, LIST
    WRITE this, LIST
    PRINT this, LIST
    PRINTF this, LIST
    READ this, LIST
    READLINE this
    GETC this
    CLOSE this
    DESTROY this

## Constructors/Destructors
When a variable is tied to a class, the TIE* constructor is called.

The constructor can do almost whatever the programmer wants it to. It may simply check to see if the resource to be tied to exists. It could create it if it doesn't, or load the resource into memory; or add an internal pointer to the resource in the class as object data. For example, if it is a directory to be tied to, the constructor may check to see if that directory exists, and if it does, it will save the location of that directory to the class object.

When the variable is untied (see later), goes out of scope, or the program ends, the object associated with the variable will be destroyed. The regular object destructor method DESTROY will be called. It is a very good habit to untie() tied variables when they are no longer needed. $foo would be untie()'d from the above example like so:

    untie $foo;

## Example.pm
## main.pl

## All tied() up
By using this function, you can access a reference to the underlying object. If you were to expand this example class, you may want to add the flexibility to use a second password file midway in your program. Instead of creating a new tied object, you can change your existing one like so:

    tied(%hash)->newPwdFile('/usr/local/apache/.passwds');

Which yields the same result as:

    $obj = tie(%hash, 'Tie::Class', 'rw');
    $obj->newPwdFile('/usr/local/apache/.passwds');






