# ref: http://search.cpan.org/~cjm/HTML-Tree-5.03/lib/HTML/Element.pm
# (This class is part of the HTML::Tree dist.)

use HTML::Element;
use Data::Dumper;

#$a = HTML::Element->new('a', href => 'http://www.perl.com/');
#$a->push_content("The Perl Homepage");

#$tag = $a->tag;
#print "$tag starts out as:",  $a->starttag, "\n";
#print "$tag ends as:",  $a->endtag, "\n";
#print "$tag\'s href attribute is: ", $a->attr('href'), "\n";
## >>>
## a starts out as:<a href="http://www.perl.com/">
## a ends as:</a>
## a's href attribute is: http://www.perl.com/

#$links_r = $a->extract_links();
#print "Hey, I found ", scalar(@$links_r), " links.\n";
## >>>
## Hey, I found 1 links.

#print "And that, as HTML, is: ", $a->as_HTML, "\n";
## >>>
## And that, as HTML, is: <a href="http://www.perl.com/">The Perl Homepage</a>

#$a = $a->delete;


# == BASIC METHODS ==
# new()
# $h = HTML::Element->new('tag', 'attrname' => 'value', ... );

# == STRUCTURE-MODIFYING METHODS ==
# push_content()
$body = HTML::Element->new('body');
$body->push_content(
	['h2', 'example'],
    ['table',
        {
            width => '100%',
            border => 1,
            bordercolor => 'black',
            cellpadding => 1,
            cellspacing => 0,
        },
        ['thead',
            ['tr',
                map {['th', $_]} qw(Head1 Head2 Head3)],
        ],
        ['tbody',
            ['tr',
                map {['td', $_]} qw(Apple1 Apple2 Apple3)],
            ['tr',
                map {['td', $_]} qw(Pear1 Pear2 Pear3)],
        ]
    ],
);

print $body->as_HTML;
# >>> formated
# <table>
#     <thead>
#         <tr>
#             <th>Head1</th>
#             <th>Head2</th>
#             <th>Head3</th>
#         </tr>
#     </thead>
#     <tbody>
#         <tr>
#             <td>Apple1</td>
#             <td>Apple2</td>
#             <td>Apple3</td>
#         </tr>
#         <tr>
#             <td>Pear1</td>
#             <td>Pear2</td>
#             <td>Pear3</td>
#         </tr>
#     </tbody>
# </table>

# write into out.html
open(my $fh, '>', 'out.html');
print $fh $body->as_HTML;
close $fh;
# >>> browser view
# Head1  Head2  Head3
# Apple1 Apple2 Apple3
# Pear1  Pear2  Pear3

$tbody = $body->look_down(_tag => 'tbody');
#print Dumper($tbody);
my @descendants = $body->descendants;
print $_->tag . "\n"
    foreach @descendants;
