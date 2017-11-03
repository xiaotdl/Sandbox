http://perldoc.perl.org/functions/caller.html

**caller**
caller EXPR
caller
Returns the context of the current pure perl subroutine call.
In scalar context, returns the caller's package name if there is a caller
(that is, if we're in a subroutine or eval or require) and the undefined value otherwise.

In list context, caller returns:
```
my ($package, $filename, $line) = caller;
```

With EXPR, it returns some extra information that the debugger uses to print a stack trace. The value of EXPR indicates how many call frames to go back before the current one.
```
my ($package, $filename, $line, $subroutine, $hasargs,
    $wantarray, $evaltext, $is_require, $hints, $bitmask, $hinthash)
    = caller($i);

```
