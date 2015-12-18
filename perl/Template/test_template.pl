# ref:
# http://search.cpan.org/~abw/Template-Toolkit-2.26/lib/Template.pm
# http://perlhacks.com/articles/template-toolkit/introducing-the-template-toolkit-part-3/

use strict;
use warnings;

use Template;

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
    }
};

my $tt = Template->new;
$tt->process('template.tt', $vars)
    or die $tt->error;
