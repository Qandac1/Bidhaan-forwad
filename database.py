# database.py
"""
Database Manager for Telegram Forward Bot
Created by: @amanbotz
GitHub: https://github.com/theamanchaudhary
"""

from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
from typing import List, Dict, Optional

class Database:
    def __init__(self):
        self.client = None
        self.db = None
        self.users = None
        self.channels = None
        self.destination = None
        self.stats = None
        self.banned_users = None
        self.user_sessions = None  # Store user sessions for multi-user support
        self.user_channels = None  # Store each user's source channels
        self.user_destinations = None  # Store each user's destination channels
    
    async def connect(self, mongo_uri: str, db_name: str = 'forward_bot') -> bool:
        """Connect to MongoDB"""
        try:
            self.client = AsyncIOMotorClient(mongo_uri)
            self.db = self.client[db_name]
            
            # Collections
            self.users = self.db['users']
            self.channels = self.db['channels']
            self.destination = self.db['destination']
            self.stats = self.db['stats']
            self.banned_users = self.db['banned_users']
            self.user_sessions = self.db['user_sessions']  # User login sessions
            self.user_channels = self.db['user_channels']  # Each user's channels
            self.user_destinations = self.db['user_destinations']  # Each user's destinations
            
            # Test connection
            await self.client.admin.command('ping')
            
            # Initialize stats if not exists
            if await self.stats.count_documents({}) == 0:
                await self.stats.insert_one({
                    'total_forwards': 0,
                    'start_date': datetime.now()
                })
            
            print("✓ Connected to MongoDB")
            return True
        except Exception as e:
            print(f"✗ MongoDB connection error: {e}")
            return False
    
    # ============ USER MANAGEMENT ============
    
    async def add_user(self, user_id: int, username: str) -> bool:
        """Add a new user or update existing"""
        try:
            await self.users.update_one(
                {'user_id': str(user_id)},
                {
                    '$set': {
                        'username': username,
                        'last_active': datetime.now()
                    },
                    '$setOnInsert': {
                        'joined_date': datetime.now()
                    }
                },
                upsert=True
            )
            return True
        except Exception as e:
            print(f"Error adding user: {e}")
            return False
    
    async def get_all_users(self) -> List[Dict]:
        """Get all users"""
        try:
            cursor = self.users.find({})
            return await cursor.to_list(length=None)
        except:
            return []
    
    async def get_user_count(self) -> int:
        """Get total user count"""
        try:
            return await self.users.count_documents({})
        except:
            return 0
    
    async def is_user_banned(self, user_id: int) -> bool:
        """Check if user is banned"""
        try:
            result = await self.banned_users.find_one({'user_id': str(user_id)})
            return result is not None
        except:
            return False
    
    async def ban_user(self, user_id: int, username: str, reason: str = "No reason") -> bool:
        """Ban a user"""
        try:
            await self.banned_users.insert_one({
                'user_id': str(user_id),
                'username': username,
                'reason': reason,
                'banned_date': datetime.now()
            })
            return True
        except:
            return False
    
    async def unban_user(self, user_id: int) -> bool:
        """Unban a user"""
        try:
            result = await self.banned_users.delete_one({'user_id': str(user_id)})
            return result.deleted_count > 0
        except:
            return False
    
    async def get_banned_users(self) -> List[Dict]:
        """Get all banned users"""
        try:
            cursor = self.banned_users.find({})
            return await cursor.to_list(length=None)
        except:
            return []
    
    async def get_ban_info(self, user_id: int) -> Optional[Dict]:
        """Get ban information for a specific user"""
        try:
            return await self.banned_users.find_one({'user_id': str(user_id)})
        except:
            return None
    
    # ============ CHANNEL MANAGEMENT ============
    
    async def add_source_channel(self, channel_id: str, title: str, forward_mode: str = 'copy') -> bool:
        """Add a source channel"""
        try:
            # Check if exists
            exists = await self.channels.find_one({'channel_id': channel_id})
            if exists:
                return False
            
            await self.channels.insert_one({
                'channel_id': channel_id,
                'title': title,
                'forward_mode': forward_mode,
                'added_date': datetime.now()
            })
            return True
        except:
            return False
    
    async def remove_source_channel(self, channel_id: str) -> bool:
        """Remove a source channel"""
        try:
            result = await self.channels.delete_one({'channel_id': channel_id})
            return result.deleted_count > 0
        except:
            return False
    
    async def get_all_channels(self) -> List[Dict]:
        """Get all source channels"""
        try:
            cursor = self.channels.find({})
            return await cursor.to_list(length=None)
        except:
            return []
    
    async def set_forward_mode(self, channel_id: str, mode: str) -> bool:
        """Set forward mode for a channel"""
        try:
            await self.channels.update_one(
                {'channel_id': channel_id},
                {'$set': {'forward_mode': mode}}
            )
            return True
        except:
            return False
    
    async def get_channel_count(self) -> int:
        """Get total channel count"""
        try:
            return await self.channels.count_documents({})
        except:
            return 0
    
    # ============ DESTINATION MANAGEMENT ============
    
    async def set_destination(self, channel_id: str, title: str) -> bool:
        """Set destination channel"""
        try:
            await self.destination.delete_many({})  # Remove old destination
            await self.destination.insert_one({
                'channel_id': channel_id,
                'title': title,
                'set_date': datetime.now()
            })
            return True
        except:
            return False
    
    async def get_destination(self) -> Optional[Dict]:
        """Get destination channel"""
        try:
            return await self.destination.find_one({})
        except:
            return None
    
    # ============ STATS ============
    
    async def increment_forwards(self):
        """Increment forward count"""
        try:
            await self.stats.update_one(
                {},
                {'$inc': {'total_forwards': 1}}
            )
        except:
            pass
    
    async def get_stats(self) -> Dict:
        """Get bot statistics"""
        try:
            stats = await self.stats.find_one({})
            return {
                'total_forwards': stats.get('total_forwards', 0),
                'total_users': await self.get_user_count(),
                'total_channels': await self.get_channel_count(),
                'banned_users': await self.banned_users.count_documents({}),
                'start_date': stats.get('start_date', datetime.now())
            }
        except:
            return {
                'total_forwards': 0,
                'total_users': 0,
                'total_channels': 0,
                'banned_users': 0,
                'start_date': datetime.now()
            }
    
    # ============ USER SESSION MANAGEMENT ============
    
    async def save_user_session(self, user_id: int, session_string: str, phone: str) -> bool:
        """Save user's session string"""
        try:
            await self.user_sessions.update_one(
                {'user_id': str(user_id)},
                {
                    '$set': {
                        'session_string': session_string,
                        'phone': phone,
                        'updated_date': datetime.now()
                    },
                    '$setOnInsert': {
                        'created_date': datetime.now()
                    }
                },
                upsert=True
            )
            return True
        except:
            return False
    
    async def get_user_session(self, user_id: int) -> Optional[Dict]:
        """Get user's session"""
        try:
            return await self.user_sessions.find_one({'user_id': str(user_id)})
        except:
            return None
    
    async def delete_user_session(self, user_id: int) -> bool:
        """Delete user's session (logout)"""
        try:
            result = await self.user_sessions.delete_one({'user_id': str(user_id)})
            return result.deleted_count > 0
        except:
            return False
    
    # ============ USER CHANNEL MANAGEMENT ============
    
    async def add_user_source_channel(self, user_id: int, channel_id: str, title: str, forward_mode: str = 'copy') -> bool:
        """Add a source channel for specific user"""
        try:
            # Check if exists
            exists = await self.user_channels.find_one({
                'user_id': str(user_id),
                'channel_id': channel_id
            })
            if exists:
                return False
            
            await self.user_channels.insert_one({
                'user_id': str(user_id),
                'channel_id': channel_id,
                'title': title,
                'forward_mode': forward_mode,
                'added_date': datetime.now()
            })
            return True
        except:
            return False
    
    async def remove_user_source_channel(self, user_id: int, channel_id: str) -> bool:
        """Remove a source channel for specific user"""
        try:
            result = await self.user_channels.delete_one({
                'user_id': str(user_id),
                'channel_id': channel_id
            })
            return result.deleted_count > 0
        except:
            return False
    
    async def get_user_channels(self, user_id: int) -> List[Dict]:
        """Get all source channels for specific user"""
        try:
            cursor = self.user_channels.find({'user_id': str(user_id)})
            return await cursor.to_list(length=None)
        except:
            return []
    
    async def set_user_forward_mode(self, user_id: int, channel_id: str, mode: str) -> bool:
        """Set forward mode for a user's channel"""
        try:
            await self.user_channels.update_one(
                {'user_id': str(user_id), 'channel_id': channel_id},
                {'$set': {'forward_mode': mode}}
            )
            return True
        except:
            return False
    
    async def get_user_channel_count(self, user_id: int) -> int:
        """Get user's channel count"""
        try:
            return await self.user_channels.count_documents({'user_id': str(user_id)})
        except:
            return 0
    
    # ============ USER DESTINATION MANAGEMENT ============
    
    async def set_user_destination(self, user_id: int, channel_id: str, title: str) -> bool:
        """Set destination channel for specific user"""
        try:
            await self.user_destinations.delete_many({'user_id': str(user_id)})  # Remove old
            await self.user_destinations.insert_one({
                'user_id': str(user_id),
                'channel_id': channel_id,
                'title': title,
                'set_date': datetime.now()
            })
            return True
        except:
            return False
    
    async def get_user_destination(self, user_id: int) -> Optional[Dict]:
        """Get destination channel for specific user"""
        try:
            return await self.user_destinations.find_one({'user_id': str(user_id)})
        except:
            return None
