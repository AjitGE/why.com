import json

# This method gets the channelList from the allChannels.json file and returns it as a list/dictionary
def getChannelList():
    #allChannels.getAllChannels()
    with open("config.json", "r") as savedChannelDetailInFile:
      savedChannels = json.load(savedChannelDetailInFile)
    return savedChannels

