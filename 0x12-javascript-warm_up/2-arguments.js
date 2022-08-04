#!/usr/bin/node
const lng = process.argv.length -2;
const print = console.log;

if (!lng) print('No argument');
if (lng === 1) print('Argument found');
if (lng > 1) print('Arguments found');
