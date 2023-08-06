# amxlogs
#### finds, extracts, and clears logs from AMX devices using ftp

## LogSniffer():
### returns:
#### logs are written to file and/or logged.

### set_systems():
#### list of dicts where each dict is an AMX system.
#### minimum key requirements:
##### 'full_name' (string)
##### 'master_ip' (string)
### config():
#### user_name: user name used to login to AMX
#### password: password used to login to AMX
#### log_type: default 'error_log', case insensitive.
##### Also try 'camera_log'. Additional types depend on what you name them when you create them in the AMX program. So if you had AMX create logs called late_night_usage.txt, log_type would be 'late_night_usage'.
#### output_dir: path to dir used to store received files.
##### File name is created using 'full_name' ~amx logfile name~
#### clear_logs: default False.
##### Use True to delete the log files after they are downloaded.
#### debug_ftp: default 0.
##### Set to 1 to view ftplib's builtin debugger on stdout.
#### timeout: default 10. Seconds to timeout socket connection.
			
### run():
##### Begin connecting to systems in set_systems(), download logs that match log_type, using settings from config()
