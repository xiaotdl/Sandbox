<?php

function write($file_path, $line)
{
    echo "create/append to file: " . $file_path . "\n";
    echo "                 line: " . $line. "\n";

    $f = fopen($file_path, "a")
        or die ("Unable to open file!");

    fwrite($f, $line);

    fclose($f);
}

# required to eliminate the warning message
date_default_timezone_set('America/Los_Angeles');
function get_time()
{
    return '[' . date("m/d/Y h:i:s a", time()) . ']' . ' ';
}

function main()
{
    $file_path = join('/', array($_ENV["HOME"], 'php.out'));
    $line = get_time() . "Hey, what's up!\n";
    write($file_path, $line);
    $line = get_time() . "I'm good good.\n";
    write($file_path, $line);
}

main();
         
