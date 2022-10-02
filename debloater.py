import os

bloat_app = [
'com.android.browser',
'com.android.calendar',
'com.android.fileexplorer',
'com.mi.android.global.Fileexplorer',
'com.android.email',
'com.wps.xiaomi.aboard.lite',
'com.mipay.wallet.id',
'com.miui.miservice',
'com.android.thememanager',
'com.miui.yellowpages',
'pm uninstall -k --user 0 com.android.chrome',
'pm uninstall -k --user 0 com.android.deskclock',
'pm uninstall -k --user 0 com.google.android.apps.docs',
'pm uninstall -k --user 0 com.google.android.apps.maps',
'pm uninstall -k --user 0 com.google.android.apps.tachyon',
'pm uninstall -k --user 0 com.google.android.music',
'pm uninstall -k --user 0 com.google.android.videos',
'pm uninstall -k --user 0 com.google.android.feedback',
'pm uninstall -k --user 0 com.google.android.youtube',
'pm uninstall -k --user 0 com.mi.android.globalminusscreen',
'pm uninstall -k --user 0 com.mi.android.globalFileexplorer',
'pm uninstall -k --user 0 com.mi.globalbrowser',
'pm uninstall -k --user 0 com.mipay.wallet.in',
'pm uninstall -k --user 0 com.miui.analytics',
'pm uninstall -k --user 0 com.miui.backup',
'pm uninstall -k --user 0 com.miui.bugreport',
'pm uninstall -k --user 0 com.miui.calculator',
'pm uninstall -k --user 0 com.miui.cleanmaster',
'pm uninstall -k --user 0 com.miui.cloudbackup',
'pm uninstall -k --user 0 com.miui.cloudservice',
'pm uninstall -k --user 0 com.miui.micloudsync',
'pm uninstall -k --user 0 com.miui.cloudservice.sysbase',
'pm uninstall -k --user 0 com.miui.compass',
'pm uninstall -k --user 0 com.miui.fm',
'pm uninstall -k --user 0 com.miui.freeform',
'pm uninstall -k --user 0 com.miui.hybrid',
'pm uninstall -k --user 0 com.miui.hybrid.accessory',
'pm uninstall -k --user 0 com.miui.miservice',
'pm uninstall -k --user 0 com.miui.mishare.connectivity',
'pm uninstall -k --user 0 com.miui.miwallpaper',
'pm uninstall -k --user 0 com.miui.msa.global',
'pm uninstall -k --user 0 com.miui.notes',
'pm uninstall -k --user 0 com.miui.phrase',
'pm uninstall -k --user 0 com.miui.player',
'pm uninstall -k --user 0 com.android.soundrecorder',
'pm uninstall -k --user 0 com.miui.screenrecorder',
'pm uninstall -k --user 0 com.miui.touchassistant',
'pm uninstall -k --user 0 com.miui.videoplayer',
'pm uninstall -k --user 0 com.miui.weather2',
'pm uninstall -k --user 0 com.miui.yellowpage',
'pm uninstall -k --user 0 com.xiaomi.account',
'pm uninstall -k --user 0 com.xiaomi.calendar',
'pm uninstall -k --user 0 com.xiaomi.discover',
'pm uninstall -k --user 0 com.xiaomi.glgm',
'pm uninstall -k --user 0 com.xiaomi.midrop',
'pm uninstall -k --user 0 com.xiaomi.mipicks',
'pm uninstall -k --user 0 com.xiaomi.miplay_client',
'pm uninstall -k --user 0 com.xiaomi.mircs',
'pm uninstall -k --user 0 com.xiaomi.mirecycle', 
'pm uninstall -k --user 0 com.xiaomi.payment',
'pm uninstall -k --user 0 com.xiaomi.scanner',
'pm uninstall -k --user 0 com.xiaomi.xmsf',
'pm uninstall -k --user 0 com.xiaomi.xmsfkeeper',
'pm uninstall -k --user 0 com.netflix.partner.activation',
'pm uninstall -k --user 0 com.netflix.mediaclient',
'pm uninstall -k --user 0 com.tencent.soter.soterserver',
'pm uninstall -k --user 0 com.facebook.appmanager',
'pm uninstall -k --user 0 com.facebook.services',
'pm uninstall -k --user 0 com.facebook.system',
'pm uninstall -k --user 0 com.facebook.katana',
]

element = 0

if input("To remove selected apps press y").lower() == 'y':
  for i in range(len(bloat_app)):
    if input("remove " , bloat_app[element] , "press y for yes , n for no").lower() == 'y':
      try:
        os.system('adb shell pm uninstall -k --user 0 ',bloat_app[element])
        print('uninstalled ',bloat_app[element])
        element += 1
      except:
        print('failed to uninstall ',bloat_app[element])
    else:
      element += 1

else:
  for i in range(len(bloat_app)):
    try:
      os.system('adb shell pm uninstall -k --user 0 ',bloat_app[element])
      print('uninstalled ',bloat_app[element])
      element += 1
    except:
      print('failed to uninstall ',bloat_app[element])
      element += 1
