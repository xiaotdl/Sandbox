<?php
function curl_get($url) {
    $ch = curl_init();
    $timeout = 5;
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_HEADER, 1);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, $timeout);

    $response = curl_exec($ch);

    list($header, $body) = explode("\r\n\r\n", $response, 2);
    $http_status = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    echo $http_status;
    echo "\n---\n";
    echo $header;
    echo "\n---\n";
    echo $body;

    // // construct a new request
    // $header_text = preg_split( '/[\r\n]+/', $header);
    // foreach ( $header_text as $header_field ) {
    //     header( $header_field );
    // }
    // print $body;

    curl_close($ch);

    return $response;
}

$resp = curl_get('http://google.com/');
//echo $resp;

?>
