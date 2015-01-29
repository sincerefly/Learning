colors = require 'colors'

console.log 'colors'.rainbow

colors.setTheme
  info: 'green'
  warn: 'yellow'
  error: 'red'

console.log 'Error'.error
console.log 'Warning'.warn
console.log 'Info'.info


