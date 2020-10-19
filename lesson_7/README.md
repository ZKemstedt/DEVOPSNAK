# Lesson 7

## Client / Server

### Start Server

```bash
python lesson_7/server.py
# ctrl-c to quit
```

Powershell

```powershell
py lesson_7\server.py
# ctrl-c to quit
```

### Execute client

```bash
python lesson_7/client.py
client.py hello world
# ctrl-c to quit
```

Powershell

```powershell
py lesson_7\server.py hello world
# ctrl-c to quit
```

### Assignment

1. Test with netstat (windows, mac) or ss (ubuntu) that your server did bind a port
2. Modify the message replied by the server

   1. all vowels a, e, i, o, u, y, å, ä and ö should be replaced with a _
   2. Try to send some unicode signs, emojis etc.
