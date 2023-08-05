#!/bin/sh

#go install mover.go && 
env GOOS=darwin GOARCH=amd64 go build -o plmo mover.go
FROM=/Users/hesdx/Documents/ipfs/plotman/copyop/temp
TO=/Users/hesdx/Documents/ipfs/plotman/copyop/dst/

./plmo $FROM $TO 10010001 farming.log