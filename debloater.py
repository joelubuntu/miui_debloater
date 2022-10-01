import os

bloat_app = [
'com.android.browser',
'com.miui.calculator',
'com.android.calendar',
'com.miui.cleanmaster',
'com.android.fileexplorer',
'com.miui.compass',
'com.google.android.apps.tachyon',
'com.facebook.system',
'com.facebook.services',
'com.facebook.appmanager',
'com.mi.android.global.Fileexplorer',
'com.xiaomi.glgm',
'com.xiaomi.mipicks',
'com.android.email',
'com.xiaomi.payment',
'com.wps.xiaomi.aboard.lite',
'com.mipay.wallet.id',
'com.mipay.wallet.in',
'com.miui.notes',
'com.miui.hybrid',
'com.miui.miservice',
'com.xiaomi.midrop',
'com.android.thememanager',
'com.miui.weather2',
'com.miui.yellowpages'
]

element = 0

for i in range(len(bloat_app)):
  try:
    os.system('adb shell pm uninstall -k --user 0 ',bloat_app[element])
    print('uninstalled ',bloat_app[element])
    element += 1
  except:
    print('failed to uninstall ',bloat_app[element])
