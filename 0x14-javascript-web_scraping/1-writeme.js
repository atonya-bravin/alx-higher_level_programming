#!/usr/bin/node

// Check if the user entered 2 arguments in the shell
if (process.argv.length < 4) {
  console.log('Usage: node ' + process.argv[1] + ' FILENAME INPUT_STRING');
  process.exit(1);
}
// Call on the filesystem
const fs = require('fs');
const filename = process.argv[2];
const string = process.argv[3];
fs.readFile(filename, 'utf8', string, (err) => {
	if (err) {
		console.log(err);
		process.exit(1);
	}
	console.log(data);
});
