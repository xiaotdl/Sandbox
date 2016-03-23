list=(
"item 1"
"item 2"
)
for item in "${list[@]}";do
    echo $item
done
