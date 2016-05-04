<?php
    // php strings 
   $variable = "name";
   $literally = 'My $variable will not print!\\n';
   
   print($literally);
   print "<br />";
   
   $literally = "My $variable will print!\\n";
   
   print($literally);
?>

<?php
    // string concatination
   $string1="Hello World";
   $string2="1234";
   
   echo $string1 . " " . $string2;
?>

<?php
   // strlen()
   echo strlen("Hello world!");
?>

<?php
   // strpos()
   echo strpos("Hello world!", "world");
?>
