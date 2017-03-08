# ref:
# http://search.cpan.org/~abw/Template-Toolkit-2.26/lib/Template.pm
# http://perlhacks.com/articles/template-toolkit/introducing-the-template-toolkit-part-3/

use strict;
use warnings;

use Template;

my $urls;
push @$urls, 'google.com';
push @$urls, 'facebook.com';
my $pages = [
      { url   => 'http://foo.org',
        title => 'The Foo Organisation',
      },
      { url   => 'http://bar.org',
        title => 'The Bar Organisation',
      },
    ];

my $vars = {
    name  => 'Xiaotian',
    email => 'xiaotdl@gmail.com',
    invoice => {
        number => 101,
        items => [
            {
                desc  => 'dog',
                price => 100
            },
            {
                desc  => 'cat',
                price => 200
            }
        ]
    },
    pages => $pages,
    urls => $urls,
    lines => "\t\t1\n\t\t2\n\t\t3\n",
};

my $tt = Template->new;
$tt->process('template.tt', $vars)
    or die $tt->error;
