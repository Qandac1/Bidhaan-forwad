# 🤖 Telegram Multi-Channel Auto Forward Bot

<div align="center">

![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue?style=for-the-badge&logo=telegram)
![Python](https://img.shields.io/badge/Python-3.7+-yellow?style=for-the-badge&logo=python)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-green?style=for-the-badge&logo=mongodb)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)

**A powerful Telegram userbot that automatically forwards messages from multiple channels with advanced features!**

✨ **Created by:** [@amanbotz](https://t.me/amanbotz)  
🔗 **GitHub:** [theamanchaudhary](https://github.com/theamanchaudhary)

[Features](#-features) • [Installation](#-installation) • [Commands](#-commands) • [Screenshots](#-screenshots)

</div>

---

## ✨ Features

### 🔄 Core Features
- **Multi-Channel Support** - Monitor unlimited source channels
- **Two Forward Modes** - Copy (no attribution) or Forward (with attribution)
- **Real-Time Forwarding** - Instant message forwarding
- **MongoDB Database** - Reliable data storage
- **Easy Setup** - Just forward a message to add channels!

### 👥 User Management
- **User Tracking** - Track all bot users
- **Ban/Unban System** - Control who can use the bot
- **User Statistics** - See total users, banned users, etc.
- **User List** - View all registered users

### 📊 Advanced Features
- **Broadcast System** - Send messages to all users
- **Detailed Statistics** - Track forwards, users, channels
- **Interactive Buttons** - Easy navigation with inline buttons
- **Owner Panel** - Complete control panel for bot owner
- **Auto User Registration** - Users automatically registered on first interaction

### 🎯 Upcoming Features (Suggestions)
- **Scheduled Forwarding** - Set specific times for forwarding
- **Filter System** - Forward only specific types of messages
- **Caption Editor** - Modify captions before forwarding
- **Multiple Destinations** - Forward to multiple channels
- **Blacklist/Whitelist** - Filter specific keywords
- **Analytics Dashboard** - Web-based stats dashboard
- **Auto-Reply System** - Respond to specific messages
- **Watermark Feature** - Add watermark to forwarded media
- **Rate Limiting** - Control forward speed
- **Backup/Restore** - Database backup functionality

## 📋 Requirements

- Python 3.7 or higher
- Telegram Account
- MongoDB Database (Free tier available)
- API credentials from https://my.telegram.org

## 🚀 Installation

### Quick Deploy Options

<div align="center">

[![Deploy on Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
[![Deploy with Docker](https://img.shields.io/badge/Deploy-Docker-blue?style=for-the-badge&logo=docker)](DEPLOYMENT.md#docker-deployment)

</div>

### Local Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/theamanchaudhary/autoFrwd.git
cd autoFrwd
```

#### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 3. Get API Credentials

**Telegram API:**
1. Visit https://my.telegram.org
2. Login with your phone number
3. Click "API Development Tools"
4. Create an app and note `api_id` and `api_hash`

**MongoDB:**
1. Visit https://www.mongodb.com/cloud/atlas
2. Create a free account
3. Create a cluster
4. Get connection URI (starts with `mongodb+srv://...`)

#### 4. Setup Bot
```bash
python main.py setup
```

Follow the prompts to enter:
- API ID
- API Hash
- Bot Token (from @BotFather)
- MongoDB URI
- Owner ID (from @userinfobot)

#### 5. Start Bot
```bash
python main.py start
```

### 🐳 Docker Deployment

```bash
# Using Docker Compose
docker-compose up -d

# Or using Docker directly
docker build -t telegram-forward-bot .
docker run -d --name forward-bot telegram-forward-bot
```

[📖 Full Docker Guide](DEPLOYMENT.md#docker-deployment)

### ☁️ Heroku Deployment

```bash
# Deploy via CLI
heroku create your-bot-name
heroku config:set API_ID=your_api_id
heroku config:set API_HASH=your_api_hash
heroku config:set BOT_TOKEN=your_bot_token
heroku config:set MONGO_URI=your_mongo_uri
heroku config:set OWNER_ID=your_user_id
git push heroku main
heroku ps:scale worker=1
```

[📖 Full Heroku Guide](DEPLOYMENT.md#heroku-deployment)

## 🎮 Commands

### 📱 User Commands
| Command | Description |
|---------|-------------|
| `/start` | Start the bot and see welcome message |
| `/help` | Show help message |

### 👑 Owner Commands

#### 📥 Channel Management
| Command | Description | Example |
|---------|-------------|---------|
| `/addsource` | Add source channel | `/addsource` then forward message |
| `/setdest` | Set destination channel | `/setdest` then forward message |
| `/list` | Show all source channels | `/list` |
| `/remove <number>` | Remove channel by number | `/remove 1` |
| `/mode <number> <mode>` | Change forward mode | `/mode 1 forward` |

#### 👥 User Management
| Command | Description | Example |
|---------|-------------|---------|
| `/users` | Show all users | `/users` |
| `/ban <user_id> [reason]` | Ban a user | `/ban 123456789 Spam` |
| `/unban <user_id>` | Unban a user | `/unban 123456789` |
| `/banned` | Show banned users | `/banned` |

#### 📊 Statistics & Control
| Command | Description |
|---------|-------------|
| `/stats` | Detailed statistics |
| `/status` | Current bot status |
| `/broadcast` | Broadcast to all users |
| `/stop` | Stop the bot |

## 💡 Usage Guide

### Adding Source Channels

1. **Start the bot:** `python main.py start`
2. **Open Telegram** and message yourself
3. **Send command:** `/addsource`
4. **Go to source channel** you want to monitor
5. **Forward any message** from that channel to yourself
6. **Done!** Channel automatically added ✅

### Setting Destination

1. **Send command:** `/setdest`
2. **Go to destination channel** (where you want messages sent)
3. **Forward any message** from that channel to yourself
4. **Make sure** you're admin with post permissions
5. **Done!** Destination set ✅

### Broadcasting Messages

1. **Send command:** `/broadcast`
2. **Send your message** (text, photo, video, etc.)
3. **Bot sends to all users** automatically
4. **View results** - success/failed count

### Managing Users

```bash
# Ban a user
/ban 123456789 Spamming

# Unban a user
/unban 123456789

# View all banned users
/banned

# View all users
/users
```

## 📂 Project Structure

```
autoFrwd/
├── main.py              # Main bot file
├── database.py          # MongoDB database manager
├── config.py            # Configuration handler
├── commands.py          # Command handlers
├── requirements.txt     # Dependencies
├── config.json         # Config file (auto-generated)
├── .gitignore          # Git ignore rules
└── README.md           # Documentation
```

## 📊 Database Structure

### Collections:
- **users** - All bot users
- **channels** - Source channels
- **destination** - Destination channel
- **stats** - Bot statistics
- **banned_users** - Banned users list

## 🔒 Security & Privacy

- ✅ Session data encrypted
- ✅ MongoDB connection secured
- ✅ Owner-only commands protected
- ✅ User ban system
- ✅ Private message only commands
- ❌ Never commit `config.json` to git
- ❌ Never share session string
- ❌ Never share MongoDB URI

## 📸 Screenshots

### Owner Panel
```
👋 Welcome to Auto Forward Bot!

🔐 Owner Panel

✨ Quick Actions:
• /addsource - Add source channel
• /setdest - Set destination
• /stats - View statistics
• /broadcast - Send message to all users

✨ Created by: @amanbotz
```

### Statistics
```
📊 Bot Statistics

👥 Users:
• Total Users: 150
• Banned Users: 2
• Active Users: 148

📢 Channels:
• Source Channels: 5
• Total Forwards: 1,250

📅 Activity:
• Bot Started: 2025-01-15
• Days Active: 25
• Avg Forwards/Day: 50
```

## 🐛 Troubleshooting

### Bot not forwarding?
- ✓ Check if destination is set: `/status`
- ✓ Verify you're admin in destination
- ✓ Check source channels: `/list`
- ✓ Look at console for errors

### MongoDB connection failed?
- ✓ Check URI is correct
- ✓ Verify network access in MongoDB Atlas
- ✓ Check IP whitelist settings

### Commands not working?
- ✓ Make sure you're the owner
- ✓ Send commands in private chat
- ✓ Bot must be running

### Session expired?
- ✓ Run `python main.py setup` again

## 🎯 Suggested Features to Add

1. **Message Filters**
   - Filter by keywords
   - Filter by media type
   - Filter by message length

2. **Scheduling System**
   - Schedule forwards for specific times
   - Daily/weekly schedules
   - Time zone support

3. **Caption Editor**
   - Add custom captions
   - Replace captions
   - Append to captions

4. **Multi-Destination**
   - Forward to multiple channels
   - Different modes per destination
   - Priority system

5. **Analytics Dashboard**
   - Web-based dashboard
   - Real-time statistics
   - Export reports

6. **Auto-Reply**
   - Reply to specific keywords
   - Welcome messages
   - FAQ bot

7. **Media Processing**
   - Add watermarks
   - Compress media
   - Convert formats

8. **Advanced Filters**
   - Blacklist words
   - Whitelist senders
   - Regex support

9. **Backup System**
   - Automatic backups
   - Restore functionality
   - Export/import config

10. **Webhook Support**
    - Send notifications
    - Trigger external APIs
    - Integration with other services

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This bot is for educational and personal use. Use responsibly and follow Telegram's Terms of Service. The developer is not responsible for any misuse.

## 📞 Support

- **Telegram:** [@amanbotz](https://t.me/amanbotz)
- **GitHub:** [theamanchaudhary](https://github.com/theamanchaudhary)
- **Issues:** [Report Bug](https://github.com/theamanchaudhary/autoFrwd/issues)

## 💖 Acknowledgments

- [Telethon](https://github.com/LonamiWebs/Telethon) - Telegram client library
- [MongoDB](https://www.mongodb.com/) - Database
- [Motor](https://motor.readthedocs.io/) - Async MongoDB driver

---

---

<div align="center">

**Made with ❤️ by [@amanbotz](https://t.me/amanbotz)**  
**GitHub:** [theamanchaudhary](https://github.com/theamanchaudhary)

⭐ Star this repo if you found it helpful!

</div>

````
