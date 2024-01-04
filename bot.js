const { Client } = require('discord.js');
const client = new Client();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
  if (msg.content.toLowerCase() === 'ping') {
    msg.reply('Pong!');
  }
});

client.login('5f75244b329b888c16120bdb4113755941bed410919ef84e11a7b572315a7e52');
