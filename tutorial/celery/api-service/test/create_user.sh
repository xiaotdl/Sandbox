curl --request POST \
    --header "Content-Type: application/json" \
    --data '{"name": "admin","email": "admin@f5.com"}' \
    http://localhost:5000/api/user

curl --request POST \
    --header "Content-Type: application/json" \
    --data '{"name": "user_example","email": "example@f5.com"}' \
    http://localhost:5000/api/user

curl --request POST \
    --header "Content-Type: application/json" \
    --data '{"name": "test","email": "test@f5.com"}' \
    http://localhost:5000/api/user

