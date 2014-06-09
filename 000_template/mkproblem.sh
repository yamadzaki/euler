#!/bin/bash

mkdir -p ../machine/$1
if [ -e ../boot-images/pxe/module.list ]; then
    mv ../boot-images/pxe/module.list ../machine/$1/.
else
    echo ".list files not found"
    exit 1
fi

if [ -e ../boot-images/pxe/vbe_modes.list ]; then
    mv ../boot-images/pxe/vbe_modes.list ../machine/$1/.
fi

if [ -e ../boot-images/pxe/firmware.list ]; then
    mv ../boot-images/pxe/firmware.list ../machine/$1/.

