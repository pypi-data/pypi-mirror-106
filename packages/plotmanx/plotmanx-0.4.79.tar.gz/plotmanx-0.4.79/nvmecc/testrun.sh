#!/bin/sh

#test development only

env GOOS=darwin GOARCH=amd64 go build -o plmo vncc.go
FROM=/Users/hesdx/Documents/ipfs/plotman/nvmecc/temp
TO=/Users/hesdx/Documents/ipfs/plotman/nvmecc/dst/

./plmo $FROM $TO 50010001 farming.log