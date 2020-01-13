|---------------------------|
| TeamSpen's Hammer Addons  |
|---------------------------|

# Features

* Auto-packing - filtered based on search paths in gameinfo, and based on a FGD database + `comp_pack` entities.
* Static prop combining - merges together adjacent props to allow them to be efficently drawn in batches.
* A unified FGD database allowing keyvalues to be shared among games, and accurately defining when features were added and removed.
* Many many upgrades to entity options and layouts.
* New sprites for almost all entities, both custom made and from a number of sources:
	* [The TF2 Ultimate Mapping Resource Pack][tf2]
	* [ZPS: Supplemental Hammer Icons][zps]
	* [ts2do's HL FGDs][ts2do]
* Adds lots more AutoVisgroups for easily hiding entities.
* Several `comp_` entities with additional features. These are mainly intended for use in instances, allowing modifying entities outside of the instance to conform or doing normally impossible things like positioning things in the void.
	To use, decompile props and configure the folder & studioMDL's path then place `comp_propcombine_set` entities.
* For games supporing VScript:
	* In any `RunScriptCode` input, backticks can be used for string literals, instead of the disallowed `"` character. 
	* In addition to the normal `Entity Scripts` section, a new `Init Code` field can be used to write code that's packed and added to those scripts. Useful for setting configuration options etc. Backticks can be used here too.

# Installation

* Download the release from the [releases tab][releases].
* Use the provided FGD instead of the vanilla one. (Issues/PRs welcome for any entity improvements.)
* Add the `hammer/` folder to gameinfo.txt, to provide sprites for the compiler.
* Add the postcompiler to the compile commands: 
	1. Create a new command after VBSP, using the "Executable" type and 
	choosing the postcompiler EXE.
	2. In the parameters, enter `--propcombine $path/$file`.
* Compile a map once, which should produce the config file `Game Folder/srctools.vdf` (this can be placed in any parent folder of the VMF).
* Configure the file as desired, then compile your maps to apply the changes.
* If using BEEMOD2.4, change Hammer -> Options -> Build Programs to use `vrad_original.exe`.

[releases]: https://github.com/TeamSpen210/HammerAddons/releases
[skotty]: http://forums.thinking.withportals.com/downloads.php?view=detail&df_id=507
[tf2]: http://forums.tf2maps.net/showthread.php?t=4674
[ts2do]: http://halflife2.filefront.com/file/HalfLife_2_Upgraded_Base_FGDs;48139
[zps]: http://www.necrotalesgames.com/tools/index.php