# Generates Kodi playlist by default, If you want OTT Navigator Supported Playlist, pass '--ott-navigator' as argument.
import jwtoken as jwt


m3ustr = '#EXTM3U  x-tvg-url="https://github.com/mitthu786/tvepg/blob/main/tataplay/epg.xml.gz" \n\n'
kodiPropLicenseType = "#KODIPROP:inputstream.adaptive.license_type=clearkey"

def processTokenChunks(channelList):
    global m3ustr
    kodiPropLicenseUrl = ""
    for channel in channelList:
        if 'channel_license_url' in channel:
           clearKey = channel['channel_license_url']
        else:
           clearKey = ""
        kodiPropLicenseUrl = "#KODIPROP:inputstream.adaptive.license_key=" + str(clearKey)
        m3ustr += kodiPropLicenseType + "\n" + kodiPropLicenseUrl + "\n" + "#EXTINF:-1 "
        m3ustr += "tvg-id="+ "\"ts" + channel['channel_id'] + "\" " + "group-title=" + "\"" + channel['channel_genre'] + "\" " + "tvg-logo=\"" + channel['channel_logo'] + "\" ," + channel['channel_name'] + "\n" + channel['channel_url'] + "\n\n"


def m3ugen():
    global m3ustr
    channelList = jwt.getChannelList()
    processTokenChunks(channelList)

    print("================================================================")
    print("Found total {0} channels subscribed by user \nSaving them to m3u file".format(len(channelList)))
    print("================================================================")
    saveM3ustringtofile(m3ustr)


def saveM3ustringtofile(m3ustr):
    with open("allChannelPlaylist.m3u", "w") as allChannelPlaylistFile:
        allChannelPlaylistFile.write(m3ustr)


def getPrintNote():
    s = " *****************************************************\n" + "Welcome To TataSky Channel Generation Script\n" + \
        "**********************************************************\n" + \
        "- Using this script you can generate playable links based on the channels you have subscribed to \n" + \
        "- You can always read the README.md file if you don't know how to use the generated file \n" + \
        "- You can login using your password or generate an OTP. You need to enter both the Registered Mobile Number \n" + \
        "\n Caution: This doesn't promote any kind of hacking or compromising anyone's details"

    return s


if __name__ == '__main__':
    m3ugen()
