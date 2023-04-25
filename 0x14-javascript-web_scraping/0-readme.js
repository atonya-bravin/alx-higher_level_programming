#!/usr/bin/node

// Check if the user entered 2 arguments in the shell
if (process.argv.length < 3) {
  console.log('Usage: node ' + process.argv[1] + ' FILENAME');
  process.exit(1);
}
// Call on the filesystem
const fs = require('fs');
const filename = process.argv[2];
fs.readFile(filename, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
    process.exit(1);
  }
  console.log(data);
});
