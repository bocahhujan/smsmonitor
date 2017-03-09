from py2exe.build_exe import py2exe
from distutils.core import setup
setup(
	options = {
        "py2exe": {
			'bundle_files': 1 ,
            "dll_excludes": ["MSVCP90.dll"] ,
			"includes" : ["sip", "PyQt4.QtSql"]
        }},
    windows =[{
			   "script": "sms_monitor.pyw" ,
	 		   "icon_resources": [(1, "sms.ico")]
			  }]
	)
