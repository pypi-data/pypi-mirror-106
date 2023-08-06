#!/usr/bin/env bash


for (( i = 0; i < 100; i++ )); do
  name="$(cat /dev/urandom | env LC_CTYPE=C tr -cd 'a-f0-9' | head -c 32).plot"
  openssl rand -out ${name} -base64 $(( 2**30 * 1/4 ))
done