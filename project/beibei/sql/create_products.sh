 curl --request POST \
    --header "Content-Type: application/json" \
    --data '{"name":"medicine a si pi lin","code":"4005808847013", "batch": "1", "spec": "100mg x 30pill", "tag": "5305db6d"}' \
    http://localhost:5000/product

 curl --request POST \
    --header "Content-Type: application/json" \
    --data '{"name":"medicine bu luo fen","code":"4005808847014", "batch": "1", "spec": "0.3g x 20pill", "tag": "44d23ca1"}' \
    http://localhost:5000/product
