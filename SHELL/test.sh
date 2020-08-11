#!/bin/bash

echo Number given: $1
a=0; b=0; b0=0; b1=0; b2=0; b3=0; b4=0; b5=0; b6=0; b7=0;

a=$(($1/2)); b=$(($1%2)); b0=$b;
echo $a $b $b0
a=$(($a/2)); b=$(($a%2)); b1=$b;
echo $a $b $b1
a=$(($a/2)); b=$(($a%2)); b2=$b;
echo $a $b $b2

