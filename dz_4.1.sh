#!/bin/bash

get_size() {
        path="$1"
        size=$(du -h -s "$path" | cut -f1)
        echo $size
}

list=$(ls -A)

for item in $list; do
        size=$(get_size "$item")
        echo -e "$size\t $item"
done | sort -r -h -k1,2 