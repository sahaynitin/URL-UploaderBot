from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

I am Fastest Url Uploader Bot. 
Just send me the link to get started !

Made With 💕 By @Tellybots_4u
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏡 Return Home", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("📡 Update Channel", url="https://t.me/tellybots_4u")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("👲 About", callback_data="about")
        ],
        [InlineKeyboardButton("🚦 Bot Status", url="https://t.me/tellybots_4u")],
        [InlineKeyboardButton("💬 Support Group", url="https://t.me/tellybots_support")],
    ]

    # Help Message
    HELP = """
I am UrL Uploader Bot
    
1. Send url Link|New Name with Extension.

2. Send Custom Thumbnail (Optional).

3. Select the button.

   SVideo - Give File as video with Screenshots
   Dfile   - Give File with Screenshots
   Video  - Give File as video without Screenshots
   File  - Give File without Screenshots

 **Available Commands** 

/about - About The Bot
/help - This Message
/start - Start the Bot
    """

    # About Message
    ABOUT = """
**About This Bot** 

A telegram Fastest Url Uploader Bot

Source Code : [Click Here](https://t.me/tellybots_digital)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @Tellybots_4u
    """

