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
