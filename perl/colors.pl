#!/usr/bin/perl

use strict;
use warnings;

# == print string in colors ==

# Ref: http://unix.stackexchange.com/a/124408
# Ref: http://misc.flogisoft.com/bash/tip_colors_and_formatting#colors
# bldblk='\e[1;30m' # Black - Bold
# bldred='\e[1;31m' # Red
# bldgrn='\e[1;32m' # Green
# bldylw='\e[1;33m' # Yellow
# bldblu='\e[1;34m' # Blue
# bldpur='\e[1;35m' # Purple
# bldcyn='\e[1;36m' # Cyan
# bldwht='\e[1;37m' # White
# txtrst='\e[0m'    # Text Reset
my %COLORS = (
    '${black}'     => "\e[0;30m",
    '${red}'       => "\e[0;31m",
    '${green}'     => "\e[0;32m",
    '${yellow}'    => "\e[0;33m",
    '${blue}'      => "\e[0;34m",
    '${purple}'    => "\e[0;35m",
    '${cyan}'      => "\e[0;36m",
    '${white}'     => "\e[0;37m",

    '${bldblack}'  => "\e[1;30m",
    '${bldred}'    => "\e[1;31m",
    '${bldgreen}'  => "\e[1;32m",
    '${bldyellow}' => "\e[1;33m",
    '${bldblue}'   => "\e[1;34m",
    '${bldpurple}' => "\e[1;35m",
    '${bldcyan}'   => "\e[1;36m",
    '${bldwhite}'  => "\e[1;37m",

    '${rst}'       => "\e[0m",
);

sub color {
    my ($colorTag, $str) = @_;
    return $str
        unless defined $str && $str ne '';
    return "\${$colorTag}$str\${rst}";
}

sub black { color('black', shift); }
sub red { color('red', shift); }
sub green { color('green', shift); }
sub yellow { color('yellow', shift); }
sub blue { color('blue', shift); }
sub purple { color('purple', shift); }
sub cyan { color('cyan', shift); }
sub white { color('white', shift); }

sub bldblack { color('bldblack', shift); }
sub bldred { color('bldred', shift); }
sub bldgreen { color('bldgreen', shift); }
sub bldyellow { color('bldyellow', shift); }
sub bldblue { color('bldblue', shift); }
sub bldpurple { color('bldpurple', shift); }
sub bldcyan { color('bldcyan', shift); }
sub bldwhite { color('bldwhite', shift); }

sub colorPrint {
    my $str = shift;
    foreach my $colorTag (keys %COLORS) {
        my $escapeSeq = $COLORS{$colorTag};
        $colorTag = quotemeta($colorTag);
        $str =~ s/$colorTag/$escapeSeq/g;
    }
    print $str;
}

colorPrint "Hello World!\n"
           . black("Hello") . bldblack(" World!") . "\n"
           . red("Hello") . bldred(" World!") . "\n"
           . green("Hello") . bldgreen(" World!") . "\n"
           . yellow("Hello") . bldyellow(" World!") . "\n"
           . blue("Hello") . bldblue(" World!") . "\n"
           . purple("Hello") . bldpurple(" World!") . "\n"
           . cyan("Hello") . bldcyan(" World!") . "\n"
           . white("Hello") . bldwhite(" World!") . "\n";
