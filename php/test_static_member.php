<?php
# -> - calling an instance variable of a class
# :: - calling a static member/class variable of a class
# $this - refer to the current object, use $this->member for non-static members
# self - refer to the current class, use self::$member for static members
class FooBar {
    public static function fizz() {
        echo "Fizz\n";
    }

    public function buzz() {
        echo "Buzz\n";
    }

    public function test() {
        $this->buzz();
        self::fizz();
    }
}


$myFooBar = new FooBar();
$myFooBar->buzz();
FooBar::fizz();
$myFooBar->test();
