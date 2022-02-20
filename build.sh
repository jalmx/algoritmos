#!/bin/bash

echo "Init build"

mkdocs build &> /dev/null

echo "Done"