import os , platform , sys 
def debloat():
	bloat_app = [
	    'com.android.chrome',
	    'com.android.deskclock',
	    'com.google.android.apps.docs',
    	'com.google.android.apps.maps',
	    'com.google.android.apps.photos',
	    'com.google.android.apps.tachyon',
    	'com.google.android.apps.subscriptions.red',
    	'com.google.android.music',
    	'com.google.android.videos',
    	'com.google.android.feedback',
    	'com.google.android.youtube',
    	'com.mi.android.globalminusscreen',
    	'com.mi.android.globalFileexplorer',
    	'com.mi.globalbrowser',
    	'com.mipay.wallet.in',
    	'com.miui.analytics',
    	'com.miui.backup',
    	'com.miui.bugreport',
    	'com.miui.calculator',
    	'com.miui.cleanmaster',
    	'com.miui.cloudbackup',
    	'com.miui.cloudservice',
    	'com.miui.micloudsync',
    	'com.miui.cloudservice.sysbase',
    	'com.miui.compass',
    	'com.miui.fm',
    	'com.miui.freeform',
    	'com.miui.hybrid',
    	'com.miui.hybrid.accessory',
    	'com.miui.miservice',
    	'com.miui.mishare.connectivity',
    	'com.miui.miwallpaper',
    	'com.miui.msa.global',
    	'com.miui.notes',
    	'com.miui.phrase',
    	'com.miui.player',
    	'com.android.soundrecorder',
    	'com.miui.screenrecorder',
    	'com.miui.touchassistant',
    	'com.miui.videoplayer',
    	'com.miui.weather2',
    	'com.miui.yellowpage',
    	'com.xiaomi.account',
    	'com.xiaomi.calendar',
    	'com.xiaomi.discover',
    	'com.xiaomi.glgm',
    	'com.xiaomi.midrop',
    	'com.xiaomi.mipicks',
    	'com.xiaomi.miplay_client',
    	'com.xiaomi.mircs',
    	'com.xiaomi.mirecycle',
    	'com.xiaomi.misettings',
    	'com.xiaomi.payment',
    	'com.xiaomi.scanner',
    	'com.xiaomi.xmsf',
    	'com.xiaomi.xmsfkeeper',
    	'com.netflix.partner.activation',
    	'com.netflix.mediaclient',
    	'com.tencent.soter.soterserver',
    	'com.facebook.appmanager',
    	'com.facebook.services',
    	'com.facebook.system',
    	'com.facebook.katanapm',
    	'com.android.calendar',
    	'com.android.vending',
    	'com.android.browser',
    	'com.android.providers.downloads.ui',
    	'com.miui.gallery',
    	'com.google.android.gm',
    	'com.google.android.apps.inputmethod.hindi',
    	'com.android.email',
    	'cn.wps.xiaomi.abroad.lite',
    	'com.android.thememanager',
    	'com.miui.android.fashiongallery',
    	'com.android.providers.downloads.ui',
    	'com.google.android.inputmethod.latin',
    	'com.google.android.googlequicksearchbox',
    	'com.google.android.gms',
    	'com.google.android.gsf',
    	'com.miui.analytics',
    	'com.android.providers.calendar',
    	'com.miui.fmservice',
    	'com.xiaomi.mi_connect_service',
    	'com.android.providers.downloads',
    	'com.miui.home',
    	'com.android.providers.partnerbookmarks',
#    	'com.bsp.cathlog',
    	'com.google.android.onetimeinitializer',
    	'com.google.android.partnersetup',
    	'com.google.android.printservice.recommendation',
    	'com.milink.service',
    	'com.mipay.wallet.id',
    	'com.miui.antispam',
    	'com.miui.daemon',
    	'com.miui.translation.kingsoft',
    	'com.miui.translation.xmcloud',
    	'com.miui.translation.youdao',
    	'com.miui.translationservice',
    	'com.miui.userguide',
    	'com.xiaomi.joyose',
    	'com.xiaomi.micloud.sdk',
    	]
	element = 0
	   
	for element in range(len(bloat_app)):
	    if platform.system() == 'Windows':
	    	try:
	    		print('\nuninstalling ' + bloat_app[element])
	    		os.system('platform-tools\\adb.exe shell pm uninstall -k --user 0 ' + bloat_app[element])
	    		element += 1
	    	except:
	    		print('failed to uninstall ' + bloat_app[element])
	    elif platform.system() == 'Linux':
	    	try:
	    		print('\nuninstalling ' + bloat_app[element])
	    		os.system('adb shell pm uninstall -k --user 0 ' + bloat_app[element])
	    		element += 1
	    	except:
	    		print('failed to uninstall ' + bloat_app[element])
	os.system('adb shell reboot')
  
def recover(package):
  if platform.system() == 'Windows':
      try:
        os.system('platform-tools\\adb.exe shell cmd package install-existing ' + package)
        print('Installed ' + package)
      except:
        print('failed to Install ' + package)
  if platform.system() == 'Linux':
    try:
      os.system('adb shell cmd package install-existing ' + package)
      print('Installed ' + package)
    except:
      print('failed to Install ' + package)

if sys.argv[1] == "debloat":
  debloat()
elif sys.argv[1] == "recover":
  recover(sys.argv[2])
