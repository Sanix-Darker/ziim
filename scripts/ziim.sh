#!/usr/bin/env bash

if [[ ! $@ ]]; then
    python3 -m ziim -h
else
    python3 -m ziim $@
fi
