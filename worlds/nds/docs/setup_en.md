# Setup Guide for Natural Disaster Survival

## Prerequisites
Before starting. Make sure you have
- The x64 versions of [.NET 6.0 Runtime, Desktop Runtime, and the ASP.NET Runtime](https://builds.dotnet.microsoft.com/dotnet/Sdk/6.0.428/dotnet-sdk-6.0.428-win-x64.exe) installed for OnlyRetroRobloxHere
- The x86 versions of Microsoft Visual C++ [2005](https://www.microsoft.com/en-us/download/details.aspx?id=26347) and [2008](https://www.microsoft.com/en-US/download/details.aspx?id=26368) installed for running the older Roblox clients
- [OnlyRetroRobloxHere](https://onlyretrorobloxhere.itch.io/orrh) from Itch.io ([Setup Guide](https://orrh.thread.zone/wiki/article/setting+up+orrh)) and extracted
- The patched version of [OnlyRetroRobloxHere.WebServer.dll](https://docs.google.com/document/d/1OMIBqNByCIjMw5h2s-JnG8AK-MjKfRhuCTQ3ki8tSUk/edit?tab=t.0) placed at the root of your OnlyRetroRobloxHere install. It should overwrite the old one
- And a [xdelta patcher](https://www.romhacking.net/utilities/598/)
## Installation
- Download and install the Natural Disaster Survival [APWorld](https://github.com/KLanausse/MultiworldGG/releases/tag/Natural-Disaster-Survival)
- Go to the [Natural Disaster Survival Archipelago Releases Page](https://github.com/KLanausse/RobloxAPs/releases/tag/Natural-Disaster-Survival) and download `Natural Disaster Survival.rbxl`, `ArchipelagoAssetPack.zip` and `NDSAssetPack.zip`
- Extract the folder in both `ArchipelagoAssetPack.zip` and `NDSAssetPack.zip` and move it to your assetpacks folder (`OnlyRetroRobloxHere/assetpacks`)
- Go to your maps folder (`OnlyRetroRobloxHere/maps`) and create a folder called "Archipelago" if one doesn't already exist. Then move `Natural Disaster Survival.rbxl` to that folder.

### Patching The Client
- Download [rbx-apclientpp for 2013L-v2013.12.12.5](https://github.com/KLanausse/rbx-apclientpp/releases/download/v1.1/rbx-apclientpp-2013L-v2013.12.12.5.zip) and extract `rbx-apclientpp.studio.dll` and `RobloxStudioBeta.xdelta`.
- Rename `rbx-apclientpp.studio.dll` to just `rbx-apclientpp.dll` and move it to your 2013L Studio folder `OnlyRetroRobloxHere/data/clients/2013L/Studio/` (Don't close the folder just yet)
- Make a backup of `RobloxStudioBeta.exe`. Call it something like "`RobloxStudioBeta.backup.exe`"
- Patch `RobloxStudioBeta.exe` using your xdelta patcher and `RobloxStudioBeta.xdelta`. Save the patch file as `RobloxStudioBeta.patched.exe` in the same folder.
- Delete `RobloxStudioBeta.exe` and then rename `RobloxStudioBeta.patched.exe` to just `RobloxStudioBeta.exe`

Afterwards, everything should be installed and ready for you to play!
Just verify that everything is in the right place as seen below.
```
OnlyRetroRobloxHere/
├───assetpacks/
│   ├───Natural Disaster Survival/
│   │   ├───AssetPack.json
│   │   ├───580954.png
│   │   ...
│   └───Archipelago/
│       ├───AssetPack.json
│       ├───96481249.ogg
│       ...
├───data/
│   └───clients/
│       └───2013L/
│           └───Studio/
│               ├───rbx-apclientpp.dll
│               ├───RobloxStudioBeta.exe
│               ├───RobloxStudioBeta.backup.exe
│               ...
└───maps/
    └───Archipelago/
        └───Natural Disaster Survival.rbxl
```

## Playing
To play, open OnlyRetroRobloxHere and click on 2013L in the Clients list.
Afterwards, go to the host tab and select Natural Disaster Survival under the Archipelago folder. Then click the big red **Host** button *(Feel free to check disable rendering before clicking Host if you wana save GPU resources)*.
The server should now start up.

To join, go back to the Play tab and change your Chat Style to just "Bubble" then click "Play This"!
Once in-game, go to the Tracker Billboard and click the big green Connect button. Input your server, slot name and password and then click "Connect To The Multiworld". After a few seconds, you should connected and all set to go!


