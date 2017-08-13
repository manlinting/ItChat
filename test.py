#!/usr/bin/env python
#########################################################################
# Author: lincolnlin
# Created Time: Sun Aug 13 07:52:32 2017
# File Name: test.py
# Description: 
#########################################################################
import itchat

''''
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text
    '''

@itchat.msg_register(itchat.content.TEXT)
def _(msg):
    # equals to print(msg['FromUserName'])
    print(msg.fromUserName)


itchat.auto_login(enableCmdQR =1)
author = itchat.search_friends(nickName='lincoln')[0]
author.send('greeting, littlecoder!')

#itchat.run()
