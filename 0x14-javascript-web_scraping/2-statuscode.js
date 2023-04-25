#!/usr/bin/node

const https = require('https');

const url = process.argv[1];

https.get(url, (res) => {
  console.log(`code: ${res.statusCode}`);
});
