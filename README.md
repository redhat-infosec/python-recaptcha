# python-recaptcha
This Python module brings in Google's reCAPTCHA v1 and v2 support. Although
v1 is being deactivated starting from the 31st of March 2018 it's kept around
for backwards compatibility and it's still marked as the default library option.

## Toggling version 2
1. Call any of the displayhtml, load_script functions with the version param
   set to 2
2. Make sure you call the appropriate submit function, **submit** for v1 and
   **v2submit** for v2 (the list of params differs as v2 comes with no
   recaptcha_challenge_field param)

## Examples (Mailman)
Please note you may have to regenerate the patch below for it to apply correctly
as the source files can be different across Mailman releases and installations.

```git
diff --git a/Mailman/Cgi/listinfo.py b/Mailman/Cgi/listinfo.py
--- a/Mailman/Cgi/listinfo.py
+++ b/Mailman/Cgi/listinfo.py
@@ -30,6 +31,8 @@ from Mailman import Errors
 from Mailman import i18n
 from Mailman.htmlformat import *
 from Mailman.Logging.Syslog import syslog
+from recaptcha.client import captcha
 
 # Set up i18n
 _ = i18n._
@@ -200,6 +203,9 @@ def list_listinfo(mlist, lang):
     replacements[''] = mlist.FormatFormStart('listinfo')
     replacements[''] = mlist.FormatBox('fullname', size=30)
 
+    # Captcha
+    replacements['<mm-recaptcha-javascript>'] = captcha.displayhtml(mm_cfg.RECAPTCHA_PUBLIC_KEY, use_ssl=True, version=2)
+    replacements['<mm-recaptcha-script>'] = captcha.load_script(version=2)
+
     # Do the expansion.
     doc.AddItem(mlist.ParseTags('listinfo.html', replacements, lang))
     print doc.Format()

diff --git a/Mailman/Cgi/subscribe.py b/Mailman/Cgi/subscribe.py
--- a/Mailman/Cgi/subscribe.py
+++ b/Mailman/Cgi/subscribe.py
@@ -21,6 +21,8 @@ import sys
 import os
 import cgi
 import signal
+from recaptcha.client import captcha
 
 from Mailman import mm_cfg
 from Mailman import Utils
@@ -132,6 +130,17 @@ def process_form(mlist, doc, cgidata, lang):
     remote = os.environ.get('REMOTE_HOST',
                             os.environ.get('REMOTE_ADDR',
                                            'unidentified origin'))

+   # recaptcha
+   captcha_response = captcha.v2submit(
+       cgidata.getvalue('g-recaptcha-response', ""),
+       mm_cfg.RECAPTCHA_PRIVATE_KEY,
+       remote
+    )
+    if not captcha_response.is_valid:
+        results.append(_('Invalid captcha: %s' % captcha_response.error_code))

     # Was an attempt made to subscribe the list to itself?
     if email == mlist.GetListEmail():
         syslog('mischief', 'Attempt to self subscribe %s: %s', email, remote)
```
