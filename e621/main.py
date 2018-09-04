"""Loads the latest image from E621.net
"""
___name___         = "e621"
___license___      = "MIT"
___dependencies___ = ["app", "wifi", "http", "homescreen"]
___categories___   = ["Other"]
___launchable___   = True

import ugfx, wifi, http, json
from homescreen import sleep_or_exit

ugfx.clear()
ugfx.text(5, 5, "Connecting To WIFI", ugfx.BLACK)
wifi.connect()
ugfx.text(5, 5, "Connecting To WIFI", ugfx.WHITE)
while True:
    try:
        ugfx.text(5, 5, ">", ugfx.BLACK)
        url = json.loads(http.get("https://e621.net/post/index.json?limit=1&tags=order:random", headers={"User-Agent":"TiLDA MK4 (itlin)"}).content)[0]["file_url"]
        ugfx.text(5, 5, ">>", ugfx.BLACK)
        ugfx.text(5, 5, ">>", ugfx.GREEN)
        print(url[-3:])
        if url[-3:] == "png":
            print("png")
            ugfx.display_image(0,0,bytearray(http.get("https://process.filestackapi.com/AhTgLagciQByzXpFGRI0Az/resize=width:240,height:320,fit:crop/rotate=deg:180/" + url).raise_for_status().content))
        else:
            print("jpg")
            ugfx.display_image(0,0,bytearray(http.get("https://process.filestackapi.com/AhTgLagciQByzXpFGRI0Az/resize=width:240,height:320,fit:crop/rotate=deg:180/output=format:png/" + url).raise_for_status().content))
    except (OSError, ValueError) as e:
        print(e)
        ugfx.text(5, 5, ">>", ugfx.RED)
    sleep_or_exit(1)

