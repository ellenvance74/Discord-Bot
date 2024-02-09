const { Client } = require('discord.js');
const client = new Client();

// Bot event: Triggered when the bot is ready
client.once('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

// Bot event: Triggered when a message is received
client.on('message', (message) => {
  // Ignore messages from bots and messages without the bot's prefix
  if (message.author.bot || !message.content.startsWith('!')) return;

  // Extract the command and arguments from the message content
  const args = message.content.slice(1).split(/ +/);
  const command = args.shift().toLowerCase();

  // Simple command example: !ping
  if (command === 'ping') {
    message.channel.send('Pong!');
  }
  // Add more commands as needed...

  // Example of handling a custom command
  // if (command === 'custom') {
  //   // Handle the custom command...
  // }

  // You can add more command handling logic based on your bot's functionality
});

// Log in to Discord with the bot token
client.login('qq0QloaroGOJt737Sq9rlB-qn9azf6Tl');
