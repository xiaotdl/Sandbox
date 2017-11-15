https://perldoc.perl.org/PerlIO.html

# PerlIO
On demand loader for PerlIO layers and root of PerlIO::\* name space

## SYNOPSIS
```
  open($fh, "<:crlf", "my.txt"); # support platform-native and
                                 # CRLF text files
  open($fh, "<", "his.jpg"); # portably open a binary file for reading
  binmode($fh);
  Shell:
    PERLIO=perlio perl ....
```

## Description

### Builtin Layers
The following layers are currently defined:
- :unix
    Lowest level layer which provides basic PerlIO operations in terms of UNIX/POSIX numeric file descriptor calls (open(), read(), write(), lseek(), close()).
- :stdio
    Layer which calls fread , fwrite and fseek/ftell etc. Note that as this is "real" stdio it will ignore any layers beneath it and go straight to the operating system via the C library as usual.
- :perlio
    A from scratch implementation of buffering for PerlIO. Provides fast access to the buffer for sv_gets which implements perl's readline/<> and in general attempts to minimize data copying.
    :perlio will insert a :unix layer below itself to do low level IO.
- :crlf
    A layer that implements DOS/Windows like CRLF line endings. On read converts pairs of CR,LF to a single "\n" newline character. On write converts each "\n" to a CR,LF pair.
    Based on the :perlio layer.
- :utf8
    Declares that the stream accepts perl's internal encoding of characters. (Which really is UTF-8 on ASCII machines, but is UTF-EBCDIC on EBCDIC machines.) This allows any character perl can represent to be read from or written to the stream. The UTF-X encoding is chosen to render simple text parts (i.e. non-accented letters, digits and common punctuation) human readable in the encoded file.
(CAUTION: This layer does not validate byte sequences. For reading input, you should instead use :encoding(UTF-8) instead of bare :utf8 .)
- :bytes
    This is the inverse of the :utf8 layer. It turns off the flag on the layer below so that data read from it is considered to be "octets" i.e. characters in the range 0..255 only. Likewise on output perl will warn if a "wide" character is written to a such a stream.
- :raw
    The :raw layer is defined as being identical to calling binmode($fh) - the stream is made suitable for passing binary data, i.e. each byte is passed as-is. The stream will still be buffered.
- :pop
    A pseudo layer that removes the top-most layer. Gives perl code a way to manipulate the layer stack. Note that :pop only works on real layers and will not undo the effects of pseudo layers like :utf8 .
```
    open($fh,...)
    ...
    binmode($fh,":encoding(...)");  # next chunk is encoded
    ...
    binmode($fh,":pop");            # back to un-encoded
```

### Custom Layers
:encoding
:mmap
:via


