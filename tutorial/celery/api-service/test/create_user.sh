curl --request POST \
    --header "Content-Type: application/json" \
    --data '{"name": "admin","email": "admin@company.com"}' \
    http://localhost:5000/api/user

curl --request POST \
    --header "Content-Type: application/json" \
    --data '{"name": "user_example","email": "example@company.com"}' \
    http://localhost:5000/api/user

curl --request POST \
    --header "Content-Type: application/json" \
    --data '{"name": "test","email": "test@company.com"}' \
    http://localhost:5000/api/user

